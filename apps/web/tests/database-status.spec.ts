import { test, expect } from "@playwright/test";
import { readFileSync } from "node:fs";
import { resolve } from "node:path";

const env = readFileSync(resolve(process.cwd(), "../../.env"), "utf8");
const setting = (name: string) =>
  process.env[name] ||
  env
    .split(/\r?\n/)
    .find((line) => line.startsWith(name + "="))
    ?.slice(name.length + 1) ||
  "";

test("settings displays actual database schema and pgvector inspection", async ({
  page,
}) => {
  test.setTimeout(90000);
  await expect
    .poll(
      async () =>
        (
          await page.context().request.post("/api/auth/login", {
            headers: { Origin: "http://localhost:3000" },
            data: {
              email: setting("OWNER_EMAIL"),
              password: setting("OWNER_PASSWORD"),
            },
          })
        ).status(),
      { intervals: [1000, 5000, 10000], timeout: 65000 },
    )
    .toBe(200);
  await page.goto("/?view=settings");
  const facts = await (
    await page.context().request.get("/api/operations/database")
  ).json();
  expect(["sqlite", "postgresql"]).toContain(facts.backend);
  expect(facts.schema_current).toBe(true);
  const panel = page.locator("section").filter({
    has: page.getByRole("heading", {
      name: "Database & semantic memory",
      exact: true,
    }),
  });
  await expect(panel).toContainText(facts.backend);
  await panel
    .getByRole("button", { name: "Check database", exact: true })
    .click();
  await expect(panel).toContainText("Schema current");
  await expect(panel).toContainText(facts.schema_revision);
  if (facts.backend === "postgresql") {
    expect(facts.pgvector_version).toBeTruthy();
    await expect(panel).toContainText("HNSW available");
  } else {
    await expect(panel).toContainText("Existing records remain in SQLite");
  }
  await page.setViewportSize({ width: 390, height: 844 });
  await expect(
    panel.getByRole("button", { name: "Check database" }),
  ).toBeVisible();
  expect(
    await page.evaluate(
      () => document.documentElement.scrollWidth <= window.innerWidth,
    ),
  ).toBe(true);
});

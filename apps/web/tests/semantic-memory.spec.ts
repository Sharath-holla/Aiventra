import { test, expect } from "@playwright/test";
import { readFileSync } from "node:fs";
import { resolve } from "node:path";

const env = readFileSync(resolve(process.cwd(), "../../.env"), "utf8");
const setting = (name: string) =>
  process.env[name] ||
  env
    .split(/\r?\n/)
    .find((l) => l.startsWith(name + "="))
    ?.slice(name.length + 1) ||
  "";
const headers = { Origin: "http://localhost:3000" };

test("memory UI saves real versions, searches stored evidence, reloads and purges its own fixture", async ({
  page,
}) => {
  test.setTimeout(90000);
  expect(
    (
      await page.context().request.post("/api/auth/login", {
        headers,
        data: {
          email: setting("OWNER_EMAIL"),
          password: setting("OWNER_PASSWORD"),
        },
      })
    ).status(),
  ).toBe(200);
  const title = `Memory browser fixture ${Date.now()}`;
  await page.goto("/?view=memory");
  await page.getByLabel("Memory title", { exact: true }).fill(title);
  await page
    .getByLabel("Memory content", { exact: true })
    .fill(
      "Retry failed invoice payments with an idempotency key. Explicit browser fixture.",
    );
  await page
    .getByLabel("Memory type", { exact: true })
    .selectOption("architecture_decision");
  await page.getByRole("button", { name: "Save memory", exact: true }).click();
  const row = page
    .locator("details")
    .filter({ has: page.locator("summary").filter({ hasText: title }) })
    .first();
  await expect(row).toBeVisible();
  await row.locator("summary").click();
  await row
    .getByRole("button", { name: "Inspect versions", exact: true })
    .click();
  await expect(
    page.getByRole("heading", { name: "Revise saved memory", exact: true }),
  ).toBeVisible();
  await page
    .getByLabel("Memory content", { exact: true })
    .fill(
      "Resolved duplicate invoice payments using idempotency and recorded recovery evidence. Explicit browser fixture.",
    );
  await page.getByRole("button", { name: "Save memory", exact: true }).click();
  await expect(row.locator("summary")).toContainText("v2");
  await page.reload();
  await expect(row.locator("summary")).toContainText("v2");
  await page.getByLabel("Search memory", { exact: true }).fill("invoice");
  await page
    .getByRole("button", { name: "Search memory", exact: true })
    .click();
  await expect(row).toBeVisible();
  await row.locator("summary").click();
  await row
    .getByRole("button", { name: "Inspect versions", exact: true })
    .click();
  await expect(page.getByText("Version 1 ·", { exact: false })).toBeVisible();
  await expect(page.getByText("Version 2 ·", { exact: false })).toBeVisible();
  await page.setViewportSize({ width: 390, height: 844 });
  await expect
    .poll(async () =>
      page.locator(".sidebar").evaluate((e) => e.getBoundingClientRect().right),
    )
    .toBeLessThanOrEqual(1);
  await page
    .locator("section")
    .filter({
      has: page.getByRole("heading", { name: "Company memory", exact: true }),
    })
    .first()
    .evaluate((e) => e.scrollIntoView({ block: "start", behavior: "instant" }));
  await page.evaluate(() => window.scrollBy(0, -76));
  expect(
    await page.evaluate(() => document.documentElement.scrollWidth),
  ).toBeLessThanOrEqual(391);
  await page.screenshot({
    path: "../../artifacts/semantic-memory-mobile.png",
    animations: "disabled",
  });
  await row
    .getByRole("button", { name: "Purge memory content", exact: true })
    .click();
  await expect(row).toHaveCount(0);
});

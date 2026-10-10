import { expect, type APIRequestContext } from "@playwright/test";
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

export async function loginOwner(request: APIRequestContext) {
  // Exercise the real persistent account throttle. Never raise production
  // limits or accept an authentication failure as a successful login.
  const deadline = Date.now() + 65000;
  while (true) {
    const response = await request.post("/api/auth/login", {
      headers: { Origin: "http://localhost:3000" },
      data: {
        email: setting("OWNER_EMAIL"),
        password: setting("OWNER_PASSWORD"),
      },
    });
    expect([200, 429]).toContain(response.status());
    if (response.status() === 200) return;
    if (Date.now() >= deadline)
      throw new Error("Owner login throttle did not clear within 65 seconds");
    await new Promise((resolve) => setTimeout(resolve, 5000));
  }
}

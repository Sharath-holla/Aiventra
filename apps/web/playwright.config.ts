import { defineConfig } from "@playwright/test";
export default defineConfig({
  testDir: "./tests",
  timeout: 60000,
  expect: { timeout: 15000 },
  use: {
    baseURL: "http://localhost:3000",
    viewport: { width: 1440, height: 1100 },
    trace: "off",
  },
  workers: 1,
  reporter: "list",
});

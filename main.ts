import { execSync } from "node:child_process";
import { copyFile, mkdir } from "node:fs/promises";

await mkdir("/output", { recursive: true });
execSync("python3 gen_image.py", { stdio: "inherit" });
await copyFile("/output/entry.png", "/output/entry.png");
console.log("entry.png → /output/entry.png");
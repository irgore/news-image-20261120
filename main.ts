import { existsSync, mkdirSync, copyFileSync } from "node:fs";
import { execSync } from "node:child_process";

const OUT = process.env.OUTPUT_DIR || "/output";
if (!existsSync(OUT)) mkdirSync(OUT, { recursive: true });

console.log("Generating newspaper front page...");
execSync("python3 gen_image.py", { stdio: "inherit", env: { ...process.env, OUTPUT_DIR: OUT } });

const src = `${OUT}/entry.png`;
if (existsSync(src)) {
  console.log(`Newspaper generated: ${src}`);
} else {
  console.error("ERROR: entry.png not found");
  process.exit(1);
}
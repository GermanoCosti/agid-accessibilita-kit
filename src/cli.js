#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import readline from "node:readline";
import {
  renderChecklistMd,
  renderDichiarazioneHtml,
  renderFeedbackHtml,
  renderFooterSnippet
} from "./templates.js";

function getArg(name) {
  const idx = process.argv.findIndex((a) => a === name);
  if (idx === -1) return null;
  return process.argv[idx + 1] ?? null;
}

function printHelp() {
  console.log("AGID Accessibilita Kit (bozze)");
  console.log("");
  console.log("Comandi:");
  console.log("  init [--out-dir ./accessibilita]   Genera pagine + snippet + checklist");
  console.log("");
  console.log("Opzioni:");
  console.log("  --out-dir   Cartella output");
  console.log("  --help      Mostra aiuto");
}

async function ask(question, defValue) {
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
  const q = defValue ? `${question} [${defValue}]: ` : `${question}: `;
  const answer = await new Promise((resolve) => rl.question(q, resolve));
  rl.close();
  const v = String(answer || "").trim();
  return v || defValue || "";
}

function writeFile(outDir, name, content) {
  fs.mkdirSync(outDir, { recursive: true });
  const p = path.join(outDir, name);
  fs.writeFileSync(p, content, "utf8");
  return p;
}

const help = process.argv.includes("--help") || process.argv.includes("-h");
if (help) {
  printHelp();
  process.exit(0);
}

const cmd = process.argv[2] || "";
if (!cmd || cmd === "help") {
  printHelp();
  process.exit(cmd ? 0 : 1);
}

if (cmd !== "init") {
  console.error(`Comando non riconosciuto: ${cmd}`);
  printHelp();
  process.exit(1);
}

const outDir = path.resolve(process.cwd(), getArg("--out-dir") || "accessibilita");
const configPath = path.resolve(process.cwd(), "agid-accessibilita.config.json");

const ente = await ask("Nome organizzazione (azienda/ente)", "Nome organizzazione");
const sito = await ask("URL sito (https://...)", "https://www.esempio.it");
const email = await ask("Email accessibilita (mailto)", "accessibilita@esempio.it");
const basePath = await ask("Percorso pubblico (es. /accessibilita)", "/accessibilita");

const cfg = { ente, sito, email, basePath, outDir };
fs.writeFileSync(configPath, JSON.stringify(cfg, null, 2), "utf8");

const p1 = writeFile(outDir, "dichiarazione-accessibilita.html", renderDichiarazioneHtml(cfg));
const p2 = writeFile(outDir, "feedback-accessibilita.html", renderFeedbackHtml(cfg));
const p3 = writeFile(outDir, "footer-snippet.html", renderFooterSnippet(cfg));
const p4 = writeFile(outDir, "CHECKLIST.md", renderChecklistMd());

console.log("OK. File generati:");
console.log(`- ${p1}`);
console.log(`- ${p2}`);
console.log(`- ${p3}`);
console.log(`- ${p4}`);
console.log("");
console.log("Suggerimento: incolla il contenuto di footer-snippet.html nel footer del sito.");


import assert from "node:assert/strict";
import { renderFooterSnippet, renderDichiarazioneHtml, renderFeedbackHtml } from "../src/templates.js";

try {
  const snippet = renderFooterSnippet({ basePath: "/accessibilita" });
  assert.equal(snippet.includes("Dichiarazione di accessibilita"), true);
  assert.equal(snippet.includes("Feedback accessibilita"), true);

  const d = renderDichiarazioneHtml({ ente: "X", sito: "https://x.it", email: "a@x.it", basePath: "/a" });
  assert.equal(d.includes("<h1>Dichiarazione di accessibilita</h1>"), true);
  assert.equal(d.includes("mailto:a@x.it"), true);

  const f = renderFeedbackHtml({ ente: "X", sito: "https://x.it", email: "a@x.it" });
  assert.equal(f.includes("<h1>Feedback accessibilita</h1>"), true);
  assert.equal(f.includes("mailto:a@x.it"), true);

  console.log("OK: 3/3 test passati");
} catch (e) {
  console.error("ERRORE TEST:", e.message);
  process.exit(1);
}


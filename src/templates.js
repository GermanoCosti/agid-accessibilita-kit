export function renderFooterSnippet({ basePath = "/accessibilita" } = {}) {
  const b = String(basePath || "/accessibilita").replace(/\/+$/, "");
  return `<!-- Snippet footer (bozza) -->\n` +
    `<a href="${b}/dichiarazione-accessibilita.html">Dichiarazione di accessibilita</a>\n` +
    `<span aria-hidden="true"> | </span>\n` +
    `<a href="${b}/feedback-accessibilita.html">Feedback accessibilita</a>\n`;
}

export function renderDichiarazioneHtml({
  ente = "Nome organizzazione",
  sito = "https://www.esempio.it",
  email = "accessibilita@esempio.it",
  basePath = "/accessibilita"
} = {}) {
  const b = String(basePath || "/accessibilita").replace(/\/+$/, "");
  return `<!doctype html>
<html lang="it">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Dichiarazione di accessibilita - ${ente}</title>
  </head>
  <body>
    <main>
      <h1>Dichiarazione di accessibilita</h1>
      <p><strong>Organizzazione:</strong> ${ente}</p>
      <p><strong>Sito/app:</strong> <a href="${sito}">${sito}</a></p>

      <h2>Stato di conformita (bozza)</h2>
      <p>Questa e' una bozza. Compila e pubblica la dichiarazione secondo le procedure ufficiali applicabili.</p>

      <h2>Feedback e contatti</h2>
      <p>Per segnalazioni relative all'accessibilita: <a href="mailto:${email}">${email}</a></p>
      <p>Pagina feedback: <a href="${b}/feedback-accessibilita.html">${b}/feedback-accessibilita.html</a></p>

      <h2>Data</h2>
      <p>Ultimo aggiornamento: <span data-placeholder="data-aggiornamento">____-__-__</span></p>
    </main>
  </body>
</html>
`;
}

export function renderFeedbackHtml({
  ente = "Nome organizzazione",
  email = "accessibilita@esempio.it",
  sito = "https://www.esempio.it"
} = {}) {
  return `<!doctype html>
<html lang="it">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Feedback accessibilita - ${ente}</title>
  </head>
  <body>
    <main>
      <h1>Feedback accessibilita</h1>
      <p>Se hai incontrato un problema di accessibilita su <a href="${sito}">${sito}</a>, puoi contattarci.</p>

      <h2>Email</h2>
      <p>Scrivi a: <a href="mailto:${email}">${email}</a></p>

      <h2>Cosa indicare nella segnalazione</h2>
      <ul>
        <li>Pagina (URL) dove hai avuto il problema</li>
        <li>Dispositivo e browser</li>
        <li>Tecnologia assistiva (se usata)</li>
        <li>Descrizione del problema</li>
      </ul>
    </main>
  </body>
</html>
`;
}

export function renderChecklistMd() {
  return `# Checklist accessibilita (bozza)\n\n` +
    `- Link nel footer a Dichiarazione di accessibilita\n` +
    `- Canale feedback (email/form) funzionante\n` +
    `- Attributo lang su <html>\n` +
    `- Presenza di un <h1> principale\n` +
    `- Immagini con alt appropriato\n` +
    `- Form con label/aria-label\n` +
    `- Link e pulsanti con nome accessibile\n`;
}

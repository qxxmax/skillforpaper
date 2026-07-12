import fs from "node:fs/promises";
import path from "node:path";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const payload = JSON.parse(await fs.readFile(path.join(root, "workbook_data.json"), "utf8"));
const workbook = Workbook.create();

const NAVY = "#26364D";
const GREEN = "#2F7D6D";
const BLUSH = "#D94F70";
const GOLD = "#E2A93B";
const PALE = "#EEF3F5";
const INK = "#1F2933";
const LINE = "#D8E0E5";

function colLetter(index) {
  let value = index;
  let output = "";
  while (value > 0) {
    const remainder = (value - 1) % 26;
    output = String.fromCharCode(65 + remainder) + output;
    value = Math.floor((value - 1) / 26);
  }
  return output;
}

function columnWidth(header) {
  const key = header.toLowerCase();
  if (key.includes("title")) return 42;
  if (key.includes("author")) return 34;
  if (key.includes("url") || key.includes("path") || key.includes("sha")) return 38;
  if (["problem", "method", "result", "limitation", "claim", "boundary", "screen_reason", "relation_basis", "supported_content", "next_search_or_experiment", "why_it_matters"].some((token) => key.includes(token))) return 46;
  if (key.includes("anchor") || key.includes("context") || key.includes("evidence_ids")) return 30;
  if (key.includes("status") || key.includes("decision") || key.includes("family") || key.includes("cluster") || key.includes("facet")) return 20;
  if (key.includes("id") || key === "year" || key === "count" || key === "pages" || key === "score") return 14;
  return 18;
}

function safeTableName(name) {
  return `${name.replace(/[^A-Za-z0-9]/g, "")}Table`;
}

const summary = workbook.worksheets.add("Summary");

for (const [sheetName, block] of Object.entries(payload.sheets)) {
  const sheet = workbook.worksheets.add(sheetName);
  const matrix = [block.headers, ...block.rows];
  const rows = matrix.length;
  const cols = block.headers.length;
  const used = sheet.getRangeByIndexes(0, 0, rows, cols);
  used.values = matrix;
  used.format = {
    font: { name: "Aptos", size: 9, color: INK },
    verticalAlignment: "top",
    wrapText: true,
    borders: { insideHorizontal: { style: "thin", color: LINE } },
  };
  const header = sheet.getRangeByIndexes(0, 0, 1, cols);
  header.format = {
    fill: NAVY,
    font: { name: "Aptos Display", size: 10, bold: true, color: "#FFFFFF" },
    verticalAlignment: "center",
    wrapText: true,
    borders: { bottom: { style: "medium", color: GREEN } },
  };
  header.format.rowHeight = 30;
  const body = rows > 1 ? sheet.getRangeByIndexes(1, 0, rows - 1, cols) : null;
  if (body) {
    body.format.rowHeight = ["Reading Notes", "Evidence", "Claims", "Gaps", "Relations Core", "Relations All"].includes(sheetName) ? 58 : 34;
  }
  for (let index = 0; index < cols; index += 1) {
    sheet.getRangeByIndexes(0, index, rows, 1).format.columnWidth = columnWidth(block.headers[index]);
  }
  sheet.freezePanes.freezeRows(1);
  if (cols > 6) sheet.freezePanes.freezeColumns(2);
  sheet.showGridLines = false;
  const address = `A1:${colLetter(cols)}${rows}`;
  if (sheetName === "Relations All") {
    if (body) body.format.fill = "#FFFFFF";
  } else {
    const table = sheet.tables.add(address, true, safeTableName(sheetName));
    table.style = "TableStyleMedium2";
  }
}

summary.showGridLines = false;
summary.getRange("A1:K2").merge();
summary.getRange("A1").values = [["SPS literature audit — clean-room run"]];
summary.getRange("A1:K2").format = {
  fill: NAVY,
  font: { name: "Aptos Display", size: 22, bold: true, color: "#FFFFFF" },
  verticalAlignment: "center",
  horizontalAlignment: "left",
};

const sourcesRows = payload.sheets.Sources.rows.length + 1;
const candidateRows = payload.sheets.Candidates.rows.length + 1;
const evidenceRows = payload.sheets.Evidence.rows.length + 1;

const cards = [
  { labelRange: "A4:C4", valueRange: "A5:C6", label: "Verified full texts", formula: `=COUNTA('Sources'!A2:A${sourcesRows})`, fill: GREEN },
  { labelRange: "E4:G4", valueRange: "E5:G6", label: "Deduplicated candidates", formula: `=COUNTA('Candidates'!A2:A${candidateRows})`, fill: GOLD },
  { labelRange: "I4:K4", valueRange: "I5:K6", label: "Evidence anchors", formula: `=COUNTA('Evidence'!A2:A${evidenceRows})`, fill: BLUSH },
];
for (const card of cards) {
  summary.getRange(card.labelRange).merge();
  summary.getRange(card.valueRange).merge();
  summary.getRange(card.labelRange).values = [[card.label]];
  summary.getRange(card.valueRange).formulas = [[card.formula]];
  summary.getRange(card.labelRange).format = {
    fill: PALE,
    font: { bold: true, color: NAVY, size: 10 },
    horizontalAlignment: "center",
    verticalAlignment: "center",
    borders: { top: { style: "thin", color: card.fill }, left: { style: "thin", color: card.fill }, right: { style: "thin", color: card.fill } },
  };
  summary.getRange(card.valueRange).format = {
    fill: "#FFFFFF",
    font: { bold: true, color: card.fill, size: 24 },
    horizontalAlignment: "center",
    verticalAlignment: "center",
    numberFormat: "#,##0",
    borders: { bottom: { style: "medium", color: card.fill }, left: { style: "thin", color: card.fill }, right: { style: "thin", color: card.fill } },
  };
}

summary.getRange("A8:B8").values = [["Audit stage", "Count"]];
summary.getRange("A8:B8").format = { fill: NAVY, font: { bold: true, color: "#FFFFFF" } };
for (let i = 0; i < 6; i += 1) {
  const row = 9 + i;
  const sourceRow = 2 + i;
  summary.getRange(`A${row}:B${row}`).formulas = [[`='Funnel'!A${sourceRow}`, `='Funnel'!B${sourceRow}`]];
}
summary.getRange("A9:B14").format = { borders: { insideHorizontal: { style: "thin", color: LINE } } };
summary.getRange("B9:B14").format.numberFormat = "#,##0";
summary.getRange("A8:B14").format.columnWidth = 24;

const chart = summary.charts.add("bar", summary.getRange("A8:B14"));
chart.title = "671 records → 31 verified full texts";
chart.hasLegend = false;
chart.xAxis = { axisType: "textAxis", textStyle: { fontSize: 9 } };
chart.yAxis = { numberFormatCode: "#,##0" };
chart.setPosition("D8", "K22");

summary.getRange("A24:B24").values = [["Method family", "Full-text papers"]];
summary.getRange("A24:B24").format = { fill: NAVY, font: { bold: true, color: "#FFFFFF" } };
const families = ["Path-space control", "Normalizing flows", "Stochastic flows", "Diffusion", "Autoregressive", "Scaling / multiscale", "Diagnostics / theory", "SPS"];
for (let i = 0; i < families.length; i += 1) {
  const row = 25 + i;
  summary.getRange(`A${row}`).values = [[families[i]]];
  summary.getRange(`B${row}`).formulas = [[`=COUNTIF('Sources'!E$2:E$${sourcesRows},A${row})`]];
}
summary.getRange("A24:B32").format = { borders: { insideHorizontal: { style: "thin", color: LINE } } };
summary.getRange("B25:B32").format.numberFormat = "0";
summary.getRange("A35:K35").merge();
summary.getRange("A35").values = [["Boundary: auditable coverage under the declared scope; SPS forward citations remain on monitor."]];
summary.getRange("A35:K35").format = {
  fill: "#FFF5E6",
  font: { bold: true, color: "#7A4E00", size: 10 },
  wrapText: true,
  borders: { left: { style: "medium", color: GOLD } },
};
summary.getRange("A1:K35").format.font.name = "Aptos";
summary.getRange("A:A").format.columnWidth = 25;
summary.getRange("B:B").format.columnWidth = 15;
summary.freezePanes.freezeRows(2);

const summaryInspect = await workbook.inspect({
  kind: "table",
  range: "Summary!A1:K35",
  include: "values,formulas",
  tableMaxRows: 35,
  tableMaxCols: 11,
  maxChars: 7000,
});
console.log(summaryInspect.ndjson);

const errorInspect = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 300 },
  summary: "final formula error scan",
});
console.log(errorInspect.ndjson);

const qaDir = path.join(root, "qa_workbook");
await fs.mkdir(qaDir, { recursive: true });
const sheetNames = ["Summary", ...Object.keys(payload.sheets)];
for (const sheetName of sheetNames) {
  const block = payload.sheets[sheetName];
  const range = sheetName === "Summary"
    ? "A1:K35"
    : `A1:${colLetter(Math.min(block.headers.length, 10))}${Math.min(block.rows.length + 1, 18)}`;
  const preview = await workbook.render({ sheetName, range, scale: 1, format: "png" });
  const safe = sheetName.replace(/[^A-Za-z0-9]+/g, "_").toLowerCase();
  await fs.writeFile(path.join(qaDir, `${safe}.png`), new Uint8Array(await preview.arrayBuffer()));
}

const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(path.join(root, "sps_literature_audit_cleanroom.xlsx"));
console.log(`exported ${path.join(root, "sps_literature_audit_cleanroom.xlsx")}`);

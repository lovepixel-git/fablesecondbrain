import { readdir, readFile, writeFile } from "node:fs/promises"
import { extname, join } from "node:path"
import { fileURLToPath } from "node:url"

// Post-build sanitizer for the published output. Two jobs:
// 1. strip inline data source maps so no absolute build paths ship
// 2. genericize internal vault folder references (.raw/, references/*) so a
//    shared build does not expose the repository's internal folder layout
const publicDir = fileURLToPath(new URL("../public/", import.meta.url))
const targetExtensions = new Set([".html", ".js", ".css", ".json", ".xml"])

// [pattern, replacement] applied in order; most specific patterns first
const replacements = [
  [/[ \t]*\/\/# sourceMappingURL=data:[^<\r\n]*/g, ""],
  [/[ \t]*\/\*# sourceMappingURL=data:[\s\S]*?\*\//g, ""],
  [/\.raw\/\.manifest\.json/g, "the source manifest"],
  [/\.raw\/sources\//g, "the immutable source store"],
  [/\.raw\//g, "the immutable source layer"],
  [/references\/source-ledger\.json/g, "the source ledger"],
  [/references\/claim-ledger\.md/g, "the claim ledger"],
  [/references\/CONFIDENCE_TAGS\.md/g, "the confidence tags reference"],
  [/references\/canon/g, "the canon layer"],
]

let scanned = 0
let updated = 0

async function walk(dir) {
  const entries = await readdir(dir, { withFileTypes: true })

  for (const entry of entries) {
    const fullPath = join(dir, entry.name)

    if (entry.isDirectory()) {
      await walk(fullPath)
      continue
    }

    if (!entry.isFile() || !targetExtensions.has(extname(entry.name))) {
      continue
    }

    scanned += 1
    const original = await readFile(fullPath, "utf8")
    const sanitized = replacements.reduce((text, [pattern, value]) => text.replace(pattern, value), original)

    if (sanitized !== original) {
      await writeFile(fullPath, sanitized)
      updated += 1
    }
  }
}

await walk(publicDir)
console.log(`Sanitized ${updated} of ${scanned} public files (source maps + folder references).`)

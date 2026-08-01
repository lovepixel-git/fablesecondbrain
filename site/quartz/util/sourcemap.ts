import fs from "fs"
import sourceMapSupport from "source-map-support"
import { fileURLToPath } from "url"

export const options: sourceMapSupport.Options = {
  // source map hack to get around query param
  // import cache busting
  retrieveSourceMap(source) {
    if (source.includes(".quartz-cache")) {
      let realSource = fileURLToPath(source.split("?", 2)[0] + ".map")
      // On a plain `quartz build` (no --serve) esbuild does not emit a .map,
      // so guard the read: a missing map must not crash the build.
      if (!fs.existsSync(realSource)) {
        return null
      }
      return {
        map: fs.readFileSync(realSource, "utf8"),
      }
    } else {
      return null
    }
  },
}

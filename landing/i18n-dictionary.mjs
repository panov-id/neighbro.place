// Shared access to the landing's i18n dictionary.
//
// The dictionary lives as an object literal (`var T = { … }`) inside index.html rather
// than in a separate file, so both the completeness check and the page generator have to
// read it out of the markup. Doing that in one place keeps them from drifting apart.

// Return the source text of the `T = { … }` literal, located by balancing braces while
// skipping over string contents (a brace inside a translation must not end the object).
export function extractDictionarySource(html) {
  const declaration = html.match(/\b(?:const|let|var)\s+T\s*=\s*\{/);
  if (!declaration) throw new Error("could not find the T dictionary");

  const start = declaration.index + declaration[0].length - 1;
  let depth = 0;
  let insideString = null;

  for (let position = start; position < html.length; position++) {
    const character = html[position];
    const previous = html[position - 1];

    if (insideString) {
      if (character === insideString && previous !== "\\") insideString = null;
      continue;
    }
    if (character === '"' || character === "'" || character === "`") insideString = character;
    else if (character === "{") depth++;
    else if (character === "}") {
      depth--;
      if (depth === 0) return html.slice(start, position + 1);
    }
  }
  throw new Error("unbalanced braces in T");
}

// Evaluate that literal into a plain object: { [language]: { [key]: translation } }.
export function readDictionary(html) {
  return Function("return (" + extractDictionarySource(html) + ")")();
}

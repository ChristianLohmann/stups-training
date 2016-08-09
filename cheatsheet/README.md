# Cheatsheet generator

Replaces Pokemon placeholders (using Pystache) with real Pokemon data. Currently available: `pokemonName`, `pokemonImage` (base64 encoded PNG). Saves result to `./STUPS_cheatsheet_<pokedex>.svg`.

Usage:

    python -m create.py --start <start pokedex number> --end <exclusive end pokedex number> --file <path to template>

Defaults:

* Start: 1
* End: 10
* File: `./SUPTS_cheatsheet.svg`

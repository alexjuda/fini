# 🐜 fini

Get stuff _fini_-shed. Tiny CLI for hard working ants.

## Idea

Keep your daily todos as plain text markdown files. Edit them with your favorite `$EDITOR`. Roll
over unfinished todos from the previous day. Keep files under a git repo synchronized with GitHub.

## Commands

```bash
export FINI_DIR="~/Documents/fini-todos"

# Opens up a daily todo file in your $EDITOR.
fini edit

# Makes a commit & pushes to origin.
fini sync

# Finds the todo file from a previous day and copies over for today.
fini rollover

# fini rollover + fini edit + fini sync
fini
```

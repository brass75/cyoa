set quiet

# Run a story
story story="story.json":
    uv run cyoa {{ story }} 

# lint & format
ruff:
  #! /bin/bash
  echo "Running lint and format ..."
  uvx ruff check . --fix --exit-non-zero-on-fix
  rc=$?
  uvx ruff format .
  if [[ $rc != 0 ]]; then
    uvx ruff check .
  fi
  echo "... Done"

# Run basedpyright
[no-quiet]
bpr:
  uvx basedpyright .

# Run ty
[no-quiet]
ty:
  uvx ty check .

# Run all type checks
types: ty bpr


# Run all checks
checks: ruff types

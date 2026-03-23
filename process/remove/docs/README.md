# remove

Drop unneeded columns with `remove_columns(...)`.

## What It Teaches

- Removing columns simplifies a dataset schema.
- This is useful after preprocessing when intermediate fields are no longer needed.
- Narrower schemas are easier to inspect and pass to downstream code.

## Run

From the repository root:

```bash
uv run python process/remove/src/main.py
```

## Expected Result

The script prints:

- the cleaned dataset summary
- the remaining column names
- rows without the removed `debug_note` column

## Notes

- Column removal is often paired with `map`, where temporary columns may be created first.

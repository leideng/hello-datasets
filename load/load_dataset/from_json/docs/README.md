# load_dataset from_json

Load a local JSON Lines file with `load_dataset("json", ...)`.

## What It Teaches

- `load_dataset` can use a built-in JSON loader.
- Local JSON data is commonly stored as JSON Lines, with one object per line.
- `load_dataset(...)` usually returns a `DatasetDict`, even for a single file.

## Files

- `data/sample.jsonl` contains the local example data.
- `src/main.py` loads the file and prints summary information.

## Run

From the repository root:

```bash
uv run python load/load_dataset/from_json/src/main.py
```

## Expected Result

The script prints:

- the returned `DatasetDict`
- the train split summary
- the inferred features
- the first record

## Notes

- The default split name is often `train` when loading a single local file this way.
- JSON Lines is usually easier to stream and process than a single huge JSON array.

# load_dataset from_webdataset

Load a local tar shard in WebDataset format with `load_dataset("webdataset", ...)`.

## What It Teaches

- WebDataset stores one example across multiple files that share the same prefix.
- File extensions become dataset fields such as `txt` or `json`.
- A tar archive is enough for a minimal local example.

## Run

From the repository root:

```bash
uv run python load/load_dataset/from_webdataset/src/main.py
```

## Expected Result

The script:

- creates a local tar shard in WebDataset format
- loads it with the packaged `webdataset` loader
- prints the inferred features and first example

## Notes

- Files such as `sample-0001.txt` and `sample-0001.json` are grouped into one example.
- This example uses text and JSON fields because they decode cleanly without optional media dependencies.

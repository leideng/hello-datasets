# load_dataset from_arrow

Load a local Apache Arrow file with `load_dataset("arrow", ...)`.

## What It Teaches

- `load_dataset` can read Arrow IPC files directly.
- Arrow is the native columnar format used internally by `datasets`.
- A local Arrow file is useful when you already have a columnar preprocessing step.

## Run

From the repository root:

```bash
uv run python load/load_dataset/from_arrow/main.py
```

## Expected Result

The script:

- creates a small local Arrow file in `data/`
- loads it with `load_dataset`
- prints the inferred schema and a sample row

## Notes

- The script writes the Arrow file on demand so the example stays self-contained.
- This example uses a local cache directory under the example folder.

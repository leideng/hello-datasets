# load_dataset from_csv

Load a local CSV file with `load_dataset("csv", ...)`.

## What It Teaches

- `load_dataset` has a built-in CSV loader.
- A local CSV file is enough to start experimenting with dataset ingestion.
- The result is usually a `DatasetDict` with a `train` split for a single file input.

## Files

- `data/sample.csv` contains the example input file.
- `main.py` loads the CSV and prints dataset information.

## Run

From the repository root:

```bash
uv run python load/load_dataset/from_csv/main.py
```

## Expected Result

The script prints:

- the `DatasetDict`
- the inferred schema
- the first two rows

## Notes

- CSV is often the quickest way to explore `load_dataset` with local structured data.
- Once loaded, you can immediately use `map`, `filter`, `shuffle`, and export methods.

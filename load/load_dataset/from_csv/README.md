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

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from pathlib import Path`
  Imports `Path` so local files such as `data/` inputs and cache directories can be built safely.
- Line 3: `from datasets import load_dataset`
  Imports `load_dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 6: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 7: `    data_file = Path(__file__).resolve().parent / "data" / "sample.csv"`
  Builds the path to the local sample data used by the example.
- Line 8: `    cache_dir = Path(__file__).resolve().parent / ".cache"`
  Keeps generated cache artifacts inside this example folder instead of a global location.
- Line 10: `    dataset_dict = load_dataset(`
  Calls `load_dataset(...)`, the core loader used to read this data format.
- Line 15: `    train_dataset = dataset_dict["train"]`
  Pulls out the `train` split so the example can inspect the loaded records directly.
- Line 24: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- CSV is often the quickest way to explore `load_dataset` with local structured data.
- Once loaded, you can immediately use `map`, `filter`, `shuffle`, and export methods.

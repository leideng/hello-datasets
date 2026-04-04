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

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `from pathlib import Path`
  Imports `Path` so file and directory paths can be built in a platform-safe way.
- Line 3: `from datasets import load_dataset`
  Imports `load_dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 6: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 7: `    data_file = Path(__file__).resolve().parent / "data" / "sample.csv"`
  Builds the path to a local input file used by the example.
- Line 8: `    cache_dir = Path(__file__).resolve().parent / ".cache"`
  Creates a local cache path so generated dataset artifacts stay inside this example folder.
- Line 10: `    dataset_dict = load_dataset(`
  Calls `load_dataset(...)` to load data with one of the built-in dataset loaders.
- Line 11: `        "csv",`
  Provides one literal sample value used by the example data or configuration.
- Line 12: `        data_files=str(data_file),`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 13: `        cache_dir=str(cache_dir),`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 14: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 15: `    train_dataset = dataset_dict["train"]`
  Selects the loaded `train` split so the example can inspect it directly.
- Line 17: `    print("Dataset loaded with load_dataset('csv', data_files=...)")`
  Prints information so you can observe what the dataset operation produced.
- Line 18: `    print(dataset_dict)`
  Prints information so you can observe what the dataset operation produced.
- Line 19: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 20: `    print("Features:", train_dataset.features)`
  Prints information so you can observe what the dataset operation produced.
- Line 21: `    print("Rows 0 and 1:", train_dataset[:2])`
  Prints information so you can observe what the dataset operation produced.
- Line 24: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 25: `    main()`
  Calls `main()` to start the example.

## Notes

- CSV is often the quickest way to explore `load_dataset` with local structured data.
- Once loaded, you can immediately use `map`, `filter`, `shuffle`, and export methods.

# load_dataset from_json

Load a local JSON Lines file with `load_dataset("json", ...)`.

## What It Teaches

- `load_dataset` can use a built-in JSON loader.
- Local JSON data is commonly stored as JSON Lines, with one object per line.
- `load_dataset(...)` usually returns a `DatasetDict`, even for a single file.

## Files

- `data/sample.jsonl` contains the local example data.
- `main.py` loads the file and prints summary information.

## Run

From the repository root:

```bash
uv run python load/load_dataset/from_json/main.py
```

## Expected Result

The script prints:

- the returned `DatasetDict`
- the train split summary
- the inferred features
- the first record

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `from pathlib import Path`
  Imports `Path` so file and directory paths can be built in a platform-safe way.
- Line 3: `from datasets import load_dataset`
  Imports `load_dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 6: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 7: `    data_file = Path(__file__).resolve().parent / "data" / "sample.jsonl"`
  Builds the path to a local input file used by the example.
- Line 8: `    cache_dir = Path(__file__).resolve().parent / ".cache"`
  Creates a local cache path so generated dataset artifacts stay inside this example folder.
- Line 10: `    dataset_dict = load_dataset(`
  Calls `load_dataset(...)` to load data with one of the built-in dataset loaders.
- Line 11: `        "json",`
  Provides one literal sample value used by the example data or configuration.
- Line 12: `        data_files=str(data_file),`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 13: `        cache_dir=str(cache_dir),`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 14: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 15: `    train_dataset = dataset_dict["train"]`
  Selects the loaded `train` split so the example can inspect it directly.
- Line 17: `    print("Dataset loaded with load_dataset('json', data_files=...)")`
  Prints information so you can observe what the dataset operation produced.
- Line 18: `    print(dataset_dict)`
  Prints information so you can observe what the dataset operation produced.
- Line 19: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 20: `    print("Train split:", train_dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 21: `    print("Features:", train_dataset.features)`
  Prints information so you can observe what the dataset operation produced.
- Line 22: `    print("First row:", train_dataset[0])`
  Prints information so you can observe what the dataset operation produced.
- Line 25: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 26: `    main()`
  Calls `main()` to start the example.

## Notes

- The default split name is often `train` when loading a single local file this way.
- JSON Lines is usually easier to stream and process than a single huge JSON array.

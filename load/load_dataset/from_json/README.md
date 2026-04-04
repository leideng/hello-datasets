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

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from pathlib import Path`
  Imports `Path` so local files such as `data/` inputs and cache directories can be built safely.
- Line 3: `from datasets import load_dataset`
  Imports `load_dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 6: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 7: `    data_file = Path(__file__).resolve().parent / "data" / "sample.jsonl"`
  Builds the path to the local sample data used by the example.
- Line 8: `    cache_dir = Path(__file__).resolve().parent / ".cache"`
  Keeps generated cache artifacts inside this example folder instead of a global location.
- Line 10: `    dataset_dict = load_dataset(`
  Calls `load_dataset(...)`, the core loader used to read this data format.
- Line 15: `    train_dataset = dataset_dict["train"]`
  Pulls out the `train` split so the example can inspect the loaded records directly.
- Line 25: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- The default split name is often `train` when loading a single local file this way.
- JSON Lines is usually easier to stream and process than a single huge JSON array.

# load overview

Compare the main beginner-friendly dataset loading entry points in one small example.

## What It Teaches

- `load_dataset(...)` is the standard entry point for files, URLs, and Hub datasets.
- `Dataset.from_dict(...)` is useful when your data already exists in Python memory.
- `Dataset.from_generator(...)` is useful when rows are produced by code instead of read from a file.

## Files

- `data/sample.jsonl` contains a tiny local file for the `load_dataset(...)` example.
- `main.py` loads one dataset with each API and prints a short comparison.

## Run

From the repository root:

```bash
uv run python topics/01-load/overview/main.py
```

## Expected Result

The script prints:

- one dataset loaded from a local JSON Lines file
- one dataset created from an in-memory Python dictionary
- one dataset created from a Python generator
- the first row from each dataset

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from pathlib import Path`
  Imports `Path` so local files and cache directories can be built safely.
- Line 3: `from datasets import Dataset, load_dataset`
  Imports the two main loading APIs compared by this example.
- Line 6: `def generate_rows():`
  Defines a tiny generator that yields row dictionaries one at a time.
- Line 12: `    example_dir = Path(__file__).resolve().parent`
  Finds the example folder so local paths stay self-contained.
- Line 16: `    file_dataset = load_dataset(...)[\"train\"]`
  Loads a local file with the standard `load_dataset(...)` workflow.
- Line 17: `    dict_dataset = Dataset.from_dict(...)`
  Creates a dataset directly from Python column data already in memory.
- Line 18: `    generator_dataset = Dataset.from_generator(...)`
  Builds a dataset from rows yielded by Python code.
- Line 28: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- These three APIs cover most beginner loading workflows.
- The stored dataset interface is the same after loading, even though the input source is different.
- Start with `load_dataset(...)` for external data and `Dataset.from_*` when your data is already inside Python.

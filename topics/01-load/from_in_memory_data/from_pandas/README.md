# from_pandas

Create a Hugging Face `Dataset` from a Pandas DataFrame.

## What It Teaches

- `Dataset.from_pandas(...)` converts tabular in-memory data into a dataset.
- Pandas is convenient when data cleaning already happened in a DataFrame workflow.
- `preserve_index=False` avoids turning the DataFrame index into an extra dataset column.

## Run

From the repository root:

```bash
uv run python topics/01-load/from_in_memory_data/from_pandas/main.py
```

## Expected Result

The script prints:

- a dataset summary
- the inferred feature schema
- one example row

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `import pandas as pd`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 2: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 5: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 14: `    dataset = Dataset.from_pandas(dataframe, preserve_index=False)`
  Converts a pandas DataFrame into a Hugging Face dataset.
- Line 23: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- If you keep the index, it may appear as an extra column.
- This is a useful bridge when moving from Pandas-based exploration into `datasets`.

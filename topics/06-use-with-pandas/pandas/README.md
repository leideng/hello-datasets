# tabular_format pandas

Convert a dataset to a Pandas DataFrame with `to_pandas()`.

## What It Teaches

- `to_pandas()` is a convenient bridge into the Pandas ecosystem.
- This is useful for quick inspection, plotting, and familiar dataframe workflows.
- The conversion materializes the data as a DataFrame.

## Run

From the repository root:

```bash
uv run python topics/06-use-with-pandas/pandas/main.py
```

## Expected Result

The script prints:

- the dataset summary
- the resulting DataFrame type
- the DataFrame contents

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `import pandas as pd`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 2: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 5: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 6: `    dataset = Dataset.from_dict(`
  Creates a tiny in-memory dataset so the transformation can be demonstrated without external files.
- Line 23: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- Use this when you specifically want Pandas operations, not when you need to stay in `datasets`.

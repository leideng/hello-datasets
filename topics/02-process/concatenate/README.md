# concatenate

Combine multiple datasets with `concatenate_datasets(...)`.

## What It Teaches

- Datasets with the same schema can be stacked vertically.
- Concatenation is useful when merging shards or appending extra examples.
- All input datasets should have compatible columns and feature types.

## Run

From the repository root:

```bash
uv run python topics/02-process/concatenate/main.py
```

## Expected Result

The script prints:

- the combined dataset summary
- all rows from both source datasets in order

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from datasets import Dataset, concatenate_datasets`
  Imports `Dataset, concatenate_datasets` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 4: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 5: `    train_like = Dataset.from_dict(`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 11: `    extra_like = Dataset.from_dict(`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 26: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- This operation keeps row order unless you shuffle afterward.

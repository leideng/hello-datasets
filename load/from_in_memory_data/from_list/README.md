# from_list

Create a Hugging Face `Dataset` from a row-oriented Python list of dictionaries.

## What It Teaches

- `Dataset.from_list(...)` works well when your data starts as records.
- Each dictionary in the list represents one row.
- Feature types are inferred from the Python values.

## Run

From the repository root:

```bash
uv run python load/from_in_memory_data/from_list/main.py
```

## Expected Result

The script prints:

- a short dataset summary
- the column names
- one sample row

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 4: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 11: `    dataset = Dataset.from_list(records)`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 20: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- Compared with `from_dict`, this input is row-oriented instead of column-oriented.
- This is usually more convenient when prototyping from JSON-like records.

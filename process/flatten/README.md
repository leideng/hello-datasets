# flatten

Expand nested struct columns with `Dataset.flatten(...)`.

## What It Teaches

- Nested dictionary-like columns can be expanded into top-level columns.
- Flattening is useful before export or when downstream code expects simple schemas.
- Nested fields become dotted column names such as `meta.title`.

## Run

From the repository root:

```bash
uv run python process/flatten/main.py
```

## Expected Result

The script prints:

- the flattened dataset summary
- top-level columns such as `meta.title` and `meta.difficulty`

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 4: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 5: `    dataset = Dataset.from_dict(`
  Creates a tiny in-memory dataset so the transformation can be demonstrated without external files.
- Line 15: `    flattened_dataset = dataset.flatten()`
  Flattens nested fields into top-level columns.
- Line 24: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- Flattening is especially useful after loading nested JSON-like records.

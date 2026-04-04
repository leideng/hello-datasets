# cast

Change the dataset feature schema with `cast(...)`.

## What It Teaches

- `cast` lets you replace inferred features with an explicit schema.
- `ClassLabel` is useful for categorical targets such as sentiment classes.
- Explicit feature definitions make the dataset easier to interpret downstream.

## Run

From the repository root:

```bash
uv run python topics/02-process/cast/main.py
```

## Expected Result

The script prints:

- the cast dataset summary
- the updated features
- the decoded human-readable class names

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from datasets import ClassLabel, Dataset, Features, Value`
  Imports `ClassLabel, Dataset, Features, Value` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 4: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 5: `    dataset = Dataset.from_dict(`
  Creates a tiny in-memory dataset so the transformation can be demonstrated without external files.
- Line 23: `    cast_dataset = dataset.cast(target_features)`
  Casts columns to an explicit feature schema.
- Line 32: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- Casting is most useful when inference does not capture the semantics you want.

# split

Create train and test subsets with `train_test_split(...)`.

## What It Teaches

- A single dataset can be split into a `DatasetDict`.
- `test_size` controls the fraction reserved for testing.
- A fixed `seed` makes the split reproducible.

## Run

From the repository root:

```bash
uv run python topics/02-process/split/main.py
```

## Expected Result

The script prints:

- the resulting `DatasetDict`
- the train rows
- the test rows

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 4: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 5: `    dataset = Dataset.from_dict(`
  Creates a tiny in-memory dataset so the transformation can be demonstrated without external files.
- Line 12: `    split_dataset = dataset.train_test_split(test_size=0.25, seed=13)`
  Splits one dataset into train and test partitions.
- Line 21: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- This is a common first step before training and evaluation.
- You can create validation splits the same way from the training subset.

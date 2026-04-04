# split

Create train and test subsets with `train_test_split(...)`.

## What It Teaches

- A single dataset can be split into a `DatasetDict`.
- `test_size` controls the fraction reserved for testing.
- A fixed `seed` makes the split reproducible.

## Run

From the repository root:

```bash
uv run python process/split/main.py
```

## Expected Result

The script prints:

- the resulting `DatasetDict`
- the train rows
- the test rows

## Notes

- This is a common first step before training and evaluation.
- You can create validation splits the same way from the training subset.

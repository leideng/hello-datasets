# select

Pick specific row indices with `Dataset.select(...)`.

## What It Teaches

- `select` keeps rows by position.
- It is useful for slicing examples, debugging, or building small subsets.
- The selected indices are zero-based positions in the dataset.

## Run

From the repository root:

```bash
uv run python process/select/src/main.py
```

## Expected Result

The script prints:

- the selected dataset summary
- only rows `0`, `2`, and `4`

## Notes

- `select` is different from `filter`: it uses explicit row indices instead of a predicate function.

# filter

Keep only rows that match a condition with `Dataset.filter(...)`.

## What It Teaches

- `filter` removes rows that do not satisfy a predicate.
- The filter function returns `True` to keep a row and `False` to drop it.
- Filtering is one of the most common cleanup steps before training or evaluation.

## Run

From the repository root:

```bash
uv run python process/filter/src/main.py
```

## Expected Result

The script prints:

- the filtered dataset summary
- only the rows whose `priority` is `high`

## Notes

- `filter` changes the number of rows.
- Prefer simple predicates first, then add more complex logic only when needed.

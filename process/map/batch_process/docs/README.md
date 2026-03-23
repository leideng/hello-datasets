# batch_process

Apply a batched transformation with `Dataset.map(..., batched=True)`.

## What It Teaches

- `map` can process examples one by one or in batches.
- Batched processing is often simpler and faster for vectorized transformations.
- A batched function receives lists for each input column and should return lists of equal length.

## Run

From the repository root:

```bash
uv run python process/map/batch_process/src/main.py
```

## Expected Result

The script prints:

- the transformed dataset summary
- the new column names
- the resulting rows with a derived `summary` column

## Notes

- Batched `map` is a common default when a transformation can be expressed over lists.
- The output batch length must match the input batch length unless you are intentionally changing row counts.

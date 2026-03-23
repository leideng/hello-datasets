# multi_split_process

Apply one map function across all splits in a `DatasetDict`.

## What It Teaches

- `DatasetDict.map(...)` applies the same transformation to every split.
- This is convenient when train, validation, and test need consistent preprocessing.
- The split structure stays intact after processing.

## Run

From the repository root:

```bash
uv run python process/map/multi_split_process/src/main.py
```

## Expected Result

The script prints:

- the transformed `DatasetDict`
- the processed train rows
- the processed test rows

## Notes

- This pattern is cleaner than looping over each split manually for simple shared preprocessing.

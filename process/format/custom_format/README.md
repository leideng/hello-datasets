# custom_format

Apply a custom retrieval-time transform with `with_transform(...)`.

## What It Teaches

- A dataset can transform rows when you read them, without rewriting the stored data.
- `with_transform(...)` is useful for presentation logic or lightweight preprocessing.
- The transform runs on retrieved batches rather than permanently changing the dataset.

## Run

From the repository root:

```bash
uv run python process/format/custom_format/main.py
```

## Expected Result

The script prints:

- the transformed dataset summary
- one transformed item
- a transformed slice

## Notes

- This is different from `map`, which creates a new dataset with stored transformed columns.

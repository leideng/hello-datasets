# data_augmentation

Use `map` to expand a dataset with augmented examples.

## What It Teaches

- Batched `map` can change the number of rows when used for augmentation.
- One input example can produce multiple output examples.
- This pattern is common for text normalization, paraphrasing, or synthetic variants.

## Run

From the repository root:

```bash
uv run python process/map/data_augmentation/src/main.py
```

## Expected Result

The script prints:

- a larger dataset than the input
- both original and augmented rows

## Notes

- When output row counts change, return lists whose lengths match the new number of rows.

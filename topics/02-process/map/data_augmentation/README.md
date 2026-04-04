# data_augmentation

Use `map` to expand a dataset with augmented examples.

## What It Teaches

- Batched `map` can change the number of rows when used for augmentation.
- One input example can produce multiple output examples.
- This pattern is common for text normalization, paraphrasing, or synthetic variants.

## Run

From the repository root:

```bash
uv run python topics/02-process/map/data_augmentation/main.py
```

## Expected Result

The script prints:

- a larger dataset than the input
- both original and augmented rows

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 4: `def augment_batch(batch: dict[str, list]) -> dict[str, list]:`
  Defines `augment_batch`, the function that groups one logical step of the example.
- Line 8: `    for text in batch["text"]:`
  Loops over example items to build or transform the dataset input.
- Line 12: `    return {`
  Returns the transformed value that the dataset API will store or use next.
- Line 18: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 19: `    dataset = Dataset.from_dict(`
  Creates a tiny in-memory dataset so the transformation can be demonstrated without external files.
- Line 28: `    augmented_dataset = dataset.map(augment_batch, batched=True, remove_columns=["text"])`
  Applies `map(...)` to create transformed columns or rows from the original dataset.
- Line 36: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- When output row counts change, return lists whose lengths match the new number of rows.

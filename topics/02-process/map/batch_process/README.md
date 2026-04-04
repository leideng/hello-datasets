# batch_process

Apply a batched transformation with `Dataset.map(..., batched=True)`.

## What It Teaches

- `map` can process examples one by one or in batches.
- Batched processing is often simpler and faster for vectorized transformations.
- A batched function receives lists for each input column and should return lists of equal length.

## Run

From the repository root:

```bash
uv run python topics/02-process/map/batch_process/main.py
```

## Expected Result

The script prints:

- the transformed dataset summary
- the new column names
- the resulting rows with a derived `summary` column

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 4: `def add_summary(batch: dict[str, list]) -> dict[str, list]:`
  Defines `add_summary`, the function that groups one logical step of the example.
- Line 5: `    return {`
  Returns the transformed value that the dataset API will store or use next.
- Line 8: `            for title, priority in zip(batch["title"], batch["priority"])`
  Loops over example items to build or transform the dataset input.
- Line 13: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 14: `    dataset = Dataset.from_dict(`
  Creates a tiny in-memory dataset so the transformation can be demonstrated without external files.
- Line 26: `    mapped_dataset = dataset.map(add_summary, batched=True, batch_size=2)`
  Applies `map(...)` to create transformed columns or rows from the original dataset.
- Line 35: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- Batched `map` is a common default when a transformation can be expressed over lists.
- The output batch length must match the input batch length unless you are intentionally changing row counts.

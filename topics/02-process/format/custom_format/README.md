# custom_format

Apply a custom retrieval-time transform with `with_transform(...)`.

## What It Teaches

- A dataset can transform rows when you read them, without rewriting the stored data.
- `with_transform(...)` is useful for presentation logic or lightweight preprocessing.
- The transform runs on retrieved batches rather than permanently changing the dataset.

## Run

From the repository root:

```bash
uv run python topics/02-process/format/custom_format/main.py
```

## Expected Result

The script prints:

- the transformed dataset summary
- one transformed item
- a transformed slice

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 4: `def build_preview(batch: dict[str, list]) -> dict[str, list]:`
  Defines `build_preview`, the function that groups one logical step of the example.
- Line 5: `    return {`
  Returns the transformed value that the dataset API will store or use next.
- Line 8: `            for identifier, text in zip(batch["id"], batch["text"])`
  Loops over example items to build or transform the dataset input.
- Line 13: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 14: `    dataset = Dataset.from_dict(`
  Creates a tiny in-memory dataset so the transformation can be demonstrated without external files.
- Line 30: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- This is different from `map`, which creates a new dataset with stored transformed columns.

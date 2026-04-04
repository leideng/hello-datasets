# filter

Keep only rows that match a condition with `Dataset.filter(...)`.

## What It Teaches

- `filter` removes rows that do not satisfy a predicate.
- The filter function returns `True` to keep a row and `False` to drop it.
- Filtering is one of the most common cleanup steps before training or evaluation.

## Run

From the repository root:

```bash
uv run python process/filter/main.py
```

## Expected Result

The script prints:

- the filtered dataset summary
- only the rows whose `priority` is `high`

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 4: `def keep_high_priority(example: dict[str, str]) -> bool:`
  Defines `keep_high_priority`, the function that groups one logical step of the example.
- Line 5: `    return example["priority"] == "high"`
  Returns the transformed value that the dataset API will store or use next.
- Line 8: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 9: `    dataset = Dataset.from_dict(`
  Creates a tiny in-memory dataset so the transformation can be demonstrated without external files.
- Line 22: `    filtered_dataset = dataset.filter(keep_high_priority)`
  Applies `filter(...)` to keep only rows that satisfy the condition.
- Line 30: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- `filter` changes the number of rows.
- Prefer simple predicates first, then add more complex logic only when needed.

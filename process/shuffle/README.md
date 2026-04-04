# shuffle

Randomize row order with `Dataset.shuffle(...)`.

## What It Teaches

- `shuffle` changes row order without changing row contents.
- Providing a fixed `seed` makes the result reproducible.
- Reproducibility matters for debugging and experiments.

## Run

From the repository root:

```bash
uv run python process/shuffle/main.py
```

## Expected Result

The script prints:

- the shuffled dataset summary
- the rows in deterministic shuffled order

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 4: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 5: `    dataset = Dataset.from_dict(`
  Creates a tiny in-memory dataset so the transformation can be demonstrated without external files.
- Line 18: `    shuffled_dataset = dataset.shuffle(seed=7)`
  Shuffles the row order to demonstrate randomized dataset access.
- Line 26: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- Always set a seed in learning examples so output is stable.

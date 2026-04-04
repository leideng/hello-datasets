# interleave

Mix rows from multiple datasets with `interleave_datasets(...)`.

## What It Teaches

- Interleaving alternates examples from multiple datasets.
- This is useful when mixing sources or balancing data streams.
- `stopping_strategy` controls how the function behaves when datasets have different lengths.

## Run

From the repository root:

```bash
uv run python process/interleave/main.py
```

## Expected Result

The script prints:

- the interleaved dataset summary
- rows alternating between the two sources

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from datasets import Dataset, interleave_datasets`
  Imports `Dataset, interleave_datasets` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 4: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 5: `    first_dataset = Dataset.from_dict(`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 11: `    second_dataset = Dataset.from_dict(`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 26: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- `all_exhausted` continues until every input dataset is exhausted.

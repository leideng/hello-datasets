# multi_split_process

Apply one map function across all splits in a `DatasetDict`.

## What It Teaches

- `DatasetDict.map(...)` applies the same transformation to every split.
- This is convenient when train, validation, and test need consistent preprocessing.
- The split structure stays intact after processing.

## Run

From the repository root:

```bash
uv run python topics/02-process/map/multi_split_process/main.py
```

## Expected Result

The script prints:

- the transformed `DatasetDict`
- the processed train rows
- the processed test rows

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from datasets import Dataset, DatasetDict`
  Imports `Dataset, DatasetDict` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 4: `def add_length(batch: dict[str, list]) -> dict[str, list]:`
  Defines `add_length`, the function that groups one logical step of the example.
- Line 5: `    return {"length": [len(text) for text in batch["text"]]}`
  Returns the transformed value that the dataset API will store or use next.
- Line 8: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 9: `    dataset_dict = DatasetDict(`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 11: `            "train": Dataset.from_dict({"text": ["train-a", "train-b"]}),`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 12: `            "test": Dataset.from_dict({"text": ["test-a"]}),`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 16: `    mapped_dataset_dict = dataset_dict.map(add_length, batched=True)`
  Applies `map(...)` to create transformed columns or rows from the original dataset.
- Line 25: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- This pattern is cleaner than looping over each split manually for simple shared preprocessing.

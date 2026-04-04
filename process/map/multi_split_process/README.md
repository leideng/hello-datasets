# multi_split_process

Apply one map function across all splits in a `DatasetDict`.

## What It Teaches

- `DatasetDict.map(...)` applies the same transformation to every split.
- This is convenient when train, validation, and test need consistent preprocessing.
- The split structure stays intact after processing.

## Run

From the repository root:

```bash
uv run python process/map/multi_split_process/main.py
```

## Expected Result

The script prints:

- the transformed `DatasetDict`
- the processed train rows
- the processed test rows

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `from datasets import Dataset, DatasetDict`
  Imports `Dataset, DatasetDict` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 4: `def add_length(batch: dict[str, list]) -> dict[str, list]:`
  Defines the function `add_length` so the example logic is grouped into a named step.
- Line 5: `    return {"length": [len(text) for text in batch["text"]]}`
  Returns the computed value back to the caller.
- Line 8: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 9: `    dataset_dict = DatasetDict(`
  Starts a multi-line function call whose arguments are listed on the next lines.
- Line 10: `        {`
  Continues the multi-line Python structure opened by the previous line.
- Line 11: `            "train": Dataset.from_dict({"text": ["train-a", "train-b"]}),`
  Provides one literal sample value used by the example data or configuration.
- Line 12: `            "test": Dataset.from_dict({"text": ["test-a"]}),`
  Provides one literal sample value used by the example data or configuration.
- Line 13: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 14: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 16: `    mapped_dataset_dict = dataset_dict.map(add_length, batched=True)`
  Stores the result of a dataset operation so the next lines can inspect it.
- Line 18: `    print("DatasetDict after map across multiple splits")`
  Prints information so you can observe what the dataset operation produced.
- Line 19: `    print(mapped_dataset_dict)`
  Prints information so you can observe what the dataset operation produced.
- Line 20: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 21: `    print("Train rows:", mapped_dataset_dict["train"][:])`
  Prints information so you can observe what the dataset operation produced.
- Line 22: `    print("Test rows:", mapped_dataset_dict["test"][:])`
  Prints information so you can observe what the dataset operation produced.
- Line 25: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 26: `    main()`
  Calls `main()` to start the example.

## Notes

- This pattern is cleaner than looping over each split manually for simple shared preprocessing.

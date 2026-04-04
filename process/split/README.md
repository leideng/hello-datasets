# split

Create train and test subsets with `train_test_split(...)`.

## What It Teaches

- A single dataset can be split into a `DatasetDict`.
- `test_size` controls the fraction reserved for testing.
- A fixed `seed` makes the split reproducible.

## Run

From the repository root:

```bash
uv run python process/split/main.py
```

## Expected Result

The script prints:

- the resulting `DatasetDict`
- the train rows
- the test rows

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 4: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 5: `    dataset = Dataset.from_dict(`
  Creates a small in-memory dataset from Python lists so the transformation can be demonstrated clearly.
- Line 6: `        {`
  Continues the multi-line Python structure opened by the previous line.
- Line 7: `            "id": list(range(8)),`
  Provides one literal sample value used by the example data or configuration.
- Line 8: `            "text": [f"example-{i}" for i in range(8)],`
  Provides one literal sample value used by the example data or configuration.
- Line 9: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 10: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 12: `    split_dataset = dataset.train_test_split(test_size=0.25, seed=13)`
  Stores the result of a dataset operation so the next lines can inspect it.
- Line 14: `    print("Dataset after train_test_split")`
  Prints information so you can observe what the dataset operation produced.
- Line 15: `    print(split_dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 16: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 17: `    print("Train rows:", split_dataset["train"][:])`
  Prints information so you can observe what the dataset operation produced.
- Line 18: `    print("Test rows:", split_dataset["test"][:])`
  Prints information so you can observe what the dataset operation produced.
- Line 21: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 22: `    main()`
  Calls `main()` to start the example.

## Notes

- This is a common first step before training and evaluation.
- You can create validation splits the same way from the training subset.

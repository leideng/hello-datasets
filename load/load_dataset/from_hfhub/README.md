# load_dataset from_hfhub

Load a public dataset directly from Hugging Face Hub with `load_dataset(repo_id, ...)`.

## What It Teaches

- `load_dataset(...)` can download a dataset by Hub repository ID.
- You can request only a small slice such as `train[:3]` while learning.
- Hub-hosted datasets are one of the most common entry points for `datasets`.

## Run

From the repository root:

```bash
uv run python load/load_dataset/from_hfhub/main.py
```

## Expected Result

In a normal networked environment, the script:

- downloads a small public dataset sample
- prints the dataset summary, features, and rows

In a restricted environment, the script catches the failure and explains that Hub access is required.

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `from datasets import load_dataset`
  Imports `load_dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 4: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 5: `    repo_id = "cornell-movie-review-data/rotten_tomatoes"`
  Saves a value into `repo_id` so later lines can reuse it.
- Line 7: `    print(f"Trying to load a small sample from Hugging Face Hub: {repo_id}")`
  Prints information so you can observe what the dataset operation produced.
- Line 8: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 10: `    try:`
  Starts a `try` block so the example can handle errors or guarantee cleanup.
- Line 11: `        dataset = load_dataset(repo_id, split="train[:3]")`
  Saves a value into `dataset` so later lines can reuse it.
- Line 12: `    except Exception as exc:`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 13: `        print("This example requires network access to Hugging Face Hub.")`
  Prints information so you can observe what the dataset operation produced.
- Line 14: `        print(f"Loading failed in the current environment: {type(exc).__name__}: {exc}")`
  Prints information so you can observe what the dataset operation produced.
- Line 15: `        return`
  Stops the function early when the script cannot continue.
- Line 17: `    print("Dataset loaded from Hugging Face Hub")`
  Prints information so you can observe what the dataset operation produced.
- Line 18: `    print(dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 19: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 20: `    print("Features:", dataset.features)`
  Prints information so you can observe what the dataset operation produced.
- Line 21: `    print("Rows:", dataset[:])`
  Prints information so you can observe what the dataset operation produced.
- Line 24: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 25: `    main()`
  Calls `main()` to start the example.

## Notes

- This example intentionally uses a public dataset and a small split slice.
- If you work in an offline or sandboxed environment, this example may not be runnable until network access is available.

# load_dataset from_hfhub

Load a public dataset directly from Hugging Face Hub with `load_dataset(repo_id, ...)`.

## What It Teaches

- `load_dataset(...)` can download a dataset by Hub repository ID.
- You can request only a small slice such as `train[:3]` while learning.
- Hub-hosted datasets are one of the most common entry points for `datasets`.

## Run

From the repository root:

```bash
uv run python topics/01-load/load_dataset/from_hfhub/main.py
```

## Expected Result

In a normal networked environment, the script:

- downloads a small public dataset sample
- prints the dataset summary, features, and rows

In a restricted environment, the script catches the failure and explains that Hub access is required.

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from datasets import load_dataset`
  Imports `load_dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 4: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 11: `        dataset = load_dataset(repo_id, split="train[:3]")`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 24: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- This example intentionally uses a public dataset and a small split slice.
- If you work in an offline or sandboxed environment, this example may not be runnable until network access is available.

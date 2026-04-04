# tensor_format torch

Retrieve dataset rows as PyTorch tensors with `with_format("torch")`.

## What It Teaches

- `with_format("torch")` changes retrieval output to PyTorch tensor objects.
- This is useful when preparing dataset batches for PyTorch training loops.
- The stored dataset is unchanged; only returned values are formatted differently.

## Run

From the repository root:

```bash
uv run python topics/04-use-with-pytorch/torch/main.py
```

## Expected Result

If PyTorch is installed, the script prints:

- the dataset summary
- the types of returned item and batch values
- example tensor-formatted outputs

If PyTorch is not installed, the script prints a short dependency message and exits cleanly.

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 4: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 6: `        import torch  # noqa: F401`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 12: `    dataset = Dataset.from_dict(`
  Creates a tiny in-memory dataset so the transformation can be demonstrated without external files.
- Line 19: `    torch_dataset = dataset.with_format("torch")`
  Changes the output format so fetched items come back as tensors, arrays, tables, or another target type.
- Line 20: `    first_item = torch_dataset[0]`
  Reads one formatted example so the script can show what a single item looks like.
- Line 21: `    first_batch = torch_dataset[:2]`
  Reads multiple rows at once so the example can compare batched output.
- Line 32: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- This repo does not force heavyweight framework dependencies for every example.

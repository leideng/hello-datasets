# tensor_format torch

Retrieve dataset rows as PyTorch tensors with `with_format("torch")`.

## What It Teaches

- `with_format("torch")` changes retrieval output to PyTorch tensor objects.
- This is useful when preparing dataset batches for PyTorch training loops.
- The stored dataset is unchanged; only returned values are formatted differently.

## Run

From the repository root:

```bash
uv run python process/format/tensor_format/torch/src/main.py
```

## Expected Result

If PyTorch is installed, the script prints:

- the dataset summary
- the types of returned item and batch values
- example tensor-formatted outputs

If PyTorch is not installed, the script prints a short dependency message and exits cleanly.

## Notes

- This repo does not force heavyweight framework dependencies for every example.

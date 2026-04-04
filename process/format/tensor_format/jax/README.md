# tensor_format jax

Retrieve dataset rows as JAX arrays with `with_format("jax")`.

## What It Teaches

- `with_format("jax")` changes retrieval output to JAX-compatible array objects.
- This is useful when feeding examples into JAX-based training or inference code.
- The dataset remains stored the same way underneath.

## Run

From the repository root:

```bash
uv run python process/format/tensor_format/jax/main.py
```

## Expected Result

If JAX is installed, the script prints:

- the dataset summary
- the returned item and batch types
- example JAX-formatted outputs

If JAX is not installed, the script prints a short dependency message and exits cleanly.

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 4: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 6: `        import jax  # noqa: F401`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 12: `    dataset = Dataset.from_dict(`
  Creates a tiny in-memory dataset so the transformation can be demonstrated without external files.
- Line 19: `    jax_dataset = dataset.with_format("jax")`
  Changes the output format so fetched items come back as tensors, arrays, tables, or another target type.
- Line 20: `    first_item = jax_dataset[0]`
  Reads one formatted example so the script can show what a single item looks like.
- Line 21: `    first_batch = jax_dataset[:2]`
  Reads multiple rows at once so the example can compare batched output.
- Line 32: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- This repo keeps optional framework examples lightweight by making the dependency explicit.

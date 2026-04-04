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

## Notes

- This repo keeps optional framework examples lightweight by making the dependency explicit.

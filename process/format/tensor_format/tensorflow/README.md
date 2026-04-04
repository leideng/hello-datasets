# tensor_format tensorflow

Retrieve dataset rows as TensorFlow tensors with `with_format("tensorflow")`.

## What It Teaches

- `with_format("tensorflow")` changes retrieval output to TensorFlow tensors.
- This is useful when preparing examples for TensorFlow or Keras workflows.
- The format change affects retrieval, not dataset storage.

## Run

From the repository root:

```bash
uv run python process/format/tensor_format/tensorflow/main.py
```

## Expected Result

If TensorFlow is installed, the script prints:

- the dataset summary
- the returned item and batch types
- example tensor-formatted outputs

If TensorFlow is not installed, the script prints a short dependency message and exits cleanly.

## Notes

- This keeps the example self-contained without making TensorFlow a mandatory repo dependency.

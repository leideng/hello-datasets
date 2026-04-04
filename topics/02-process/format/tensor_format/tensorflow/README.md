# tensor_format tensorflow

Retrieve dataset rows as TensorFlow tensors with `with_format("tensorflow")`.

## What It Teaches

- `with_format("tensorflow")` changes retrieval output to TensorFlow tensors.
- This is useful when preparing examples for TensorFlow or Keras workflows.
- The format change affects retrieval, not dataset storage.

## Run

From the repository root:

```bash
uv run python topics/02-process/format/tensor_format/tensorflow/main.py
```

## Expected Result

If TensorFlow is installed, the script prints:

- the dataset summary
- the returned item and batch types
- example tensor-formatted outputs

If TensorFlow is not installed, the script prints a short dependency message and exits cleanly.

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 4: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 6: `        import tensorflow as tf  # noqa: F401`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 12: `    dataset = Dataset.from_dict(`
  Creates a tiny in-memory dataset so the transformation can be demonstrated without external files.
- Line 19: `    tensorflow_dataset = dataset.with_format("tensorflow")`
  Changes the output format so fetched items come back as tensors, arrays, tables, or another target type.
- Line 20: `    first_item = tensorflow_dataset[0]`
  Reads one formatted example so the script can show what a single item looks like.
- Line 21: `    first_batch = tensorflow_dataset[:2]`
  Reads multiple rows at once so the example can compare batched output.
- Line 32: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- This keeps the example self-contained without making TensorFlow a mandatory repo dependency.

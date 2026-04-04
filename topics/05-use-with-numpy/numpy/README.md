# tensor_format numpy

Retrieve dataset rows as NumPy arrays with `with_format("numpy")`.

## What It Teaches

- `with_format("numpy")` changes how examples are returned when accessed.
- Individual items and slices can come back as NumPy arrays instead of plain Python objects.
- This is useful for numerical workflows and lightweight model input preparation.

## Run

From the repository root:

```bash
uv run python topics/05-use-with-numpy/numpy/main.py
```

## Expected Result

The script prints:

- the dataset summary
- the types of retrieved values
- example NumPy-formatted items and batches

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `import numpy as np`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 2: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 5: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 6: `    dataset = Dataset.from_dict(`
  Creates a tiny in-memory dataset so the transformation can be demonstrated without external files.
- Line 13: `    numpy_dataset = dataset.with_format("numpy")`
  Changes the output format so fetched items come back as tensors, arrays, tables, or another target type.
- Line 14: `    first_item = numpy_dataset[0]`
  Reads one formatted example so the script can show what a single item looks like.
- Line 15: `    first_batch = numpy_dataset[:2]`
  Reads multiple rows at once so the example can compare batched output.
- Line 26: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- This changes retrieval format only; it does not rewrite stored data.

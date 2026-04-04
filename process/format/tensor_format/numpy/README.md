# tensor_format numpy

Retrieve dataset rows as NumPy arrays with `with_format("numpy")`.

## What It Teaches

- `with_format("numpy")` changes how examples are returned when accessed.
- Individual items and slices can come back as NumPy arrays instead of plain Python objects.
- This is useful for numerical workflows and lightweight model input preparation.

## Run

From the repository root:

```bash
uv run python process/format/tensor_format/numpy/main.py
```

## Expected Result

The script prints:

- the dataset summary
- the types of retrieved values
- example NumPy-formatted items and batches

## Notes

- This changes retrieval format only; it does not rewrite stored data.

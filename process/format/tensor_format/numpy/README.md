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

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `import numpy as np`
  Performs part of the dataset transformation being demonstrated in this example.
- Line 2: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 5: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 6: `    dataset = Dataset.from_dict(`
  Creates a small in-memory dataset from Python lists so the transformation can be demonstrated clearly.
- Line 7: `        {`
  Continues the multi-line Python structure opened by the previous line.
- Line 8: `            "id": [1, 2, 3],`
  Provides one literal sample value used by the example data or configuration.
- Line 9: `            "values": [[1.0, 1.5], [2.0, 2.5], [3.0, 3.5]],`
  Provides one literal sample value used by the example data or configuration.
- Line 10: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 11: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 13: `    numpy_dataset = dataset.with_format("numpy")`
  Changes the dataset output format so fetched items come back in the requested representation.
- Line 14: `    first_item = numpy_dataset[0]`
  Reads one example row so the script can show the returned value and its type.
- Line 15: `    first_batch = numpy_dataset[:2]`
  Reads multiple rows at once so the script can show batched output.
- Line 17: `    print("Dataset with NumPy output format")`
  Prints information so you can observe what the dataset operation produced.
- Line 18: `    print(numpy_dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 19: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 20: `    print("Item 0 types:", {key: type(value) for key, value in first_item.items()})`
  Prints information so you can observe what the dataset operation produced.
- Line 21: `    print("Item 0:", first_item)`
  Prints information so you can observe what the dataset operation produced.
- Line 22: `    print("Batch types:", {key: type(value) for key, value in first_batch.items()})`
  Prints information so you can observe what the dataset operation produced.
- Line 23: `    print("Batch values:", first_batch)`
  Prints information so you can observe what the dataset operation produced.
- Line 26: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 27: `    main()`
  Calls `main()` to start the example.

## Notes

- This changes retrieval format only; it does not rewrite stored data.

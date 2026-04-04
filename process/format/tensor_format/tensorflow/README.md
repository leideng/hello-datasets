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

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 4: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 5: `    try:`
  Starts a `try` block so the example can handle errors or guarantee cleanup.
- Line 6: `        import tensorflow as tf  # noqa: F401`
  Performs part of the dataset transformation being demonstrated in this example.
- Line 7: `    except ImportError:`
  Handles the case where an optional dependency is not installed.
- Line 8: `        print("This example requires TensorFlow.")`
  Prints information so you can observe what the dataset operation produced.
- Line 9: `        print("Install it in the root environment before running this script.")`
  Prints information so you can observe what the dataset operation produced.
- Line 10: `        return`
  Stops the function early when the script cannot continue.
- Line 12: `    dataset = Dataset.from_dict(`
  Creates a small in-memory dataset from Python lists so the transformation can be demonstrated clearly.
- Line 13: `        {`
  Continues the multi-line Python structure opened by the previous line.
- Line 14: `            "id": [1, 2, 3],`
  Provides one literal sample value used by the example data or configuration.
- Line 15: `            "values": [[1.0, 1.5], [2.0, 2.5], [3.0, 3.5]],`
  Provides one literal sample value used by the example data or configuration.
- Line 16: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 17: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 19: `    tensorflow_dataset = dataset.with_format("tensorflow")`
  Changes the dataset output format so fetched items come back in the requested representation.
- Line 20: `    first_item = tensorflow_dataset[0]`
  Reads one example row so the script can show the returned value and its type.
- Line 21: `    first_batch = tensorflow_dataset[:2]`
  Reads multiple rows at once so the script can show batched output.
- Line 23: `    print("Dataset with TensorFlow output format")`
  Prints information so you can observe what the dataset operation produced.
- Line 24: `    print(tensorflow_dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 25: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 26: `    print("Item 0 types:", {key: type(value) for key, value in first_item.items()})`
  Prints information so you can observe what the dataset operation produced.
- Line 27: `    print("Item 0:", first_item)`
  Prints information so you can observe what the dataset operation produced.
- Line 28: `    print("Batch types:", {key: type(value) for key, value in first_batch.items()})`
  Prints information so you can observe what the dataset operation produced.
- Line 29: `    print("Batch values:", first_batch)`
  Prints information so you can observe what the dataset operation produced.
- Line 32: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 33: `    main()`
  Calls `main()` to start the example.

## Notes

- This keeps the example self-contained without making TensorFlow a mandatory repo dependency.

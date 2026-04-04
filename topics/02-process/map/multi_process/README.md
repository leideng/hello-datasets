# multi_process

Use `num_proc` with `map(...)` for process-based parallel preprocessing.

## What It Teaches

- `num_proc` can distribute a mapping workload across multiple worker processes.
- This is useful for heavier CPU-bound transforms on larger datasets.
- Some restricted environments block local multiprocessing primitives.

## Run

From the repository root:

```bash
uv run python topics/02-process/map/multi_process/main.py
```

## Expected Result

The script prints:

- whether it ran in parallel or used a fallback
- the transformed dataset
- rows with a derived `length` column

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `import socket`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 3: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 6: `def supports_local_process_manager() -> bool:`
  Defines `supports_local_process_manager`, the function that groups one logical step of the example.
- Line 8: `        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:`
  Starts a context manager so temporary resources are created and cleaned up safely.
- Line 11: `        return True`
  Returns the transformed value that the dataset API will store or use next.
- Line 13: `        return False`
  Returns the transformed value that the dataset API will store or use next.
- Line 16: `def add_length(batch: dict[str, list]) -> dict[str, list]:`
  Defines `add_length`, the function that groups one logical step of the example.
- Line 17: `    return {"length": [len(text) for text in batch["text"]]}`
  Returns the transformed value that the dataset API will store or use next.
- Line 20: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 21: `    dataset = Dataset.from_dict(`
  Creates a tiny in-memory dataset so the transformation can be demonstrated without external files.
- Line 33: `        mapped_dataset = dataset.map(add_length, batched=True, num_proc=2)`
  Applies `map(...)` to create transformed columns or rows from the original dataset.
- Line 39: `        mapped_dataset = dataset.map(add_length, batched=True)`
  Applies `map(...)` to create transformed columns or rows from the original dataset.
- Line 49: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- In sandboxes that block process management, the example falls back to plain `map(...)` without `num_proc`.

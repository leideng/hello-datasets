# multi_process

Use `num_proc` with `map(...)` for process-based parallel preprocessing.

## What It Teaches

- `num_proc` can distribute a mapping workload across multiple worker processes.
- This is useful for heavier CPU-bound transforms on larger datasets.
- Some restricted environments block local multiprocessing primitives.

## Run

From the repository root:

```bash
uv run python process/map/multi_process/main.py
```

## Expected Result

The script prints:

- whether it ran in parallel or used a fallback
- the transformed dataset
- rows with a derived `length` column

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `import socket`
  Performs part of the dataset transformation being demonstrated in this example.
- Line 3: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 6: `def supports_local_process_manager() -> bool:`
  Defines the function `supports_local_process_manager` so the example logic is grouped into a named step.
- Line 7: `    try:`
  Starts a `try` block so the example can handle errors or guarantee cleanup.
- Line 8: `        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:`
  Performs part of the dataset transformation being demonstrated in this example.
- Line 9: `            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)`
  Performs part of the dataset transformation being demonstrated in this example.
- Line 10: `            sock.bind(("127.0.0.1", 0))`
  Performs part of the dataset transformation being demonstrated in this example.
- Line 11: `        return True`
  Returns the computed value back to the caller.
- Line 12: `    except OSError:`
  Performs part of the dataset transformation being demonstrated in this example.
- Line 13: `        return False`
  Returns the computed value back to the caller.
- Line 16: `def add_length(batch: dict[str, list]) -> dict[str, list]:`
  Defines the function `add_length` so the example logic is grouped into a named step.
- Line 17: `    return {"length": [len(text) for text in batch["text"]]}`
  Returns the computed value back to the caller.
- Line 20: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 21: `    dataset = Dataset.from_dict(`
  Creates a small in-memory dataset from Python lists so the transformation can be demonstrated clearly.
- Line 22: `        {`
  Continues the multi-line Python structure opened by the previous line.
- Line 23: `            "text": [`
  Provides one literal sample value used by the example data or configuration.
- Line 24: `                "parallel map can speed up heavier transforms",`
  Provides one literal sample value used by the example data or configuration.
- Line 25: `                "but tiny examples often do not benefit",`
  Provides one literal sample value used by the example data or configuration.
- Line 26: `                "the api still matters for learning",`
  Provides one literal sample value used by the example data or configuration.
- Line 27: `                "sandbox restrictions may block worker management",`
  Provides one literal sample value used by the example data or configuration.
- Line 28: `            ]`
  Continues the multi-line Python structure opened by the previous line.
- Line 29: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 30: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 32: `    if supports_local_process_manager():`
  Performs part of the dataset transformation being demonstrated in this example.
- Line 33: `        mapped_dataset = dataset.map(add_length, batched=True, num_proc=2)`
  Applies `map(...)` to create a transformed version of the dataset.
- Line 34: `        execution_mode = "parallel"`
  Saves a value into `execution_mode` so later lines can reuse it.
- Line 35: `    else:`
  Performs part of the dataset transformation being demonstrated in this example.
- Line 36: `        print("Multiprocessing is blocked in this environment.")`
  Prints information so you can observe what the dataset operation produced.
- Line 37: `        print("Falling back to plain map(...) for a runnable example.")`
  Prints information so you can observe what the dataset operation produced.
- Line 38: `        print()`
  Prints information so you can observe what the dataset operation produced.
- Line 39: `        mapped_dataset = dataset.map(add_length, batched=True)`
  Applies `map(...)` to create a transformed version of the dataset.
- Line 40: `        execution_mode = "fallback-plain-map"`
  Saves a value into `execution_mode` so later lines can reuse it.
- Line 42: `    print("Dataset after multi-process style map")`
  Prints information so you can observe what the dataset operation produced.
- Line 43: `    print("Execution mode:", execution_mode)`
  Prints information so you can observe what the dataset operation produced.
- Line 44: `    print(mapped_dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 45: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 46: `    print("Rows:", mapped_dataset[:])`
  Prints information so you can observe what the dataset operation produced.
- Line 49: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 50: `    main()`
  Calls `main()` to start the example.

## Notes

- In sandboxes that block process management, the example falls back to plain `map(...)` without `num_proc`.

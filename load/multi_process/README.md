# multi_process

Load local files with multiple worker processes using `num_proc`.

## What It Teaches

- Some dataset loading workflows can use multiple processes.
- `num_proc` is useful when many local files need to be parsed.
- A multi-file input pattern is common for sharded datasets.

## Run

From the repository root:

```bash
uv run python load/multi_process/main.py
```

## Expected Result

The script:

- loads two local JSON Lines shards
- requests `num_proc=2`
- prints the combined dataset rows

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `from pathlib import Path`
  Imports `Path` so file and directory paths can be built in a platform-safe way.
- Line 2: `import socket`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 4: `from datasets import load_dataset`
  Imports `load_dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 7: `def try_parallel_load(data_files: list[str], cache_dir: Path):`
  Defines the function `try_parallel_load` so the example logic is grouped into a named step.
- Line 8: `    return load_dataset(`
  Returns the computed value back to the caller.
- Line 9: `        "json",`
  Provides one literal sample value used by the example data or configuration.
- Line 10: `        data_files=data_files,`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 11: `        num_proc=2,`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 12: `        cache_dir=str(cache_dir),`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 13: `    )["train"]`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 16: `def supports_local_process_manager() -> bool:`
  Defines the function `supports_local_process_manager` so the example logic is grouped into a named step.
- Line 17: `    try:`
  Starts a `try` block so the example can handle errors or guarantee cleanup.
- Line 18: `        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 19: `            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 20: `            sock.bind(("127.0.0.1", 0))`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 21: `        return True`
  Returns the computed value back to the caller.
- Line 22: `    except OSError:`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 23: `        return False`
  Returns the computed value back to the caller.
- Line 26: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 27: `    example_dir = Path(__file__).resolve().parent`
  Finds the example folder so nearby `data/` and `.cache/` paths can be built relative to this file.
- Line 28: `    data_files = sorted(str(path) for path in (example_dir / "data").glob("*.jsonl"))`
  Saves a value into `data_files` so later lines can reuse it.
- Line 29: `    cache_dir = example_dir / ".cache"`
  Creates a local cache path so generated dataset artifacts stay inside this example folder.
- Line 31: `    if supports_local_process_manager():`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 32: `        dataset = try_parallel_load(data_files, cache_dir)`
  Saves a value into `dataset` so later lines can reuse it.
- Line 33: `        execution_mode = "parallel"`
  Saves a value into `execution_mode` so later lines can reuse it.
- Line 34: `    else:`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 35: `        print("Parallel loading was blocked in this environment.")`
  Prints information so you can observe what the dataset operation produced.
- Line 36: `        print("Falling back to num_proc=1 because local process sockets are unavailable.")`
  Prints information so you can observe what the dataset operation produced.
- Line 37: `        print()`
  Prints information so you can observe what the dataset operation produced.
- Line 38: `        dataset = load_dataset(`
  Starts a multi-line function call whose arguments are listed on the next lines.
- Line 39: `            "json",`
  Provides one literal sample value used by the example data or configuration.
- Line 40: `            data_files=data_files,`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 41: `            num_proc=1,`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 42: `            cache_dir=str(cache_dir),`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 43: `        )["train"]`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 44: `        execution_mode = "fallback-single-process"`
  Saves a value into `execution_mode` so later lines can reuse it.
- Line 46: `    print("Dataset loaded with multiple worker processes")`
  Prints information so you can observe what the dataset operation produced.
- Line 47: `    print("Execution mode:", execution_mode)`
  Prints information so you can observe what the dataset operation produced.
- Line 48: `    print(dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 49: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 50: `    print("Number of rows:", len(dataset))`
  Prints information so you can observe what the dataset operation produced.
- Line 51: `    print("Rows:", dataset[:])`
  Prints information so you can observe what the dataset operation produced.
- Line 54: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 55: `    main()`
  Calls `main()` to start the example.

## Notes

- This example keeps the data tiny so the multiprocessing behavior is easy to understand.
- On very small inputs, multiprocessing may add overhead instead of improving total runtime.
- In restricted sandboxes, multiprocessing may be blocked. This example falls back to `num_proc=1` and prints that it did so.

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

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from pathlib import Path`
  Imports `Path` so local files such as `data/` inputs and cache directories can be built safely.
- Line 2: `import socket`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 4: `from datasets import load_dataset`
  Imports `load_dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 7: `def try_parallel_load(data_files: list[str], cache_dir: Path):`
  Defines `try_parallel_load`, the function that groups one logical step of the example.
- Line 8: `    return load_dataset(`
  Returns the transformed value that the dataset API will store or use next.
- Line 16: `def supports_local_process_manager() -> bool:`
  Defines `supports_local_process_manager`, the function that groups one logical step of the example.
- Line 18: `        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:`
  Starts a context manager so temporary resources are created and cleaned up safely.
- Line 21: `        return True`
  Returns the transformed value that the dataset API will store or use next.
- Line 23: `        return False`
  Returns the transformed value that the dataset API will store or use next.
- Line 26: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 27: `    example_dir = Path(__file__).resolve().parent`
  Finds the example folder so local `data/` and `.cache/` paths stay relative to this example.
- Line 29: `    cache_dir = example_dir / ".cache"`
  Keeps generated cache artifacts inside this example folder instead of a global location.
- Line 32: `        dataset = try_parallel_load(data_files, cache_dir)`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 38: `        dataset = load_dataset(`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 54: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- This example keeps the data tiny so the multiprocessing behavior is easy to understand.
- On very small inputs, multiprocessing may add overhead instead of improving total runtime.
- In restricted sandboxes, multiprocessing may be blocked. This example falls back to `num_proc=1` and prints that it did so.

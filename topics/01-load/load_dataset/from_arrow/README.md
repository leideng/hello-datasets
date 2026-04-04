# load_dataset from_arrow

Load a local Apache Arrow file with `load_dataset("arrow", ...)`.

## What It Teaches

- `load_dataset` can read Arrow IPC files directly.
- Arrow is the native columnar format used internally by `datasets`.
- A local Arrow file is useful when you already have a columnar preprocessing step.

## Run

From the repository root:

```bash
uv run python topics/01-load/load_dataset/from_arrow/main.py
```

## Expected Result

The script:

- creates a small local Arrow file in `data/`
- loads it with `load_dataset`
- prints the inferred schema and a sample row

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from pathlib import Path`
  Imports `Path` so local files such as `data/` inputs and cache directories can be built safely.
- Line 3: `import pyarrow as pa`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 4: `from datasets import load_dataset`
  Imports `load_dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 7: `def write_arrow_file(arrow_file: Path) -> None:`
  Defines `write_arrow_file`, the function that groups one logical step of the example.
- Line 8: `    arrow_file.parent.mkdir(parents=True, exist_ok=True)`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 18: `    with pa.OSFile(str(arrow_file), "wb") as sink:`
  Starts a context manager so temporary resources are created and cleaned up safely.
- Line 19: `        with pa.ipc.new_file(sink, table.schema) as writer:`
  Starts a context manager so temporary resources are created and cleaned up safely.
- Line 23: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 24: `    example_dir = Path(__file__).resolve().parent`
  Finds the example folder so local `data/` and `.cache/` paths stay relative to this example.
- Line 25: `    data_file = example_dir / "data" / "sample.arrow"`
  Builds the path to the local sample data used by the example.
- Line 26: `    cache_dir = example_dir / ".cache"`
  Keeps generated cache artifacts inside this example folder instead of a global location.
- Line 30: `    dataset_dict = load_dataset(`
  Calls `load_dataset(...)`, the core loader used to read this data format.
- Line 35: `    train_dataset = dataset_dict["train"]`
  Pulls out the `train` split so the example can inspect the loaded records directly.
- Line 44: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- The script writes the Arrow file on demand so the example stays self-contained.
- This example uses a local cache directory under the example folder.

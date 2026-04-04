# load_dataset from_parquet

Load a local Parquet file with `load_dataset("parquet", ...)`.

## What It Teaches

- `load_dataset` has built-in Parquet support.
- Parquet is a common storage format for structured tabular data.
- Local Parquet files are a practical bridge between data engineering outputs and `datasets`.

## Run

From the repository root:

```bash
uv run python load/load_dataset/from_parquet/main.py
```

## Expected Result

The script:

- creates a small local Parquet file in `data/`
- loads it with `load_dataset`
- prints the schema and loaded rows

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `from pathlib import Path`
  Imports `Path` so local files such as `data/` inputs and cache directories can be built safely.
- Line 3: `import pandas as pd`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 4: `from datasets import load_dataset`
  Imports `load_dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 7: `def write_parquet_file(parquet_file: Path) -> None:`
  Defines `write_parquet_file`, the function that groups one logical step of the example.
- Line 8: `    parquet_file.parent.mkdir(parents=True, exist_ok=True)`
  This is one of the key lines that shapes how the dataset is loaded, transformed, or formatted.
- Line 24: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 25: `    example_dir = Path(__file__).resolve().parent`
  Finds the example folder so local `data/` and `.cache/` paths stay relative to this example.
- Line 26: `    data_file = example_dir / "data" / "sample.parquet"`
  Builds the path to the local sample data used by the example.
- Line 27: `    cache_dir = example_dir / ".cache"`
  Keeps generated cache artifacts inside this example folder instead of a global location.
- Line 31: `    dataset_dict = load_dataset(`
  Calls `load_dataset(...)`, the core loader used to read this data format.
- Line 36: `    train_dataset = dataset_dict["train"]`
  Pulls out the `train` split so the example can inspect the loaded records directly.
- Line 45: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- The example writes its own sample file to keep setup minimal.
- Parquet often preserves types more explicitly than CSV.

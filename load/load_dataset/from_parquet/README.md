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

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `from pathlib import Path`
  Imports `Path` so file and directory paths can be built in a platform-safe way.
- Line 3: `import pandas as pd`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 4: `from datasets import load_dataset`
  Imports `load_dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 7: `def write_parquet_file(parquet_file: Path) -> None:`
  Defines the function `write_parquet_file` so the example logic is grouped into a named step.
- Line 8: `    parquet_file.parent.mkdir(parents=True, exist_ok=True)`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 10: `    dataframe = pd.DataFrame(`
  Starts a multi-line function call whose arguments are listed on the next lines.
- Line 11: `        {`
  Continues the multi-line Python structure opened by the previous line.
- Line 12: `            "id": [1, 2, 3],`
  Provides one literal sample value used by the example data or configuration.
- Line 13: `            "task": [`
  Provides one literal sample value used by the example data or configuration.
- Line 14: `                "write parquet locally",`
  Provides one literal sample value used by the example data or configuration.
- Line 15: `                "load parquet with datasets",`
  Provides one literal sample value used by the example data or configuration.
- Line 16: `                "inspect the resulting schema",`
  Provides one literal sample value used by the example data or configuration.
- Line 17: `            ],`
  Closes part of the sample data structure being built.
- Line 18: `            "done": [True, True, False],`
  Provides one literal sample value used by the example data or configuration.
- Line 19: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 20: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 21: `    dataframe.to_parquet(parquet_file, index=False)`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 24: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 25: `    example_dir = Path(__file__).resolve().parent`
  Finds the example folder so nearby `data/` and `.cache/` paths can be built relative to this file.
- Line 26: `    data_file = example_dir / "data" / "sample.parquet"`
  Builds the path to a local input file used by the example.
- Line 27: `    cache_dir = example_dir / ".cache"`
  Creates a local cache path so generated dataset artifacts stay inside this example folder.
- Line 29: `    write_parquet_file(data_file)`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 31: `    dataset_dict = load_dataset(`
  Calls `load_dataset(...)` to load data with one of the built-in dataset loaders.
- Line 32: `        "parquet",`
  Provides one literal sample value used by the example data or configuration.
- Line 33: `        data_files=str(data_file),`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 34: `        cache_dir=str(cache_dir),`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 35: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 36: `    train_dataset = dataset_dict["train"]`
  Selects the loaded `train` split so the example can inspect it directly.
- Line 38: `    print("Dataset loaded with load_dataset('parquet', data_files=...)")`
  Prints information so you can observe what the dataset operation produced.
- Line 39: `    print(dataset_dict)`
  Prints information so you can observe what the dataset operation produced.
- Line 40: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 41: `    print("Features:", train_dataset.features)`
  Prints information so you can observe what the dataset operation produced.
- Line 42: `    print("All rows:", train_dataset[:])`
  Prints information so you can observe what the dataset operation produced.
- Line 45: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 46: `    main()`
  Calls `main()` to start the example.

## Notes

- The example writes its own sample file to keep setup minimal.
- Parquet often preserves types more explicitly than CSV.

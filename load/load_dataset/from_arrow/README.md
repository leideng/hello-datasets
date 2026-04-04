# load_dataset from_arrow

Load a local Apache Arrow file with `load_dataset("arrow", ...)`.

## What It Teaches

- `load_dataset` can read Arrow IPC files directly.
- Arrow is the native columnar format used internally by `datasets`.
- A local Arrow file is useful when you already have a columnar preprocessing step.

## Run

From the repository root:

```bash
uv run python load/load_dataset/from_arrow/main.py
```

## Expected Result

The script:

- creates a small local Arrow file in `data/`
- loads it with `load_dataset`
- prints the inferred schema and a sample row

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `from pathlib import Path`
  Imports `Path` so file and directory paths can be built in a platform-safe way.
- Line 3: `import pyarrow as pa`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 4: `from datasets import load_dataset`
  Imports `load_dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 7: `def write_arrow_file(arrow_file: Path) -> None:`
  Defines the function `write_arrow_file` so the example logic is grouped into a named step.
- Line 8: `    arrow_file.parent.mkdir(parents=True, exist_ok=True)`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 10: `    table = pa.table(`
  Starts a multi-line function call whose arguments are listed on the next lines.
- Line 11: `        {`
  Continues the multi-line Python structure opened by the previous line.
- Line 12: `            "id": [1, 2, 3],`
  Provides one literal sample value used by the example data or configuration.
- Line 13: `            "topic": ["arrow", "ipc", "datasets"],`
  Provides one literal sample value used by the example data or configuration.
- Line 14: `            "difficulty": ["medium", "medium", "easy"],`
  Provides one literal sample value used by the example data or configuration.
- Line 15: `        }`
  Continues the multi-line Python structure opened by the previous line.
- Line 16: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 18: `    with pa.OSFile(str(arrow_file), "wb") as sink:`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 19: `        with pa.ipc.new_file(sink, table.schema) as writer:`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 20: `            writer.write_table(table)`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 23: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 24: `    example_dir = Path(__file__).resolve().parent`
  Finds the example folder so nearby `data/` and `.cache/` paths can be built relative to this file.
- Line 25: `    data_file = example_dir / "data" / "sample.arrow"`
  Builds the path to a local input file used by the example.
- Line 26: `    cache_dir = example_dir / ".cache"`
  Creates a local cache path so generated dataset artifacts stay inside this example folder.
- Line 28: `    write_arrow_file(data_file)`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 30: `    dataset_dict = load_dataset(`
  Calls `load_dataset(...)` to load data with one of the built-in dataset loaders.
- Line 31: `        "arrow",`
  Provides one literal sample value used by the example data or configuration.
- Line 32: `        data_files=str(data_file),`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 33: `        cache_dir=str(cache_dir),`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 34: `    )`
  Continues the multi-line Python structure opened by the previous line.
- Line 35: `    train_dataset = dataset_dict["train"]`
  Selects the loaded `train` split so the example can inspect it directly.
- Line 37: `    print("Dataset loaded with load_dataset('arrow', data_files=...)")`
  Prints information so you can observe what the dataset operation produced.
- Line 38: `    print(dataset_dict)`
  Prints information so you can observe what the dataset operation produced.
- Line 39: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 40: `    print("Features:", train_dataset.features)`
  Prints information so you can observe what the dataset operation produced.
- Line 41: `    print("Row 0:", train_dataset[0])`
  Prints information so you can observe what the dataset operation produced.
- Line 44: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 45: `    main()`
  Calls `main()` to start the example.

## Notes

- The script writes the Arrow file on demand so the example stays self-contained.
- This example uses a local cache directory under the example folder.

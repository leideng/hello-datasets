# load_dataset from_webdataset

Load a local tar shard in WebDataset format with `load_dataset("webdataset", ...)`.

## What It Teaches

- WebDataset stores one example across multiple files that share the same prefix.
- File extensions become dataset fields such as `txt` or `json`.
- A tar archive is enough for a minimal local example.

## Run

From the repository root:

```bash
uv run python load/load_dataset/from_webdataset/main.py
```

## Expected Result

The script:

- creates a local tar shard in WebDataset format
- loads it with the packaged `webdataset` loader
- prints the inferred features and first example

## Line-by-Line Code Explanation

Blank lines are omitted below. Each bullet points to the matching source line in `main.py`.

- Line 1: `import io`
  Imports in-memory byte streams used to create binary content without a separate file.
- Line 2: `import json`
  Imports JSON support so the script can read or write JSON records.
- Line 3: `import tarfile`
  Imports tar archive support because this example builds a small WebDataset tar file.
- Line 4: `from pathlib import Path`
  Imports `Path` so file and directory paths can be built in a platform-safe way.
- Line 6: `from datasets import load_dataset`
  Imports `load_dataset` from Hugging Face `datasets`, which provides the main API used in this example.
- Line 9: `def write_webdataset_tar(tar_file: Path) -> None:`
  Defines the function `write_webdataset_tar` so the example logic is grouped into a named step.
- Line 10: `    tar_file.parent.mkdir(parents=True, exist_ok=True)`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 12: `    examples = [`
  Starts a multi-line collection literal used by this example.
- Line 13: `        (`
  Continues the multi-line Python structure opened by the previous line.
- Line 14: `            "sample-0001",`
  Provides one literal sample value used by the example data or configuration.
- Line 15: `            "webdataset groups files by shared prefix",`
  Provides one literal sample value used by the example data or configuration.
- Line 16: `            {"label": "concept", "difficulty": "medium"},`
  Closes part of the sample data structure being built.
- Line 17: `        ),`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 18: `        (`
  Continues the multi-line Python structure opened by the previous line.
- Line 19: `            "sample-0002",`
  Provides one literal sample value used by the example data or configuration.
- Line 20: `            "each extension becomes a separate field",`
  Provides one literal sample value used by the example data or configuration.
- Line 21: `            {"label": "structure", "difficulty": "medium"},`
  Closes part of the sample data structure being built.
- Line 22: `        ),`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 23: `    ]`
  Continues the multi-line Python structure opened by the previous line.
- Line 25: `    with tarfile.open(tar_file, "w") as archive:`
  Opens a tar archive so sample files can be written into it.
- Line 26: `        for key, text, metadata in examples:`
  Starts a loop that repeats the same operation for each item in a collection.
- Line 27: `            txt_bytes = text.encode("utf-8")`
  Saves a value into `txt_bytes` so later lines can reuse it.
- Line 28: `            txt_info = tarfile.TarInfo(name=f"{key}.txt")`
  Saves a value into `txt_info` so later lines can reuse it.
- Line 29: `            txt_info.size = len(txt_bytes)`
  Saves a value into `txt_info.size` so later lines can reuse it.
- Line 30: `            archive.addfile(txt_info, io.BytesIO(txt_bytes))`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 32: `            json_bytes = json.dumps(metadata).encode("utf-8")`
  Saves a value into `json_bytes` so later lines can reuse it.
- Line 33: `            json_info = tarfile.TarInfo(name=f"{key}.json")`
  Saves a value into `json_info` so later lines can reuse it.
- Line 34: `            json_info.size = len(json_bytes)`
  Saves a value into `json_info.size` so later lines can reuse it.
- Line 35: `            archive.addfile(json_info, io.BytesIO(json_bytes))`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 38: `def main() -> None:`
  Defines the function `main` so the example logic is grouped into a named step.
- Line 39: `    example_dir = Path(__file__).resolve().parent`
  Finds the example folder so nearby `data/` and `.cache/` paths can be built relative to this file.
- Line 40: `    data_file = example_dir / "data" / "sample.tar"`
  Builds the path to a local input file used by the example.
- Line 41: `    cache_dir = example_dir / ".cache"`
  Creates a local cache path so generated dataset artifacts stay inside this example folder.
- Line 43: `    write_webdataset_tar(data_file)`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 45: `    dataset = load_dataset(`
  Starts a multi-line function call whose arguments are listed on the next lines.
- Line 46: `        "webdataset",`
  Provides one literal sample value used by the example data or configuration.
- Line 47: `        data_files=str(data_file),`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 48: `        cache_dir=str(cache_dir),`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 49: `    )["train"]`
  Performs one step of the example so the overall dataset workflow is easier to follow.
- Line 51: `    print("Dataset loaded with load_dataset('webdataset', data_files=...)")`
  Prints information so you can observe what the dataset operation produced.
- Line 52: `    print(dataset)`
  Prints information so you can observe what the dataset operation produced.
- Line 53: `    print()`
  Prints information so you can observe what the dataset operation produced.
- Line 54: `    print("Features:", dataset.features)`
  Prints information so you can observe what the dataset operation produced.
- Line 55: `    print("First row:", dataset[0])`
  Prints information so you can observe what the dataset operation produced.
- Line 58: `if __name__ == "__main__":`
  Runs the script entry point only when this file is executed directly.
- Line 59: `    main()`
  Calls `main()` to start the example.

## Notes

- Files such as `sample-0001.txt` and `sample-0001.json` are grouped into one example.
- This example uses text and JSON fields because they decode cleanly without optional media dependencies.

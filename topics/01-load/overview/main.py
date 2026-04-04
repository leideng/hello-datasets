from pathlib import Path

from datasets import Dataset, load_dataset


def generate_rows():
    for row_id, text in enumerate(["generator row one", "generator row two"], start=1):
        yield {"id": row_id, "text": text}


def main() -> None:
    example_dir = Path(__file__).resolve().parent
    data_file = example_dir / "data" / "sample.jsonl"
    cache_dir = example_dir / ".cache"

    file_dataset = load_dataset("json", data_files=str(data_file), cache_dir=str(cache_dir))["train"]
    dict_dataset = Dataset.from_dict({"id": [1, 2], "text": ["dict row one", "dict row two"]})
    generator_dataset = Dataset.from_generator(generate_rows, cache_dir=str(cache_dir))

    print("Three common loading entry points")
    print("load_dataset:", file_dataset)
    print("Dataset.from_dict:", dict_dataset)
    print("Dataset.from_generator:", generator_dataset)
    print()
    print("First file row:", file_dataset[0])
    print("First dict row:", dict_dataset[0])
    print("First generator row:", generator_dataset[0])


if __name__ == "__main__":
    main()

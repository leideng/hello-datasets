from pathlib import Path

from datasets import load_dataset


def main() -> None:
    data_file = Path(__file__).resolve().parent.parent / "data" / "sample.jsonl"
    cache_dir = Path(__file__).resolve().parent.parent / ".cache"

    dataset_dict = load_dataset(
        "json",
        data_files=str(data_file),
        cache_dir=str(cache_dir),
    )
    train_dataset = dataset_dict["train"]

    print("Dataset loaded with load_dataset('json', data_files=...)")
    print(dataset_dict)
    print()
    print("Train split:", train_dataset)
    print("Features:", train_dataset.features)
    print("First row:", train_dataset[0])


if __name__ == "__main__":
    main()

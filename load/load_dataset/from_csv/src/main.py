from pathlib import Path

from datasets import load_dataset


def main() -> None:
    data_file = Path(__file__).resolve().parent.parent / "data" / "sample.csv"
    cache_dir = Path(__file__).resolve().parent.parent / ".cache"

    dataset_dict = load_dataset(
        "csv",
        data_files=str(data_file),
        cache_dir=str(cache_dir),
    )
    train_dataset = dataset_dict["train"]

    print("Dataset loaded with load_dataset('csv', data_files=...)")
    print(dataset_dict)
    print()
    print("Features:", train_dataset.features)
    print("Rows 0 and 1:", train_dataset[:2])


if __name__ == "__main__":
    main()

from pathlib import Path

from datasets import load_dataset


def main() -> None:
    example_dir = Path(__file__).resolve().parent.parent
    data_file = example_dir / "data" / "sample.csv"
    cache_dir = example_dir / ".cache"
    file_url = data_file.resolve().as_uri()

    dataset = load_dataset(
        "csv",
        data_files=file_url,
        cache_dir=str(cache_dir),
    )["train"]

    print("Dataset loaded from a file:// URL")
    print("URL:", file_url)
    print(dataset)
    print()
    print("Features:", dataset.features)
    print("Rows:", dataset[:])


if __name__ == "__main__":
    main()

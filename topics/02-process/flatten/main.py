from datasets import Dataset


def main() -> None:
    dataset = Dataset.from_dict(
        {
            "id": [1, 2],
            "meta": [
                {"title": "first example", "difficulty": "easy"},
                {"title": "second example", "difficulty": "medium"},
            ],
        }
    )

    flattened_dataset = dataset.flatten()

    print("Dataset after flatten")
    print(flattened_dataset)
    print()
    print("Column names:", flattened_dataset.column_names)
    print("Rows:", flattened_dataset[:])


if __name__ == "__main__":
    main()

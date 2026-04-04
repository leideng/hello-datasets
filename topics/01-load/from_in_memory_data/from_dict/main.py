from datasets import Dataset


def main() -> None:
    dataset = Dataset.from_dict(
        {
            "id": [1, 2, 3],
            "text": [
                "datasets can be built from plain Python dicts",
                "each key becomes a column",
                "all columns must have the same length",
            ],
            "label": ["tip", "concept", "warning"],
        }
    )

    print("Dataset created with Dataset.from_dict")
    print(dataset)
    print()
    print("Column names:", dataset.column_names)
    print("Features:", dataset.features)
    print()
    print("First row:", dataset[0])


if __name__ == "__main__":
    main()

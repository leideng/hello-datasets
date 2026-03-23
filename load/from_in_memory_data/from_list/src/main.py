from datasets import Dataset


def main() -> None:
    records = [
        {"id": 1, "title": "load from a list", "difficulty": "easy"},
        {"id": 2, "title": "rows are Python dicts", "difficulty": "easy"},
        {"id": 3, "title": "schema is inferred automatically", "difficulty": "medium"},
    ]

    dataset = Dataset.from_list(records)

    print("Dataset created with Dataset.from_list")
    print(dataset)
    print()
    print("Column names:", dataset.column_names)
    print("Row 1:", dataset[1])


if __name__ == "__main__":
    main()

from datasets import Dataset


def main() -> None:
    dataset = Dataset.from_dict(
        {
            "id": [1, 2, 3],
            "text": [
                "keep the important column",
                "drop metadata you no longer need",
                "simplify the final schema",
            ],
            "debug_note": ["a", "b", "c"],
        }
    )

    cleaned_dataset = dataset.remove_columns(["debug_note"])

    print("Dataset after remove_columns")
    print(cleaned_dataset)
    print()
    print("Column names:", cleaned_dataset.column_names)
    print("Rows:", cleaned_dataset[:])


if __name__ == "__main__":
    main()

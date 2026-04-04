from datasets import Dataset


def main() -> None:
    dataset = Dataset.from_dict(
        {
            "sentence": [
                "rename columns to match your downstream code",
                "clear column names reduce confusion",
            ],
            "label": [1, 0],
        }
    )

    renamed_dataset = dataset.rename_column("sentence", "text")

    print("Dataset after rename_column")
    print(renamed_dataset)
    print()
    print("Column names:", renamed_dataset.column_names)
    print("Rows:", renamed_dataset[:])


if __name__ == "__main__":
    main()

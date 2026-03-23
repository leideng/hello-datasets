from datasets import Dataset


def main() -> None:
    dataset = Dataset.from_dict(
        {
            "id": [10, 11, 12, 13, 14],
            "text": [
                "zero-based row selection",
                "select keeps explicit indices",
                "this is the third row",
                "this is the fourth row",
                "this is the fifth row",
            ],
        }
    )

    selected_dataset = dataset.select([0, 2, 4])

    print("Dataset after select")
    print(selected_dataset)
    print()
    print("Rows:", selected_dataset[:])


if __name__ == "__main__":
    main()

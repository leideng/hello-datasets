from datasets import Dataset, concatenate_datasets


def main() -> None:
    train_like = Dataset.from_dict(
        {
            "id": [1, 2],
            "text": ["first dataset row 1", "first dataset row 2"],
        }
    )
    extra_like = Dataset.from_dict(
        {
            "id": [3, 4],
            "text": ["second dataset row 1", "second dataset row 2"],
        }
    )

    combined_dataset = concatenate_datasets([train_like, extra_like])

    print("Dataset after concatenate_datasets")
    print(combined_dataset)
    print()
    print("Rows:", combined_dataset[:])


if __name__ == "__main__":
    main()

from datasets import Dataset, interleave_datasets


def main() -> None:
    first_dataset = Dataset.from_dict(
        {
            "source": ["tips", "tips", "tips"],
            "text": ["tip-1", "tip-2", "tip-3"],
        }
    )
    second_dataset = Dataset.from_dict(
        {
            "source": ["examples", "examples"],
            "text": ["example-1", "example-2"],
        }
    )

    interleaved_dataset = interleave_datasets([first_dataset, second_dataset], stopping_strategy="all_exhausted")

    print("Dataset after interleave_datasets")
    print(interleaved_dataset)
    print()
    print("Rows:", interleaved_dataset[:])


if __name__ == "__main__":
    main()

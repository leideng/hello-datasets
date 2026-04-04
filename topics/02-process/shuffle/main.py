from datasets import Dataset


def main() -> None:
    dataset = Dataset.from_dict(
        {
            "id": [1, 2, 3, 4, 5],
            "text": [
                "first",
                "second",
                "third",
                "fourth",
                "fifth",
            ],
        }
    )

    shuffled_dataset = dataset.shuffle(seed=7)

    print("Dataset after shuffle")
    print(shuffled_dataset)
    print()
    print("Rows:", shuffled_dataset[:])


if __name__ == "__main__":
    main()

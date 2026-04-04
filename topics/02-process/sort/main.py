from datasets import Dataset


def main() -> None:
    dataset = Dataset.from_dict(
        {
            "id": [1, 2, 3, 4],
            "score": [0.82, 0.95, 0.74, 0.91],
        }
    )

    sorted_dataset = dataset.sort("score", reverse=True)

    print("Dataset after sort")
    print(sorted_dataset)
    print()
    print("Rows:", sorted_dataset[:])


if __name__ == "__main__":
    main()

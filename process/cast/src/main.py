from datasets import ClassLabel, Dataset, Features, Value


def main() -> None:
    dataset = Dataset.from_dict(
        {
            "text": [
                "this review is positive",
                "this review is negative",
                "this review is positive too",
            ],
            "label": [1, 0, 1],
        }
    )

    target_features = Features(
        {
            "text": Value("string"),
            "label": ClassLabel(names=["negative", "positive"]),
        }
    )

    cast_dataset = dataset.cast(target_features)

    print("Dataset after cast")
    print(cast_dataset)
    print()
    print("Features:", cast_dataset.features)
    print("Decoded labels:", [cast_dataset.features["label"].int2str(v) for v in cast_dataset["label"]])


if __name__ == "__main__":
    main()

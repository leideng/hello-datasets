from datasets import Dataset


def augment_batch(batch: dict[str, list]) -> dict[str, list]:
    augmented_text = []
    augmented_variant = []

    for text in batch["text"]:
        augmented_text.extend([text, text.upper()])
        augmented_variant.extend(["original", "uppercase"])

    return {
        "text": augmented_text,
        "variant": augmented_variant,
    }


def main() -> None:
    dataset = Dataset.from_dict(
        {
            "text": [
                "small examples are easier to inspect",
                "augmentation can increase row count",
            ]
        }
    )

    augmented_dataset = dataset.map(augment_batch, batched=True, remove_columns=["text"])

    print("Dataset after augmentation-style map")
    print(augmented_dataset)
    print()
    print("Rows:", augmented_dataset[:])


if __name__ == "__main__":
    main()

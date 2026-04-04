from datasets import Dataset


def build_preview(batch: dict[str, list]) -> dict[str, list]:
    return {
        "preview": [
            f"[{identifier}] {text.upper()}"
            for identifier, text in zip(batch["id"], batch["text"])
        ]
    }


def main() -> None:
    dataset = Dataset.from_dict(
        {
            "id": [1, 2, 3],
            "text": ["custom formatter", "returns derived values", "works on retrieval"],
        }
    )

    formatted_dataset = dataset.with_transform(build_preview)

    print("Dataset with a custom retrieval transform")
    print(formatted_dataset)
    print()
    print("Item 0:", formatted_dataset[0])
    print("Items 0:2:", formatted_dataset[:2])


if __name__ == "__main__":
    main()

from datasets import Dataset


def main() -> None:
    try:
        import torch  # noqa: F401
    except ImportError:
        print("This example requires PyTorch.")
        print("Install it in the root environment before running this script.")
        return

    dataset = Dataset.from_dict(
        {
            "id": [1, 2, 3],
            "values": [[1.0, 1.5], [2.0, 2.5], [3.0, 3.5]],
        }
    )

    torch_dataset = dataset.with_format("torch")
    first_item = torch_dataset[0]
    first_batch = torch_dataset[:2]

    print("Dataset with PyTorch output format")
    print(torch_dataset)
    print()
    print("Item 0 types:", {key: type(value) for key, value in first_item.items()})
    print("Item 0:", first_item)
    print("Batch types:", {key: type(value) for key, value in first_batch.items()})
    print("Batch values:", first_batch)


if __name__ == "__main__":
    main()

from datasets import Dataset


def main() -> None:
    try:
        import tensorflow as tf  # noqa: F401
    except ImportError:
        print("This example requires TensorFlow.")
        print("Install it in the root environment before running this script.")
        return

    dataset = Dataset.from_dict(
        {
            "id": [1, 2, 3],
            "values": [[1.0, 1.5], [2.0, 2.5], [3.0, 3.5]],
        }
    )

    tensorflow_dataset = dataset.with_format("tensorflow")
    first_item = tensorflow_dataset[0]
    first_batch = tensorflow_dataset[:2]

    print("Dataset with TensorFlow output format")
    print(tensorflow_dataset)
    print()
    print("Item 0 types:", {key: type(value) for key, value in first_item.items()})
    print("Item 0:", first_item)
    print("Batch types:", {key: type(value) for key, value in first_batch.items()})
    print("Batch values:", first_batch)


if __name__ == "__main__":
    main()

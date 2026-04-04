import numpy as np
from datasets import Dataset


def main() -> None:
    dataset = Dataset.from_dict(
        {
            "id": [1, 2, 3],
            "values": [[1.0, 1.5], [2.0, 2.5], [3.0, 3.5]],
        }
    )

    numpy_dataset = dataset.with_format("numpy")
    first_item = numpy_dataset[0]
    first_batch = numpy_dataset[:2]

    print("Dataset with NumPy output format")
    print(numpy_dataset)
    print()
    print("Item 0 types:", {key: type(value) for key, value in first_item.items()})
    print("Item 0:", first_item)
    print("Batch types:", {key: type(value) for key, value in first_batch.items()})
    print("Batch values:", first_batch)


if __name__ == "__main__":
    main()

import io
import json
import tarfile
from pathlib import Path

from datasets import load_dataset


def write_webdataset_tar(tar_file: Path) -> None:
    tar_file.parent.mkdir(parents=True, exist_ok=True)

    examples = [
        (
            "sample-0001",
            "webdataset groups files by shared prefix",
            {"label": "concept", "difficulty": "medium"},
        ),
        (
            "sample-0002",
            "each extension becomes a separate field",
            {"label": "structure", "difficulty": "medium"},
        ),
    ]

    with tarfile.open(tar_file, "w") as archive:
        for key, text, metadata in examples:
            txt_bytes = text.encode("utf-8")
            txt_info = tarfile.TarInfo(name=f"{key}.txt")
            txt_info.size = len(txt_bytes)
            archive.addfile(txt_info, io.BytesIO(txt_bytes))

            json_bytes = json.dumps(metadata).encode("utf-8")
            json_info = tarfile.TarInfo(name=f"{key}.json")
            json_info.size = len(json_bytes)
            archive.addfile(json_info, io.BytesIO(json_bytes))


def main() -> None:
    example_dir = Path(__file__).resolve().parent
    data_file = example_dir / "data" / "sample.tar"
    cache_dir = example_dir / ".cache"

    write_webdataset_tar(data_file)

    dataset = load_dataset(
        "webdataset",
        data_files=str(data_file),
        cache_dir=str(cache_dir),
    )["train"]

    print("Dataset loaded with load_dataset('webdataset', data_files=...)")
    print(dataset)
    print()
    print("Features:", dataset.features)
    print("First row:", dataset[0])


if __name__ == "__main__":
    main()

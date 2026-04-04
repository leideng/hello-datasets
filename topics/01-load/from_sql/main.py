import sqlite3
from pathlib import Path

from datasets import Dataset


def write_sqlite_database(database_file: Path) -> None:
    database_file.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(database_file)
    try:
        connection.execute("DROP TABLE IF EXISTS examples")
        connection.execute(
            """
            CREATE TABLE examples (
                id INTEGER,
                title TEXT,
                split TEXT
            )
            """
        )
        connection.executemany(
            "INSERT INTO examples (id, title, split) VALUES (?, ?, ?)",
            [
                (1, "load from sqlite", "train"),
                (2, "query only the rows you need", "train"),
                (3, "sql can prepare data before loading", "eval"),
            ],
        )
        connection.commit()
    finally:
        connection.close()


def main() -> None:
    example_dir = Path(__file__).resolve().parent
    database_file = example_dir / "data" / "sample.sqlite"
    cache_dir = example_dir / ".cache"

    write_sqlite_database(database_file)

    connection = sqlite3.connect(database_file)
    try:
        dataset = Dataset.from_sql(
            "SELECT id, title, split FROM examples WHERE split = 'train'",
            connection,
            cache_dir=str(cache_dir),
        )
    finally:
        connection.close()

    print("Dataset loaded with Dataset.from_sql(...)")
    print(dataset)
    print()
    print("Features:", dataset.features)
    print("Rows:", dataset[:])


if __name__ == "__main__":
    main()

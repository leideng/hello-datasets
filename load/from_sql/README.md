# from_sql

Load dataset rows from a SQL query with `Dataset.from_sql(...)`.

## What It Teaches

- `Dataset.from_sql(...)` can read query results into a Hugging Face dataset.
- SQL is useful when filtering or reshaping data before loading it.
- SQLite is enough for a minimal local example.

## Run

From the repository root:

```bash
uv run python load/from_sql/main.py
```

## Expected Result

The script:

- creates a local SQLite database in `data/`
- runs a SQL query that selects only training rows
- loads the query result into a dataset
- prints the schema and loaded rows

## Key Code Explanation

This section focuses on the important lines in `main.py`. Straightforward lines such as simple `print(...)` calls are intentionally omitted.

- Line 1: `import sqlite3`
  Imports SQLite support so the example can build and query a local database.
- Line 2: `from pathlib import Path`
  Imports `Path` so local files such as `data/` inputs and cache directories can be built safely.
- Line 4: `from datasets import Dataset`
  Imports `Dataset` from Hugging Face `datasets`, which is the main API demonstrated by this example.
- Line 7: `def write_sqlite_database(database_file: Path) -> None:`
  Defines `write_sqlite_database`, the function that groups one logical step of the example.
- Line 8: `    database_file.parent.mkdir(parents=True, exist_ok=True)`
  Creates the parent folder if it does not exist yet.
- Line 10: `    connection = sqlite3.connect(database_file)`
  Opens a SQLite connection so SQL commands can run against the sample database.
- Line 12: `        connection.execute("DROP TABLE IF EXISTS examples")`
  Runs a SQL statement that prepares the example table structure.
- Line 13: `        connection.execute(`
  Runs a SQL statement that prepares the example table structure.
- Line 22: `        connection.executemany(`
  Inserts multiple sample rows so the SQL loading step has data to read.
- Line 30: `        connection.commit()`
  Saves the inserted SQL rows to disk.
- Line 32: `        connection.close()`
  Closes the database connection after the work is finished.
- Line 35: `def main() -> None:`
  Defines `main`, the function that groups one logical step of the example.
- Line 36: `    example_dir = Path(__file__).resolve().parent`
  Finds the example folder so local `data/` and `.cache/` paths stay relative to this example.
- Line 37: `    database_file = example_dir / "data" / "sample.sqlite"`
  Builds the path to the local sample data used by the example.
- Line 38: `    cache_dir = example_dir / ".cache"`
  Keeps generated cache artifacts inside this example folder instead of a global location.
- Line 40: `    write_sqlite_database(database_file)`
  Calls the helper that creates the SQLite sample database before loading from it.
- Line 42: `    connection = sqlite3.connect(database_file)`
  Opens a SQLite connection so SQL commands can run against the sample database.
- Line 44: `        dataset = Dataset.from_sql(`
  Loads SQL query results directly into a Hugging Face dataset.
- Line 50: `        connection.close()`
  Closes the database connection after the work is finished.
- Line 59: `if __name__ == "__main__":`
  Runs the example only when this file is executed directly.

## Notes

- This example uses a local SQLite file, so it has no external database dependency.
- The SQL query is part of the example's teaching goal, not just setup.
- This folder stays under `load/from_sql/` because the topic is still SQL-based dataset loading.

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

## Notes

- This example uses a local SQLite file, so it has no external database dependency.
- The SQL query is part of the example's teaching goal, not just setup.
- This folder stays under `load/from_sql/` because the topic is still SQL-based dataset loading.

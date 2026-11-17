# SQL *(suggested)*

The language of databases. Every app stores data, and most backend and AI work touches a database. SQL is a skill you use for life.

## Install

```bash
sudo pacman -S --needed sqlite postgresql
sudo systemctl enable --now postgresql   # first run needs initdb; see Arch wiki
sqlite3 practice.db
```

Or practise in the browser at [sqlbolt.com](https://sqlbolt.com) and [sqlzoo.net](https://sqlzoo.net) with no install.

## Syllabus

### Level 1 – Querying
- [ ] `SELECT`, `FROM`, `WHERE`, `ORDER BY`, `LIMIT`
- [ ] Filtering: `AND`, `OR`, `IN`, `LIKE`, `BETWEEN`, `NULL`
- [ ] Aggregates: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`
- [ ] `GROUP BY` and `HAVING`

### Level 2 – Relations
- [ ] Tables, primary keys, foreign keys
- [ ] `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL JOIN`
- [ ] Subqueries and CTEs (`WITH`)
- [ ] Set operations: `UNION`, `INTERSECT`, `EXCEPT`

### Level 3 – Design and changing data
- [ ] `CREATE TABLE`, data types, constraints
- [ ] `INSERT`, `UPDATE`, `DELETE`, transactions
- [ ] Normalisation (1NF, 2NF, 3NF)
- [ ] Indexes and why they speed up queries
- [ ] `EXPLAIN` to read query plans

### Level 4 – Advanced
- [ ] Window functions (`ROW_NUMBER`, `RANK`, `LAG`)
- [ ] Views, stored procedures, triggers
- [ ] Transactions and isolation levels
- [ ] PostgreSQL features: JSONB, `pgvector` for AI embeddings

## Resources

| | Resource | Notes |
|---|---|---|
| ⭐🆓 | [SQLBolt](https://sqlbolt.com/) | Interactive lessons |
| ⭐🆓 | [SQLZoo](https://sqlzoo.net/) | Practice exercises |
| 🆓 | [PostgreSQL docs tutorial](https://www.postgresql.org/docs/current/tutorial.html) | Official |
| 🆓 | [Use The Index, Luke](https://use-the-index-luke.com/) | Indexing and performance |
| 🆓 | [Mode SQL Tutorial](https://mode.com/sql-tutorial/) | Analytics-focused |
| 💲 | *SQL Antipatterns* – Bill Karwin | Common mistakes |
| 💲 | *Designing Data-Intensive Applications* – Martin Kleppmann | Also in System Architecture |

## Projects

1. 🛠️ **Library database** with books, members and loans
2. 🛠️ **Sales analysis** with window functions on a public CSV dataset
3. 🛠️ **Backend for the Go or Rust projects** above

## Study timeline (about 6 weeks)
| Weeks | Focus | Done when |
|---|---|---|
| 1–2 | Level 1: querying | Ten queries on a sample database, without help |
| 3 | Level 2: relations | Multi-table reports using joins |
| 4 | Level 3: design | A schema you designed and normalised to 3NF |
| 5–6 | Level 4: advanced | Window-function analysis, and an index you justify with `EXPLAIN` |

## Common pitfalls
- **NULL comparisons.** `col = NULL` is never true. Use `IS NULL`.
- **`SELECT *` in application code.** It breaks when columns change.
- **Missing indexes** on columns used in joins and `WHERE` clauses.
- **N+1 queries:** one query per row, usually from an ORM loop.
- **Timestamps without time zones.** Store timestamps with time zones.
- **`COUNT(*)` vs `COUNT(column)`.** They treat NULLs differently.

## Where SQL is used
Almost every application. PostgreSQL, MySQL, SQLite and SQL Server are common databases. BigQuery, Snowflake and DuckDB are used for analytics.

## Ecosystem
- **PostgreSQL extensions:** PostGIS (maps), pgvector (embeddings), TimescaleDB (time series)
- **Tools:** `psql`, DBeaver (free GUI), DuckDB (local analytics)

## More reading
- *The Art of SQL* — Faroult & Robson (💲)
- *SQL Performance Explained* — Markus Winand (💲)
- [PostgreSQL Tutorial](https://www.postgresqltutorial.com/)

## My personal take

*These are my own opinions, not a fixed syllabus. Disagree and make your own call.*

- SQL is the most useful language on this list for most people. Almost every job touches a database eventually.
- Learn to read EXPLAIN output early. That's where real understanding of performance comes from.
- Practise on a dataset you care about, not only on toy tables.

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

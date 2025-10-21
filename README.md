# Pokémon Data Pipeline

This project demonstrates how to extract data from an external **REST API** (the [PokéAPI](https://pokeapi.co/)), transform it into a structured format using **Python + Pandas**, and load it into a **PostgreSQL** database using **SQLAlchemy**.

---

## Overview

The script:

1. Connects to a local PostgreSQL database.
2. Iterates through Pokémon IDs (1–119).
3. Fetches detailed Pokémon data (name, types, abilities, stats) from the PokéAPI.
4. Transforms the nested JSON into clean, tabular form.
5. Loads the data into a table named `poke_store` in PostgreSQL.

This is a beginner-friendly example of an **ETL (Extract–Transform–Load)** data pipeline.

---

## Prerequisites

Before running, make sure you have:

* **PostgreSQL** installed and running locally.
* A database created (e.g., `my_new_database`).
* **Python 3.9+** installed.
* The following Python packages:

  * `sqlalchemy`
  * `psycopg2`
  * `pandas`
  * `requests`

You can install them with:

```bash
pip install sqlalchemy psycopg2 pandas requests
```

---

## ⚙️ Database Setup

1. Log into PostgreSQL:

   ```bash
   psql -U postgres
   ```

2. Create the database:

   ```sql
   CREATE DATABASE my_new_database;
   ```

3. Verify connection details in your script:

   ```
   postgresql+psycopg2://postgres:1234@localhost:5432/my_new_database
   ```

   *(Adjust username, password, or port if needed.)*



# Articles Project

This project models a simple Articles system with **Authors**, **Magazines**, and **Articles** using **SQLite** as the database and **Python** for the backend logic. The project uses **Pipenv** for dependency management and virtual environments.

---

## Features

- Create and manage Authors, Magazines, and Articles
- Use raw SQL scripts to create and seed the database schema
- Python modules to interact with the database
- Basic CLI scripts for setup and seeding

---

## Getting Started

### Prerequisites

- Python 3.7+
- [Pipenv](https://pipenv.pypa.io/en/latest/) installed

---

### Setup

1. Clone the repository:

```bash
git clone <your-repo-url>
cd articles
Activate the Pipenv virtual environment:

bash
Copy
Edit
pipenv shell
Install dependencies:

bash
Copy
Edit
pipenv install
Create and seed the database:

bash
Copy
Edit
python scripts/setup_db.py
This will:

Create the articles.db SQLite database file

Create the tables (authors, magazines, articles)

Insert some initial sample data

Verify Setup
Check the database file:

bash
Copy
Edit
ls -l articles.db
Use the SQLite CLI to inspect tables and data:

bash
Copy
Edit
sqlite3 articles.db

sqlite> .tables
authors  magazines  articles

sqlite> SELECT * FROM authors;
Running Scripts
You can run other Python scripts inside scripts/ to interact with the database or test functionality:

bash
Copy
Edit
python scripts/your_script.py
Testing
Run automated tests (if available):

bash
Copy
Edit
pytest tests/
Project Structure
graphql
Copy
Edit
articles/
├── articles.db         
├── lib/                
│   ├── db/
│   │   ├── connection.py
│   │   ├── schema.sql
│   │   └── seed.py
│   ├── models/
│       ├── author.py
│       ├── magazine.py
│       └── article.py
├── scripts/
│   └── setup_db.py     
├── tests/              
├── Pipfile             
├── Pipfile.lock        
└── README.md           
Notes
Make sure to run the setup script from the project root so paths to schema.sql and other files resolve correctly.

If you modify the database schema (schema.sql), re-run the setup script to recreate tables.

The project currently uses raw SQL queries without an ORM.


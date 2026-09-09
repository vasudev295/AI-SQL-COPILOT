# 🚀 QueryPilot AI — Enterprise Text-to-SQL & Data Analyst Copilot

> **Ask questions in natural language. Get SQL, insights, and visualizations in seconds.**

QueryPilot AI is a **GenAI-powered Data Analyst Copilot** that converts natural-language business questions into SQL queries, executes them safely against a business database, and transforms the results into **actionable insights and visual analytics**.

Built to demonstrate how **Generative AI can automate real-world data analysis workflows** while maintaining SQL safety, validation, and business context.

---

## 🎯 Problem Statement

Business teams often depend on data analysts for every SQL query.

For example:

> ❌ "Can you write a SQL query to find the highest revenue region?"

An analyst needs to understand the requirement, write SQL, validate it, execute it, analyze the result, and create a visualization.

QueryPilot AI simplifies this workflow:

> ✅ **Business Question → AI-generated SQL → Validation → Execution → Visualization → Business Insight**

---

## ✨ Key Features

### 🤖 Natural Language → SQL

Ask questions in plain English and let Gemini generate the required SQL query.

### 🛡️ SQL Safety & Guardrails

Automatically validates generated SQL and blocks potentially destructive operations such as:

```text
DROP
DELETE
UPDATE
INSERT
ALTER
TRUNCATE
CREATE
```

The system is designed for **read-only analytics workloads**.

### 🔍 Business Context / Glossary

QueryPilot understands business terminology through a business glossary.

Example:

```text
Revenue = Total sales revenue
Average Order Value = Revenue / Number of Orders
Top Region = Region with maximum revenue
```

This helps the LLM generate SQL using business definitions rather than relying only on raw database schema.

### 🔄 Self-Correction

If generated SQL fails because of a database/query error, the system can use the error feedback to attempt a corrected query.

```text
Generate SQL
     ↓
Validate
     ↓
Execute
     ↓
Error?
  ↙     ↘
Yes      No
 ↓       ↓
Fix     Result
 ↓
Retry
```

### 📊 Automatic Data Visualization

Query results can be transformed into interactive visualizations using Plotly.

Supported analytical views include:

* Bar charts
* Line charts
* KPI-style analysis
* Tabular results

### 💡 Business-Friendly Insights

Instead of returning only raw SQL results, QueryPilot explains the findings in a way that a business stakeholder can understand.

Example:

> **West region generated the highest revenue, contributing approximately 31% of total sales.**

### 📈 Query Risk Scoring

Generated queries can be evaluated for analytical risk based on factors such as:

* Missing filters
* Complex JOINs
* Aggregations
* `SELECT *`
* Large result sets

### 🧪 Automated Testing

Core functionality is tested using **Pytest**, including SQL security and database operations.

---

# 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │       User           │
                    │ Natural Language     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Streamlit Frontend  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Query Understanding  │
                    └──────────┬───────────┘
                               │
                  ┌────────────┴────────────┐
                  ▼                         ▼
        ┌──────────────────┐      ┌──────────────────┐
        │ Database Schema  │      │ Business Glossary│
        │    Context       │      │    Context       │
        └────────┬─────────┘      └────────┬─────────┘
                 └────────────┬────────────┘
                              ▼
                    ┌──────────────────────┐
                    │    Gemini LLM        │
                    │    Text → SQL        │
                    └──────────┬───────────┘
                               ▼
                    ┌──────────────────────┐
                    │ SQL Guardrails &     │
                    │ Validation Layer     │
                    └──────────┬───────────┘
                               ▼
                    ┌──────────────────────┐
                    │   SQL Executor       │
                    │   Read-Only DB       │
                    └──────────┬───────────┘
                               ▼
                 ┌─────────────┴─────────────┐
                 ▼                           ▼
        ┌─────────────────┐        ┌──────────────────┐
        │ Data Results    │        │ Visualization    │
        └────────┬────────┘        └────────┬─────────┘
                 └─────────────┬────────────┘
                               ▼
                    ┌──────────────────────┐
                    │ Business Insights    │
                    └──────────────────────┘
```

---

# 🧠 Example Queries

Users can ask questions such as:

```text
Which region generated the highest revenue?
```

```text
What are the top 5 products by revenue?
```

```text
Show monthly revenue for 2025.
```

```text
Which products have the highest sales quantity?
```

```text
Compare revenue across different regions.
```

The system converts these questions into SQL automatically.

---

# 🗄️ Demo Database

The project currently uses a synthetic **e-commerce sales database** built for demonstrating analytics workflows.

### Tables

```text
products
├── product_id
├── product_name
├── category
└── unit_price

customers
├── customer_id
├── customer_name
└── region

sales
├── sale_id
├── sale_date
├── product_id
├── customer_id
├── quantity
└── revenue
```

The database contains sales data covering **2025**.

> The dataset is synthetic and intended for demonstration and development purposes.

---

# 🛠️ Tech Stack

| Technology       | Purpose                     |
| ---------------- | --------------------------- |
| 🐍 Python        | Core application            |
| 🤖 Gemini API    | Generative AI / Text-to-SQL |
| 🗃️ SQLite       | Analytics database          |
| 🔗 SQLAlchemy    | Database connectivity       |
| 🛡️ SQLGlot      | SQL parsing & validation    |
| 📊 Pandas        | Data processing             |
| 📈 Plotly        | Interactive visualization   |
| 🎨 Streamlit     | Data analyst interface      |
| ⚡ FastAPI        | Backend API                 |
| 🧪 Pytest        | Automated testing           |
| 🔐 Python-dotenv | Environment configuration   |

---

# 📁 Project Structure

```text
querypilot-ai/
│
├── app/
│   ├── agents/
│   │   ├── orchestrator.py
│   │   └── sql_generator.py
│   │
│   ├── api/
│   │   └── main.py
│   │
│   ├── database/
│   │   ├── connection.py
│   │   ├── executor.py
│   │   └── schema.py
│   │
│   ├── rag/
│   │   └── glossary.py
│   │
│   ├── security/
│   │   ├── sql_guard.py
│   │   └── risk.py
│   │
│   ├── visualization/
│   │   └── charts.py
│   │
│   └── frontend/
│       └── streamlit_app.py
│
├── data/
│   ├── business.db
│   └── create_database.py
│
├── prompts/
│   └── business_glossary.md
│
├── tests/
│   ├── test_database.py
│   └── test_sql_guard.py
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/vasudev295/AI-SQL-COPILOT.git
cd AI-SQL-COPILOT
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Activate environment

**Windows:**

```powershell
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Gemini API

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash
DATABASE_URL=sqlite:///./data/business.db
MAX_ROWS=500
```

⚠️ **Never commit your real API key to GitHub.**

### 6. Create the database

```bash
python data/create_database.py
```

### 7. Run tests

```bash
python -m pytest -q
```

### 8. Start the application

```bash
python -m streamlit run app/frontend/streamlit_app.py
```

Open:

```text
http://localhost:8501
```

---

# 🔐 Security Design

QueryPilot AI does not blindly execute LLM-generated SQL.

The pipeline includes:

```text
LLM Generated SQL
       ↓
SQL Parsing
       ↓
Forbidden Operation Check
       ↓
Validation
       ↓
Risk Analysis
       ↓
Read-Only Execution
```

This reduces the risk of accidentally executing destructive SQL generated by an LLM.

---

# 📊 Why This Project Matters

QueryPilot AI demonstrates a practical application of Generative AI in **modern data analytics**.

Instead of replacing the analyst, the system acts as a **copilot** that helps analysts and business users:

* Explore databases faster
* Generate SQL from natural language
* Reduce repetitive SQL work
* Discover trends
* Visualize results
* Understand business metrics
* Validate AI-generated queries

---

# 🚀 Future Improvements

Planned production-level improvements include:

* PostgreSQL / MySQL support
* Multi-database connectivity
* Role-based access control
* Advanced RAG pipeline
* Query caching
* Conversation memory
* Query performance optimization
* LLM evaluation framework
* Production monitoring
* Docker deployment
* Cloud deployment
* Analyst feedback loop

---

# 📌 Resume Impact

**QueryPilot AI — Enterprise Text-to-SQL & Data Analyst Copilot**

> Built a GenAI-powered Text-to-SQL analytics assistant using Python, Gemini, SQLAlchemy, SQLGlot, Pandas, Plotly, Streamlit, and FastAPI. Implemented SQL safety guardrails, business-context retrieval, automated visualization, query validation, and self-correction to transform natural-language business questions into actionable data insights.

---

# 👨‍💻 Author

**Vasudev**

GitHub:
https://github.com/vasudev295

---

## ⭐ If you found this project useful

Give the repository a ⭐ and feel free to explore or contribute!


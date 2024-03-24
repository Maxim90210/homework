cursor.execute("""
CREATE TABLE IF NOT EXISTS address (
    id INTEGER PRIMARY KEY,
    country TEXT NOT NULL,
    region TEXT NOT NULL
)
""")
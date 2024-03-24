cursor.execute("""
ALTER TABLE address
ADD COLUMN index_code TEXT DEFAULT NULL
""")
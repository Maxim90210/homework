cursor.execute("""
ALTER TABLE address
ADD COLUMN street TEXT DEFAULT 'вулиця І.Франка'
""")
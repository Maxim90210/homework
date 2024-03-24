import sqlite3

connection = sqlite3.connect('shop.db')
cursor = connection.cursor()

cursor.execute("""
SELECT o.id AS order_id, c.name AS customer_name, p.title AS product_title, o.quantity,
       p.price, (o.quantity * p.price) AS total_cost
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN products p ON o.product_id = p.id
""")

joined_data = cursor.fetchall()
for row in joined_data:
    print(row)

connection.close()
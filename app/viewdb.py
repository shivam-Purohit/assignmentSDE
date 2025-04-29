import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('travel.db')
cursor = conn.cursor()

# Query data from the 'itineraries' table
cursor.execute("SELECT * FROM itineraries")

# Fetch all results
rows = cursor.fetchall()

# Print each row
for row in rows:
    print(row)

# Close the connection
conn.close()
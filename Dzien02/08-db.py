
# Lączenie z bazą danych
import psycopg2
import datetime

conn = psycopg2.connect()
cursor = conn.cursor()

# operacja na danych
# SELECT
sql = "SELECT * FROM public.city WHERE city_id=6"
cursor.execute(sql)
row = cursor.fetchone()
print(row)

print("-"*60)
sql = "SELECT * FROM public.city WHERE city_id<10"
cursor.execute(sql)
rows = cursor.fetchall()
print(rows)

# INSERT
sql = """

    INSERT INTO public.city 
            (city, country_id, last_update)
            VALUES
            (%s , 15, %s)

"""
data = ("Marianowo", datetime.datetime.today() )
cursor.execute(sql, data)
conn.commit()

cursor.close()
conn.close()
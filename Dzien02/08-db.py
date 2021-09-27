
# Lączenie z bazą danych
import psycopg2
import datetime

conn = psycopg2.connect()
conn.set_session(autocommit=True)
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

# UPDATE
sql = "UPDATE public.city SET city=%s WHERE city=%s "
cursor.execute(sql,  ("Marionowo City","Marianowo") )
conn.commit()

# DELETE
sql = "DELETE FROM public.city WHERE city=%s"
cursor.execute(sql, ("Marionowo City",) )
conn.commit()

cursor.close()
conn.close()
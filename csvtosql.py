import csv
import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="Flashcard",
    user='postgres',
    password=1)
try:

    cur = conn.cursor()

    with open('words.csv', 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        counter = 0
        levels = 1
        for row in reader:
            #levels = int(row[0])/20 + 1

            if counter == 20:
                levels += 1
                counter = 0
            row.append(levels)
            counter += 1
            cur.execute(
                f""" insert into public."Words"(words_id,frequency,dutch,English,words_of_level) 
                VALUES ({int(row[0])},{int(row[1])},'{row[2]}','{row[3]}',{int(row[4])})""")

    cur.close()
    conn.commit()
except (Exception) as error:
    print(error)
finally:
    # close the connection at the end
    if conn is not None:
        conn.close()
        print('Database connection closed.')

import sqlite3
import mysql.connector as mysql

MY_HOST = 'localhost'
MY_USER = ''
MY_PASS = ''

def main():
    db = mysql.connect(host=MY_HOST, user=MY_USER, password=MY_PASS, database='scratch')
    cur = db.cursor(prepared=True)

    db_lite = sqlite3.connect(":memory:")
    cur_list = db_lite.cursor()

    cur.execute("DROP TABLE IF EXISTS temp")
    cur.execute("CREATE TABLE IF NOT EXISTS temp ( a TEXT, b TEXT, c TEXT )")

    values = (
        ('one', 'two', 'three'),
        ('two', 'three', 'four'),
        ('three', 'four', 'five'),
        ('four', 'five', 'six'),
        ('five', 'six', 'seven'),
        ('six', 'seven', 'eight'),
        ('seven', 'eight', 'nine'),
        ('eight', 'nine', 'ten'),
        ('nine', 'ten', 'eleven')
    )
    insert_statement = "INSERT INTO temp VALUES (?, ?, ?)"
    cur.executemany(insert_statement, values)

    cur.execute("SELECT * FROM temp")
    cur_lite.execute("CREATE TABLE IF NOT EXISTS temp ( a TEXT, b TEXT, c TEXT )")
    for row in cur:
        cur_lite.execute("INSERT INTO temp VALUES (row[0], row[1], row[2])")
        db_lite.commit()
        print(row)

    cur.close()
    db.close()

    cur_lite.execute("INSERT INTO temp VALUES ('seven', 'eight', 'nine')")
    db_lite.commit()

if __name__ == "__main__":
    main()
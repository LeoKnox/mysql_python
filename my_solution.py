import sqlite3
import mysql.connector as mysql

MY_HOST = 'pluto.local'
MY_USER = 'appuser'
MY_PASS = 'Spartacus'

def main():
    db = mysql.connect(host=MY_HOST, user=MY_USER, password=MY_PASS, database='scratch')
    cur = db.cursor(prepared=True)

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
    
    db = sqlite3.connect(":memory:")
    cur = db.cursor()

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
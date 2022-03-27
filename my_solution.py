import sqlite3

def main():
    db = sqlite3.connect(":memory:")
    cur = db.cursor()

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
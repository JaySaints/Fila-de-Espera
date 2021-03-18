from mysql.connector import connection
import json

class ConnectionDB():
    def __init__(self):
        log = json.loads(open("cnx_client.txt", 'r').readline())
        config = {
        'user': log[0]['user'],
        'password': log[0]['passwd'],
        'host': log[0]['host'],
        'database': log[0]['database']
        }
        self.cnn = connection.MySQLConnection(**config)
        self.cur = self.cnn.cursor()
        open("cnx_client.txt", 'r').close()
        self.create_table()

    def create_table(self):
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS list_PM("
            "id INT NOT NULL AUTO_INCREMENT,"
            "user VARCHAR(15) NOT NULL,"
            "created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,"
            " PRIMARY KEY (id)"
            ") ENGINE=InnoDB"
        )
        self.cnn.commit()

    # ADD
    def add_user(self, table, user):
        self.cur.execute("INSERT INTO {} (user) VALUES (%s)".format(table), (user,))
        self.cnn.commit()

    # SELECT
    def select_user(self, table):
        self.cur.execute("SELECT user, TIME(created) FROM {}".format(table))
        row = self.cur.fetchall()
        return row

    # REMOVE
    def remove_user(self, table, user):
        sql = ("DELETE FROM {} WHERE user = %s".format(table))
        self.cur.execute(sql, (user,))
        self.cnn.commit()

    def commit_cnx(self):
        return self.cnn.commit()

    def show_tables(self):
        self.cur.execute('SHOW TABLES;')
        for tables in self.cur:
            for index in tables:
                print("")
                print("- {}".format(index))

ConnectionDB()

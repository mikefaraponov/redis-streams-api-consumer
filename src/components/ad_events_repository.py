from psycopg2.extensions import connection

class AdEventsRepository:
    def __init__(self, conn: connection):
        self.conn = conn

    def add_clicks(self, clicks: list):
        sql = """INSERT INTO clicks() VALUES(%s);"""
        cur = self.conn.cursor()
        cur.executemany(sql, clicks)
        self.conn.commit()
        cur.close()

    def add_impressions(self, impressions: list):
        sql = """INSERT INTO impressions() VALUES(%s);"""
        cur = self.conn.cursor()
        cur.executemany(sql, impressions)
        self.conn.commit()
        cur.close()

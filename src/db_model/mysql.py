import pymysql

MYSQL_HOST = "localhost"
USER = "admin"
PASSWORD = "admin"
MYSQL_CONN = pymysql.connect(
    host=MYSQL_HOST,
    port=3306,
    user=USER,
    passwd=PASSWORD,
    db="blog_db",
    charset="utf8",
)

def conn_mysqldb():
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect=True)

    return MYSQL_CONN

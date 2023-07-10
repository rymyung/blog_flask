import pymysql

db_conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="admin",
    passwd="admin",
    db="blog_db",
    charset="utf8",
)
blog_db = db_conn.cursor()

sql = """
CREATE TABLE user_info(
    USER_ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    USER_EMAIL VARCHAR(100) NOT NULL,
    BLOG_ID CHAR(4),
    PRIMARY KEY(USER_ID)
);
"""
blog_db.execute(sql)
db_conn.commit()

sql = "SHOW TABLES;"
blog_db.execute(sql)
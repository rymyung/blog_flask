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

# user_email = "test@test.com"
# blog_id = "A"
# sql = f"""
# INSERT INTO user_info (USER_EMAIL, BLOG_ID)
# VALUES('{user_email}', '{blog_id}')
# """
# blog_db.execute(sql)
# db_conn.commit()

sql = """
SELECT *
FROM user_info
"""
blog_db.execute(sql)
results = blog_db.fetchall()
for result in results:
    print(result, type(result))

db_conn.close()
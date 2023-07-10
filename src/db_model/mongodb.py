import pymongo

USER = "admin"
PASSWORD = "admin"
MONGO_HOST = "localhost"
MONGO_CONN = pymongo.MongoClient(f"mongodb://{USER}:{PASSWORD}@{MONGO_HOST}")

def conn_mongodb():
    try:
        MONGO_CONN.admin.command("ismaster")
        blog_ab = MONGO_CONN.blog_session_db.blog_ab
    except:
        blog_ab = MONGO_CONN.blog_session_db.blog_ab

    return blog_ab
import pymysql
import environ
pymysql.version_info = (1, 4, 3, "final", 0)
# pip install pymysql

def accessDatabase():
    env = environ.Env(
        # set casting, default value
        DEBUG=(bool, False)
    )

    conn = pymysql.connect(host=env('DB_HOST'),
                            user=env('DB_USERNAME'), 
                            password=env('DB_PASSWORD'), 
                            db=env('DB_NAME'),
                            charset='utf8'
                            )
    return conn


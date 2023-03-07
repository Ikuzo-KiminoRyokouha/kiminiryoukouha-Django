import pymysql
import environ
# pip install pymysql

def accessDatabase():
    env = environ.Env(
        # set casting, default value
        DEBUG=(bool, False)
    )

    conn = pymysql.connect(host=env('DB_HOST'),
                            user=env('DB_USERNAME'), 
                            password=env('DB_PASSWORD'), 
                            db='ikuzo',
                            charset='utf8'
                            )
    return conn


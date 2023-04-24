import MySQLdb
MySQLdb.version_info = (1, 4, 3, "final", 0)
import environ
# pip install pymysql

def accessDatabase():
    env = environ.Env(
        # set casting, default value
        DEBUG=(bool, False)
    )

    conn = MySQLdb.connect(host=env('DB_HOST'),
                            user=env('DB_USERNAME'), 
                            password=env('DB_PASSWORD'), 
                            db='ikuzo2',
                            charset='utf8'
                            )
    return conn


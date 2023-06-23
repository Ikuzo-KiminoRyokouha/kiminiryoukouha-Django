import pymysql
pymysql.version_info = (1, 4, 3, "final", 0)
from destinations.utils.accessDatabase import accessDatabase
import environ


def getPlanDestination(userId):
    env = environ.Env(
        # set casting, default value
        DEBUG=(bool, False)
    )

    conn = accessDatabase()
    curs = conn.cursor(pymysql.cursors.DictCursor)
    # 커서(cursor)는 데이터베이스에 SQL 문을 실행하거나 실행된 결과를 돌려받는 통로
    selectNowPlanSql = "SELECT travel.id , travel.planId , travel.destinationId FROM "+ env('DB_NAME')+".travel left join "+ env('DB_NAME')+".plan on travel.planId = plan.id WHERE  plan.userId="+str(userId) 
    curs.execute(selectNowPlanSql)
    rows = curs.fetchall()
    conn.close()
    return rows
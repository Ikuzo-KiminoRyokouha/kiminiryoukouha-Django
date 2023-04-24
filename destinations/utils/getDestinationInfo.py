import MySQLdb
MySQLdb.version_info = (1, 4, 3, "final", 0)
from destinations.utils.accessDatabase import accessDatabase


def getPlanDestination(userId):
    conn = accessDatabase()
    curs = conn.cursor(MySQLdb.cursors.DictCursor)
    # 커서(cursor)는 데이터베이스에 SQL 문을 실행하거나 실행된 결과를 돌려받는 통로
    selectNowPlanSql = "SELECT travel.id , travel.planId , travel.destinationId FROM ikuzo.travel left join ikuzo.plan on travel.planId = plan.id WHERE  plan.userId="+str(userId) 
    curs.execute(selectNowPlanSql)
    rows = curs.fetchall()
    conn.close()
    return rows
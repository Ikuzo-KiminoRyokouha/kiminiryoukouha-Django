import pandas
from destinations.utils.accessDatabase import accessDatabase


def dataToCSV():
    conn = accessDatabase()
    selectRatingSql = 'SELECT userId, destinationId,rating , createdAt FROM rating'
    selectDestinationSql = 'SELECT id , title , createdAT, cat3, areacode ,sigungucode FROM destination '
    rating = pandas.read_sql_query(selectRatingSql,conn)
    destination = pandas.read_sql_query(selectDestinationSql,conn)
    rating.to_csv(r'pandas_output.csv',index=False ,header=False)
    destination.to_csv(r'pandas_destination_output.csv',index=False )

    conn.close()
print('reset rating data and ')
dataToCSV()

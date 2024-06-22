from sqlalchemy import text
from db.mysql import Session

def get_user_details():
    session = Session()
    sql_query = text('SELECT * FROM user_details')
    result = session.execute(sql_query)
    return result.fetchall()
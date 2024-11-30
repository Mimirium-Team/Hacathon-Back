import pandas as pd
from getConnect import get_connection
def load_data_from_db(db_name="example.db"):
    conn = get_connection(db_name)
    query = "SELECT * FROM people"  # Убедитесь, что такая таблица существует
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df
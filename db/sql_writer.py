def write_to_sql(df, engine, table_name: str):
    """
    Zapisuje DataFrame do tabeli SQL.
    """
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)

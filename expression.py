from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
    )

user = 'postgres'
password = '1234'
host = '127.0.0.1'
port = 5432
database = 'chinook'

db = create_engine("postgresql+psycopg2://postgres:1234@localhost/chinook")

meta = MetaData(db)

artist_table = Table(
    "Artist", meta,
    Column("ArtistID", Integer, primary_key=True),
    Column("Name", String)
    )

with db.connect() as connection:
    select_query = artist_table.select().where(artist_table.c.Name == "Queen")

results = connection.execute(select_query)
for result in results:
    print(result)
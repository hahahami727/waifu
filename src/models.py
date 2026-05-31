from sqlalchemy import Table, Column, Integer, String, MetaData

metadata_obj = MetaData()

employers_table = Table(
    "employers",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("age", Integer),
)
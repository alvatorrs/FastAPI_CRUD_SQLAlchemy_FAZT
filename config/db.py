from sqlalchemy import create_engine, MetaData

# creamos el engine con el conector de pymysql
engine = create_engine("mysql+pymysql://root:56208856@localhost:7777/storedb")

meta = MetaData()

# creamos la conexion
conn = engine.connect()

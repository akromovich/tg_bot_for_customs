from sqlalchemy import create_engine

engine = create_engine('sqlite:///database.db')
connect = engine.connect()
cursor = conn

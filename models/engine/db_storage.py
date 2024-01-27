import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from os import getenv


base = declarative_base()

class db_storage:
	def __init__(self):
		db_user = getenv('db_user')
		passwd = getenv('db_passwd')
		host = getenv('db_host')
		database = getenv('db_name')
		db_url = f"mysql+mysqlclient://{db_user}:{passwd}@{host}/{database}"

		self.engine = create_engine(db_url)
		#self.SessionLocal = sessionmaker(autocommit=False, autoflash=False, bind=self.engine)


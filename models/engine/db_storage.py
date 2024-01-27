import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session
from os import getenv
from models.base_model import Base


base = declarative_base()


class db_storage:
	"""connect mysql to the db"""
	__engine = None
	__session = None

	def __init__(self):
		db_user = getenv('db_user')
		passwd = getenv('db_passwd')
		host = getenv('db_host')
		database = getenv('db_name')
		db_url = f"mysql+mysqlclient://{db_user}:{passwd}@{host}/{database}"

		self.engine = create_engine(db_url)

	def new(self, obj):
		""" add new item to database """
		self.__session.add(obj)

	def save(self):
		"""save all the changes made in the db"""
		self.__session.commit()

	def delete(self, obj=None):
		"""delete from the current db session if obj is not None"""
		if obj is not None:
			self.__session.delete(obj)

	def reload(self):
		"""use a sessionmaker to create a cuurent db session"""
		self.__session = Base.metadata.create_all(self.__engine)
		factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
		Session = scoped_session(factory)
		self.__session = Session()

	def close(self):
		"""Remove session"""
		self.__session.close()
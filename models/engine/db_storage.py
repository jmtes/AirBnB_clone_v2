#!/usr/bin/python3
"""This is database storage class for Airbnb
"""
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

class DBStorage:
    """
    A DBStorage class
    """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(os.environ['HBNB_MYSQL_USER'], os.environ['HBNB_MYSQL_PWD'], os.environ['HBNB_MYSQL_HOST'], os.environ['HBNB_MYSQL_DB'], pool_pre_ping=True))
        if os.environ == 'HBNB_ENV':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Returns a dictionary with objects of cls
        """
        newdict = {}
        if not cls:
            for i in session.query(State, City).all():
                key = i.__class__.__name__ + "." + i.id
                newdict[key] = i
                return (newdict)
        else:
            for i in session.query(cls).all():
                key = i.__class__.__name__ + "." + i.id
                newdict[key] = i
                return (newdict)

    def new(self, obj):
        """adds the object to the current database session
        """
        self.__session.add(obj)
        #self.save()

    def save(self):
        """
        commits all changes of the current database session
        """
        #self.__session.flush()
        self.__session.commit()

    def delete(self, obj=None):
        """deletes from the current database session obj if not None
        """
        if obj:
            obj_id = obj.id
            obj_result = session.query(type(obj).filer(type(obj).id==obj_id.delete()))
        #    self.__session.commit()

    def reload(self):
        """creates all tables in the database (feature of SQLAlchemy)
        """
        Base.metadata.create_all(self.__engine)
        Session_s = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session_s)
        self.__session = Session()




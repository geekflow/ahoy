# -*- coding: utf-8 -*-
"""
    .model.database
    ~~~~~~~~~~~~~~~~~

    :copyright: (c) 2018 by geeksaga.
    :license: MIT LICENSE 2.0, see license for more details.
"""

from sqlalchemy import create_engine
from sqlalchemy.sql.expression import insert
from sqlalchemy.orm import scoped_session, sessionmaker
# from werkzeug import check_password_hash, generate_password_hash

"""    
def init_db():
    from .model.user import User

    Base.metadata.create_all(bind=engine)
    
    Base.query
    
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
"""


class DBManager:
    __engine = None
    __session = None

    @staticmethod
    def init(db_url, db_log_flag=True):
        DBManager.__engine = create_engine(db_url, convert_unicode=True, echo=db_log_flag) 
        DBManager.__session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=DBManager.__engine))
            
        from ..model import Base
        Base.query = DBManager.__session.query_property()            
        Base.metadata.create_all(bind=DBManager.__engine)
        
    @staticmethod
    def init_db():
        from .version import Version
        
        #insert(User).values(username='admin', password=generate_password_hash('admin'), email='geeksaga@geeksaga.com')
        #dao.add(User('admin', 'geeksaga@geeksaga.com', generate_password_hash('admin')))
        #dao.commit()

    @staticmethod
    def session():
        return DBManager.__session
    
    def __del__(self):
        pass
    
#updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

#db_session = None
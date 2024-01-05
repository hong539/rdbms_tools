from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from threading import Thread
from time import sleep

engine = create_engine('mysql+mysqlconnector://your_username:your_password@localhost/mydatabase')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class TableA(Base):
    __tablename__ = 'Table_A'
    id = Column(Integer, primary_key=True)

class TableB(Base):
    __tablename__ = 'Table_B'
    id = Column(Integer, primary_key=True)

Base.metadata.create_all(engine)

def transaction1():
    session = Session()
    try:
        session.begin()
        session.query(TableA).filter_by(id=1).with_for_update().all()
        sleep(2)
        session.query(TableB).filter_by(id=1).with_for_update().all()
        session.commit()
    except OperationalError as e:
        print("Error:", e)
        session.rollback()
    finally:
        session.close()

def transaction2():
    session = Session()
    try:
        session.begin()
        session.query(TableB).filter_by(id=1).with_for_update().all()
        sleep(2)
        session.query(TableA).filter_by(id=1).with_for_update().all()
        session.commit()
    except OperationalError as e:
        print("Error:", e)
        session.rollback()
    finally:
        session.close()

thread1 = Thread(target=transaction1)
thread2 = Thread(target=transaction2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
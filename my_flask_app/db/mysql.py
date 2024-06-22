from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
url="mysql+mysqlconnector://root:abc123456@172.18.0.3:3306/test"
engine=create_engine(url,pool_size=5)
Session=sessionmaker(bind=engine)
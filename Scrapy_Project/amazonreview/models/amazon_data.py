from sqlalchemy import Column, Integer, VARCHAR, SmallInteger, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AmazonData(Base):
    __tablename__ = "amazon_data"

    id = Column('id', Integer, primary_key=True)
    brand_id = Column('brand_id', Integer)
    asin = Column('asin', VARCHAR, unique=True)
    product_name = Column('product_name', VARCHAR)
    product_link = Column('product_link', VARCHAR)
    review_links = Column('review_links', VARCHAR)
    status = Column('status', SmallInteger, default=1)
    created_at = Column('created_at', DateTime)
    created_by = Column('created_by', Integer)
    updated_at = Column('updated_at', DateTime)
    updated_by = Column('updated_by', Integer)

    def __init__(self, data):
        self.brand_id = data[0]
        self.asin = data[1]
        self.product_name = data[2]
        self.product_link = data[3]
        self.review_links = data[4]



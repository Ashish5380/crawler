from sqlalchemy import Column, Integer, VARCHAR, SmallInteger, DateTime, TEXT
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class AmazonReview(Base):
    __tablename__ = "amazon_review"

    id = Column('id', Integer, primary_key=True)
    brand_id = Column('brand_id', Integer)
    star_rating = Column('star_rating', VARCHAR)
    rating_text = Column('rating_text', TEXT)
    author = Column('author', VARCHAR)
    posted_date = Column('posted_date', DateTime)
    review_header = Column('review_header', VARCHAR)
    review_link = Column('review_link', VARCHAR)
    user_profile = Column('user_profile', VARCHAR)
    verified_user = Column('verified_user', VARCHAR)
    review_hash = Column('review_text_hash', VARCHAR)
    product_id = Column('product_id', SmallInteger, default=1)
    status = Column('status', SmallInteger, default=1)
    created_at = Column('created_at', DateTime)
    updated_at = Column('updated_at', DateTime)

    def __init__(self, review_data):
        self.brandId = review_data.get("brand_id")
        self.star_rating = review_data.get("star_rating")
        self.rating_text = review_data.get("rating_text")
        self.author = review_data.get("author")
        self.posted_date = review_data.get("posted_date")
        self.review_header = review_data.get("review_header")
        self.review_link = review_data.get("review_link")
        self.user_profile = review_data.get("user_profile")
        self.verified_user = review_data.get("verified_user")
        self.review_text_hash = review_data.get("review_text_hash")
        self.product_id = review_data.get("product_id") if review_data.get("product_id") else 1
        self.status = 1
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
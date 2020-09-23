from ecommerce_crawler.onedirect_common.config.spreadsheet import AmazonLinks
from ecommerce_crawler.onedirect_common.utils.mysqlutils import MysqlUtil
from ecommerce_crawler.onedirect_common.models.amazon_data import AmazonData
from ecommerce_crawler.onedirect_common.utils.logger import logger

from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError


class SheetToSql(MysqlUtil, AmazonLinks):

    def __init__(self, mysql_util, data):
        super().__init__()
        self.db_engine = mysql_util.db_engine
        self.spreadsheet_data = self.remove_duplicate(data)
        self.update_product_data_mysql(spreadsheet_data=self.spreadsheet_data)

    def remove_duplicate(self, data):
        new_data = []
        db_data = None
        Session = sessionmaker(bind=self.db_engine)
        session = Session()
        try:
            db_data = session.query(AmazonData).all()
        except Exception as e:
            logger.error("Unable to get dat from data base for validating. Exception :: {0}".format(e))
            raise e
        finally:
            session.close()

        for row in data:
            flag = False
            for db_row in db_data:
                if row[1] == db_row.asin:
                    logger.info("Find duplicate element for brand :: {0} and element :: {1}".format(db_row.brand_id,
                                                                                                    db_row.asin))
                    flag = True
            if flag is not True:
                new_data.append(row)
        return new_data

    def update_product_data_mysql(self, spreadsheet_data):
        logger.info("Starting to push data to DB from Spreadsheet")
        Session = sessionmaker(bind=self.db_engine)
        session = Session()

        for row in spreadsheet_data:
            try:
                data = AmazonData(row)
                session.add(data)
            except IntegrityError as ie:
                logger.error("duplicate Entry was tried to be pushed {0} with exception :: {1}".format(row, ie))
                session.rollback()
            except Exception as ex:
                logger.info("Exception Occurred while saving sheet data to DB with stack trace {0}".format(ex))
                session.rollback()
            finally:
                session.commit()
                session.close()




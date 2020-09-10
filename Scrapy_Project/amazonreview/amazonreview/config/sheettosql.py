from Scrapy_Project.amazonreview.amazonreview.utils.mysqlutils import MysqlUtil
from Scrapy_Project.amazonreview.amazonreview.config.spreadsheet import AmazonLinks


class SheetToSql(MysqlUtil, AmazonLinks):

    def __init__(self, mysqlutil, amazondata):

        super().__init__()
        self.read_connection = mysqlutil.od_read_db_engine
        self.write_connection = mysqlutil.od_write_db_engine
        self.spreadsheet_data = amazondata.data

    def update_data_mysql(self):
        self.write_connection.execute()
        self.read_connection.execute()


if __name__ == '__main__':
    SheetToSql()

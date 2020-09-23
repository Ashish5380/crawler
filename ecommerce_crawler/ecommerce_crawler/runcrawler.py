from flask import Flask, Response
from ecommerce_crawler.onedirect_common.config.sqltosheet import SheetToSql
from ecommerce_crawler.onedirect_common.utils.mysqlutils import MysqlUtil
from ecommerce_crawler.onedirect_common.config.spreadsheet import AmazonLinks

app = Flask(__name__)


class RunCrawler:

    @staticmethod
    @app.route('/sync-db', methods=['GET'])
    def run_sheet_sync():
        SheetToSql(MysqlUtil(), AmazonLinks().data)
        return Response(status=200)


if __name__ == '__main__':
    app.run(debug=True)

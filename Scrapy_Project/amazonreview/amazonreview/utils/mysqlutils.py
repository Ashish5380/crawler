from sqlalchemy import create_engine


class MysqlUtil:
    od_read_db_engine = None
    od_write_db_engine = None
    config = {}

    def generate_config(self):
        self.config.__setitem__('USER', 'amazonuser')
        self.config.__setitem__('PASS', 'Am@z0nU&3r')
        self.config.__setitem__('HOST', '172.16.1.105')
        self.config.__setitem__('PORT', '3306')
        self.config.__setitem__('DB', 'amazon')

    @classmethod
    def get_mysql_url(self, config):
        return "mysql://{0}:{1}@{2}:{3}/{4}?charset=utf8".format(
            config['USER'], config['PASS'], config['HOST'], config['PORT'], config['DB'])

    @classmethod
    def get_db_engine(self, config):
        return create_engine(self.get_mysql_url(self.config),pool_size=5, pool_recycle=360)

    def __init__(self):
        self.generate_config()
        if self.od_read_db_engine is None:
            self.od_read_db_engine = self.get_db_engine(self.generate_config())

        if self.od_write_db_engine is None:
            self.od_write_db_engine = self.get_db_engine(self.generate_config())

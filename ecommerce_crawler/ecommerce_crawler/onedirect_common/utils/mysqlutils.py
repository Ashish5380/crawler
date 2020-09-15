from sqlalchemy import create_engine


class MysqlUtil:
    db_engine = None
    db_config_map = {}

    def __init__(self):
        self.intialize_db_config_map()
        if self.db_engine is None:
            self.db_engine = self.get_db_engine(self.db_config_map)

    @classmethod
    def intialize_db_config_map(cls):
        cls.db_config_map.__setitem__('USER', 'amazonuser')
        cls.db_config_map.__setitem__('PASS', 'Am@z0nU&3r')
        cls.db_config_map.__setitem__('HOST', '172.16.1.105')
        cls.db_config_map.__setitem__('PORT', '3306')
        cls.db_config_map.__setitem__('DB', 'amazon')

    @classmethod
    def get_mysql_url(cls, config):
        return "mysql://{0}:{1}@{2}:{3}/{4}?charset=utf8".format(
            config['USER'], config['PASS'], config['HOST'], config['PORT'], config['DB'])

    @classmethod
    def get_db_engine(cls, config):
        return create_engine(cls.get_mysql_url(config), pool_size=5, pool_recycle=360)
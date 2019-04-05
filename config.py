DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = 'root'
HOST = '47.107.173.225'
PORT = '3306'
DATABASE = 'cracklcz'

SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}'.format(
    DIALECT,
    DRIVER,
    USERNAME,
    PASSWORD,
    HOST,
    PORT,
    DATABASE
)

# 便于调试
TEMPLATES_AUTO_RELOAD = True
SEND_FILE_MAX_AGE_DEFAULT = 0
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@47.107.173.225:3306/springMVC'
# 'mysql+pymysql://用户名称:密码@localhost:端口/数据库名称'
SQLALCHEMY_TRACK_MODIFICATIONS = True
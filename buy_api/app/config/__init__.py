import os


class Config:

    # MYSQL_USER = 'root'  # 数据库用户名
    # MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or 'fnnzald'  # 数据库密码
    # MYSQL_HOST = 'localhost'  # ip or host
    # MYSQL_PORT = 3306  # 数据库端口
    # MYSQL_DATABASE = 'AiTx'  # 数据库名称

    SQLITE_FILE = os.path.abspath('./buy.sqlite')
    STATIC_IMAGE_PATH = os.path.abspath('static')
    UPLOAD_IMAGE_PATH = os.path.join(STATIC_IMAGE_PATH, 'upload')


if not os.path.exists(Config.STATIC_IMAGE_PATH):
    os.mkdir(Config.STATIC_IMAGE_PATH)

if not os.path.exists(Config.UPLOAD_IMAGE_PATH):
    os.mkdir(Config.UPLOAD_IMAGE_PATH)
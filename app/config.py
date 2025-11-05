import os
from dotenv import load_dotenv

load_dotenv()

MYSQL_USER = os.getenv("MYSQLUSER", "root")
MYSQL_PASSWORD = os.getenv("MYSQLPASSWORD", "AqTBsOLdQFshorJbUtYhZZMElCReCnIL")
MYSQL_HOST = os.getenv("MYSQLHOST", "ballast.proxy.rlwy.net")
MYSQL_PORT = os.getenv("MYSQLPORT", "29391")
MYSQL_DB = os.getenv("MYSQLDATABASE", "railway")
DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
#DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data.db")
SECRET_KEY = os.getenv("SECRET_KEY", "changeme")

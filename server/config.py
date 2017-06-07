import os
import urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

db_name = url.path[1:]
db_host = url.hostname
db_password = url.password
db_user = url.username

docker_db_name = 'transactiondb'

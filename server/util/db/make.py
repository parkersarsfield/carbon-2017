import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from config import docker_db_name
from subprocess import call

db_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '..', 'db')

call(['docker', 'run', '-d', '-p', '5432:5432', '-v', '{}:/var/lib/postgresql/data'.format(db_path), '--name', docker_db_name, 'postgres'])

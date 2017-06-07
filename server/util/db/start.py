import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from config import docker_db_name
from subprocess import call

call(['docker', 'start', docker_db_name])

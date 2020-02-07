import datetime
import config as conf
from imp import reload

# don't cache config
reload (conf)

def nowStr():
    return datetime.datetime.now().strftime("%Y-%m-%d--%H-%M.%S")

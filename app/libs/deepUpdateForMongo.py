
from app.services.rules.ruler import Ruler

def updaterIds(data, path):
    last = path[-1]
    if isinstance(last, str):
        data = Ruler.searchID(last, data)
        data = Ruler.searchAt(last, data)

    return data

import json
from datetime import datetime, timedelta, date

def clean_input(query):
    """ cleans user input to be ready for DB query. uppercases everything """
    INVALID_CHARACTERS = ".'\";()!=-"

    for c in INVALID_CHARACTERS:
        query = query.replace(c, "")

    return query.upper()

NON_SERIALIZABLE_CLASSES = [ datetime, timedelta, date ]

def is_non_serializable(object_):
    """ returns True if object_ cannot be serialized in json """
    return any([isinstance(object_, class_) for class_ in NON_SERIALIZABLE_CLASSES])

def remove_non_serializable_fields(obj):
    if is_non_serializable(obj):
        obj = str(obj)
    elif isinstance(obj, list) or isinstance(obj, tuple):
        obj = [remove_non_serializable_fields(x) for x in obj]
    elif isinstance(obj, dict):
        for key, value in obj.items():
            obj[key] = remove_non_serializable_fields(value)

    return obj

def to_json(d):
    """ formats dicts to json strings """
    return json.dumps(
        remove_non_serializable_fields(d)
    )

def send(object):
    print(to_json({"return": object}))

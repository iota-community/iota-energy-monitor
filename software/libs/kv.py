import ujson


def get(key):
    with open("config.json", 'r') as conf_file:
        config = ujson.loads(conf_file.read())
    return config[key]


def getAll():
    with open("config.json", 'r') as conf_file:
        config = ujson.loads(conf_file.read())
    return config


def set(key, value):
    with open("config.json", 'r') as conf_file:
        config = ujson.loads(conf_file.read())
    config[key] = value
    with open("config.json", 'w') as conf_file:
        conf_file.write(ujson.dumps(config))
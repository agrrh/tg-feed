import yaml


class Config(object):
    def __init__(self, path):
        with open(path) as fp:
            data = yaml.load(fp, Loader=yaml.SafeLoader)

        for k, v in data.items():
            setattr(self, k, v)

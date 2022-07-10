from configparser import ConfigParser


class ConfigProvider:
    def __init__(self) -> None:
        self.config = ConfigParser()

    def parse_config(self, filename):
        self.config.read(filename)
        return self.config

    def get_value(self, category, field):
        return self.config.getfloat(f"{type(category).__name__}", field)

import json


class Config:

    @staticmethod
    def config():
        # Read the file
        with open('config.json') as config_file:
            config = json.load(config_file)

        # Assert values are acceptable
        assert config['browser'] in ['Firefox', 'Chrome']
        assert isinstance(config['implicit_wait'], int)
        assert config['implicit_wait'] > 0

        # Return config so it can be used
        return config

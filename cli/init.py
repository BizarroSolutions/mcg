from cement.utils.misc import init_defaults
from cli.Mcg import Mcg
from core.db.MongoDB import MongoDB


def main():
    # Logging config (mcg section in file mcg.conf)
    defaults = init_defaults('mcg', 'log.logging')
    defaults['log.logging']['file'] = 'mcg.log'

    with Mcg('mcg', config_defaults=defaults) as app:
        # First setup the application
        app.setup()

        # Parse the configuration file
        app.config.parse_file('mcg.conf')

        MongoDB(
            {
                "user": app.config.get('mongodb', 'user'),
                "password": app.config.get('mongodb', 'password'),
                "host": app.config.get('mongodb', 'host'),
                "port": app.config.get('mongodb', 'port'),
                "db": app.config.get('mongodb', 'db')
            }
        )

        app.run()
        app.close()

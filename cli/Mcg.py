from cement.core.foundation import CementApp
from cli.BaseController import BaseController


class Mcg(CementApp):
    class Meta:
        label = 'mcg'
        base_controller = BaseController
        config_files = [
            './mcg.conf',
        ]

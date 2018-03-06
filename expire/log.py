#!/usr/bin/env python

import logging

import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)


class Logger:
    """
    Token from https://github.com/gaojiuli/toapi/blob/master/toapi/log.py
    """

    def __init__(self, name, level=logging.DEBUG):
        logging.basicConfig(format='%(asctime)s %(message)-10s ',
                            datefmt='%Y/%m/%d %H:%M:%S')

        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

    def info(self, color, type, message):
        self.logger.info(color + '[%-8s] %-2s %s' % (type, 'OK', message) + Style.RESET_ALL)

    def error(self, type, message):
        self.logger.error(Fore.RED + '[%-8s] %-4s %s' % (type, 'FAIL', message) + Style.RESET_ALL)

    def exception(self, type, message):
        self.error(type, message)


logger = Logger(__name__)

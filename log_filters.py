import logging


class ErrorLogFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'ERROR'


class WarningLogFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'WARNING'


class CriticalLogFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'CRITICAL'

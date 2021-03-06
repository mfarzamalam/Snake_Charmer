import logging

LOG_FORMAT = '{lineno} -- {name} -- {asctime} -- {message}'

basicConfig(filename='logfile.log', Level=DEBUG, style='{', format=LOG_FORMAT)


debug('DEBUG')
info('INFO')
warning('WARNING')
error('ERROR')
critical('CRITICAL')
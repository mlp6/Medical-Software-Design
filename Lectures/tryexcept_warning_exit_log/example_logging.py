import logging

# it can be useful to have argparse allow the developer to change the logging level from the CLI
#logging.basicConfig(filename='log.txt',level=logging.DEBUG)
# lets put some timestamps on our messages
#logging.basicConfig(filename="tslog.txt", format='%(asctime)s %(message)s')
# lets format the timstamp a bit more
logging.basicConfig(filename="megatslog.txt", format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

logging.debug('Debug level messages encompass all other log levels.')
logging.info('Status quo')
logging.warning('Something might be a bit off')

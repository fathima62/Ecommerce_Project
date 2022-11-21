import logging 
logging.basicConfig(filename="log_msg.log" , format= '{%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger('django')
logger.setLevel(logging.DEBUG)

# a=10
# b=0
# try :
#     c= a/b


logging.debug("the debug message is deplaying")
logging.info ("the info message is deplaying")
logging.warning("the warning message is deplaying")
logging.error ("the error message is deplaying")
logging.critical("the critical message is deplaying")
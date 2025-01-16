import logging
#
logging.basicConfig(level=logging.DEBUG, filename='logfile.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("debug")
logging.info("Program works very well user...1")
# logging.warning("warning")
# logging.error("Ooops! There is an error in this program user")
# logging.critical("critical")

# try:
#     print(10/0)
# except Exception as e:
#     logging.error("you cant do this...")
#
# if 2+2 == 4:
#     print("2 + 2 = 4 if you don't know")
#
# assert 2+2 == 5, "wrong result"
#
# """
#
# >>> 2 + 2
# 5
# """
#
# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()

def adder(*args, **kwargs):
    result = 0
    for _ in args:
        result += _
    for _ in kwargs.values():
        result += _
    return result
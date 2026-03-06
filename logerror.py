import logging

# DEBUG: Detailed information, typically of interest only when diagnosing problems

# INFO: Confirmation that things are working as expected

# WARNING: An indicaton that something unexpected happened, or incative of some problem in the near future(
# eg disk space low). The software is still working as expected

# ERROR: Due to a more serious problem

##l
## https://docs.python.org/3/howto/logging.html#logging-basic-tutorial

logging.basicConfig(filename='test.log',level=logging.DEBUG)


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

def multiply(x, y):
    return x * y

num_1 = 10
num_2 = 5

add_result = add(num_1, num_2)
logging.debug("Add:{} + {} = {}".format(num_1, num_2, add_result))

subtract_result = subtract(num_1, num_2)
logging.debug("subtract:{} - {} = {}".format(num_1, num_2, subtract_result))

divide_result = divide(num_1, num_2)
logging.debug("divide:{} - {} = {}".format(num_1, num_2, divide_result))

multiply_result =multiply(num_1, num_2)
logging.debug("multiply:{} - {} = {}".format(num_1, num_2, multiply_result))
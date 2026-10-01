### Logging in Python
# ---------------------
### Python has a built-in module: logging

import logging

logging.basicConfig(level=logging.INFO)
logging.info("Application started")
logging.info("Processing employee data")

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debug information")
logging.info("Application started")
logging.warning("Disk space is getting low")
logging.error("Database connection failed")
logging.critical("Application cannot continue")

'''
Logging Levels
==================
Python provides five commonly used levels:
-------------------------------------------

INFO
WARNING
DEBUG
ERROR
CRITICAL 
'''
#### Logging with Variables
#===========================
#Use logging's formatting support:
#----------------------------------
import logging

logging.basicConfig(level=logging.INFO)

employee_id = 101
salary = 50000

logging.info(
    "Processing employee_id=%s salary=%s",
    employee_id,
    salary
)

logging.info(
    f"Processing employee_id={employee_id} salary={salary}"
)
# NOTE: The first approach is preferred for performance reasons, 
# as it avoids unnecessary string formatting when the logging level is not enabled.

# ---------------------------------------------

#### Logging Exceptions  # This is particularly important.
# --------------------------
# 
import logging

logging.basicConfig(level=logging.INFO)


def divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        logging.error("Division failed")
        logging.exception("Exception occurred  while dividing %s by %s", a, b)
        #raise  # Re-raise the exception to propagate it further

        return None

print(divide(10, 0))

#Output:
#ERROR:root:Division failed
#None
#But we can preserve the traceback.
#Use:
#logging.exception()





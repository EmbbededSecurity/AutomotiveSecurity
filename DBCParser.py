import glob
import re
import pandas as pd
import math


# Finding variables by using regular expression(Regex)
MessageID = re.compile("BO_\s\d+")
MessageName = re.compile("BO_\s\d+\s\w+\w+\w+")
Message = re.compile("BO_\s\d+\s\w+\w+\w+" + ":")




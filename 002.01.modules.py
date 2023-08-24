#modules.py
# re is the module containing functions and constants for working with regular expressions.
import re
my_regex = re.compile("[0-9]+", re.I)

#if you already had a different re in your code, you could use an alias:
import re as regex
my_regex = regex.compile("[0-9]+", regex.I)

#if you are going to be typing the module name a lot, you can shorten it
import matplotlib.pyplot as plt

#if you need for a few specific values from a module, you can import them explicitly and use them without qualification
from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

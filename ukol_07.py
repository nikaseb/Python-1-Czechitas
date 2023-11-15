import re

regularni_vyraz1 = re.compile(r"\d?\d\ ?\W\ ?\d?\d\W\ ?\d{4}")

regularni_vyraz2 = re.compile(r"\d{3}\ \d{2}\ \ ?\w+\ ?(\w+|d+)\ ?\w*")
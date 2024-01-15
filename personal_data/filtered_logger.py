#!/usr/bin/env python3
import re
"""A function that returns
the log message obfuscated"""


def filter_datum(fields, redaction, message, separator):
    """ Args
        fields: a list of strings representing all
        fields to obfuscate
        
        redaction: a string representing by what
        the field will be obfuscated

        message: a string representing the log line

        separator: a string representing by which
        character is separating all fields in the
        log line (message)

        Returns: "xxx"ed out stuff in certain fields
        """

    return re.sub(fr'(?<={separator}|^)({"|".join(fields)})=[^;]*', lambda match: f'{match.group(1)}={redaction}', message)

    fields = ["password", "date_of_birth"]


messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))
    
#!/usr/bin/env python3
import re
from typing import List
"""A function that returns
the log message obfuscated"""


def filter_datum(fields: typing.List[str], redaction: str, message: str,
                 separator: str) -> str:
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

    for field in fields:
        pattern = r'({})([^{}]+)'.format(field + '=', separator)
        message = re.sub(pattern, r"\1{}".format(redaction), message)
    return message

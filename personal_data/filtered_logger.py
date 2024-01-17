#!/usr/bin/env python3
"""Write a function called filter_datum
that returns log messages obfuscated"""
import re
from typing import List
import logging
from logging import StreamHandler
import mysql.connector
import os

PII_FIELDS = ('name', 'email', 'ssn', 'password', 'ip',)
"""Tuple of PII fields from user data.csv"""


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ A function called filter_datum that
                     returns log messages obfuscated:

        Arguments:
            fields: a list of strings representing all fields to obfuscate
            redaction: a string representing by what the field will be
                       obfuscated
            message: a string representing the log line
            separator: a string representing by which character is
                           separating all fields in the log line (message)
    """

    for info in fields:
        message = re.sub(info + "=.*?" + separator,
                         info + "=" + redaction + separator,
                         message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        Update the class provide in the instructions to accept
        a list of strings fields.

    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Constructor Method """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ This filters the values in incoming log records
        using filter_datum """
        return filter_datum(self.fields, self.REDACTION,
                            super(RedactingFormatter, self).format(record),
                            self.SEPARATOR)

    PII_FIELDS = ('name', 'email', 'ssn', 'password', 'phone',)
    """Tuple of PII fields from user data.csv"""

    def get_logger() -> logging.Logger:
        """Implement a get_logger fx that takes no args (i.e. '()' the empty
        parentheses), and returns a logging.logger object
        (i.e. '->' = return the object 'logging.logger')."""

        """The logger should be named 'user_data' """
        logger = logging.getLogger("user_data")
        """...and log only upto logging.INFO level"""
        logger.setLevel(logging.INFO)
        """ ... it should not propagate messages to other loggers"""
        logger.propagate = False
        """ ... it should have a StreamHandler with RedactingFormatter (above)
        as formatter """

        stream_handler = StreamHandler()
        formatter = RedactingFormatter(PII_FIELDS)
        stream_handler.setFormatter(formatter)

        logger.addHandler(stream_handler)
        return logger

    def get_db() -> mysql.connector.connection.MySQLConnection:
        """ returns a connector to the database """
        return mysql.connector.connect(
                    host=os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost'),
                    database=os.environ.get('PERSONAL_DATA_DB_NAME', 'root'),
                    user=os.environ.get('PERSONAL_DATA_DB_USERNAME'),
                    password=os.environ.get('PERSONAL_DATA_DB_PASSWORD', ''))

    def main():
        """ obtain a """
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users;")
        result = cursor.fetchall()
        for row in result:
            message = f"name={row[0]}; " + \
                      f"email={row[1]}; " + \
                      f"phone={row[2]}; " + \
                      f"ssn={row[3]}; " + \
                      f"password={row[4]};"
            print(message)
            log_record = logging.LogRecord("my_logger", logging.INFO,
                                           None, None, message, None, None)
            formatter = RedactingFormatter(PII_FIELDS)
            formatter.format(log_record)
        cursor.close()
        db.close()


if __name__ == "__main__":
    main()

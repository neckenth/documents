#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import logging

from nose.tools import (assert_equal,
                        assert_in,
                        assert_is_not_none,
                        assert_not_in,
                        assert_true)

_logger = None


def get_logger():

    """
    Create and configure a new logger.

    This function is a facade to access the module's logger, which has
    been implemented using the singleton design pattern.

    Parameters
    ----------
    None

    Returns
    -------
    logging.Logger
    """

    global _logger

    if _logger is None:
        _logger = logging.getLogger()

    return _logger


_logger = get_logger()


class TestLogger(object):

    def setup(self):
        self.logger = get_logger()

    def test_logger_name(self):
        assert_equal(self.logger.name, 'exercise')

    def test_logger_severity_level(self):
        assert_equal(self.logger.level, logging.DEBUG)

    def test_stream_handler_is_attached(self):
        assert_true(any(isinstance(handler, logging.StreamHandler)
                        for handler
                        in self.logger.handlers))

    def test_stream_handler_severity_level(self):
        for handler in self.logger.handlers:
            if isinstance(handler, logging.StreamHandler):
                break
        else:
            assert False

        assert_equal(handler.level, logging.DEBUG)

    def test_file_handler_is_attached(self):
        assert_true(any(isinstance(handler, logging.FileHandler)
                        for handler
                        in self.logger.handlers))

    def test_file_handler_severity_level(self):
        for handler in self.logger.handlers:
            if isinstance(handler, logging.FileHandler):
                break
        else:
            assert False

        assert_equal(handler.level, logging.ERROR)

    def test_file_handler_formatter_is_attached(self):
        for handler in self.logger.handlers:
            if isinstance(handler, logging.FileHandler):
                break
        else:
            assert False

        assert_is_not_none(handler.formatter)

    def test_file_handler_formatter_format(self):
        for handler in self.logger.handlers:
            if isinstance(handler, logging.FileHandler):
                break
        else:
            assert False

        log_record = self.logger.makeRecord(name='exercise',
                                            level=logging.INFO,
                                            fn=None,
                                            lno=None,
                                            msg='foo',
                                            args=None,
                                            exc_info=None)

        log_message = handler.formatter.format(log_record)

        assert_in(str(datetime.date.today()), log_message)
        assert_not_in('exercise', log_message)


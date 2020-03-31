# -*- coding: utf-8 -*-
"""
src.utils.color_logger
======================

This module provides some helping functionality for convenient and comfortable logging.
"""

import logging
import click
import sys
from logging.config import dictConfig

from src.utils.config import Config


class ColorHandler(logging.StreamHandler):
    """A color log handler.

    The ``colors`` parameter is optional, and you can use any ANSI color.

      * Black
      * Red
      * Green
      * Yellow
      * Blue
      * Magenta
      * Cyan
      * White

    The default colors are:

      * debug: magenta
      * info: cyan
      * warning: yellow
      * error: red
      * critical: red
    """

    def __init__(self, stream=None, colors=None):
        logging.StreamHandler.__init__(self, stream)
        colors = colors or {}
        self.colors = {
            "critical": colors.get("critical", "red"),
            "error": colors.get("error", "red"),
            "warning": colors.get("warning", "yellow"),
            "info": colors.get("info", "cyan"),
            "debug": colors.get("debug", "magenta"),
        }
        self.config = "config_test.yml"

    def _get_color(self, level):
        if level >= logging.CRITICAL:
            return self.colors["critical"]  # pragma: no cover
        if level >= logging.ERROR:
            return self.colors["error"]  # pragma: no cover
        if level >= logging.WARNING:
            return self.colors["warning"]  # pragma: no cover
        if level >= logging.INFO:
            return self.colors["info"]
        if level >= logging.DEBUG:  # pragma: no cover
            return self.colors["debug"]  # pragma: no cover

        return None  # pragma: no cover

    def get_config(self):
        try:
            config = Config(self.config)
        except FileNotFoundError:
            print("configuration file: %s not found" % config, file=sys.stderr)
            sys.exit(1)
        return config

    def format(self, record: str) -> str:
        """The handler formatter.

        Args:
            record: The record to format.

        Returns:
            The record formatted as a string.

        """

        text = logging.StreamHandler.format(self, record)
        color = self._get_color(record.levelno)
        return click.style(text, color)

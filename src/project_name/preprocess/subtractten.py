# -*- coding: utf-8 -*-
"""
src.project_name.training.substractten
==================================

This module provides functionalities to preprocess ten
"""

import pandas as pd
import logging
import src.utils.color_logger as color_logger

import src.project_name.pipeline.abstractpipelineobject as apo
from src.utils.config import Config

log = logging.getLogger(__name__)
log.addHandler(color_logger.ColorHandler())


class SubtractTen(apo.PipelineObject):
    """
    This class subtracts ten to value
    """

    def __init__(self, config: Config):
        apo.PipelineObject.__init__(self, config)

    def __transform__(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Implementation of the transformation function that covers the transformation functionality of the
        SubtractTen.
        :param data: The dataframe the will be subtracted by this Pipeline Object
        :return: A dataframe that has been subtracted by this pipeline object
        """
        data["value"] = data["value"] - 10
        log.info("10 subtracted!")

        return data

# -*- coding: utf-8 -*-
"""
src.project_name.training.addfive
==================================

This module provides functionalities to add five
"""

import pandas as pd
import logging
import src.utils.color_logger as color_logger

import src.project_name.pipeline.abstractpipelineobject as apo
from src.utils.config import Config

log = logging.getLogger(__name__)
log.addHandler(color_logger.ColorHandler())


class AddFive(apo.PipelineObject):
    """
    This class adds five to value
    """

    def __init__(self, config: Config):
        apo.PipelineObject.__init__(self, config)

    def __transform__(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Implementation of the transformation function that covers the transformation functionality of the
        AddFive.
        :param data: The dataframe the will be added by this Pipeline Object
        :return: A dataframe that has been added by this pipeline object
        """
        data["value"] = data["value"] + 5
        log.info("5 added!")

        return data


# -*- coding: utf-8 -*-
"""
src.project_name.pipeline.abstractpipelineobject
=======================================

This module provides the abstract implementation for the pipeline objects that make up the demand forecasting pipeline.

"""

import abc
import pandas as pd
import logging
import src.utils.color_logger as color_logger
from src.utils.config import Config

log = logging.getLogger(__name__)
log.addHandler(color_logger.ColorHandler())


class PipelineObject:
    """
    This class is the base implementation for Pipeline Objects. It provides the generic ``transform`` function that
    should be used in all implementations of PipelineObjects to chain the PipelineObjects into a Pipeline.


    :arg config: the configuration object for the model run.
    """

    def __init__(self, config: Config):
        self.config = config

    @abc.abstractmethod
    def __transform__(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        abstract internal method to implement the transformation functionality

        :param data: The dataframe that will be transformed by this Pipeline Object
        :return: A dataframe that has been transformed by this pipeline object
        """
        return data

    def log_suffix(self, data):
        if isinstance(data, list):
            return f'dtype {type(data)}'
        else:
            return f'shape {data.shape}'

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        The transform function that is called by the pipeline to trigger the transformation functionality of this class.
        The functionality is implemented in the internal ``__transform__`` function.

        :param data: The dataframe that will be transformed by thie Pipeline Object
        :return: A dataframe that has been transformed by this pipeline object
        """
        suffix = "<none>"
        if data is not None:
            suffix = self.log_suffix(data)
        log.info(f'Starting {self.__class__.__name__} with input of {suffix}')

        out_data: pd.DataFrame = self.__transform__(data)

        suffix = "<none>"
        if out_data is not None:
            suffix = self.log_suffix(out_data)
        log.info(f'Finished {self.__class__.__name__} with output of {suffix}')

        del suffix

        return out_data

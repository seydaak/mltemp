# -*- coding: utf-8 -*-
"""
src.project_name.preprocess.trainingpipe
=======================================

This module implements the pipeline that manages and executes preprocess operations.
"""
import pandas as pd
import src.project_name.pipeline.abstractpipelineobject as apo
import src.project_name.pipeline.pipeline as ppl
import src.project_name.preprocess.subtractfive as sbf
import src.project_name.preprocess.subtractten as sbt
from src.utils.config import Config


class PreprocessPipe(apo.PipelineObject):
    """
    This class implements the complete preprocess pipeline.
    """

    def __init__(self, config: Config):
        apo.PipelineObject.__init__(self, config)
        self.pipe = ppl.Pipeline(self.config)
        self.subtractfive = sbf.SubtractFive(self.config)
        self.subtractten = sbt.SubtractTen(self.config)

        self.pipe.add(self.subtractfive)
        self.pipe.add(self.subtractten)

    def __transform__(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Implementation of the transformation function that covers the transformation functionality of the
        PreprocessPipe
        :param data: The dataframe the will be subtracted by this Pipeline Object
        :return: A dataframe that has been subtracted by this pipeline object
        """

        return self.pipe.transform(data)

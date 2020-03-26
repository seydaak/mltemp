# -*- coding: utf-8 -*-
"""
src.project_name.training.trainingpipe
=======================================

This module implements the pipeline that manages and executes training operations.
"""
import pandas as pd


import src.project_name.pipeline.abstractpipelineobject as apo
import src.project_name.pipeline.pipeline as ppl
import src.project_name.training.addfive as adf
import src.project_name.training.addten as adt
from src.utils.config import Config




class TrainingPipe(apo.PipelineObject):
    """
    This class implements the complete training pipeline.
    """

    def __init__(self, config: Config):
        apo.PipelineObject.__init__(self, config)
        self.pipe = ppl.Pipeline(self.config)
        self.addfive = adf.AddFive(self.config)
        self.addten = adt.AddTen(self.config)

        self.pipe.add(self.addfive)
        self.pipe.add(self.addten)

    def __transform__(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Implementation of the transformation function that covers the transformation functionality of the
        TrainingPipe
        :param data: The dataframe the will be added by this Pipeline Object
        :return: A dataframe that has been added by this pipeline object
        """

        return self.pipe.transform(data)

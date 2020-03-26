# -*- coding: utf-8 -*-
"""
src.project_name.pipeline.pipeline
=========================

This module provides the functionality to execute and manage a pipeline of pipelineojects that implement the
``src.project_name.pipeline.abstractpipelineobject`` class.

"""

import pandas as pd
import src.project_name.pipeline.abstractpipelineobject as apo
from src.utils.config import Config


class Pipeline(apo.PipelineObject):
    """
    The class to manage the pipeline object. It provides the transform function that is called throughout the pipeline.
    """

    def __init__(self, config: Config):
        apo.PipelineObject.__init__(self, config)
        self.pipeline = []

    def __transform__(self, data: pd.DataFrame) -> pd.DataFrame:
        """
            Implementation transform function of the pipeline itself iterates through the specified pipeline objects.
            This allows for nested pipelines.

            :type data: pd.DataFrame
            :param data: The dataframe the will be transformed by thie Pipeline Object
            :return: A dataframe that has been transformed by this pipeline object
            """

        for pipeline_object in self.pipeline:
            # inside the pipeline all transformation should happen in place to avoid unnecessary memory usage.
            # once a set of transformation is encapsulated in a pipeline the intermediate results are abstracted from.
            data: pd.DataFrame = pipeline_object.transform(data)

        return data

    def add(self, pipelineobject: apo.PipelineObject) -> None:
        """
        Adds a new src.project_name.pipeline.abstractpipelineobject.PipelineObject to the pipeline.

        :type pipelineobject: apo.PipelineObject
        :param pipelineobject: The PipelineObject that is added to the pipeline
        :return:
        """

        self.pipeline = self.pipeline + [pipelineobject]
        return None

    def set_pipeline(self, pipelineobjects: list) -> None:
        """
        Get the new pipeline with a list of pairs of name and ``src.project_name.pipeline.abstractpipelineobject``

        :type pipelineobjects: list(apo.PipelineObject)
        :param pipelineobjects: a list of pairs of ``src.project_name.pipeline.abstractpipelineobject``
        :return:
        """

        self.pipeline = pipelineobjects

        return None

    def get_pipeline(self) -> list:
        """
        Get the current pipeline.

        :return: the current pipeline as a list ``src.project_name.pipeline.abstractpipelineobject``.
        """

        return self.pipeline

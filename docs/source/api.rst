API Documentation
#################

This page covers the complete source code documentation of the modules for the project. The source code is
divided into three main modules: ``src.project_name.pipeline``, ``src.project_name.preparation`` and ``src.project_name.training``.

src.project_name.pipeline
================
The pipeline package contains the basic constructs to build the preparation, training and scoring pipeline for the project.

At its core there is the the ``src.project_name.pipeline.abstractpipelineobject`` module. It provides the interface for the basic
building block of the pipeline: the pipeline object. The pipeline object has a ``transform`` function that is called
when it is registered in an implementation of the ``src.project_name.pipeline.pipeline.Pipeline``. The pipeline is itself an
implementation of the ``src.project_name.pipeline.abstractpipelineobject.PipelineObject`` and implements the ``transform``
functions. Through this a pipeline can contain other pipelines as objects, allowing for nested execution and more
flexible structuring and modularization of the pipeline.

.. automodule:: src.project_name.pipeline.abstractpipelineobject
   :members:
.. automodule:: src.project_name.pipeline.pipeline
   :members:

src.project_name.preparation
===================
This package comprises the data preparation pipeline. The data preparation pipeline is typically the first pipeline that
is executed, even before generating features or training any model.

The data preparation pipeline is managed in the ``src.project_name.preparation.preparation`` module. The class
``src.project_name.preparation.preparation.Preparation`` contains the implementation of the data preparation pipeline for the
project.


.. automodule:: src.project_name.preparation.dataloader
   :members:

src.project_name.training
================
The training package contains all functionality to generate features, train and test time series and machine learning
models.

The main module for this pipeline is the ``src.project_name.training.Training`` module. It registers and executes all the modules
that make up the training step of the project.

.. automodule:: src.project_name.training.trainingpipe
   :members:
.. automodule:: src.project_name.training.addfive
   :members:
.. automodule:: src.project_name.training.addten
   :members:

src.project_name.preprocess
================
The preprocess package contains ...


.. automodule:: src.project_name.preprocess.preprocesspipe
   :members:
.. automodule:: src.project_name.preprocess.subtractfive
   :members:
.. automodule:: src.project_name.preprocess.subtractten
   :members:


src.utils
=========
This package contains helper modules to develop, run and maintain the the packages of the project.


.. automodule:: src.utils.color_logger
   :members:
.. automodule:: src.utils.config
   :members:
.. automodule:: src.utils.constants
   :members:
.. automodule:: src.utils.helper_functions
   :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
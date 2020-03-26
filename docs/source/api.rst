API Documentation
#################

This page covers the complete source code documentation of the modules for the Arcelik dna project. The source code is
divided into three main modules: ``src.dna.pipeline``, ``src.dna.preparation`` and ``src.dna.training``.

src.dna.pipeline
================
The pipeline package contains the basic constructs to build the preparation, training and scoring pipeline for the
Arcelik DNA project.

At its core there is the the ``src.dna.pipeline.abstractpipelineobject`` module. It provides the interface for the basic
building block of the pipeline: the pipeline object. The pipeline object has a ``transform`` function that is called
when it is registered in an implementation of the ``src.dna.pipeline.pipeline.Pipeline``. The pipeline is itself an
implementation of the ``src.dna.pipeline.abstractpipelineobject.PipelineObject`` and implements the ``transform``
functions. Through this a pipeline can contain other pipelines as objects, allowing for nested execution and more
flexible structuring and modularization of the pipeline.

.. automodule:: src.dna.pipeline.abstractpipelineobject
   :members:
.. automodule:: src.dna.pipeline.pipeline
   :members:

src.dna.preparation
===================
This package comprises the data preparation pipeline. The data preparation pipeline is typically the first pipeline that
is executed, even before generating features or training any model.

The data preparation pipeline is managed in the ``src.dna.preparation.preparation`` module. The class
``src.dna.preparation.preparation.Preparation`` contains the implementation of the data preparation pipeline for the DNA
project.

.. automodule:: src.dna.preparation.datacleaningpipe
   :members:
.. automodule:: src.dna.preparation.dataloader
   :members:
.. automodule:: src.dna.preparation.listpriceimputer
   :members:
.. automodule:: src.dna.preparation.outlierremover
   :members:
.. automodule:: src.dna.preparation.preparation
   :members:
.. automodule:: src.dna.preparation.promodatapreparator
   :members:
.. automodule:: src.dna.preparation.traintestsplitter
   :members:


src.dna.training
================
The training package contains all functionality to generate features, train and test time series and machine learning
models.

The main module for this pipeline is the ``src.dna.training.Training`` module. It registers and executes all the modules
that make up the training step of the Arcelik dna project.


.. automodule:: src.dna.training.aggregatorseparatorpipe
   :members:
.. automodule:: src.dna.training.calendarfeatureengine
   :members:
.. automodule:: src.dna.training.confidenceindexfeatureengine
   :members:
.. automodule:: src.dna.training.currencyfeatureengine
   :members:
.. automodule:: src.dna.training.dataaggregator
   :members:
.. automodule:: src.dna.training.dataseparator
   :members:
.. automodule:: src.dna.training.featureengine
   :members:
.. automodule:: src.dna.training.gapsfiller
   :members:
.. automodule:: src.dna.training.historicsalesfeaturesengine
   :members:
.. automodule:: src.dna.training.inflationfeatureengine
   :members:
.. automodule:: src.dna.training.interestfeatureengine
   :members:
.. automodule:: src.dna.training.modelevaluator
   :members:
.. automodule:: src.dna.training.modelscorer
   :members:
.. automodule:: src.dna.training.movingaverage
   :members:
.. automodule:: src.dna.training.otvfeatureengine
   :members:
.. automodule:: src.dna.training.scoring
   :members:
.. automodule:: src.dna.training.timeseriesmodelbuilder
   :members:
.. automodule:: src.dna.training.timeseriesmodelpipe
   :members:
.. automodule:: src.dna.training.training
   :members:
.. automodule:: src.dna.training.traintestsplit
   :members:
.. automodule:: src.dna.training.uidgenerator
   :members:

src.dna.disaggragation
======================
This package disaggregates the outputs on h4 level to sku level

.. automodule:: src.dna.disaggregation.skudisaggregator
   :members:

src.utils
=========
This package contains helper modules to develop, run and maintain the the packages of the Arcelik DNA demand forecasting
algorithm conveniently.

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
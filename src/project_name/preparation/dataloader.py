# -*- coding: utf-8 -*-
"""
src.project_name.preparation.dataloader
==============================

This module provides the functionality to read data from different source files or source systems.
"""

import pandas as pd
from src.utils.config import Config


class DataLoader:
    """
    Load and Save Data
    """

    def __init__(self, config: Config):
        self.config = config

        self.folder_path = self.config.get("data.folder_path")
        self.dataset_name = self.config.get("data.file_name")
        self.save_name = self.config.get("data.save_name")

    def get_data(self):
        type = self.dataset_name.split(".")[-1]

        if type == "csv":
            data = self.read_csv()

        return data

    def read_csv(self) -> pd.DataFrame:
        """
        This function reads csv files
        :return: A dataframe has bas been read
        """

        data = pd.read_csv(self.folder_path + self.dataset_name)

        return data

    def save_csv(self, data: pd.DataFrame):
        data.to_csv(self.folder_path + self.save_name, index=False)

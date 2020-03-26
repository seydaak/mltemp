# -*- coding: utf-8 -*-
"""
src.utils.config
================

This module manages the configuration.
"""

import os
from collections.abc import Mapping, Sequence
import yaml
from pathlib import Path


class Config(object):
    """ config manager """

    _config_user = None
    _config = None

    def __init__(self, file_name: str):
        """
        Initialize a new instance of Config

        :param file_name: Name of the config file including the extension (e.g., 'config.yml')
        """
        # Fix the path of the project root relative to the present file, to ensure robustness under imports
        project_root = Path(__file__).parents[2]

        # Define the config path relative to the fixed project_root (instead of in relative terms)
        self._config_path = Path(project_root, file_name)

        # Split file_name into stem and extension ('config.yml' -> 'config', '.yml')
        # to define user config name 'config.user.yml', where 'user' is taken from the environment variables
        filename_stem = self._config_path.stem
        file_extension = self._config_path.suffix
        username = os.getenv("USER", "user")
        username = username.replace(" ", "_")
        self._config_user_path = Path(project_root, filename_stem + "." + username + file_extension)

        if os.path.isfile(self._config_path) and os.access(self._config_path, os.R_OK):
            with open(self._config_path, 'r') as stream:
                try:
                    self._config = yaml.load(stream, Loader=yaml.FullLoader)
                except yaml.YAMLError as exc:
                    print(exc)
        else:
            raise FileNotFoundError

        if os.path.isfile(self._config_user_path) and os.access(self._config_user_path, os.R_OK):
            with open(self._config_user_path, 'r') as stream:
                try:
                    self._config_user = yaml.load(stream, Loader=yaml.FullLoader)
                except yaml.YAMLError as exc:
                    print(exc)

    def _get(self, key, config):
        """ internal implementation of get """
        current_data = config

        for chunk in key.split('.'):
            if isinstance(current_data, Mapping):
                current_data = current_data[chunk]
            elif isinstance(current_data, Sequence):
                chunk = int(chunk)

                current_data = current_data[chunk]
            else:
                return current_data

        return current_data

    def get(self, key):
        """ return the config for the passed key """
        try:
            data = self._get(key, self._config)

            if self._config_user is not None:
                try:
                    data_user = self._get(key, self._config_user)
                except KeyError:
                    return data
                return data_user

            return data
        except KeyError:
            raise KeyError(key)
        except ValueError:
            raise ValueError("Sequence index not an integer")
        except IndexError:
            raise IndexError("Sequence index out of range")

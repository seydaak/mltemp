# -*- coding: utf-8 -*-
"""
src.utils.helper_functions
==========================

Module for helper functions that are sued in various modules of this project.
"""

from typing import Union
import numpy as np
import pandas as pd


def weeks_until_next_event(x: pd.Timestamp,
                           date_col: str,
                           event_df: pd.DataFrame,
                           upper_cutoff: Union[int, None] = None) -> int:
    """
    Calculate weeks until next occurence of an event in the event_df dataframe.

    :param x: Timestamp for which we want to check the number of weeks until the next event in the event_df
    :param date_col: Name of date-column in event_df
    :param event_df: Dataframe that contains all dates on which the EVENT occurs
    :param upper_cutoff: Upper cutoff that we want to apply to the number of weeks
    :return: Number of weeks until the next occurence of EVENT.
    """

    # filter event_df for future dates only
    filtered_df = event_df.loc[event_df[date_col] >= x, date_col]

    if filtered_df.shape[0] == 0:
        date_diff = 999
    else:
        next_event_df = filtered_df.min()
        date_diff = (next_event_df - x)
        date_diff = int(date_diff / np.timedelta64(1, 'W'))

    # apply upper cutoff
    if upper_cutoff is not None:
        date_diff = min(upper_cutoff, date_diff)

    return date_diff

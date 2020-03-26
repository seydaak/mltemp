# -*- coding: utf-8 -*-
"""
src.utils.constants
===================

This module contains constant python values to be called throughout the model execution.
"""

import numpy as np

# Aggregation periods
AGGREGATION_PERIOD_WEEKLY = 'week'

# Encodings for reading files from S3
ENCODING_ISO8859_9 = "iso8859_9"
ENCODING_UTF_8 = "UTF-8"

# Data constants: Column lists, date columns, ...

# Data types for the schema while reading the master table from S3
MASTER_SCHEMA_DTYPES = {'source': str,
                        'dealer_code': str,
                        'sales_date': str,
                        'sku_code': str,
                        'sales_quantity': np.int32,
                        'unit_price': float,
                        'discount_amount': float,
                        'sales_price': float,
                        'paro_camp_code': str,
                        'paro_camp_name': str,
                        'paro_discount_amount': float,
                        'dealer_name': str,
                        'dealer_type_definition': str,
                        'dealer_active': str,
                        'sales_neighborhood_code': str,
                        'sales_neighborhood_definition': str,
                        'channel_definition': str,
                        'brand': str,
                        'hierarchy': str,
                        'h1_name': str,
                        'h2_name': str,
                        'h3_name': str,
                        'h4_name': str,
                        'list_price': float,
                        'day_of_week': np.int16,
                        'week_of_year': np.int16,
                        'first_date_of_week': str,
                        'is_weekday': bool,
                        'is_business_day': bool,
                        'is_holiday': bool,
                        'holiday_name': str,
                        'company_definition': str,
                        'marketing_code': str,
                        'brandID': np.int16,
                        'subeID': np.int16}

# Columns to be used in the dna pipeline, these columns are selected upon read, all other columns are filtered out.
MASTER_SCHEMA_COLUMNS = ['source', 'dealer_code', 'city_code', 'sales_date', 'sku_code', 'sales_quantity', 'unit_price',
                         'discount_amount','sales_price', 'paro_camp_code', 'paro_camp_name', 'paro_discount_amount', 'dealer_active',
                         'brand', 'channel_definition', 'hierarchy', 'h1_name', 'h2_name', 'h3_name', 'h4_name',
                         'list_price', 'first_date_of_week', 'is_business_day', 'is_holiday', 'company_definition',
                         'brandID', 'subeID']

MASTER_SCHEMA_DATE_LIST = ['sales_date', 'first_date_of_week']

# Resampling constants
WEEKLY_RESAMPLING = 'W-Mon'
MONTHLY_RESAMPLING = 'MS'

NUMERICS = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

FEATURE_MASTER_COLUMNS = ['sales_quantity', 'sales_date', 'group_name', 'brand', 'h4_name', 'company_definition',
                          'channel_definition', 'ramadan_flag', '1 Mayıs Emek ve Dayanışma Günü', '1 Ocak YılBaşı',
                          '15 Temmuz Demokrasi ve Milli Birlik Günü', '19 Mayıs Atatürk ü Anma Gençlik ve Spor Bayramı',
                          '23 Nisan Ulusal Egemenlik ve Çocuk Bayramı', '29 Ekim Cumhuriyet Bayramı',
                          '30 Ağustos Zafer Bayramı', 'Kurban Bayramı', 'Kurban Bayramı Arefesi',
                          'Ramazan Bayramı', 'Ramazan Bayramı Arefesi', 'total_holiday_count', 'year', 'month',
                          'quarter', 'usd buy price _mean', 'usd buy price _amax',
                          'usd buy price _amin', 'usd buy price _std', 'usd buy price _median', 'usd buy price _trend',
                          'usd sell price_mean', 'usd sell price_amax', 'usd sell price_amin', 'usd sell price_std',
                          'usd sell price_median', 'usd sell price_trend', 'euro buy price_mean',
                          'euro buy price_amax', 'euro buy price_amin', 'euro buy price_std',
                          'euro buy price_median', 'euro buy price_trend', 'euro sell price_mean',
                          'euro sell price_amax', 'euro sell price_amin', 'euro sell price_std',
                          'euro sell price_median', 'euro sell price_trend', 'usd buy price _trend12weeks',
                          'usd sell price_trend12weeks', 'euro buy price_trend12weeks', 'euro sell price_trend12weeks',
                          'usd buy price _trend52weeks', 'usd sell price_trend52weeks', 'euro buy price_trend52weeks',
                          'euro sell price_trend52weeks', 'otv_available', 'otv_end_effect', 'otv_ended',
                          'otv_end_effect2', 'sales_quantity_1_periods_ago', 'sales_quantity_2_periods_ago',
                          'sales_quantity_3_periods_ago', 'sales_quantity_4_periods_ago',
                          'sales_quantity_5_periods_ago', 'sales_quantity_6_periods_ago',
                          'sales_quantity_7_periods_ago', 'sales_quantity_8_periods_ago',
                          'sales_quantity_9_periods_ago', 'sales_quantity_10_periods_ago',
                          'sales_quantity_11_periods_ago', 'sales_quantity_12_periods_ago',
                          'sales_quantity_13_periods_ago', 'sales_quantity_14_periods_ago',
                          'sales_quantity_15_periods_ago', 'sales_quantity_16_periods_ago',
                          'sales_quantity_17_periods_ago', 'sales_quantity_18_periods_ago',
                          'sales_quantity_19_periods_ago', 'sales_quantity_20_periods_ago',
                          'sales_quantity_21_periods_ago', 'sales_quantity_22_periods_ago',
                          'sales_quantity_23_periods_ago', 'sales_quantity_24_periods_ago',
                          'sales_quantity_25_periods_ago', 'sales_quantity_26_periods_ago',
                          'sales_quantity_27_periods_ago', 'sales_quantity_28_periods_ago',
                          'sales_quantity_29_periods_ago', 'sales_quantity_30_periods_ago',
                          'sales_quantity_31_periods_ago', 'sales_quantity_32_periods_ago',
                          'sales_quantity_33_periods_ago', 'sales_quantity_34_periods_ago',
                          'sales_quantity_35_periods_ago', 'sales_quantity_36_periods_ago',
                          'sales_quantity_37_periods_ago', 'sales_quantity_38_periods_ago',
                          'sales_quantity_39_periods_ago', 'sales_quantity_40_periods_ago',
                          'sales_quantity_41_periods_ago', 'sales_quantity_42_periods_ago',
                          'sales_quantity_43_periods_ago', 'sales_quantity_44_periods_ago',
                          'sales_quantity_45_periods_ago', 'sales_quantity_46_periods_ago',
                          'sales_quantity_47_periods_ago', 'sales_quantity_48_periods_ago',
                          'sales_quantity_49_periods_ago', 'sales_quantity_50_periods_ago',
                          'sales_quantity_51_periods_ago', 'sales_quantity_52_periods_ago',
                          'sales_quantity_1', 'sales_quantity_2', 'sales_quantity_3', 'sales_quantity_4',
                          'rate_sales', 'rate_units', 'rate_sales_h2', 'rate_units_h2', 'rate_sales_growth',
                          'rate_units_growth', 'rate_sales_h2_growth', 'rate_units_h2_growth', 'inflation_rate',
                          '4_week_growth', '12_week_growth', '52_week_growth', 'consumer_confidence_index',
                          '4_week_growth_conf', '4week_per_change', '12_week_growth_conf', '12week_per_change',
                          '24_week_growth_conf', '24week_per_change', '52_week_growth_conf', '52week_per_change',
                          'EUR_interest', 'TL_interest', 'USD_interest', 'EUR_interest_4w_growth',
                          'EUR_interest_12w_growth', 'EUR_interest_24w_growth', 'EUR_interest_52w_growth',
                          'TL_interest_4w_growth', 'TL_interest_12w_growth', 'TL_interest_24w_growth',
                          'TL_interest_52w_growth', 'USD_interest_4w_growth', 'USD_interest_12w_growth',
                          'USD_interest_24w_growth', 'USD_interest_52w_growth', 'train_test', 'ml_predicted_quantity',
                          'ml_sales_quantity_1', 'ml_sales_quantity_2', 'ml_sales_quantity_3', 'ml_sales_quantity_4',
                          'last_week_of_prediction']

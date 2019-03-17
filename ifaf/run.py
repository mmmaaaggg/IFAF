#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author  : MG
@Time    : 2019/1/21 16:59
@File    : run.py
@contact : mmmaaaggg@163.com
@desc    : 
"""
import pandas as pd
from ifaf.utils.db import with_db_session
from ifaf.backend import engine_md


def get_df(instrument_type):
    sql_str = """SELECT trade_date, close, TermStructure, Volume, OI FROM wind_future_continuous_adj
      where instrument_type=%s ORDER BY trade_date"""
    df = pd.read_sql(sql_str, engine_md, index_col='trade_date', params=[instrument_type]).sort_index()
    close_s = df['close']
    df['pct_change'] = close_s.pct_change()
    df['ma5'] = close_s.rolling(5).mean()
    df['ma10'] = close_s.rolling(10).mean()
    return df


def factor_analysis(df: pd.DataFrame, target_label, shift_num=-1, params: dict={}) -> dict:
    """
    对多因子相关性，有效性进行分析
    :param df:每一列为一个引子
    :param pct_change_label: df[pct_change_label] 对应的引子分析的参照对象
    :param shift_num: 错位对齐，多数情况下错1为（时间序列数据中，当前行数据对应预测下一行 pct_change_label 的涨跌
    :param params: 因子分析参数：包括正/负收益预测准确度分析("1/-1 factors")
    :return:
    """
    result_dic = {}
    # 获取引子列名称
    factor_column_name_set = set(df.columns)
    factor_column_name_set.remove(target_label)
    factor_column_name_list = list(factor_column_name_set)
    # 去除时间序列
    df_new = df[factor_column_name_list].join(df[target_label].shift(shift_num), how="inner")
    # 因子相关性分析
    # corr_pearson = df_new.corr()
    corr_kendall = df_new.corr(method='kendall')
    result_dic["corr"] = corr_kendall
    #
    return result_dic


def run():
    instrument_type = "RU"
    df = get_df(instrument_type)
    result_dic = factor_analysis(df, target_label='pct_change', )

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


def factor_analysis(df :pd.DataFrame, target_label, shift_num=1) -> dict:
    """
    对多因子相关性，有效性进行分析
    :param df:每一列为一个引子
    :param pct_change_label: df[pct_change_label] 对应的引子分析的参照对象
    :param shift_num: 错位对齐，多数情况下错1为（时间序列数据中，当前行数据对应预测下一行 pct_change_label 的涨跌
    :return:
    """
    result_dic = {}
    return result_dic


def run():
    df = None
    result_dic = factor_analysis(df, target_label='pct_change', )

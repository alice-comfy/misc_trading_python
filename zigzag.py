import pandas as pd
import numpy as np

#python recreation of the tradingview ZigZag indicator. Produced with some original tweaks & GPT-4 base.
#uses pandas library. I haven't been able to find any way of creating in polars, or a faster lib. 

def find_pivots(df, depth, dev_threshold):
    """
    Find pivots in the DataFrame and classify them as highs or lows.

    :param df: pandas DataFrame with 'high' and 'low' columns
    :param depth: The number of bars required for pivot detection
    :param dev_threshold: The minimum percentage deviation for a pivot
    :return: pandas DataFrame with pivot highs and lows
    """

    pivots_high = pd.Series(index=df.index, dtype=np.float64)
    pivots_low = pd.Series(index=df.index, dtype=np.float64)

    for i in range(depth, len(df) - depth):
        max_range = df['high'][i - depth:i + depth + 1].max()
        min_range = df['low'][i - depth:i + depth + 1].min()

        if df['high'][i] == max_range:
            pivots_high[i] = df['high'][i]
        elif df['low'][i] == min_range:
            pivots_low[i] = df['low'][i]

    return pivots_low.dropna(), pivots_high.dropna()

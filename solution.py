import pandas as pd
import numpy as np
from scipy.stats import ks_2samp


chat_id = 461750643 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    val = ks_2samp(x, y)
    return val.pvalue < alpha # Ваш ответ, True или False

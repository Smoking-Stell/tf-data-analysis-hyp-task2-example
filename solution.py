import pandas as pd
import numpy as np
from hyppo.ksample import MMD


chat_id = 461750643 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    stat, pvalue = MMD(gamma=1).test(x, y)
    return pvalue < alpha # Ваш ответ, True или False

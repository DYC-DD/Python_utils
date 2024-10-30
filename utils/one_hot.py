import numpy as np
from sklearn.preprocessing import OneHotEncoder

# one hot encode工具
def one_hot_encode(data):
    """
    將輸入的資料轉換為 One-Hot 編碼格式。

    參數:
    data (list or array-like): 要進行 One-Hot 編碼的資料（可以是列表、陣列或其他可迭代的結構）

    回傳:
    np.ndarray: 經過 One-Hot 編碼後的陣列
    """
    # 初始化OneHotEncoder
    encoder = OneHotEncoder(sparse_output=False)

    # 將輸入資料轉換為2D格式
    data_reshaped = np.array(data).reshape(-1, 1)

    # 進行One-Hot編碼
    one_hot_encoded = encoder.fit_transform(data_reshaped)

    return one_hot_encoded

"""
使用範例
data = ['cat', 'dog', 'bird', 'cat', 'dog']
encoded_data = one_hot_encode(data)
print(encoded_data)
"""

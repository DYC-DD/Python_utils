from datetime import datetime, timedelta

# 加減天數的函式
def calculate_date_by_days(base_date: str, days: int) -> str:
    """
    根據輸入的日期和天數計算新的日期。
    :param base_date: 輸入的日期，格式為 YYYYMMDD
    :param days: 加減的天數（正數加天，負數減天）
    :return: 計算後的日期，格式為 YYYYMMDD
    """
    try:
        date_object = datetime.strptime(base_date, "%Y%m%d")
        new_date = date_object + timedelta(days=days)
        return new_date.strftime("%Y%m%d")
    except ValueError:
        return "日期格式錯誤，請輸入 YYYYMMDD 格式的日期。"

# 計算兩個日期之間的天數差
def calculate_days_difference(date1: str, date2: str) -> int:
    """
    計算兩個日期之間的天數差。
    :param date1: 第一天的日期，格式為 YYYYMMDD
    :param date2: 第二天的日期，格式為 YYYYMMDD
    :return: 天數差
    """
    try:
        date_object1 = datetime.strptime(date1, "%Y%m%d")
        date_object2 = datetime.strptime(date2, "%Y%m%d")
        difference = (date_object2 - date_object1).days
        return difference
    except ValueError:
        return "日期格式錯誤，請輸入 YYYYMMDD 格式的日期。"




# ===== 使用範例 =====

# === 加減天數的函式 ===
# from date_calculator import calculate_date_by_days
# new_date = calculate_date_by_days("20241210", 100)
# print("加 100 天後的日期：", new_date)

# === 計算兩個日期之間的天數差 ===
# from date_calculator import calculate_days_difference
# days_diff = calculate_days_difference("20241210", "20241220")
# print("日期差為：", days_diff, "天")

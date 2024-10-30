import time

# 計時器
class Timer:
    def __init__(self):
        """ 初始化 Timer 類別，並將開始時間設置為 None """
        self.start_time = None

    def start(self):
        """ 啟動計時器，記錄當前時間 """
        self.start_time = time.time()

    def stop(self):
        """ 停止計時器，並返回運行的時間(以小時、分鐘、秒、毫秒為單位) """
        if self.start_time is None:
            raise Exception("計時器尚未開始，請先呼叫 start()")
        
        end_time = time.time()  # 取得結束時間
        elapsed_time = end_time - self.start_time  # 計算經過的時間
        
        hours = int(elapsed_time // 3600)  # 小時
        minutes = int((elapsed_time % 3600) // 60)  # 分鐘
        seconds = int(elapsed_time % 60)  # 秒
        milliseconds = int((elapsed_time * 1000) % 1000)  # 毫秒
        
        # 以小時:分鐘:秒.毫秒的格式返回運行時間
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}"
    

"""
使用方式

from timer import Timer # 計時器
timer = Timer()
timer.start() # 開始計時

...程式碼...

print("程式已運行完成，運行時間:", timer.stop()) # 停止計時並顯示運行時間
"""
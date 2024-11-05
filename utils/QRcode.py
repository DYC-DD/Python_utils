# 引入 qrcode 套件
import qrcode

# 定義生成 QR Code 的函式
def generate_qr_code(url, filename="qrcode.png"):
    """
    生成 QR Code 並儲存為圖片檔案
    :param url: 要轉換的網站網址
    :param filename: 儲存的檔案名稱，預設為 'qrcode.png'
    """
    # 建立 QR Code 物件
    qr = qrcode.QRCode(
        version=1,  # 控制 QR Code 大小，範圍從 1 到 40，數字越大，生成的圖案越大
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # 設置錯誤容忍率
        box_size=10,  # 每個格子的像素數
        border=1  # QR Code 圖案的邊框寬度
    )
    
    # 將網址加入到 QR Code 中
    qr.add_data(url)
    qr.make(fit=True)  # 自動調整尺寸以適應內容

    # 生成 QR Code 圖像
    img = qr.make_image(fill='black', back_color='white')
    
    # 儲存 QR Code 圖片
    img.save(filename)
    print(f"QR Code 已經儲存為 {filename}")


"""
安裝套件：
pip install qrcode[pil]


# 使用範例
from QRcode import generate_qr_code
url = "https://github.com/DYC-DD"
generate_qr_code(url, filename="name.png")
"""
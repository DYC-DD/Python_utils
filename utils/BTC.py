# ========== 此程式尚未計算到很多考慮因素，僅供參考! ==========
# ========== 此程式尚未計算到很多考慮因素，僅供參考! ==========
# ========== 此程式尚未計算到很多考慮因素，僅供參考! ==========

import requests

def get_current_btc_price_and_usd_to_twd_rate():
    """
    獲取比特幣的最新價格及美元對新台幣的即時匯率。
    """
    try:
        # 幣安 API URL，用於獲取 BTC 對 USDT 的價格
        binance_api_url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
        response = requests.get(binance_api_url)
        response.raise_for_status()
        btc_data = response.json()
        btc_price_usdt = float(btc_data['price'])  # BTC 對 USDT 的價格

        # 即匯站 API URL，用於獲取 USD 對 TWD 的即時匯率
        rter_api_url = "https://tw.rter.info/capi.php"
        response = requests.get(rter_api_url)
        response.raise_for_status()
        exchange_data = response.json()
        usd_to_twd_rate = float(exchange_data['USDTWD']['Exrate'])  # USD 對 TWD 的匯率

        # 計算 BTC 對 TWD 的價格
        btc_price_twd = btc_price_usdt * usd_to_twd_rate
        return btc_price_twd, usd_to_twd_rate
    except Exception as e:
        print(f"無法獲取比特幣價格或匯率: {e}")
        return None, None

def calculate_profit_or_loss(buy_price, buy_amount, current_price):
    """
    計算單筆交易的盈虧。
    :param buy_price: 購買比特幣時的價格（每顆，以新台幣計算）
    :param buy_amount: 購買的比特幣數量
    :param current_price: 當前比特幣的價格（每顆，以新台幣計算）
    :return: 該筆交易的盈虧金額（新台幣）
    """
    invested_value = buy_price * buy_amount  # 投資總額
    current_value = current_price * buy_amount  # 當前市值
    profit_or_loss = current_value - invested_value  # 盈虧計算
    return invested_value, current_value, profit_or_loss

def main():
    print("=== 比特幣多筆交易盈虧計算程式 ===")
    transactions = []  # 儲存所有交易的清單

    # 持續讓使用者輸入交易資料，直到使用者選擇停止
    while True:
        try:
            buy_price = float(input("請輸入購買比特幣時的價格（每顆，以新台幣計算）: "))
            buy_amount = float(input("請輸入購買的比特幣數量: "))
            transactions.append((buy_price, buy_amount))  # 將交易資料加入清單
        except ValueError:
            print("輸入無效，請輸入正確的數字！")
            continue

        more = input("是否還有其他交易要輸入？(y/n): ").strip().lower()
        if more != 'y':
            break

    # 獲取當前比特幣價格和美元對台幣匯率
    current_price, usd_to_twd_rate = get_current_btc_price_and_usd_to_twd_rate()
    if current_price is None or usd_to_twd_rate is None:
        print("無法獲取比特幣目前價格或匯率，請稍後再試。")
        return

    total_invested = 0  # 總投資金額初始化
    total_current_value = 0  # 總市值初始化
    total_profit_or_loss = 0  # 總盈虧初始化

    # 計算每筆交易的詳細數據，並累加總數據
    print("\n=== 每筆交易詳情 ===")
    for i, (buy_price, buy_amount) in enumerate(transactions, start=1):
        invested_value, current_value, profit_or_loss = calculate_profit_or_loss(buy_price, buy_amount, current_price)
        total_invested += invested_value
        total_current_value += current_value
        total_profit_or_loss += profit_or_loss

        # 計算美金對應金額
        invested_usd = invested_value / usd_to_twd_rate
        current_usd = current_value / usd_to_twd_rate
        profit_or_loss_usd = profit_or_loss / usd_to_twd_rate

        print(f"交易 {i}:")
        print(f"  購買價格: {buy_price:.2f} 台幣/顆")
        print(f"  購買數量: {buy_amount:.6f} 顆")
        print(f"  投資金額: {invested_value:.2f} 台幣 ({invested_usd:.2f} 美金)")
        print(f"  當前市值: {current_value:.2f} 台幣 ({current_usd:.2f} 美金)")
        if profit_or_loss > 0:
            print(f"  盈餘: {profit_or_loss:.2f} 台幣 ({profit_or_loss_usd:.2f} 美金)")
        elif profit_or_loss < 0:
            print(f"  虧損: {-profit_or_loss:.2f} 台幣 ({-profit_or_loss_usd:.2f} 美金)")
        else:
            print("  持平，無盈虧。")
        print("-" * 30)

    # 計算總美金金額
    total_invested_usd = total_invested / usd_to_twd_rate
    total_current_usd = total_current_value / usd_to_twd_rate
    total_profit_or_loss_usd = total_profit_or_loss / usd_to_twd_rate

    # 輸出總盈虧結果
    print("\n=== 總結 ===")
    print(f"總投資金額: {total_invested:.2f} 台幣 ({total_invested_usd:.2f} 美金)")
    print(f"總當前市值: {total_current_value:.2f} 台幣 ({total_current_usd:.2f} 美金)")
    if total_profit_or_loss > 0:
        print(f"總共賺了: {total_profit_or_loss:.2f} 台幣 ({total_profit_or_loss_usd:.2f} 美金)")
    elif total_profit_or_loss < 0:
        print(f"總共虧了: {-total_profit_or_loss:.2f} 台幣 ({-total_profit_or_loss_usd:.2f} 美金)")
    else:
        print("總共沒有盈虧，您的投資持平。")

if __name__ == "__main__":
    main()

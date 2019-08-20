import unittest

from contract.ContractClient import ContractClient


class TestAPI(unittest.TestCase):
    def setUp(self):
        apiid = 'you apikey'
        secret = 'you secret'
        self.client = ContractClient(apiid, secret)

    def test_market_order_book(self):
        res = self.client.market_order_book('BTCUSDT', 10)
        print(res)

    def test_tickers(self):
        res = self.client.market_tickers()
        print(res)

    def test_kline(self):
        res = self.client.market_klines('BTCUSDT', 1, 1557425760, 1557425820)
        print(res)

    def test_trades(self):
        res = self.client.market_trades('BTCUSDT', 1)
        print(res)

    def test_account_info(self):
        res = self.client.account_info()
        print(res)

    def test_position_list(self):
        res = self.client.position_list('BTCUSDT')
        print(res)

    def test_place_order(self):
        res = self.client.trade_order_place('ETHUSDT', 20, 1, 'openLong', '259.65', 'xxx', marginMode='fixed')
        print(res)

    def test_cancel(self):
        res = self.client.trade_order_cancel('583008136387211264')
        print(res)

    def test_openorders(self):
        res = self.client.trade_order_open_orders('BTCUSDT', 1, 10)
        print(res)

    def test_order_info(self):
        res = self.client.trade_order_info('583009061747142656')
        print(res)

    def test_closed_order(self):
        res = self.client.trade_order_closed_orders(symbol='BTCUSDT', pageNum=1, pageSize=50)
        print(res)

    def test_batch_Cancel(self):
        res = self.client.trade_order_batch_cancel(["578639816552972288", "578639902896914432"])
        print(res)

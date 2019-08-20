# -*- coding: utf-8 -*-

from contract.util import *


class ContractClient:
    """
    client for CoinBene contract ,include functions of  account ,market ,trade operations
    """

    def __init__(self, apiid, secret):
        self.apiid = apiid
        self.secret = secret
        self.base_url = 'http://openapi-contract.coinbene.com'

    def _gen_parameter(self):
        """
        gen common info for sign
        :return:
        """
        dic = {'apiid': self.apiid, 'secret': self.secret}
        return dic

    def account_info(self):
        """
        get contract account info
        :return:
        """
        dic = self._gen_parameter()
        requrl = '/api/swap/v2/account/info'
        dic['requestURI'] = requrl
        url = self.base_url + requrl
        return request_sign_get(url, dic)

    def position_list(self, symbol=None):
        """
        get  all contract positions
        :param symbol: symbol name could be None
        :return:
        """
        dic = self._gen_parameter()
        if symbol is not None:
            dic['symbol'] = symbol
        requrl = '/api/swap/v2/position/list'
        dic['requestURI'] = requrl
        url = self.base_url + requrl
        return request_sign_get(url, dic)

    def market_order_book(self, symbol, size):
        """
        get symbol's order book
        :param symbol: symbol name
        :param size: size
        :return:
        """
        dic = {'symbol': symbol, 'size': size}
        requrl = '/api/swap/v2/market/orderBook'
        url = self.base_url + requrl
        return request_nosign_get(url, dic)

    def market_tickers(self):
        """
        get contract tickers info
        :return:
        """
        dic = {}
        requrl = '/api/swap/v2/market/tickers'
        url = self.base_url + requrl
        return request_nosign_get(url, dic)

    def market_trades(self, symbol, limit):
        """
        get latest trade info
        :param symbol:
        :param limit:
        :return:
        """
        dic = {'symbol': symbol, 'limit': limit}
        requrl = '/api/swap/v2/market/trades'
        url = self.base_url + requrl
        return request_nosign_get(url, dic)

    def market_klines(self, symbol, resolution, fromT, toT):
        """
        get kline info
        :param symbol:
        :param resolution: time size one of ["1", "3", "5", "15", "30", "60", "120", "240", "360", "720", "D", "W", "M"]
        :param fromT:  begin time  SEC level timestamp
        :param toT:   end time SEC level timestamp
        :return:
        """
        dic = {'symbol': symbol, 'resolution': resolution, 'from': fromT, 'to': toT}
        requrl = '/api/swap/v2/market/klines'
        url = self.base_url + requrl
        return request_nosign_get(url, dic)

    def trade_order_place(self, symbol, leverage, quantity, direction, orderPrice=None, clientId=None,
                          marginMode='crossed'):
        """
        place order can open or close your contract orders
        :param symbol:  symbol  name
        :param leverage: one of [2, 3, 5, 10, 20]
        :param quantity: quantity
        :param direction: one of [openLong,openShort,closeLong,closeShort]
        :param orderPrice: limit price,if choose market price None
        :param clientId: clientId is just for you to mark this order
        :return:
        """
        dic = self._gen_parameter()
        dic['symbol'] = symbol
        dic['leverage'] = leverage
        dic['quantity'] = quantity
        dic['direction'] = direction
        dic['marginMode'] = marginMode
        if orderPrice is not None:
            dic['orderPrice'] = orderPrice
        if clientId is not None:
            dic['clientId'] = clientId
        requrl = '/api/swap/v2/order/place'
        dic['requestURI'] = requrl
        url = self.base_url + requrl
        return request_sign_post(url, dic)

    def trade_order_cancel(self, orderId):
        """
        cancel order
        :param orderId: orderId
        :return:
        """
        dic = self._gen_parameter()
        dic['orderId'] = orderId
        requrl = '/api/swap/v2/order/cancel'
        dic['requestURI'] = requrl
        url = self.base_url + requrl
        return request_sign_post(url, dic)

    def trade_order_batch_cancel(self, orderIds):
        """
        batch cancel orders ,at most 10
        :param orderIds: list of orderId
        :return:
        """
        dic = self._gen_parameter()
        dic['orderIds'] = orderIds
        requrl = '/api/swap/v2/order/batchCancel'
        dic['requestURI'] = requrl
        url = self.base_url + requrl
        return request_sign_post(url, dic)

    def trade_order_open_orders(self, symbol, pageNum, pageSize):
        """
        query current orders in trades
        :param symbol: symbol name
        :param pageNum:
        :param pageSize:
        :return:
        """
        dic = self._gen_parameter()
        dic['symbol'] = symbol
        dic['pageNum'] = pageNum
        dic['pageSize'] = pageSize
        requrl = '/api/swap/v2/order/openOrders'
        dic['requestURI'] = requrl
        url = self.base_url + requrl
        return request_sign_get(url, dic)

    def trade_order_info(self, orderId):
        """
        query order details
        :param orderId: orderId
        :return:
        """
        dic = self._gen_parameter()
        dic['orderId'] = orderId
        requrl = '/api/swap/v2/order/info'
        dic['requestURI'] = requrl
        url = self.base_url + requrl
        return request_sign_get(url, dic)

    def trade_order_closed_orders(self, beginTime=None, endTime=None, direction=None, orderType=None, pageNum=None,
                                  pageSize=None,
                                  symbol=None):
        """
        query history orders
        :param beginTime:  begin time  SEC level timestamp
        :param endTime:    end time  SEC level timestamp
        :param direction:  one of [openLong,   openShort, closeLong, closeShort]
        :param orderType:  one of [limit,market]
        :param pageNum:    pageNum
        :param pageSize:   pageSize
        :param symbol:     symbol name
        :return:
        """
        dic = self._gen_parameter()

        if beginTime is not None:
            dic['beginTime'] = beginTime
        if endTime is not None:
            dic['endTime'] = endTime
        if direction is not None:
            dic['direction'] = direction
        if orderType is not None:
            dic['orderType'] = orderType
        if pageNum is not None:
            dic['pageNum'] = pageNum
        if pageSize is not None:
            dic['pageSize'] = pageSize
        if symbol is not None:
            dic['symbol'] = symbol
        requrl = '/api/swap/v2/order/closedOrders'
        dic['requestURI'] = requrl
        url = self.base_url + requrl
        return request_sign_get(url, dic)

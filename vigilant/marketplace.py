import vigilant.datamodel
import vigilant.logging


class Marketplace(object):
    def place_order(self, coin: str, fiat: str, volume: float) -> None:
        raise NotImplementedError()

    def get_spot_price(self, coin: str, fiat: str) -> vigilant.datamodel.Price:
        raise NotImplementedError()

    def get_name(self):
        raise NotImplementedError()


class BuyError(Exception):
    pass


class TickerError(Exception):
    pass

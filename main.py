import logging

from connectors.binance_futures import BinanceFuturesClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root


logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':

    binance = BinanceFuturesClient("2d0158eb48f9d15445880af8437793743db9a17c1d8fe15e0d7613bb9f87bca1", "be0545eff551802102767b0921c744870ffc5c397bb755a653346ee7a2d25b17", True)
    bitmex = BitmexClient("J3AdQI0XzbwOJU4krRynjg-5", "ifm0BmTVIaqnz-mjZwJT25fVCmbA1bjEj00spHoEtDX_2kAB", True)

    root = Root(binance, bitmex)
    root.mainloop()

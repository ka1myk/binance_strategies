#!/usr/bin/python

# ['1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w', '1M']

from tradingview_ta import TA_Handler, Interval, Exchange
import subprocess

ETHBUSDPERP_1m = TA_Handler(
    symbol="ETHBUSDPERP",
    screener="crypto",
    exchange="BINANCE",
    interval=Interval.INTERVAL_1_MINUTE,
)

ETHBUSDPERP_5m = TA_Handler(
    symbol="ETHBUSDPERP",
    screener="crypto",
    exchange="BINANCE",
    interval=Interval.INTERVAL_5_MINUTES,
)

ETHBUSDPERP_15m = TA_Handler(
    symbol="ETHBUSDPERP",
    screener="crypto",
    exchange="BINANCE",
    interval=Interval.INTERVAL_15_MINUTES,
)

ETHBUSDPERP_30m = TA_Handler(
    symbol="ETHBUSDPERP",
    screener="crypto",
    exchange="BINANCE",
    interval=Interval.INTERVAL_30_MINUTES,
)

while True:
    while (
            ETHBUSDPERP_1m.get_analysis().summary["RECOMMENDATION"]
            in ("STRONG_BUY", "BUY")
            and ETHBUSDPERP_5m.get_analysis().summary["RECOMMENDATION"]
            in ("STRONG_BUY", "BUY")
            and ETHBUSDPERP_15m.get_analysis().summary["RECOMMENDATION"]
            in ("STRONG_BUY", "BUY")
            and ETHBUSDPERP_30m.get_analysis().summary["RECOMMENDATION"]
            in ("STRONG_BUY", "BUY")
    ):

        try:
            w.kill()
        except Exception as ex:
            print(ex)

        l = subprocess.Popen(
            [
                "python3",
                "passivbot.py",
                "binance_01",
                "ETHBUSD",
                "/root/passivbot_configs/long.json",
            ]
        )
    try:
        l.kill()
    except Exception as ex:
        print(ex)

    w = subprocess.Popen(
        [
            "python3",
            "passivbot.py",
            "binance_01",
            "ETHBUSD",
            "/root/passivbot_configs/long.json",
            "-lm",
            "gs",
        ]
    )

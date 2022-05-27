from binance.client import Client
import requests, json, time

with open('/root/binance_strategies/api-keys.json') as p:
    creds = json.load(p)
client = Client(creds['binance_01']['key'], creds['binance_01']['secret'])

while True:
    try:

        with open('/root/binance_strategies/variables.json') as v:
            variables = json.load(v)

        time_to_wait_one_more_check = variables['time_to_wait_one_more_check']
        time_to_cool_down = variables['time_to_cool_down']
        leverage = variables['leverage']
        multiplier = variables['multiplier']

        symbol = 'ETHBUSD'
        pricePrecision = 2
        quantityPrecision = 3
        minNotional = 0.003
        quantity = round(minNotional * multiplier, quantityPrecision)

        liquidations_in_USD = variables['liquidations_in_USD']

        headers = {'coinglassSecret': '50f90ddcd6a8437992431ab0f1b698c1'}
        url = requests.get(
            "https://open-api.coinglass.com/api/pro/v1/futures/liquidation/detail/chart?symbol=ETH&timeType=9",
            headers=headers)
        text = url.text
        data = json.loads(text)

        long_signal = float(data['data'][90]['buyVolUsd'])
        if long_signal > liquidations_in_USD:
            client.futures_create_order(symbol=symbol,
                                        side='BUY',
                                        positionSide='LONG',
                                        type='MARKET',
                                        leverage=leverage,
                                        quantity=quantity)

        short_signal = float(data['data'][90]['sellVolUsd'])
        if short_signal > liquidations_in_USD:
            client.futures_create_order(symbol=symbol,
                                        side='SELL',
                                        positionSide='SHORT',
                                        type='MARKET',
                                        leverage=leverage,
                                        quantity=quantity)

        # # do not modify! #
        # time.sleep(1.5)
        #
        # # cancel all orders by symbol to create new #
        # client.futures_cancel_all_open_orders(symbol=symbol)
        #
        # if abs(float(client.futures_position_information(symbol=symbol)[1].get(
        #         'positionAmt'))) < 0:
        #     # create close long order with profit long_profit_percent #
        #     client.futures_create_order(symbol=symbol, side='SELL', positionSide='LONG', type='LIMIT',
        #                                 timeInForce='GTC',
        #                                 price=round(abs(float(
        #                                     client.futures_position_information(symbol=symbol)[1].get(
        #                                         'entryPrice'))) * long_profit_percent,
        #                                             pricePrecision),
        #                                 quantity=abs(
        #                                     float(client.futures_position_information(symbol=symbol)[1].get(
        #                                         'positionAmt'))))
        #
        # if abs(float(client.futures_position_information(symbol=symbol)[2].get(
        #         'positionAmt'))) < 0:
        #     # create close long order with profit short_profit_percent#
        #     client.futures_create_order(symbol=symbol, side='BUY', positionSide='SHORT', type='LIMIT',
        #                                 timeInForce='GTC',
        #                                 price=round(abs(float(
        #                                     client.futures_position_information(symbol=symbol)[2].get(
        #                                         'entryPrice'))) * short_profit_percent,
        #                                             pricePrecision),
        #                                 quantity=abs(
        #                                     float(client.futures_position_information(symbol=symbol)[2].get(
        #                                         'positionAmt'))))
        time.sleep(time_to_cool_down)



    except Exception as e:
        print("Function errored out!", e)
        print("Retrying ... ")

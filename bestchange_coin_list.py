import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
from binance import Client
from datetime import datetime
from bestchange_api import BestChange
from create_bc import dp, bot
from po_bc import con, cur
import psycopg2
admin_id = 394652149

api_key = '1QrbAnjDYWcnmKoQYVn2ZSphucr4yXZtWEwUATG103rqfgJqG0VZ5kW7vdtMIS0Q'
secret_key = 'IU08Ye3WRhrjBEZl28vA9CN3TWL2fLSEv1XMZA8kYjmASbWOPpvVwhXfF6s6WQyS'
client = Client(api_key, secret_key)


async def bestchange_scaner(prmin, user_id):
    start_time = datetime.now()
    # print(start_time)
    sum = 1000
    api = BestChange()
    currencies = api.currencies().get()
    exch = api.exchangers().get()
    bc_list = [{'coin': '0x (ZRX)', 'id': 168}, {'coin': 'Algorand (ALGO)', 'id': 216},
               {'coin': 'Avalanche (AVAX)', 'id': 217}, {'coin': 'BAT (BAT)', 'id': 61},
               {'coin': 'BinanceCoin BEP2 (BNB)', 'id': 16}, {'coin': 'BinanceCoin BEP20 (BNB)', 'id': 19},
               {'coin': 'Bitcoin (BTC)', 'id': 93}, {'coin': 'Bitcoin Cash (BCH)', 'id': 172},
               {'coin': 'Cardano (ADA)', 'id': 181}, {'coin': 'Chainlink (LINK)', 'id': 197},
               {'coin': 'Cosmos (ATOM)', 'id': 198}, {'coin': 'Dash (DASH)', 'id': 140},
               {'coin': 'Decentraland (MANA)', 'id': 227}, {'coin': 'Dogecoin (DOGE)', 'id': 115},
               {'coin': 'EOS (EOS)', 'id': 178}, {'coin': 'Ether Classic (ETC)', 'id': 160},
               {'coin': 'Ethereum (ETH)', 'id': 139}, {'coin': 'Ethereum BEP20 (ETH)', 'id': 212},
               {'coin': 'ICON (ICX)', 'id': 104}, {'coin': 'IOTA (MIOTA)', 'id': 179},
               {'coin': 'Komodo (KMD)', 'id': 134}, {'coin': 'Litecoin (LTC)', 'id': 99},
               {'coin': 'Maker (MKR)', 'id': 213}, {'coin': 'Monero (XMR)', 'id': 149},
               {'coin': 'NEAR Protocol (NEAR)', 'id': 76}, {'coin': 'NEM (XEM)', 'id': 173},
               {'coin': 'NEO (NEO)', 'id': 177}, {'coin': 'OMG Network (OMG)', 'id': 48},
               {'coin': 'Ontology (ONT)', 'id': 135}, {'coin': 'Polkadot (DOT)', 'id': 201},
               {'coin': 'Polygon (MATIC)', 'id': 138}, {'coin': 'Qtum (QTUM)', 'id': 26},
               {'coin': 'Ravencoin (RVN)', 'id': 205}, {'coin': 'Ripple (XRP)', 'id': 161},
               {'coin': 'Shiba BEP20 (SHIB)', 'id': 32}, {'coin': 'Shiba ERC20 (SHIB)', 'id': 210},
               {'coin': 'Solana (SOL)', 'id': 82}, {'coin': 'Stellar (XLM)', 'id': 182},
               {'coin': 'TRON (TRX)', 'id': 185}, {'coin': 'Terra (LUNA)', 'id': 2}, {'coin': 'Tezos (XTZ)', 'id': 175},
               {'coin': 'Uniswap (UNI)', 'id': 202}, {'coin': 'VeChain (VET)', 'id': 8},
               {'coin': 'Waves (WAVES)', 'id': 133}, {'coin': 'Yearn.finance (YFI)', 'id': 220},
               {'coin': 'Zcash (ZEC)', 'id': 162}]
    # for i in bc_list:
    #     list_id = i['id']
    #     id_list.append(list_id)
    # print(id_list)
    id_list = [168, 216, 217, 61, 16, 19, 93, 172, 181, 197, 198, 140, 227, 115, 178, 160, 139, 212, 104, 179, 134, 99,
               213, 149, 76, 173, 177, 48, 135, 201, 138, 26, 205, 161, 32, 210, 82, 182, 185, 2, 175, 202, 8, 133, 220,
               162]
    bestchange_links = {168: 'zrx', 216: 'algorand', 217: 'avalanche', 61: 'bat', 16: 'binance-coin-bep2',
                        19: 'binance-coin', 93: 'bitcoin', 172: 'bitcoin-cash', 181: 'cardano',
                        197: 'chainlink',
                        198: 'cosmos', 140: 'dash', 227: 'decentraland', 115: 'dogecoin', 178: 'eos',
                        160: 'ethereum-classic',
                        139: 'ethereum', 212: 'ethereum-bep20', 104: 'icon', 179: 'iota', 134: 'komodo)',
                        99: 'litecoin',
                        213: 'maker', 149: 'monero', 76: 'near', 173: 'nem', 177: 'neo', 48: 'omg',
                        135: 'ontology', 201: 'polkadot', 138: 'polygon', 26: 'qtum', 205: 'ravencoin',
                        161: 'ripple',
                        32: 'shiba-inu-bep20', 210: 'shiba-inu', 82: 'solana', 182: 'stellar', 185: 'tron',
                        2: 'terra',
                        175: 'tezos', 202: 'uniswap', 8: 'vechain', 133: 'waves', 220: 'yearn-finance',
                        162: 'zcash'}
    rates_list = []
    # print(id_list)

    for i in id_list:
        try:
            for j in id_list:
                try:
                    # print(f"i: {i}, j: {j}")

                    res = api.rates().filter(i, j)
                    q_give = res[0]['give']
                    q_get = res[0]['get']
                    give_coin = res[0]['give_id']
                    get_coin = res[0]['get_id']

                    give_link = bestchange_links[give_coin]
                    get_link = bestchange_links[get_coin]

                    exchange = res[0]['exchange_id']
                    coins_rate = res[0]['rate']
                    reserve = res[0]['reserve']
                    min_sum = res[0]['min_sum']
                    max_sum = res[0]['max_sum']
                    give = res[0]['give']
                    get = res[0]['get']
                    exch_name = exch[exchange]['name']
                    give_coin_name = currencies[i]['name']
                    get_coin_name = currencies[j]['name']
                    dict_tmp = {'give_coin': give_coin_name,
                                'get_coin': get_coin_name,
                                'exchange_name': exch_name,
                                'rate': coins_rate,
                                'reserve': reserve,
                                'min_sum': min_sum,
                                'max_sum': max_sum,
                                'give': give,
                                'get': get,
                                'give_link': give_link,
                                'get_link': get_link}
                    rates_list.append(dict_tmp)
                    # print(dict_tmp)
                except:
                    pass
        except:
            pass

    cur.execute(f"delete from binance_tickers")
    con.commit()
    # cur.execute("create table binance_tickers(id bigint primary key,"
    #             "ZRX_price float, ALGO_price float, AVAX_price float,"
    #             "BAT_price float, BNB_price float,BTC_price float, BCH_price float, ADA_price float, LINK_price float, ATOM_price float, DASH_price float, MANA_price float, DOGE_price float, EOS_price float, ETC_price float, ETH_price float, ICX_price float, MIOTA_price float, KMD_price float, LTC_price float, MKR_price float, XMR_price float, NEAR_price float, XEM_price float, NEO_price float, OMG_price float, ONT_price float, DOT_price float,MATIC_price float, QTUM_price float, RVN_price float, XRP_price float, SHIB_price float, SOL_price float, XLM_price float, TRX_price float, LUNA_price float, XTZ_price float, UNI_price float, VET_price float, WAVES_price float,YFI_price float, ZEC_price float)")

    global id
    cur.execute(f'select count(*) from binance_tickers')
    id = cur.fetchone()[0]
    cur.execute(f"insert into binance_tickers(id) values ({id})")
    con.commit()
    for i in bc_list:
        try:
            aa = i['coin']
            aaa = aa.split()[-1].replace('(', '').replace(')', '')
            if aaa != 'MIOTA':
                symbol = f'{aaa}USDT'
                # print(symbol)
                price = client.get_ticker(symbol=symbol)
                last_price = float(price['lastPrice'])
                cur.execute(f"update binance_tickers set {aaa}_price = {last_price} where id = {id}")
                con.commit()
            else:
                symbol = 'IOTAUSDT'
                # print(symbol)
                price = client.get_ticker(symbol=symbol)
                last_price = float(price['lastPrice'])
                cur.execute(f"update binance_tickers set {aaa}_price = {last_price} where id = {id}")
                con.commit()

        except:
            pass

    bc_parse = []
    for j in rates_list:
        try:
            aa = j['give_coin']
            aaa = aa.split()[-1].replace('(', '').replace(')', '')
            # print('give_coin: ', aaa)
            bb = j['get_coin']
            bbb = bb.split()[-1].replace('(', '').replace(')', '')
            # print('get_coin: ', bbb)
            cc = j['rate']
            # print('rate: ', cc)
            cur.execute(f"select {aaa}_price from binance_tickers")
            price_aaa = cur.fetchone()[0]
            # print('market price give coin: ', price_aaa)
            cur.execute(f"select {bbb}_price from binance_tickers")
            price_bbb = cur.fetchone()[0]
            # print('market price get coin: ', price_bbb)
            profit = sum / price_aaa / cc * price_bbb
            give_l = j['give_link']
            get_l = j['get_link']
#             qu_give = j['q_give']
#             qu_get = j['q_get']
#             mi_sum = j['min_sum']
#             ma_sum = j['max_sum']
            exchanger_name = j['exchange_name']
            # if profit - sum >= 2:
            tmp_dict = {'give_coin': aaa, 'get_coin': bbb, 'bestchange_rate': cc, 'binance_price_give': price_aaa,
                        'binance_price_get': price_bbb, 'profit': profit, 'give_l': give_l, 'get_l': get_l,
                        'exchanger_name': exchanger_name}
            bc_parse.append(tmp_dict)

        except:
            pass

    if len(bc_parse) != 0:
        df = pd.DataFrame(bc_parse)
        str = df.sort_values(by='profit', ascending=False)
        strstr = str.head(1)
        try:
            max_message = strstr.iloc[0].to_json()
            items_max = json.loads(max_message)
            give_coin_name = items_max['give_coin']
            get_coin_name = items_max['get_coin']
            bc_rate = items_max['bestchange_rate']
            binance_price_give = items_max['binance_price_give']
            binance_price_get = items_max['binance_price_get']
            slvr_proc_max = (float(items_max['profit']) - 1000) / (1000 / 100)
            round_slvr_proc_max = round(slvr_proc_max, 3)
            give_li = items_max['give_l']
            get_li = items_max['get_l']
            exch_name = items_max['exchanger_name']
#             qua_give = j['qu_give']
#             qua_get = j['qu_get']
#             minn = j['min']
#             maxx = j['max']

            cur.execute(f"select tele_id from arbi_users")
            users = cur.fetchall()

            if slvr_proc_max > prmin:
                for i in users:
                    mes_for_user_id = i[0]

#                     await bot.send_message(mes_for_user_id,
#                                            f"Profit scheme just has been found! Profit before taxes: {round_slvr_proc_max}%\n\n"
#                                            f"Buy {give_coin_name} on the Binance spot market by this price: {binance_price_give}\n\n"
#                                            f"Swap {give_coin_name} on the bestchange site for {get_coin_name} by this link:\n"
#                                            f"https://www.bestchange.ru/{give_li}-to-{get_li}.html\n\n"
#                                            f"Give: {qua_give} {give_coin_name}\nGet: {qua_get} {get_coin_name}\n"
#                                            f"Price rate: {bc_rate}\n"
#                                            f"Min transaction: {minn}\n"
#                                            f"Max transaction: {maxx}\n"
#                                            f"Exchange name: {exch_name}\n\n"
#                                            f"Sell {get_coin_name} on the Binance spot market by this price: {binance_price_get}")
                    await bot.send_message(mes_for_user_id,
                                           f"Profit scheme just has been found! Profit before taxes: {round_slvr_proc_max}%\n\n"
                                           f"Buy {give_coin_name} on the Binance spot market by this price: {binance_price_give}\n\n"
                                           f"Swap {give_coin_name} on the bestchange site for {get_coin_name} by this link:\n"
                                           f"https://www.bestchange.ru/{give_li}-to-{get_li}.html\n\n"
                                           f"Price rate: {bc_rate}\n"
                                           f"Exchange name: {exch_name}\n\n"
                                           f"Sell {get_coin_name} on the Binance spot market by this price: {binance_price_get}")



            else:
                await bot.send_message(admin_id, 'No results')



        except Exception as e:
            await bot.send_message(admin_id, f'error: {e}')
            pass


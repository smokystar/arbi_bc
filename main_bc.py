from aiogram.utils import executor
from create_bc import dp
import psycopg2
from po_bc import con, cur

# cur.execute(f"insert into arbi_users(tele_id) values (323039084) ")
# con.commit()
# con = psycopg2.connect(user="uhwgxkaboaglce",
#                                 password="75db761e1367ffdf929f791edc4dcd1a58936cbe3fa9e87c920ca16338f2374c",
#                                 host="ec2-52-48-159-67.eu-west-1.compute.amazonaws.com",
#                                 port="5432",
#                                 database="d5ehlrsmpq329l")
# cur = con.cursor()

async def on_startup(_):
    print('Bot is online')

import commands_bc
# cur.execute("create table binance_tickers(id bigint primary key,"
#             "ZRX_price float, ALGO_price float, AVAX_price float,"
#             "BAT_price float, BNB_price float,BTC_price float, BCH_price float, ADA_price float, LINK_price float, ATOM_price float, DASH_price float, MANA_price float, DOGE_price float, EOS_price float, ETC_price float, ETH_price float, ICX_price float, MIOTA_price float, KMD_price float, LTC_price float, MKR_price float, XMR_price float, NEAR_price float, XEM_price float, NEO_price float, OMG_price float, ONT_price float, DOT_price float,MATIC_price float, QTUM_price float, RVN_price float, XRP_price float, SHIB_price float, SOL_price float, XLM_price float, TRX_price float, LUNA_price float, XTZ_price float, UNI_price float, VET_price float, WAVES_price float,YFI_price float, ZEC_price float)")
# con.commit()

commands_bc.register_handlers_client_partners(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

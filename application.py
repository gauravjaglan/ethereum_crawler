from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from ethereum_crawler import get_transaction_data

app = Flask(__name__)

@app.route('/', methods=("POST", "GET"))
def eth_table():

    tx_ad = request.args.get('tx_id')
    block_start = request.args.get("block_start")
    block_end = request.args.get("block_end")
    date = request.args.get("date")

    #tx_id=0xaa7a9ca87d3694b5755f213b5d04094b8d0f0a6f&block_start=9000000&block_end=9099999&date=2019-12-13
    #df = get_transaction_data("0xaa7a9ca87d3694b5755f213b5d04094b8d0f0a6f",'9000000','9099999', '2019-12-13')
    crawler_response = get_transaction_data(tx_ad,block_start,block_end, date)
    if crawler_response[1] == 200:
        df = crawler_response[0]
        return render_template('simple.html',  dat = df['ethereum consumed'].sum(),ad = tx_ad, column_names=df.columns.values, row_data=list(df.values.tolist()), zip=zip)
    else:
        print(crawler_response[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0')

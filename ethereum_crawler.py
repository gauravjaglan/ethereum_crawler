import requests
import pandas


def get_transaction_data(transaction_address, block_start, block_end, date):
    url = r"https://api.etherscan.io/api?module=account&action=txlist&address={0}&startblock={1}&endblock={2}&sort=desc&apikey={3}&timeStamp=1574748494".format(transaction_address, block_start, block_end, api_key)
    #&page=1&offset=10
    payload = ""
    headers = {}
    try:
        response = requests.request("GET", url)
        if response.status_code==200:
            transactions = pandas.DataFrame(response.json()['result'])
            transactions = transactions.loc[(transactions['timeStamp'] <= date)]
            transactions.timeStamp = pandas.to_datetime(transactions['timeStamp'], unit='s')
            transactions['gasPrice'] = transactions['gasPrice'].apply(float)
            transactions['gasUsed'] = transactions['gasUsed'].apply(float)
            transactions['ethereum consumed'] = (transactions['gasPrice'].apply(float)*transactions['gasUsed'].apply(float))/1000000000000000000
            return transactions[['blockNumber','from','gas','gasPrice','ethereum consumed','timeStamp']], 200
        else:
            return "",response.status_code
    except Exception as e:
        return str(e) ,response.status_code

get_transaction_data("0xaa7a9ca87d3694b5755f213b5d04094b8d0f0a6f",'9000000','9099999', '2021-12-13')


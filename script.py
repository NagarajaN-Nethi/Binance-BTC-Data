def pre_process():
    '''
    
    Getting data for BinanceCoin BTC (BNB-BTC) price.
    Converting it to Pandas DataFrame.
    Cleaning up the column names.
    Pre Processing the data to convert the dates into datatime objects.
    Converting numberic data to floats.
    
    '''
    from binance import Client
    import pandas as pd
    api_key = 'v8XFbtW56pLDsXaAON1f3GxdSjRm53UTm5FoXyGeEgmCo19aniqgoE5tcux6ZAXe'
    api_secret = 'ruieiXJ0VYVxBk4wSGfxbtzHiWHPKcVlG47BfugifPamRpgjZjv2zwaIErL6ypEr'
    client = Client(api_key, api_secret)
    data = pd.DataFrame(client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1DAY, '1 Jan 2010' ))
    data.columns = ['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time', 'Quote Asset Volume', 
                    'Number of Trades', 'TB Base Volume', 'TB Quote Volume', 'Ignore']
    data['Open Time'] = pd.to_datetime(data['Open Time']/1000, unit='s')
    data['Close Time'] = pd.to_datetime(data['Close Time']/1000, unit='s')
    num_columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'Quote Asset Volume', 'TB Base Volume', 'TB Quote Volume']
    for cols in num_columns:
        data[cols] = data[cols].astype(float)
    data.drop('Ignore', axis = 1, inplace = True)
    
    return data    
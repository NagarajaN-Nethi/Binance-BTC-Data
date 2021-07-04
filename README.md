# Binance Data Visualization and Modeling

I successfully used the Binance API to grab Bitcoin live price data from Binance.

Check out the API [here](https://www.binance.com/en/my/settings/api-management)

Before you can start using the API, you have to register in the site. You can do so by going [here](https://www.binance.com/en/register?ref=HOC2XML2).

After getting registered in the site, use your API and Secret Key in the script.

For getting the data I have created a script which can with a few changes can be used to get any crypto being traded at binance by changing the ticker in line 16 of the script.
The date range can also be changed in the same line to tune the data as per your needs.

Then I have made some visualization to understand the trend of price of Bitcoin over the years.

After visualizing, I have created a RAndom Forest Regressor to model the data to predict the closing price of Bitcoin.

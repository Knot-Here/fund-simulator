# fund-simulator

A basic fund simulator. `usd_fund.py` is for USD-based funds and `eth_fund.py` is for ETH-based funds. All simulations are outputted in .csv in the `/output` directory

## How to Use

![image](https://user-images.githubusercontent.com/120458367/208680917-12a58f59-160c-438d-95a0-1357b3c9878a.png)

Very simple, just requires python with pandas (alot of IDE's have pandas but it exports locally)

  - start_date: The day that the fund started to trade
  - number_of_days: The numbers of days that the fund operated in the simulation
  - fund_amount = The amount of ETH or USD that the fund holds
  - max_daily_win = The max amount that the fund would profit per day
  - max_daily_loss = The max amount that the fund would lose per day

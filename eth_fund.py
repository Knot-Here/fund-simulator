import datetime
import random
import pandas as pd
pd.set_option('display.float_format', lambda x: '%.3f' % x)

#VARIABLES
start_date = "21/12/20"
number_of_days = 364
fund_amount = 1000
max_daily_win = 0.02
max_daily_loss = -0.02

date_1 = datetime.datetime.strptime(start_date, "%y/%m/%d")
add_day = date_1 + datetime.timedelta(days=1)
data = []
def main():
    dic = {"date": date_1, 
        "fund_amount": fund_amount
        }
    data.append(dic)
    fund = fund_amount
    date = date_1
    for i in range(number_of_days):
        date = date + datetime.timedelta(days=1)
        daily_result = random.uniform(max_daily_loss, max_daily_win)
        result =  daily_result * fund
        fund = result + fund
        dic = {"date": date,
            "fund_amount": fund}
        data.append(dic)
        

main()
df = pd.DataFrame(data)
df.to_csv('output/eth_fund.csv')
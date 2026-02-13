import pandas as pd
stock=pd.read_csv("D:\\downloads\\nitishh\\pandas_project\\stock market trading analyis system\\stocks.csv")
trade=pd.read_csv("D:\\downloads\\nitishh\\pandas_project\\stock market trading analyis system\\trades.csv")

trade["trade_date"]=pd.to_datetime(trade["trade_date"])

main=pd.merge(stock,trade,on="stock_id",how="inner")

main["trade_value"]=main["price"] * main["quantity"]

main["month"]=main["trade_date"].dt.month_name()
main.loc[main["trade_type"]=="BUY","trade_value"] *= -1

stock_wise_profit=main.groupby("stock_name")["trade_value"].sum()

sector_profit=main.groupby("sector")["trade_value"].sum()

best_sector_perform=sector_profit.sort_values(ascending=False)

month_profit=main.groupby("month")["trade_value"].sum()

high_profit_stock=main.groupby("stock_name")["trade_value"].sum()
high_profit_stock.sort_values(ascending=False,inplace=True)

high_volume_stock=main.groupby("stock_name")["quantity"].sum().sort_values(ascending=False)

pivot=pd.pivot_table(data=main,
                     index="month",
                     columns="sector",
                     values="trade_value",
                     aggfunc="sum")

main.to_csv("final1.csv")

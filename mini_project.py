import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"C:\Users\ji873\Downloads\crypto50_combined.csv")
df["Year"] = pd.to_datetime(df["Date"]).dt.year
#print(df)
crypto = df.loc[0:,('Symbol','Date','Year','Open')]
btc = crypto[crypto['Symbol'] == 'BTC']
grp = btc.groupby('Year')["Open"].mean()
#print(grp)


##Line graph
plt.figure(figsize = (10,5),dpi = 300)
plt.plot(grp.index,grp.values)
plt.title("BTC Opening price average",fontdict={'fontname':'Comic Sans MS','fontsize':12,'color':'green'})
plt.xlabel("Year",fontdict={'fontname':'Comic Sans MS','fontsize':10,'color':'red'})
plt.ylabel("Opening Price(USD)",fontdict={'fontname':'Comic Sans MS','fontsize':10,'color':'red'})
plt.tight_layout()#it automatically adjusts the size , that so every label etc. will be visible
plt.savefig("Line_chart_BTC_Opening_price_average.png",dpi=300)
plt.show()

##Bar graph
plt.figure(figsize = (10,5),dpi = 300)
plt.bar(grp.index,grp.values)
plt.title("BTC Opening price average",fontdict={'fontname':'Comic Sans MS','fontsize':12,'color':'green'})
plt.xlabel("Year",fontdict={'fontname':'Comic Sans MS','fontsize':10,'color':'red'})
plt.ylabel("Opening price(USD)",fontdict={'fontname':'Comic Sans MS','fontsize':10,'color':'red'})
plt.tight_layout()
plt.savefig("Bar_chart_BTC_Opening_price_average.png",dpi=300)
plt.show()
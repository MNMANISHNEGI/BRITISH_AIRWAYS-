import pandas as pd
df = pd.read_excel("C:\\Users\\91789\\PycharmProjects\\britishairwaystask\\4.3 Customer Booking Data.xlsx")
df.head()
print(df.info())
df["flight_day"].unique()
mapping = {
    "Mon": 1,
    "Tue": 2,
    "Wed": 3,
    "Thu": 4,
    "Fri": 5,
    "Sat": 6,
    "Sun": 7,
}
df["flight_day"] = df["flight_day"].map(mapping)
df["flight_day"].unique()
pd.options.display.width= None
pd.options.display.max_columns= None
#pd.set_option('display.max_rows', 3000)
#pd.set_option('display.max_columns', 3000)
print(df.describe())
#df.to_csv("C:\\Users\\91789\\PycharmProjects\\britishairwaystask/BA_buying.csv")

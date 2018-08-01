'引用package-pandas處理資料處理'
import pandas as pd
'引用package gmplot處理網頁標點的需求'
from gmplot import gmplot

'透過def將經緯度數據轉成可以使用的類型'
def parseLocation(loc):
    return (float(loc[1:loc.index(",")]), float(loc[loc.index(",")+1:-1]))

'透過read_csv並設定compression，取出壓縮檔內的資料'
df = pd.read_csv("NYPD_7_Major_Felony_Incidents.zip", compression="zip")
'調整部分檔名-去除空白或是特殊符號，讓之後的'
df.rename(columns={"Occurrence Year": "OccurrenceYear", "DayOfWeek": "Day_Of_Week"}, inplace=True)

'只列出需要的欄位資料'
clean_df = df[(df["OccurrenceYear"]>2005) & df["Offense"].notnull() & df["OccurrenceYear"].notnull()].copy()
'使用apply將經緯度轉換成可使用的資料型態'
clean_df["loc"] = clean_df.apply(lambda row: parseLocation(row["Location 1"]), axis=1)

'篩選資料指顯示2015年且為BURGLARY的資料'
df2 = clean_df[(clean_df["OccurrenceYear"]==2015) & (clean_df["Offense"]=="BURGLARY")]

'在 谷歌地圖 上繪製數據，用於生成HTML和 javascript，以便在 谷歌地圖 上呈現所有數據。 '
gmap = gmplot.GoogleMapPlotter.from_geocode("紐約市")

lats = []
lons = []

for i in range(len(df2)):
    lats.append(df2.iloc[i]["loc"][0])
    lons.append(df2.iloc[i]["loc"][1])

'設定標註點的顯示內容'
gmap.scatter(lats, lons, "#6f00d2", size=30, marker=False)
gmap.draw("NYC.html")
import pandas as pd
from gmplot import gmplot

def parseLocation(loc):
    return (float(loc[1:loc.index(",")]), float(loc[loc.index(",")+1:-1]))

df = pd.read_csv("NYPD_7_Major_Felony_Incidents.zip", compression="zip")
df.rename(columns={"Occurrence Year": "OccurrenceYear", "DayOfWeek": "Day_Of_Week"}, inplace=True)

clean_df = df[(df["OccurrenceYear"]>2005) & df["Offense"].notnull() & df["OccurrenceYear"].notnull()].copy()
clean_df["loc"] = clean_df.apply(lambda row: parseLocation(row["Location 1"]), axis=1)

df2 = clean_df[(clean_df["OccurrenceYear"]==2015) & (clean_df["Offense"]=="BURGLARY")]

gmap = gmplot.GoogleMapPlotter.from_geocode("New York City")

lats = []
lons = []

for i in range(len(df2)):
    lats.append(df2.iloc[i]["loc"][0])
    lons.append(df2.iloc[i]["loc"][1])

gmap.scatter(lats, lons, "#4440CB", size=20, marker=False)
gmap.draw("NYC.html")
import altair as alt
import pandas as pd
import numpy as np

source = pd.read_csv('Currently_infected_cumu.tsv', sep='\t')
source = source.rename(columns={"Unnamed: 0": "Country/Region"})

Spa = source["Country/Region"] == "Spain"
Dkk = source["Country/Region"] == "Denmark"
Fra = source["Country/Region"] == "France"
Ger = source["Country/Region"] == "Germany"
Ita = source["Country/Region"] == "Italy"

hue = Spa | Dkk | Fra | Ger | Ita

df = source[hue]

new_frame = pd.DataFrame(columns= ["Country", "Date", "Infection"])
days = ['1/22/2020',
 '1/23/2020',
 '1/24/2020',
 '1/25/2020',
 '1/26/2020',
 '1/27/2020',
 '1/28/2020',
 '1/29/2020',
 '1/30/2020',
 '1/31/2020',
 '2/1/2020',
 '2/2/2020',
 '2/3/2020',
 '2/4/2020',
 '2/5/2020',
 '2/6/2020',
 '2/7/2020',
 '2/8/2020',
 '2/9/2020',
 '2/10/2020',
 '2/11/2020',
 '2/12/2020',
 '2/13/2020',
 '2/14/2020',
 '2/15/2020',
 '2/16/2020',
 '2/17/2020',
 '2/18/2020',
 '2/19/2020',
 '2/20/2020',
 '2/21/2020',
 '2/22/2020',
 '2/23/2020',
 '2/24/2020',
 '2/25/2020',
 '2/26/2020',
 '2/27/2020',
 '2/28/2020',
 '2/29/2020',
 '3/1/2020',
 '3/2/2020',
 '3/3/2020',
 '3/4/2020',
 '3/5/2020',
 '3/6/2020',
 '3/7/2020',
 '3/8/2020',
 '3/9/2020',
 '3/10/2020',
 '3/11/2020']
import time
import datetime

count = 0
for i in range(20, len(days)):
    date_today = pd.Timestamp(time.mktime(datetime.datetime.strptime(days[i],
                                             "%m/%d/%Y").timetuple()), unit='s')
    new_frame.loc[count] = ['France', date_today, source[Fra].values[0][1:][i]]
    count += 1
    new_frame.loc[count] = ['Denmark', date_today, source[Dkk].values[0][1:][i]]
    count += 1
    new_frame.loc[count] = ['Spain', date_today, source[Spa].values[0][1:][i]]
    count += 1
    new_frame.loc[count] = ['Germany', date_today, source[Ger].values[0][1:][i]]
    count += 1
    new_frame.loc[count] = ['Italy', date_today, source[Ita].values[0][1:][i]]
    count += 1


okay = alt.Chart(new_frame).mark_line().encode(
    x='Date',
    y='Infection',
    color = "Country"
).interactive()
okay.save('chhhhhhhart.html')

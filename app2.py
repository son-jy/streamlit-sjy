import plotly.express as px
import plotly
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# 한글 안깨지게 하는 코드 
from matplotlib import font_manager, rc
font = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font)

#plt.figure(figsize=(12,8))

import altair as alt
from vega_datasets import data
import pandas as pd
import streamlit as st

emp = pd.read_csv("c:\\data\\emp.csv")
source = emp[['ename','sal']]

bars = alt.Chart(source).mark_bar().encode(
    x='sal',
    y="ename"
)

text = bars.mark_text(
    align='left',
    baseline='middle',
    dx=3  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text='sal'
)

a = (bars + text).properties(height=500)

st.dataframe(emp)  # Same as st.write(df)
st.altair_chart(a, use_container_width=True)

money = pd.read_csv("c:\\data\\money_data7.csv")

money = money[:] [money['A_YEAR']==2022]

fig, ax = plt.subplots(2,2, figsize=(12,8))

plt.subplot(221)
plt.plot(  list( money['A_MONTH'] ), list( money['A_RATE'] ), color='red' , marker='o'     ) 
plt.xticks(tuple(money['A_MONTH']) )
plt.title('미국금리')


plt.subplot(222)
plt.plot(  list( money['A_MONTH'] ), list( money['K_RATE'] ), color='blue' , marker='o'     ) 
plt.xticks(tuple(money['A_MONTH']) )
plt.title('한국금리')

plt.subplot(223)
plt.plot(  list( money['A_MONTH'] ), list( money['KOSPI'] ), color='green' , marker='o'     ) 
plt.xticks(tuple(money['A_MONTH']) )
plt.title('코스피 지수')

plt.subplot(224)
plt.plot(  list( money['A_MONTH'] ), list( money['HOUSE_PRICE'] ), color='yellow' , marker='o'     ) 
plt.xticks(tuple(money['A_MONTH']) )
plt.title('집값')

st.pyplot(fig)

import plotly.express as px
import plotly
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# 한글 안깨지게 하는 코드 
from matplotlib import font_manager, rc
font = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font)

#plt.figure(figsize=(12,8))

money = pd.read_csv("c:\\data\\money_data7.csv")

# 년도 선택 박스 넣기
import streamlit as st

option = st.selectbox(
    'How would you like to choice year ?',
    ('2020', '2021', '2022'))

option2 = int(option)

st.write('You selected:', option)

money = money[:] [money['A_YEAR']== option2]

fig, ax = plt.subplots(2,2, figsize=(12,8))

plt.subplot(221)
plt.plot(  list( money['A_MONTH'] ), list( money['A_RATE'] ), color='red' , marker='o'     ) 
plt.xticks(tuple(money['A_MONTH']) )
plt.title('미국금리')


plt.subplot(222)
plt.plot(  list( money['A_MONTH'] ), list( money['K_RATE'] ), color='blue' , marker='o'     ) 
plt.xticks(tuple(money['A_MONTH']) )
plt.title('한국금리')

plt.subplot(223)
plt.plot(  list( money['A_MONTH'] ), list( money['KOSPI'] ), color='green' , marker='o'     ) 
plt.xticks(tuple(money['A_MONTH']) )
plt.title('코스피 지수')

plt.subplot(224)
plt.plot(  list( money['A_MONTH'] ), list( money['HOUSE_PRICE'] ), color='yellow' , marker='o'     ) 
plt.xticks(tuple(money['A_MONTH']) )
plt.title('집값')

st.pyplot(fig)
import streamlit as st
import numpy as np
import pandas as pd
from time import time

# タイトルを表示
st.title('st.cache')

# キャッシュを使用したデータ生成関数の試験
begin_time_with_cache = time()
st.subheader('Using st.cache')

# キャッシュを使用したデータ生成関数。有効時間を30秒に設定
@st.cache_data(ttl=30)
def load_data_a():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_a())
end_time_with_cache = time()

# キャッシュを使用した場合の処理時間を表示
st.info(end_time_with_cache - begin_time_with_cache)

# キャッシュを使用しないデータ生成関数の試験
begin_time_without_cache = time()
st.subheader('Not using st.cache')

# キャッシュを使用しないデータ生成関数
def load_data_b():
  df = pd.DataFrame(
    np.random.rand(2000000, 5),
    columns=['a', 'b', 'c', 'd', 'e']
  )
  return df

st.write(load_data_b())
end_time_without_cache = time()

# キャッシュを使用しない場合の処理時間を表示
st.info(end_time_without_cache - begin_time_without_cache)
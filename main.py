import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("超入門")

st.write('プログレスバー')

'START!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.05)


left_column , right_column = st.columns(2)

button = left_column.button('ここは左カラムだよー')

if button:
    right_column.write('ここは右カラム')


expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ内容')

expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ内容')

expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ内容')

# option = st.text_input('趣味を教えて下さい')

# 'あなたの趣味は、', option ,'です' 

# text = st.slider('あなたの今の調子は？',0,100,50)

# 'コンディション',text




# if st.checkbox('show image'):
#     img = Image.open('sample.jpg')
#     st.image(img,caption="うんこである",use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69,139.70],
#     columns=['lat','lon']
# )

# df

# st.map(df)
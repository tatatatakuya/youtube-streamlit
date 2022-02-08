import streamlit as st
import time

st.title('Streamlit、超超入門')

st.write('Intaractive Widgets')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムにボタンを表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ内容を書く')
expander2 = st.expander('問い合わせ')
expander2.write('問い合わせ内容を書く')
expander2 = st.expander('問い合わせ')
expander2.write('問い合わせ内容を書く')


# text = st.sidebar.text_input('あなたの趣味を教えてください。')


# 'あなたの趣味：',text

# condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション:', condition

# if st.checkbox('Show Image'):
#     img = Image.open('img03.jpg')
#     st.image(img, caption='Takuya Hiraoka', use_column_width=True)


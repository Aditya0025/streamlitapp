# import streamlit as st
# import numpy as np
# import pandas as pd
# import pickle


# # st.write("""
# #     # Credit card fraud detection
# #     """)
# # st.sidebar.slider('All Features V1-V28, normAmount',0.0,1.0,0.5)
# # # st.sidebar.header('User Input Parameter')
# # st.subheader("User Input Parameter")

# def user_input_features():
#     V1 = st.sidebar.slider('All Features V1-V28, normAmount',0.0,1.0,0.5)
#     data = {'V1': V1,
#            'V2': V1,
#            'V3': V1,
#            'V4': V1,
#            'V5': V1,
#            'V6': V1,
#            'V7': V1,
#            'V8': V1,
#            'V9': V1,
#            'V10': V1,
#            'V11': V1,
#            'V12': V1,
#            'V13': V1,
#            'V14': V1,
#            'V15': V1,
#            'V16': V1,
#            'V17': V1,
#            'V18': V1,
#            'V19': V1,
#            'V20': V1,
#            'V21': V1,
#            'V22': V1,
#            'V23': V1,
#            'V24': V1,
#            'V25': V1,
#            'V26': V1,
#            'V27': V1,
#            'V28': V1,
#            'normAmount': V1
#            }
#     features = pd.DataFrame(data,index=[0])
#     return features

# if __name__ == "__main__":
#     st.write("""
#     # Credit card fraud detection
#     """)

#     st.sidebar.header('User Input Parameter')
#     df = user_input_features()
#     st.subheader("User Input Parameter")
#     st.write(df)
#     filename = r'C:\Users\ADITYA\Desktop\Coding\Chat bot\streamlit\XGBoost_OS'
#     model = pickle.load(open(filename,'rb'))
#     pred = model.predict(df)
#     st.subheader('Prediction - 1 denotes frauduluent transaction, 0 denotes non-fraudulent transaction')
#     st.write(pred)

import streamlit as st
import numpy as np
import pandas as pd 

st.title("My first App")

st.write("Here's Our first attempt at using data table")

# st.write(pd.DataFrame({'Name': [1,2,3,4,5], 
# 'Last_Name' : [10,20,30,40,50]}))
# '''Magic Command '''
df = pd.DataFrame({'Name': [1,2,3,4,5],'Last_Name' : [10,20,30,40,50]})
df

# Line_data
chart_data = pd.DataFrame(np.random.randn(20,3),
columns=['a','b','c'])
st.line_chart(chart_data)


# Map with Open Street Maps
map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(map_data)


# Checkbox to show and Hide
if st.checkbox("Show datframe"):

    chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

# Selectbox 

option = st.selectbox('Whcih number do you like',df['Last_Name'])
'you selected:', option



# Interesting Part Beta columns and beta expander(similar to boostrap columns)

left_column,right_column = st.beta_columns(2)
pressed = left_column.button("Press here")
if pressed:
    right_column.write("Wohoo!!")

expander = st.beta_expander("FAQ")
expander.write("Here is the work we doe for really long explanation")


# Progess bar 

import time
'For long Computation'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # this will print all code even the triple quotes string
    # '''Update the progress bar with each iteration'''
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)




import streamlit as st
import pandas as pd
from pydataset import data

st.title('🎈 pydataset')

selected_data = st.sidebar.selectbox('Select a dataset', data().dataset_id)
title_data = data()[ data()['dataset_id'] == selected_data]['title']


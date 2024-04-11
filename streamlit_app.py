import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as mse
from math import sqrt
import matplotlib.pyplot as plt
import time
import requests
import json

st.title('Real Estate Predictions')


def run_status():
	latest_iteration = st.empty()
	bar = st.progress(0)
	for i in range(100):
		latest_iteration.text(f'Percent Complete {i+1}')
		bar.progress(i + 1)
		time.sleep(0.1)
		st.empty()

st.subheader('Multi Model Predictions')

@st.cache
def load_data():
	df=pd.read_excel('data.xls')
	df=df.drop(['country'],axis=1)
	df=df[df['price']>0]
	df.rename(columns={'statezip':'zip'}, inplace=True)
	df['zip']=df['zip'].str.replace('WA','').astype(int)
	df['floors']=df['floors'].astype(int)
	df=df[df['bedrooms']>0]
	df=df[df['bathrooms']>0]
	return df

df=load_data()

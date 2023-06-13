import pandas as pd
import numpy as np
#import plotly.express as px
#import plotly as pl
#import seaborn as sns
import streamlit as st
#import scipy.stats as stats
import altair as alt
from numpy.random import seed
#import random

st.set_page_config(layout='wide')

##Code to resolve the padding issue above title
st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
        </style>
        """, unsafe_allow_html=True)

st.title(" :red[Theoritical Distributions] Interactive Gallery")

# Setting random seed
theseed = st.number_input('Enter a Random Seed', min_value=0,step=1)
np.random.seed(theseed)

# Add whitespace using Markdown
st.markdown("<br><br>", unsafe_allow_html=True)

normal, poisson = st.columns(2)

##### Normal Distributions
with normal:
    st.subheader('Normal or Gaussian Distribution')

    col1, col2 = st.columns(2)

    with col1:
        norm_mean = st.number_input('Enter Mean/Loc', min_value=0.0, value=0.0, key='norm_mean')
        norm_sd = st.number_input('Enter Standard Deviation /Scale', min_value=0.0, value=1.0, key='norm_sd')
        norm_size = st.slider('Select Sample Size', min_value=1, max_value=1000, value=500, key='norm_size')

        np.random.seed(theseed)
        norm_data = np.random.normal(loc=norm_mean, scale=norm_sd, size=norm_size)

        df = pd.DataFrame({'value': norm_data})

        chart = alt.Chart(df).transform_density('value',
                                                as_=['value', 'density'], ).mark_area(opacity=0.5,
                                                                                      color='green').encode(
            alt.X('value:Q', title='Value'),
            alt.Y('density:Q', title='Density')
        )

    with col2:
        st.altair_chart(chart, use_container_width=True)

##### Poisson Distributions
with poisson:
    st.subheader('Poisson Distribution')

    col1, col2 = st.columns(2)

    with col1:
        poisson_mean = st.number_input('Enter Mean/Loc', min_value=0.1, value=0.1, key='poisson_mean')
        poisson_size = st.slider('Select Sample Size', min_value=1, max_value=1000, value=500, key='poisson_size')

        np.random.seed(theseed)
        poisson_data = np.random.poisson(lam=poisson_mean, size=poisson_size)

        df_poisson = pd.DataFrame({'value': poisson_data})

        chart_poisson = alt.Chart(df_poisson).transform_density('value',
                                                                as_=['value', 'density'], ).mark_area(opacity=0.5,
                                                                                                      color='green').encode(
            alt.X('value:Q', title='Value'),
            alt.Y('density:Q', title='Density')
        )

        with col2:
            st.altair_chart(chart_poisson,use_container_width=True)

# Add whitespace using Markdown
st.markdown("<br>", unsafe_allow_html=True)

exponential, uniform = st.columns(2)

##### Exponential Distributions
with exponential:
    st.subheader('Exponential Distribution')

    col2, col3 = st.columns(2)

    with col2:
        expon_scale = st.number_input('Enter Scale', min_value=0.1,value=0.1, key='expon_scale')
        expon_size = st.slider('Select Sample Size', min_value=1, max_value=1000, value=500, key='expon_size')

        np.random.seed(theseed)

        expon_data = np.random.exponential(scale=expon_scale, size=expon_size)

        df_expon = pd.DataFrame({'value': expon_data})

        chart_expon = alt.Chart(df_expon).transform_density('value',
                                                            as_=['value', 'density'], ).mark_area(opacity=0.5,
                                                                                                  color='green').encode(
            alt.X('value:Q', title='Value'),
            alt.Y('density:Q', title='Density')
        )

    with col3:
        st.altair_chart(chart_expon,use_container_width=True)

##### Uniform Distributions
with uniform:
    st.subheader('Uniform Distribution (Continuous)')

    col2, col3 = st.columns(2)

    with col2:
        uniform_low = st.number_input('Enter Low',value=0.0, key='uniform_low')
        uniform_high = st.number_input('Enter High',value=1.0, key='uniform_high')
        uniform_size = st.slider('Select Sample Size', min_value=1, max_value=1000, value=500, key='uniform_size')

        np.random.seed(theseed)

        uniform_data = np.random.uniform(low=uniform_low, high=uniform_high, size=uniform_size)

        df_uniform = pd.DataFrame({'value': uniform_data})

        chart_uniform = alt.Chart(df_uniform).transform_density('value',
                                                                as_=['value', 'density'], ).mark_area(opacity=0.5,
                                                                                                      color='green').encode(
            alt.X('value:Q', title='Value'),
            alt.Y('density:Q', title='Density')
        )

    with col3:
        st.altair_chart(chart_uniform,use_container_width=True)

# Add whitespace using Markdown
st.markdown("<br>", unsafe_allow_html=True)

binomial, uniform_dis = st.columns(2)

##### Binomial Distributions
with binomial:
    st.subheader('Binomial Distribution')

    col2, col3 = st.columns(2)

    with col2:
        bino_n = st.number_input('Enter n', min_value=0, value=5, key='bino_n')
        bino_p = st.number_input('Select p', min_value=0.0, max_value=1.0, value=0.5, key='bino_p')
        bino_size = st.slider('Select Sample Size', min_value=1, max_value=1000, value=500, key='bino_size')

        np.random.seed(theseed)

        bino_data = np.random.binomial(n=bino_n, p=bino_p, size=bino_size)

        df_bino = pd.DataFrame({'value': bino_data})

        chart_bino =alt.Chart(df_bino).mark_bar(opacity=0.5).encode(
            alt.X('value:O', title='Value'),
            alt.Y('count()', title='Count')
        )

    with col3:
        st.altair_chart(chart_bino,use_container_width=True)

##### Uniform Distributions (discrete)

with uniform_dis:
    st.subheader('Uniform Distribution (Discrete)')

    col2, col3 = st.columns(2)

    with col2:
        d_uniform_low = st.number_input('Enter Low', min_value=-100, max_value=100, value=1, key='d_uniform_low')
        d_uniform_high = st.number_input('Enter High', min_value=-100, max_value=100, value=7, key='d_uniform_high')
        d_uniform_size = st.slider('Select Sample Size', min_value=1, max_value=1000,value=500, key='d_uniform_size')

        np.random.seed(theseed)

        d_uniform_data = np.random.randint(low=d_uniform_low, high=d_uniform_high, size=d_uniform_size)

        df_d_uniform = pd.DataFrame({'value': d_uniform_data})

        chart_d_uniform = alt.Chart(df_d_uniform).mark_bar(opacity=0.5).encode(
            alt.X('value:O', title='Value'),
            alt.Y('count()', title='Count')
        )

    with col3:
        st.altair_chart(chart_d_uniform,use_container_width=True)

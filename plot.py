#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 19:11:19 2023

@author: khushiagarwal
"""
import plotly
import plotly.graph_objs as go
import pandas as pd
def plot(df):
    data = [go.Scatter(
        x = df['Polarity'],
        y = df['Subjectivity'],
)]
    layout = go.Layout(
        xaxis=dict(
            title='Data',    
        ),
        yaxis=dict(
            title='Totale positivi',  
        )
    )
    fig = go.Figure(data=data, layout=layout)
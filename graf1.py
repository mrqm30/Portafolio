#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 09:47:39 2022

@author: cygnus
"""
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
import plotly.graph_objects as go
from dash.dependencies import Input, Output
df = pd.read_excel('/home/cygnus/Documentos/SMXFinancial/Semana_13_17_06/PortafolioSMX-master/app_admin/Analisis de Portafolio.xlsx')

app = Dash(__name__)

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}

app.layout = html.Div([
    dcc.Tabs(id='tabs-example-1', value='tab-1', children=[
        dcc.Tab(label='Moneda', value='tab-1', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Producto', value='tab-2', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Saldo insoluto actual', value='tab-3', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Fondeador', value='tab-4', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Admin. de Ingresos', value='tab-5', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Monto del contrato', value='tab-6', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Cobranza mínima requeria', value='tab-7', style=tab_style, selected_style=tab_selected_style)
    ]),
    html.Div(id='tabs-example-content-1')
], style = {"width":"70%"})

@app.callback(
    Output('tabs-example-content-1', 'children'),
    Input('tabs-example-1', 'value')
)


def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Tab content 1'),
            dcc.Graph(
                figure = go.Figure(data=[go.Pie(labels=df['Moneda'], values=df.index, hole=0.3)],
                                   layout = go.Layout(
                                       title='Tipo de Moneda',
                                       margin=dict(
                                           l=50,
                                           r=50,
                                           b=50,
                                           t=50
                                           ),
                                       annotations=[dict(text='Total:\n2180MXN, \n235 USD', x=0.5, y=-0.1, font_size=20, showarrow=False)]
                                       )
                                   )
            )
        ])
    if tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2'),
            dcc.Graph(
                figure = go.Figure(data=[go.Pie(labels=df['Producto'], values=df.index)])
            )
        ])
    if tab == 'tab-3':
        return html.Div([
            html.H3('Tab content 3'),
            dcc.Graph(
                figure = go.Figure(data=[go.Pie(labels=df['Cliente'], values=df['Saldo insoluto actual'])])
                )
        ])
    if tab == 'tab-4':
        return html.Div([
            html.H3('Tab content 4'),
            dcc.Graph(
                figure = go.Figure(data=[go.Pie(labels=df['Fondeador'], values=df.index)])
                )
        ])
    if tab == 'tab-5':
        return html.Div([
            html.H3('Tab content 5'),
            dcc.Graph(
                figure = go.Figure(data=[go.Pie(labels=df['Admin. de ingresos'], values=df.index)])
                )
        ])
    if tab == 'tab-6':
        return html.Div([
            html.H3('Tab content 6'),
            dcc.Graph(
                figure = go.Figure(data=[go.Pie(labels=df['Cliente'], values=df['Monto del contrato'])])
                )
        ])
    elif tab == 'tab-7':
        return html.Div([
            html.H3('Tab content 7'),
            dcc.Graph(
                figure = go.Figure(data=[go.Pie(labels=df['Cliente'], values=df['Cobranza mínima requerida'])])    

            )
        ])
    
if __name__ == '__main__':
    app.run_server(debug=True)
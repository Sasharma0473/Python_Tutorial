import numpy as np
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

external_stylesheets = [
    {
        "href": "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css",
        "rel": "stylesheet",
        "integrity": "sha384-MakUpkW+CY5fAdyg0crU2mG+WZ1KCIAtKW+3QtFSoU0XsI9yMzLRh+xtgFq3HlF4",
        "crossorigin": "anonymous"
    }
]

patient_data = pd.read_csv('IndividualDetails.csv')
total_patient = patient_data.shape[0]
active_patients = patient_data[patient_data['current_status']=='Hospitalized'].shape[0]
recovered_patients = patient_data[patient_data['current_status']=='Recovered'].shape[0]
death_patients = patient_data[patient_data['current_status']=='Deceased'].shape[0]

options = [
    {'label':'All','value':'All'},
    {'label':'Hospitalized','value':'Hospitalized'},
    {'label':'Recovered','value':'Recovered'},
    {'label':'Deceased','value':'Deceased'}
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1(children="Corona Virus Pandemic", style={"color": "White", "text-align": "center"}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H2("Total Cases", className='text-light'),
                    html.H3(total_patient, className='text-light')
                ], className='card-body', style={"color": "Black"})
            ], className='card', style={"backgroundColor": "gray", "border": "2px solid Black"})
        ], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H2("Active Cases", className='text-light'),
                    html.H3(active_patients, className='text-light')
                ], className='card-body', style={"color": "Black"})
            ], className='card', style={"backgroundColor": "Red", "border": "2px solid Black"})
        ], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H2("Total Recovered", className='text-light'),
                    html.H3(recovered_patients, className='text-light')
                ], className='card-body', style={"color": "Black"})
            ], className='card', style={"backgroundColor": "Green", "border": "2px solid Black"})
        ], className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H2("Death Cases", className='text-light'),
                    html.H3(death_patients, className='text-light')
                ], className='card-body', style={"color": "Black"})
            ], className='card', style={"backgroundColor": "Yellow", "border": "3px solid Black"})
        ], className='col-md-3')
    ], className='row'),
    
    # Two More Graphs need to plot but could not able to find the problem statement for that need to as somebody.
    html.Div([
        html.Div([],className='col-md-6'),
        html.Div([],className='col-md-6')
        ],className='row'),
    
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='picker',options=options,value='All'),
                    dcc.Graph(id='bar')
                ],className='card-body')
            ],className='card')
        ],className='col-md-12')
    ],className="row")
    
], className='container')

@app.callback(Output('bar','figure'),[Input('picker','value')])
def update_graph(type):
    if type == 'All':
        pbar = patient_data['detected_state'].value_counts().reset_index()
        return {'data':[go.Bar(x=pbar['detected_state'], y = pbar['count'])],
                'layout':go.Layout(title='State Total Count')}
    else:
        npat = patient_data[patient_data['current_status']==type]
        pbar = npat['detected_state'].value_counts().reset_index()
        return {'data':[go.Bar(x=pbar['detected_state'], y = pbar['count'])],
                'layout':go.Layout(title='State Total Count')}

if __name__ == '__main__':
    app.run_server(debug=True, port=5000)

import json

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import numpy as np
from numpy import linalg as LA
from numpy import cos, sin, pi

import plotly as py
import plotly.graph_objects as go
from Helper import Rx, Ry, Rz


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
def create_sphere(r=1, x_c=0, y_c=0, z_c=0, N=100):
    #just a sphere
    theta = np.linspace(0,2*pi,N)
    phi = np.linspace(0,pi,N)
    x = r*np.outer(cos(theta),sin(phi))
    y = r*np.outer(sin(theta),sin(phi))
    z = r*np.outer(np.ones(N),cos(phi))  # note this is 2d now

    trace = go.Surface(z=z, x=x, y=y)

    return trace

def create_ellipse(a, b, R, x_c=0, y_c=0, z_c=0,  N=100):
    y_c -= a-b
    t = np.linspace(0, 2*pi, N)
    xs = a * cos(t) + x_c
    ys = b * sin(t) + y_c
    zs = np.zeros(N) + z_c
    # coordinate of the  ellipse points with respect to the system of axes [1, 0], [0,1] with origin (0,0)
    xp, yp, zp = np.dot(R, [xs, ys, zs])
    x = [x for x in np.array(xp).flat]
    y = [y for y in np.array(yp).flat]
    z = [z for z in np.array(zp).flat]
    trace = go.Scatter3d(x=x, y=y, z=z, mode='lines')
    return trace
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}
rot = LA.multi_dot([Rx(0), Ry(pi/4), Rz(pi/4)])
#rot = LA.multi_dot([Rx(0), Ry(0), Rz(0)])

traces = [
    create_ellipse(a=2, b=4, R = rot),
    create_sphere()
]
layout = go.Layout(title='Orbit', autosize=False,
          width=1000, height=1000,
          margin=dict(l=65, r=50, b=65, t=90))

app.layout = html.Div([

    dcc.Graph(
        id='orbit',
        figure = {
            "data": traces,
            "layout": layout
        }
    ),

])

if __name__ == '__main__':
    app.run_server(debug=True)
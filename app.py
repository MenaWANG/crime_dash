import pandas as pd
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

data_path = 'data/Data_Tables_LGA_Criminal_Incidents_Year_Ending_March_2023.xlsx'
df = pd.read_excel(data_path, sheet_name = 'Table 01')
df['LGA'] = df['Local Government Area']
df['LGA'] = df['LGA'].str.strip()
df['Incidents_Rate'] = round(df['Rate per 100,000 population'],2)
wanted_fields = ['Year', 'LGA', 'Incidents_Rate']
df = df[wanted_fields]
df = df.drop_duplicates()

df2 = pd.read_excel(data_path, sheet_name = 'Table 02' )
df2['LGA'] = df2['Local Government Area']
df2['LGA'] = df2['LGA'].str.strip()
df2['Offence_Division'] = df2['Offence_Division'].str.strip()
df2['LGA_Population'] = 100000 * df2['Incidents_Recorded']/df2['LGA Rate per 100,000 population']
df2['Division_Incidents'] = df2.groupby(['Year', 'LGA', 'Offence_Division'])['Incidents_Recorded'].transform('sum')
df2['Division_Incidents_Rate'] = round(100000* df2['Division_Incidents']/df2['LGA_Population'])
wanted_fields_2 = ['Year', 'LGA', 'Offence_Division', 'Division_Incidents_Rate']
df2 = df2[wanted_fields_2]
df2 = df2.drop_duplicates()

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the Dash app
app.layout = html.Div([
    html.Meta(
        name='viewport',
        content='width=device-width, initial-scale=1.0'
    ),
    html.Link(
        rel='stylesheet',
        href='styles/custom.css'  # Specify the path to your CSS file
    ),
    html.Div([
        html.H1("Incident Rates over Years by LGA"),
        dcc.Dropdown(
            className="my-dropdown",
            id='lga-dropdown',
            options=[{'label': lga, 'value': lga} for lga in df['LGA'].unique() if lga != "Total"],
            value=df['LGA'].unique()[0:1],
            multi=True,
        ),
        dcc.Graph(id='lga-incident-graph')
    ]),
    html.Div([
        html.H1("Incident Rates over Years by Offence Division"),
        dcc.Dropdown(
            className = "my-dropdown",
            id='offence-division-dropdown',
            options=[{'label': offence, 'value': offence} for offence in df2['Offence_Division'].unique()],
            value = df2['Offence_Division'].unique()[0],
        ),
        dcc.Graph(id='division-incident-graph')
    ])
])

# Define the callback function to update the graph based on the dropdown value
@app.callback(
    Output('lga-incident-graph', 'figure'),
    Input('lga-dropdown', 'value')
)
def update_graph(selected_lga):
    filtered_df = df[df['LGA'].isin(selected_lga)]
    fig = px.line(filtered_df, x='Year', y='Incidents_Rate', color='LGA')
    fig.update_layout(
        yaxis_title = "Rate per 100K population",
        template = "plotly_dark",
        xaxis_title = "",
        margin = dict(b=0)
        )
    return fig

@app.callback(
    Output('division-incident-graph', 'figure'),
    Input('lga-dropdown', 'value'),
    Input('offence-division-dropdown', 'value')
)
def update_graph(selected_lga, selected_division):
    filtered_df = df2[df2['LGA'].isin(selected_lga)]
    filtered_df = filtered_df[filtered_df['Offence_Division']==selected_division]
    fig = px.line(filtered_df, x='Year', y='Division_Incidents_Rate', color='LGA')
    fig.update_layout(
        yaxis_title = "Rate per 100K population",
        template = "plotly_dark",
        xaxis_title = "",
        margin = dict(b=0)
        )
    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
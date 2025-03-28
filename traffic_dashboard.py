import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import mysql.connector
import pandas as pd
import plotly.express as px

# Connect to MySQL
def fetch_data():
    db = mysql.connector.connect(
        host="localhost", user="root", password="venkataganesh", database="TrafficDB"
    )
    try:
        df = pd.read_sql("SELECT * FROM TrafficLogs ORDER BY timestamp DESC", db)
        db.close()
        return df
    except Exception as e:
        print(f"Database Error: {e}")
        return pd.DataFrame()

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("🚦 Traffic Signal Agent Dashboard"),
    
    # Auto-refresh every 5 seconds
    dcc.Interval(id='interval-component', interval=5000, n_intervals=0),
    
    # Table
    html.H3("📋 Traffic Logs"),
    html.Div(id='traffic-log-table'),
    
    # Bar Chart
    html.H3("📊 Tasks Assigned to Subagents"),
    dcc.Graph(id='bar-chart'),

    # Pie Chart
    html.H3("📌 Task Distribution"),
    dcc.Graph(id='pie-chart')
])

@app.callback(
    [Output('traffic-log-table', 'children'),
     Output('bar-chart', 'figure'),
     Output('pie-chart', 'figure')],
    Input('interval-component', 'n_intervals')
)
def update_dashboard(n):
    df = fetch_data()

    # If DataFrame is empty, return a message
    if df.empty:
        return html.P("No data available. Check MySQL connection."), {}, {}

    # Generate Bar Chart
    bar_fig = px.bar(df, x="agent_name", title="Tasks Assigned to Subagents", color="agent_name")

    # Generate Pie Chart
    pie_fig = px.pie(df, names="agent_name", title="Task Distribution")

    # Generate Table
    table = html.Table([
        html.Tr([html.Th(col) for col in df.columns])] + 
        [html.Tr([html.Td(str(df.iloc[i][col])) for col in df.columns]) for i in range(len(df))]
    )

    return table, bar_fig, pie_fig

if __name__ == '__main__':
    app.run_server(debug=True)

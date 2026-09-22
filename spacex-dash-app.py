from pathlib import Path

import dash
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Input, Output, dcc, html

DATA_PATH = Path(__file__).resolve().parent / "spacex_launch_dash.csv"
spacex_df = pd.read_csv(DATA_PATH)

if spacex_df.columns[0].startswith("Unnamed") or spacex_df.columns[0] == "":
    spacex_df = spacex_df.drop(columns=spacex_df.columns[0])

spacex_df["Landing Outcome"] = spacex_df["class"].map(
    {1: "Successful landing", 0: "Unsuccessful landing"}
)

min_payload = int(spacex_df["Payload Mass (kg)"].min())
max_payload = int(spacex_df["Payload Mass (kg)"].max())
payload_step = 250
payload_marks = {
    value: f"{value:,}"
    for value in range(min_payload, max_payload + 1, 2000)
}
payload_marks[max_payload] = f"{max_payload:,}"

app = dash.Dash(__name__)
app.title = "SpaceX Launch Dashboard"
server = app.server

SUCCESS_COLORS = {
    "Successful landing": "#2ca02c",
    "Unsuccessful landing": "#d62728",
}


def empty_figure(title: str, message: str) -> go.Figure:
    fig = go.Figure()
    fig.update_layout(
        title=title,
        xaxis={"visible": False},
        yaxis={"visible": False},
        annotations=[
            {
                "text": message,
                "xref": "paper",
                "yref": "paper",
                "x": 0.5,
                "y": 0.5,
                "showarrow": False,
                "font": {"size": 16},
            }
        ],
        margin={"l": 40, "r": 40, "t": 80, "b": 40},
    )
    return fig


app.layout = html.Div(
    children=[
        html.H1(
            "SpaceX Falcon 9 Landing Outcomes",
            style={"textAlign": "center", "color": "#1f2937", "fontSize": 38},
        ),
        html.P(
            "Explore how launch site and payload mass relate to first-stage landing success.",
            style={"textAlign": "center", "maxWidth": "900px", "margin": "0 auto 1.5rem"},
        ),
        html.Label("Launch site", htmlFor="site-dropdown"),
        dcc.Dropdown(
            id="site-dropdown",
            options=[{"label": "All launch sites", "value": "ALL"}]
            + [
                {"label": site, "value": site}
                for site in sorted(spacex_df["Launch Site"].unique())
            ],
            value="ALL",
            placeholder="Select a launch site",
            searchable=True,
            clearable=False,
        ),
        html.Br(),
        html.Div(dcc.Graph(id="success-pie-chart")),
        html.Br(),
        html.Label("Payload range (kg)", htmlFor="payload-slider"),
        dcc.RangeSlider(
            id="payload-slider",
            min=min_payload,
            max=max_payload,
            step=payload_step,
            marks=payload_marks,
            value=[min_payload, max_payload],
            tooltip={"placement": "bottom", "always_visible": False},
        ),
        html.Div(dcc.Graph(id="success-payload-scatter-chart")),
    ],
    style={"maxWidth": "1100px", "margin": "0 auto", "padding": "1.5rem"},
)


@app.callback(
    Output(component_id="success-pie-chart", component_property="figure"),
    Input(component_id="site-dropdown", component_property="value"),
)
def get_pie_chart(entered_site: str):
    if entered_site == "ALL":
        success_by_site = (
            spacex_df.groupby("Launch Site", as_index=False)["class"]
            .sum()
            .rename(columns={"class": "Successful landings"})
        )
        return px.pie(
            success_by_site,
            values="Successful landings",
            names="Launch Site",
            title="Successful booster landings by launch site",
        )

    filtered_df = spacex_df[spacex_df["Launch Site"] == entered_site]
    if filtered_df.empty:
        return empty_figure(
            f"Landing outcomes for {entered_site}",
            "No launches are available for the selected site.",
        )

    outcome_counts = (
        filtered_df["Landing Outcome"]
        .value_counts()
        .rename_axis("Landing Outcome")
        .reset_index(name="Count")
    )
    return px.pie(
        outcome_counts,
        values="Count",
        names="Landing Outcome",
        title=f"Landing outcomes for {entered_site}",
        color="Landing Outcome",
        color_discrete_map=SUCCESS_COLORS,
    )


@app.callback(
    Output(component_id="success-payload-scatter-chart", component_property="figure"),
    [
        Input(component_id="site-dropdown", component_property="value"),
        Input(component_id="payload-slider", component_property="value"),
    ],
)
def get_scatter_chart(entered_site: str, payload_range):
    low, high = payload_range
    filtered_df = spacex_df[
        (spacex_df["Payload Mass (kg)"] >= low)
        & (spacex_df["Payload Mass (kg)"] <= high)
    ]

    title = "Payload mass vs. landing outcome"
    if entered_site != "ALL":
        filtered_df = filtered_df[filtered_df["Launch Site"] == entered_site]
        title = f"Payload mass vs. landing outcome for {entered_site}"
    else:
        title = "Payload mass vs. landing outcome across all launch sites"

    if filtered_df.empty:
        return empty_figure(
            title,
            "No launches match the selected launch site and payload range.",
        )

    fig = px.scatter(
        filtered_df,
        x="Payload Mass (kg)",
        y="Landing Outcome",
        color="Booster Version Category",
        hover_data=["Launch Site", "Booster Version", "Flight Number"],
        title=title,
        labels={
            "Payload Mass (kg)": "Payload mass (kg)",
            "Landing Outcome": "Landing outcome",
            "Booster Version Category": "Booster category",
        },
        category_orders={
            "Landing Outcome": ["Unsuccessful landing", "Successful landing"]
        },
    )
    fig.update_layout(legend_title_text="Booster category")
    return fig


if __name__ == "__main__":
    app.run()

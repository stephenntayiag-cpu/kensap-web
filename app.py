import os
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Initialize app with bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX], suppress_callback_exceptions=True)
app.title = "KenSAP"
server = app.server  # ✅ Expose Flask server for Render

# App layout
app.layout = html.Div([
    dbc.NavbarSimple(
        brand="KenSAP Organization",
        color="#C32148",
        dark=True,
        children=[
            dbc.NavItem(dbc.NavLink("Home", href="/")),
            dbc.NavItem(dbc.NavLink("About KenSAP", href="/About-KenSAP")),
            dbc.NavItem(dbc.NavLink("Alum", href="/Alum")),
            dbc.NavItem(dbc.NavLink("News", href="/News")),
            dbc.NavItem(dbc.NavLink("Contact", href="/Contact")),
        ]
    ),
    html.Div([
        html.Div([
            html.H1("KenSAP", style={'color': 'white', 'fontSize': '20px'}),
            html.H4("Empowering Kenya’s Brightest Minds for Global Impact",
                    style={'color': 'white', 'fontSize': '15px'}),
            dbc.Button("Learn More", color="secondary", href="/About-KenSAP", style={'marginTop': '10px'})
        ], style={'textAlign': 'center', 'padding': '5px'}),
        dcc.Location(id='url', refresh=False),
    ], style={'backgroundColor': '#C32148', 'marginBottom': '20px'}),
    html.Div(id='page-content'),
    html.Footer([
        html.Hr(),
        html.P("© 2025 KenSAP | Designed by Stephen Ntayia",
               style={'textAlign': 'center', 'color': 'gray', 'fontSize': '14px', 'marginBottom': '20px'})
    ], style={'width': '100%', 'backgroundColor': '#f9f9f9', 'padding': '10px 0'})
])

# Callback for page routing
@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/About-KenSAP':
        return html.Div([
            html.H2("Welcome to KenSAP", style={'textAlign': 'center', 'color': "#C0154B"}),
            html.P("KenSAP is an organization that helps students from economically disadvantaged families to access education in US colleges. It started 2014 and has since helped 320 students",
                   style={'fontSize': '18px', 'padding': '20px', 'lineHeight': '1.8'}),
            html.H4("Examples Of schools attended", style={'marginTop': '30px', 'color': "#C0154B"}),
            html.P(["Dartmouth", html.Br(), "Princeton", html.Br(), "Harvard", html.Br(), "MIT"],
                   style={'fontSize': '20px', 'padding': '20px', 'lineHeight': '1.8'}),
            html.H3("Students", style={'marginTop': '30px', 'color': "#C0154B"}),
            html.P(["Steven Ntayia", html.Br(), "Brenda Wairimu", html.Br(), "Valentine Chelangat"],
                   style={'fontSize': '20px', 'padding': '20px', 'lineHeight': '1.8', 'color': 'black'})
        ])
    elif pathname == '/Alum':
        return html.Div([
            html.H2("KenSAP Alum", style={'textAlign': 'center', 'color': "#C0154B"}),
            html.P([
                "1. Steven Ntayia", html.Br(),
                "2. Pishel Odhiambo", html.Br(),
                "3. Valentine Chelangat", html.Br(),
                "4. Brenda Wairumi", html.Br(),
                "5. Steven Otieno", html.Br(),
                "6. Gabriel Papai", html.Br(),
                "7. Mary Wambui", html.Br(),
                "8. Elvis Kipkoo", html.Br(),
                "9. Faith Achieng", html.Br(),
                "10. Brian Mwangi", html.Br(),
                "11. Sharon Wanjiru"
            ], style={'fontSize': '18px', 'padding': '20px', 'lineHeight': '1.8', 'color': 'black'})
        ])
    elif pathname == '/News':
        return html.Div([
            html.H4("Latest KenSAP News", style={'textAlign': 'center', 'color': "#C0154B"}),
            html.P(
                "The program recently hosted its 6th annual fundraising gala on May 21 2025 at the Ole Sereni Hotel in Nairobi, aiming to boost resources for its work placing talented, under-resourced Kenyan high-school graduates into elite North American universities. "
                "The gala is pivotal for KenSAP’s operations—raising around 20–90% of the organisation’s annual budget—with the event featuring alumni sharing their journeys and an auction of high-value donated items.",
                style={'fontSize': '18px', 'padding': '20px', 'lineHeight': '1.8', 'color': 'black'})
        ])
    elif pathname == '/Contact':
        return html.Div([
            html.H4("Contact KenSAP Personnel in case of any question",
                    style={'textAlign': 'center', 'color': "#C0154B"}),
            html.P([
                "KenSAP Office : info@kensap.org", html.Br(),
                "Executive Director (public contact) : director@kensap.org", html.Br(),
                "KenSAP Alumni Network : alumni@kensap.org", html.Br(),
                "KenSAP Official Website : https://kensap.org", html.Br(),
                "KenSAP LinkedIn Page : https://www.linkedin.com/company/kensap"
            ], style={'fontSize': '18px', 'padding': '20px', 'lineHeight': '1.8', 'color': 'black'})
        ])
    else:
        return html.Div([
            html.H4("KenSAP HOME", style={'textAlign': 'center', 'color': "#C0154B"}),
            html.P(
                "The Kenya Scholar Access Program (KenSAP) is a non-profit initiative that identifies, prepares, and connects exceptional Kenyan students from underprivileged backgrounds with educational opportunities at some of the world’s leading universities, primarily in North America. Since its founding in 2004, KenSAP has transformed the lives of hundreds of scholars who have gone on to study at prestigious institutions such as Harvard, Yale, Princeton, MIT, and Stanford.",
                style={'fontSize': '18px', 'padding': '20px', 'lineHeight': '2.0', 'color': 'black'}),
            html.P(
                "Beyond college placement, KenSAP continues to support its alumni network — a vibrant community of leaders, innovators, and changemakers contributing to Kenya’s growth and global development. The program remains fully funded through philanthropy and annual fundraising efforts, ensuring equal access for students regardless of their financial background.",
                style={'fontSize': '18px', 'padding': '20px', 'lineHeight': '1.8', 'color': 'black'}),
            html.H5("“Empowering Kenya’s Brightest Minds for Global Impact.”",
                    style={'textAlign': 'center', 'color': '#C0154B', 'fontStyle': 'italic', 'marginTop': '25px'})
        ])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run_server(debug=False, host="0.0.0.0", port=port)

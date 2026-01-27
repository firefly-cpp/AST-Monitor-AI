from flask import Flask, render_template_string, redirect
from dash import Dash, html, dcc
import plotly.express as px
import os
from packages.trendboard.trendboard.ASTTCXReader import ASTTCXReader

def create_flask_server() -> Flask:
    server = Flask(__name__)

    @server.get("/")
    def idx():
        return redirect("/dash/")

    # @server.get("/idx")
    # def index():
    #     return render_template_string("""
    #     <h1>Flask Home</h1>
    #     <p><a href="/dash/">Go to Dash</a></p>
    #     """)

    return server

def create_dash_app(server: Flask) -> Dash:
    dash_app = Dash(
        __name__,
        server=server,
        url_base_pathname="/dash/",
        suppress_callback_exceptions=True,
    )

    dirname = os.path.dirname(__file__)
    print(dirname)
    directory_name = os.path.join(dirname, 'scripts', 'tcx_path')    
    reader = ASTTCXReader(directory_name)

    fig1, fig2, fig3, fig4 = reader.build_dashboard()

    # df = px.data.iris()
    # fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

    dash_app.layout = html.Div(
        style={"maxWidth": 900, "margin": "40px auto", "fontFamily": "system-ui"},
        children=[
            html.H2("Dash inside Flask"),
            html.P("This Dash app is mounted at /dash/ and shares the same Flask server."),
            dcc.Graph(figure=fig1),
            dcc.Graph(figure=fig2),
            dcc.Graph(figure=fig3),
            dcc.Graph(figure=fig4),
            html.Hr(),
            # html.A("Back to Flask home", href="/"),
        ],
    )

    return dash_app

server = create_flask_server()
dash_app = create_dash_app(server)

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000, debug=True)
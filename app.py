import os
from dash import Dash, html, dcc, Input, Output, State  # Correctly import State here
from openai import OpenAI

# Initialize the Dash application
app = Dash(__name__)

# Layout of the application
app.layout = html.Div([
    html.H1("Interact with GPT"),
    dcc.Textarea(
        id='user-input',
        style={'width': '100%', 'height': 100},
        placeholder="Type your question here..."
    ),
    html.Button('Submit', id='submit-button', n_clicks=0),
    html.Div(id='gpt-response', style={'white-space': 'pre-line'})
])

# Function to query GPT
def ask_gpt(question):
    client = OpenAI()
    
    try:
        completion = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [{"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": question}]
        )

        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {e}"


# Callback to handle the button click
@app.callback(
    Output('gpt-response', 'children'),  # Specifies where to output data
    [Input('submit-button', 'n_clicks')],  # Specifies the input that triggers the callback
    [State('user-input', 'value')]  # The state, additional data for the callback
)
def update_output(n_clicks, value):
    if n_clicks > 0:
        return ask_gpt(value)
    else:
        return "Your GPT response will appear here."

# Main function to run the server
if __name__ == '__main__':
    app.run_server(debug=True)

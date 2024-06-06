from flask import Flask, request, jsonify, render_template
from services.gpt_service import GPTService

app = Flask(__name__)

# Initialize GPTService
gpt_service = GPTService()

@app.route('/')
def home():
    return "Welcome to Diamond Jack!"

@app.route('/ask', methods=['GET', 'POST'])
def ask():
    if request.method == 'POST':
        input_text = request.form.get('input_text')
        if not input_text:
            return jsonify({"error": "No input_text provided"}), 400
        
        response = gpt_service.get_structured_response(input_text)
        return render_template('response.html', input_text=input_text, response=response)
    
    return render_template('ask.html')

@app.route('/api/ask', methods=['POST'])
def api_ask():
    data = request.json
    input_text = data.get('input_text')
    if not input_text:
        return jsonify({"error": "No input_text provided"}), 400
    
    response = gpt_service.get_structured_response(input_text)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)

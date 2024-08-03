from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/generate_code', methods=['POST'])
def generate_code():
    data = request.json
    component_description = data.get('componentDescription')
    
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=f"Generate Streamlit code for the following component: {component_description}",
        max_tokens=150
    )
    
    return jsonify({"code": response.choices[0].text})

@app.route('/modify_code', methods=['POST'])
def modify_code():
    data = request.json
    existing_code = data.get('existingCode')
    requirements = data.get('requirements')
    
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=f"Modify the following Streamlit code: {existing_code}\nTo meet these requirements: {requirements}",
        max_tokens=150
    )
    
    return jsonify({"code": response.choices[0].text})

if __name__ == '__main__':
    app.run(debug=True)

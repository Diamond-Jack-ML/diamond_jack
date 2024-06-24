import openai
import os

class GPTService:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        print(f"Using OpenAI API Key: {self.api_key}")  # Debugging line
        openai.api_key = self.api_key

    def get_structured_response(self, input_text, user_role):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"{user_role}:\n{input_text}"}
            ]
        )
        return response['choices'][0]['message']['content'].strip()

# Usage
if __name__ == "__main__":
    gpt_service = GPTService()
    input_text = "Describe the core values of Diamond Jack."
    structured_response = gpt_service.get_structured_response(input_text)
    print(structured_response)

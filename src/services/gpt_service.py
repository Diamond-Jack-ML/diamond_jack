import openai
import os

class GPTService:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        openai.api_key = self.api_key

    def get_structured_response(self, input_text):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Convert the following input into a conceptual and logical data model:\n{input_text}",
            max_tokens=150
        )
        return response.choices[0].text.strip()

# Usage
if __name__ == "__main__":
    gpt_service = GPTService()
    input_text = "Describe the core values of Diamond Jack."
    structured_response = gpt_service.get_structured_response(input_text)
    print(structured_response)

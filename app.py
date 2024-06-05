from langchain import OpenAI, PromptTemplate, LLMChain

# Initialize OpenAI with your API key
openai = OpenAI(api_key='your-openai-api-key')

# Define a prompt template
prompt_template = PromptTemplate(
    input_variables=["input_text"],
    template="Convert the following input into a conceptual and logical data model:\n{input_text}"
)

# Create an LLMChain instance
llm_chain = LLMChain(llm=openai, prompt_template=prompt_template)

# Function to get a structured response
def get_structured_response(input_text):
    response = llm_chain.run(input_text)
    return response

# Example usage
input_text = "Describe the core values of Diamond Jack."
structured_response = get_structured_response(input_text)
print(structured_response)

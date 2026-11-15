from model import llama_response, granite_response, mistral_response

def call_all_models(system_prompt, user_prompt):
    llama_result = llama_response(system_prompt, user_prompt)
    granite_result = granite_response(system_prompt, user_prompt)
    mistral_result = mistral_response(system_prompt, user_prompt)

    print("Llama Response:\n", llama_result)
    print("\nGranite Response:\n", granite_result)
    print("\nMistral Response:\n", mistral_result)

# Example call to test all models
system_prompt = """
You are a helpful technical support assistant.
Analyze the user's message and return a response using the required JSON format.
"""
user_prompt = """
I am completing the Develop Generative AI Applications: Get Started course
using the cloud-IDE tools. When I run my Python test script, I receive an
OutputParserException because the model returns plain text instead of the
JSON format required by JsonOutputParser. Please help me fix the issue.
"""
call_all_models(system_prompt, user_prompt)

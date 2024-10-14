from huggingface_hub import InferenceClient

# Initialize the client with your token
client = InferenceClient(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    token="your_huggingface_token"
)

# Function to take user input (a question) and answer based on a document's content
def ask_question_based_on_soc3(question, soc3_doc_text):
    # Define the user question and context for answering it based on the SOC 3 document
    context = (
        f"Based on the SOC 3 document, answer the following question.\n\n"
        f"SOC 3 Document Content:\n{soc3_doc_text}\n\n"
        f"Question:\n{question}\n\n"
        f"Answer:"
    )

    # Call the model with the context to generate an answer
    response = client.chat_completion(
        messages=[{"role": "user", "content": context}],
        max_tokens=300,  # Adjust max_tokens based on input length
        stream=False
    )

    return response.choices[0].message.content

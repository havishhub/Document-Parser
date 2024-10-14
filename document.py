from huggingface_hub import InferenceClient
import fitz  # PyMuPDF

# Initialize the client with your token
client = InferenceClient(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    token="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"
)

# Function to extract text from a PDF file (SOC 3 document)
def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as pdf:
        for page_num in range(len(pdf)):
            page = pdf.load_page(page_num)
            text += page.get_text()
    return text

# Function to truncate or summarize document text if it's too long
def truncate_text(text, max_length=6000):
    if len(text) > max_length:
        return text[:max_length] + "\n... [Truncated]"
    return text

# Path to the SOC 3 document
soc3_doc_path = r'C:\Users\santo\OneDrive\Documents\code\wipro\azure.pdf'

# Extract text from the SOC 3 document
soc3_doc_text = extract_text_from_pdf(soc3_doc_path)

# Truncate the document text if it's too long
soc3_doc_text = truncate_text(soc3_doc_text)

# Function to take user input (a question) and answer based on the SOC 3 document
def ask_question_based_on_soc3(question):
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
        max_tokens=300,  # Adjust max_tokens based on the input length
        stream=False,  # Set to True if you want streaming responses
    )

    # Extract and return the answer to the question
    return response.choices[0].message.content

# Example usage: Asking a question based on the SOC 3 document
user_question = "What is the name of the company?"
answer = ask_question_based_on_soc3(user_question)
print(answer)

user_question1 = "What is the document period?"
answer1 = ask_question_based_on_soc3(user_question1)
print(answer1)

user_question2 = "Who is the auditor?"
answer2 = ask_question_based_on_soc3(user_question2)
print(answer2)

user_question3 = "What is the signed date?"
answer3 = ask_question_based_on_soc3(user_question3)
print(answer3)

user_question4 = "What is the scope?"
answer4 = ask_question_based_on_soc3(user_question4)
print(answer4)

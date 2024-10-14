Wipro Internship Project: Document Parsing 
Project Overview
This project focuses on building an intelligent system for document parsing and speech recognition, leveraging advanced AI and machine learning techniques. The system extracts essential information such as signed dates, document scope, and auditors from complex documents (e.g., SOC 3 reports) and transcribes speech to text accurately.

Key Features
Document Parsing: Extracts key data from PDF documents using PyMuPDF and performs natural language understanding for accurate information retrieval.
Speech-to-Text: Developed a robust speech recognition system using a deep learning model to convert audio input to text seamlessly.
Question Answering: Utilizes an AI model to answer specific queries based on the extracted content from documents.
Tech Stack
Programming Language: Python
Libraries:
PyMuPDF for PDF text extraction
HuggingFace Transformers for language model integration
Tesseract for OCR (if required for image-based PDF parsing)
Frameworks:
Meta-LLaMA for question-answering tasks
PyTorch for speech-to-text tasks
Code Structure
PDF Text Extraction:

Extracts text from the uploaded SOC 3 PDF using PyMuPDF.
Handles document truncation for large files.
Question Answering:

Uses the Meta-Llama-3B model to answer questions about the document content.
Speech-to-Text Module:

Converts speech input into text format for further processing and understanding.

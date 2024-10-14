Wipro Internship Project - Document Parsing and Speech Recognition 📄🎤
This project aims to build an intelligent document parsing system with advanced AI techniques to extract relevant information from complex documents, such as SOC 3 reports, and seamlessly transcribe speech to text. It combines Natural Language Processing (NLP), deep learning, and AI models to enhance the process of document analysis and voice recognition.
🌟 Key Features
Document Parsing:
Extracts essential information from PDF documents, such as signed dates, document scope, and auditors.
Uses PyMuPDF for precise text extraction from SOC 3 reports and large documents.
Employs Natural Language Understanding (NLU) for semantic interpretation of complex data.
Speech-to-Text:
Converts speech input into text using a deep learning-based model.
Integrated with PyTorch for seamless transcription and recognition.
Question Answering:
Leverages the Meta-LLaMA-3B model to answer queries about the content extracted from the documents.
AI-driven question-answering system that dynamically responds based on the document's content.
🚀 Tech Stack
Programming Language: Python
Libraries:
PyMuPDF: For PDF text extraction from SOC 3 and other complex document types.
HuggingFace Transformers: For integrating language models for query-based document extraction.
Tesseract: OCR for image-based PDF parsing (if required).
Frameworks:
Meta-LLaMA: For question-answering tasks based on document content.
PyTorch: Used for training and deploying speech-to-text models.
📂 Code Structure
1. PDF Text Extraction:
Extracts text from complex documents like SOC 3 PDF files using PyMuPDF.
Handles document truncation for larger files to ensure complete and accurate extraction.
2. Question Answering:
The Meta-LLaMA-3B model is used to answer questions based on the content extracted from the documents.
Provides relevant and precise answers, aiding in faster document analysis.
3. Speech-to-Text Module:
Converts voice commands and audio input into text using PyTorch-based speech recognition models.
Improves accessibility and ease of interaction by allowing users to ask questions or query documents via voice.
🌐 Getting Started
Clone the Repository:
git clone https://github.com/havishhub/Document-Parser.git
Navigate to the Project Directory:
cd Document-Parsing-and-Speech-Recognition

pip install -r requirements.txt
Run the Project:

For Document Parsing:
python parse_documents.py
For Speech Recognition:
python speech_to_text.py
For Question Answering:
python question_answering.py

🎯 How It Works
1. Document Parsing:
PyMuPDF is used to extract text from large documents like SOC 3 reports. It ensures that the text is parsed accurately, even for documents with complicated layouts.
After extracting the content, NLP models process the text to identify and organize key information such as signed dates, scope of the document, and auditors.
2. Speech-to-Text Module:
A PyTorch-based deep learning model transcribes your voice commands or audio input into text for further processing.
This module also supports real-time speech recognition for dynamic interactions.
3. Question Answering:
Using Meta-LLaMA-3B model, the system can respond to specific questions based on the extracted content from the document. For example, asking "Who is the auditor?" or "What is the signed date?" will prompt the model to search the document and provide an accurate response.
🛠 Technologies Used
PyMuPDF: For extracting text from PDF documents.
HuggingFace Transformers: For language processing and question answering using the Meta-LLaMA-3B model.
PyTorch: For training and deploying the speech-to-text model.
Tesseract OCR: For optical character recognition (OCR) on image-based PDFs (if needed).
🤝 Contributing
Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-name).
Commit your changes (git commit -m 'Add new feature').
Push to your branch (git push origin feature-name).
Create a pull request.

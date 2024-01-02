# Text_Similarity_App
Overview
This Text Similarity Application is designed to measure the semantic similarity between two pieces of text. Built using advanced NLP techniques, it leverages the power of the BERT model to generate contextual text embeddings and compute similarity scores.

Features
Semantic Text Similarity: Utilizes a pre-trained BERT model to understand and compare the context and semantics of two different text inputs.
Interactive Web Interface: Deployed as a web application using Streamlit, offering a user-friendly interface for real-time text similarity assessments.
Deployed on Heroku: Easily accessible via a web browser without the need for local setup.

Installation
To run the application locally, follow these steps:

Clone the Repository:
bash
Copy code
git clone https://github.com/your-username/text_similarity_app.git
Navigate to the App Directory:
bash
Copy code
cd text_similarity_app

Install Dependencies:
bash
Copy code
pip install -r requirements.txt

Run the Application:
bash
Copy code
streamlit run app.py

Usage
After starting the app, navigate to http://localhost:8501 in your web browser. Enter two different texts in the provided text areas and click on the "Calculate Similarity" button to get the similarity score.

File Structure
app.py: The main Streamlit application file.
bert_model.py: Contains the code for the BERT model implementation.
requirements.txt: Lists all the Python dependencies.
Procfile: Used for Heroku deployment.
setup.sh: Configuration settings for Streamlit on Heroku.
Deployment
This application is deployed on Heroku and can be accessed at https://your-heroku-app-url.com. The deployment uses a standard Heroku setup with a Procfile and setup.sh.

License
This project is open-source and available under the MIT License.

Acknowledgements
Special thanks to the BERT authors and the Streamlit team for providing the tools and frameworks used in this project.


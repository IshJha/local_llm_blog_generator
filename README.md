**Blog Generation with Llama 2**

**Author: Ish Jha Contact info: ishjha1929@gmail.com / jha.13@alumni.iitj.ac.in (please feel free to contact for any doubts or collaborative projects ! )**

This project demonstrates how to create a blog post using an open-source LLM model (Llama 2) hosted on your local system. 
The application is built with Streamlit and leverages the CTransformers library to generate a blog post based on user input, including the title, word count, and target audience style.

**Features**

Blog Post Generation: Create a blog post based on a given title, word count, and target audience.
Customization: Choose the blog style for different audiences such as Researchers, Data Scientists, or General readers.
Local Model Hosting: Uses a Llama 2 model hosted locally to generate content.

**Requirements**
Python 3.x
streamlit
langchain
CTransformers

**Clone the repository:**
git clone https://github.com/IshJha/local_llm_blog_generator.git
cd blog-generation-llama

**Install the required Python packages:**

If using Pipfile:
pipenv install

**Download the Llama model:**

Obtain the .gguf file for the Llama model from Hugging Face or another source.
Save the model file in a directory on your local system.
Update the model path in the script:

Replace <path to .gguf file> in getLLamaresponse function with the path to your downloaded .gguf file.

**Run the Streamlit application:**

streamlit run app.py

**Project Structure**
app.py: The main Streamlit application script that provides the user interface for generating blog posts.

requirements.txt: Lists the Python dependencies required to run the project.

How It Works

User Input:

Enter the blog post title in the text input field.

Specify the number of words for the blog post.

Select the target audience for the blog from a dropdown menu.

**Blog Generation:**

Upon clicking the "Generate" button, the application calls the getLLamaresponse function.

This function formats the user input into a prompt and generates a blog post using the Llama 2 model.

Output Display:

The generated blog post is displayed on the Streamlit app.

**Example**

To generate a blog post about "Advancements in AI" targeted at "Data Scientists" with a word count of 500 words, enter:

Blog Post Title: Advancements in AI

No of Words: 500

Writing the Blog For: Data Scientist

Click "Generate" to receive a blog post on the specified topic and style.

**Extending to Other Models**

The example provided uses the Llama 2 model, but the application can be extended to other models if a .gguf file is available.

Update the model_type and model path in the CTransformers initialization accordingly.

**Author: Ish Jha Contact info: ishjha1929@gmail.com / jha.13@alumni.iitj.ac.in (please feel free to contact for any doubts or collaborative projects ! )**

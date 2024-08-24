import streamlit as st
from langchain.llms import CTransformers
from langchain.prompts import PromptTemplate


def getLLamaresponse(input_text,no_words,blog_style):
    llm=CTransformers(model=r"<path to .gguf file>",model_type='llama',config={"max_new_tokens":256,"temperature":0.4})
    template="""
  Write a blog post on {input_text} for {blog_style} and the word count is {no_words} words. Generate a interesting blog post.
  """
    prompt=PromptTemplate(template=template,input_variables=["input_text","blog_style","no_words"])
    output=llm(prompt.format(input_text=input_text,blog_style=blog_style,no_words=no_words))
    return output


st.set_page_config(page_title="Blog Generation with using Llama 2")
st.header("Generate Blogs")
input_text=st.text_input("Enter blog post title")
col1,col2=st.columns([5,5])
with col1:
    no_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox('Writing the blog for',
                            ('Researchers','Data Scientist','General'),index=0)
    
submit=st.button("Generate")

if submit:
  st.write(getLLamaresponse(input_text,no_words,blog_style))
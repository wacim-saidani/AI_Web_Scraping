from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from langchain_google_genai import ChatGoogleGenerativeAI
import os
os.environ["GOOGLE_API_KEY"] = ""
template=(
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
)

def parse_with_llm(batches,description):
    model =  ChatGoogleGenerativeAI(model="gemini-2.0-flash")

    prompt=ChatPromptTemplate.from_template(template)
    chain=prompt|model
    response=[]
    for chunk in batches:
        result=chain.invoke({"dom_content":chunk,"parse_description":description})
        response.append(result)
    return("\n".join(msg.content for msg in response))










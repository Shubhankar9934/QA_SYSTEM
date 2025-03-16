import streamlit as st
from QA_WithPDF.data_ingestion import load_data
from QA_WithPDF.embedding import download_gemini_embedding
from QA_WithPDF.model_api import load_model

    
def main():
    st.set_page_config("QA with Documents")
    
    doc=st.file_uploader("upload your document")
    
    st.header("QA with Documents(Information Retrieval)")
    
    user_question= st.text_input("Ask your question")
    
    if st.button("submit & process"):
        with st.spinner("Processing..."):
            document=load_data(doc)
            model=load_model()
            query_engine=download_gemini_embedding(model,document)
                
            response = query_engine.query(user_question)
                
            st.write(response.response)
                
                
if __name__=="__main__":
    main()          
                
    
    
    
    
    
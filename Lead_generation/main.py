import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from transformers import pipeline
from functions import *
pipe=pipeline("zero-shot-classification")

# Page configuration
st.set_page_config(
    page_title="Company Data Explorer",
    page_icon="📈",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #f0f9ff 0%, #cbebff 100%);
}
h1 {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    color: #0366d6;
}
.stButton>button {
    background-color: #0366d6;
    color: white;
    border-radius: 8px;
    padding: 0.6em 1.2em;
    font-size: 1rem;
    transition: background-color 0.3s ease;
}
.stButton>button:hover {
    background-color: #024da1;
}
</style>
""", unsafe_allow_html=True)

# App title
st.title("📊 LEAD GENERATION (SAASQUATCH)")
st.markdown("you can further enhance your generated leads from SaasQuatch here")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

def analyze_data(df: pd.DataFrame):
    """Dummy analysis function: returns industry counts."""
    counts = df['Industry'].value_counts().reset_index()
    counts.columns = ['Industry', 'Count']
    return counts

# Preview section
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")
        st.markdown("### Preview of Uploaded Data")
        st.dataframe(df.head(), use_container_width=True)
    except Exception as e:
        st.error(f"Failed to read CSV: {e}")

# Submit button
if st.button("Submit"):
    if uploaded_file is None:
        st.warning("Please upload a CSV file before submitting.")
    else:
        # Call the analysis function
        with st.spinner("Analyzing data..."):
            st.success("File successfully submitted.")
            list=list_generator(df) # Generate list of company names or websites
            result=link_generator(list) # Generate links and bodies from the list
            df['Website']=result[0]
            df['Body']=result[1]
            info=info_generator(result[0], result[1]) #extract information from the links
            preprocessed_info=preprocessor(info) # Preprocess the information
            classified_info=classifier(preprocessed_info) #information classification using LLM
            scores=score_calculator(classified_info) # Calculate lead scores
            df['Lead scores'] = scores
            
        st.success("Analysis complete!")
        st.write("Generated Results:")
        st.dataframe(df)
        # Display graph
        colors = plt.cm.Paired(range(len(df)))
        fig, axs = plt.subplots(1, 2, figsize=(16, 6),)

        axs[0].pie(df['Industry'].value_counts(), labels=df['Industry'].value_counts().index, autopct="%1.1f%%", startangle=140)
        axs[0].set_title("Pie Chart")

        axs[1].bar(df['Company'], df['Lead scores'], color=colors)
        axs[1].set_title("Lead Score")
        axs[1].set_xlabel('Company')
        axs[1].set_ylabel("scores")
        axs[1].tick_params(axis='x', rotation=45)
        with st.container(key='custom_container'):
            st.subheader("Visualizations")
            st.pyplot(fig, use_container_width=True)
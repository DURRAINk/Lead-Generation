# **🚀 Lead Generation App**

Supercharge your outreach with automated lead generation, using web scraping and cutting-edge LLMs.

  

# ✨ Features

**📥 CSV Upload**: Ingest your company lists (Company ∣ Industry ∣ Website).

**🕸️ Web Scraping**: Crawl target sites for rich context.

**🤖 LLM Intelligence**: Classify and score leads with zero-shot learning.

**📊 Interactive Visualization**: View pie & bar charts of industry distribution and lead quality.

**🎨 Stylish UI**: Modern gradient background, themed buttons, and responsive layout.

# 🚀 Quick Start

**Clone the repository**

    git clone https://github.com/DURRAINk/Lead-Generatoin.git
    cd Lead-Generatoin

**Create & activate a virtual environment**

    python3 -m venv venv
    source venv/bin/activate   # Linux/macOS
    venv\\Scripts\\activate  # Windows

**Install dependencies**

    pip install -r requirements.txt

**Run the Streamlit app**

    streamlit run app.py

**Open your browser** at http://localhost:8501 and start generating leads! 🙌

# 📁 Project Structure

    ├── README.md            # Project overview and setup instructions
    └── Lead_generation/       # Application folder
        ├── main.py          # Streamlit main application        
        ├── functions.py     # Scrapers, preprocessing, LLM wrappers    
        └── requirements.txt # Python dependencies


# 🛠️ Usage

1. Upload a CSV with columns: Company, Industry, Website. 

2. Preview your data in-app.

3. Click Submit to:

* Scrape each Website for context.

* Invoke the zero-shot classification pipeline.

* Compute a lead score for each company.

4. View detailed tables and dynamic charts under the Visualizations section.

# 🤝 Contributing

Feel free to open issues or pull requests! We welcome:

New chart types (scatter, line, maps)

Additional LLM models or hybrid approaches

CI/CD pipelines for automated deployments

# 📝 License

This project is licensed under the MIT License.



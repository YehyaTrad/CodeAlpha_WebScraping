# 🌐 Web Scraping Project – CodeAlpha Internship

## 📌 Project Overview
This project demonstrates **web scraping using Python** as part of the **CodeAlpha Data Analytics Internship**.  
The goal of the project is to extract structured data from a public website, clean it, and prepare it for further analysis.

The website used for this project is **books.toscrape.com**, a public site designed for practicing web scraping.

---

## 🛠️ Tools & Technologies Used
- 🐍 **Python**
- 🌐 **Requests** – for fetching web pages
- 🧩 **BeautifulSoup** – for parsing HTML content
- 📊 **Pandas** – for data handling and cleaning
- 🧹 **Regex (re)** – for cleaning text data

---

## 📂 Project Structure
```text
CodeAlpha_WebScraping
├── task1_web_scraping.py # Main Python script
├── books_raw_data.csv # Raw scraped dataset
├── books_cleaned_data.csv # Cleaned & processed dataset
├── requirements.txt # Required Python libraries
└── README.md # Project documentation
```

---

## 🔍 Data Collected
The following data fields were extracted from each book:
- 📘 **Title**
- 💰 **Price**
- 📦 **Stock Availability**

---

## ⚙️ Project Workflow
1. Send HTTP requests to fetch webpage content  
2. Parse HTML using BeautifulSoup  
3. Navigate website pagination to scrape multiple pages  
4. Extract relevant data fields  
5. Save raw data into a CSV file  
6. Clean data by:
   - Removing encoding issues
   - Converting prices to numeric format
   - Handling missing and duplicate values
7. Save cleaned data for analysis

---

## 📊 Output Files
- **books_raw_data.csv** → Unprocessed scraped data  
- **books_cleaned_data.csv** → Cleaned, analysis-ready dataset  

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 2️⃣ Run the script
```
python task1_web_scraping.py
```
## 👤 Author

Yehya Trad
Data Analytics Intern – CodeAlpha

🔗 GitHub Profile: https://github.com/YehyaTrad

🔗 LinkedIn Profile:https://www.linkedin.com/in/yehya-trad-690196327?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app


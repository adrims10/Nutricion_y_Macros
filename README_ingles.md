
# Project4 - Nutrition and Macros

![image](https://github.com/user-attachments/assets/8d0cb5a0-99b8-42df-a7a3-59b992f1da6e)

Welcome!

# *It’s a pleasure to have you here*


# 📝 Project Overview:

We envisioned individuals who need a price analysis and daily routines to start getting in shape. We are offering 4 simple tools to help them get started with nutrition and exercise, beginning from an introductory level.

# Project Goals:

Data Scraping: Extract product information from sports supplement pages to optimize athletic and nutritional performance, as well as fresh product details from Ahorra Mas's website.

Data Extraction from APIs: Obtain workout routines and fitness recipes from APIs.

Database Creation: Set up a database in Dbeaver named "Health."

Analyze prices, product reviews, discounts, and create customized routines and recipes.

# Data Analysis:


## 🗂️ Project Structure
We created an environment named "Webscraping" for this project.

        ├── notebooks/           # Jupyter Notebooks for data cleaning and visualization
                                  6.Exploration data file contains conclusions and graphics
        ├── src/                 # Function files
        ├─  Data                 # Data obtained during the study, in CSV and JSON format
        ├── README.md            # Project description
        ├── README_English version.md   # Project description in English
      
## 🛠️ Installation and Requirements
This project uses Python 3.12.6.
        

1. **requests** - [Requests Documentation](https://docs.python-requests.org/en/master/)
2. **json** - [JSON Documentation](https://docs.python.org/3/library/json.html)
3. **pandas** - [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
4. **sys** - [sys Documentation](https://docs.python.org/3/library/sys.html)
5. **os** - [os Documentation](https://docs.python.org/3/library/os.html)
6. **dotenv** - [Python-dotenv Documentation](https://saurabh-kumar.com/python-dotenv/)
7. **webdriver** - [Selenium WebDriver Documentation](https://www.selenium.dev/documentation/webdriver/)
8. **BeautifulSoup** - [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
9. **numpy** - [NumPy Documentation](https://numpy.org/doc/)
10. **psycopg2** - [Psycopg2 Documentation](https://www.psycopg.org/docs/)


Each link points to the official documentation for the corresponding library.

# 📝 Websites:

  Pontemasfuerte: https://www.pontemasfuerte.com Sports supplements website.
  
  Ahorramas: https://www.ahorramas.com/ Ahorra Mas website.
  
 # 📝 APIs:
 
   api-ninjas: API for exercise routines.
   
   tasty: API for recipes.
 
**Results and Conclusions**
We obtained 9,930 routines from the API.
We obtained 120 dynamic complete products from the website Fuertisimo.
We obtained 62 dynamic complete products from the Ahorra Mas website.
We obtained 30 complete recipes from the API.

The average price of sports supplements on this website is €37.63, covering all categories.
          -The average price of proteins is €55.70.
          -The average price of BCAAs is €26.694.
          -The average price of L-Carnitine is €17.74.
          -The average price of Creatine is €30.73.
          

The maximum price of sports supplements on this website is €123.6, covering all categories.
          -The maximum price of proteins is €123.6.
          -The maximum price of BCAAs is €38.1.
          -The maximum price of L-Carnitine is €18.15.
          -The maximum price of Creatine is €53.9.

As a conclusion, protein supplements are the most expensive category, also considering that they are most frequently used and come in larger formats.


In analyzing fresh products from Ahorra Mas, we found average prices around €10, maximum prices of €27, and minimum prices of €1.39, where legumes are present.
In this section, we observe an average coupon discount of 18.5%, so prices tend to drop significantly. (See comparative graphs in notebook 6.)


Using the APIs, we achieved a filter to obtain recipes by ingredient type, language, or serving size.
On the other hand, with the workout API, we obtained customized routines (with further database updates needed).
🌟

 
**Next Steps**

Introduction of routines directly from the API, including intermediate levels and more muscle groups.
Addition of more products, both supplements and fresh products from Ahorra Mas. With a click, we can increase the sample size, though expanding the dataset wasn't the primary goal of this project.
New recipe API, as the current one encountered issues.
Database expansion.

🏍️

![OIP](https://github.com/user-attachments/assets/a3261f22-9193-45df-bf33-14a396dfd988)


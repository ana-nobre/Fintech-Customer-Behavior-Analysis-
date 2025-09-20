## Project Overview (Work In Progress)

This project simulates real-world challenges faced by modern fintech companies such as Nubank, Wise, Inter, or Revolut. Using structured SQL queries, we explore and solve common operational and analytical problems related to customer engagement, credit risk, and system performance.

The goal is to demonstrate practical SQL skills applied to fintech operations, from customer lifecycle analysis to credit scoring, using realistic datasets and scenarios.

---

## Datasets Used

**Default of Credit Card Clients Dataset**  
Dataset from the UCI Machine Learning Repository (via Kaggle) containing demographic and financial information about customers, including their payment behavior and credit default status.  
🔗 https://www.kaggle.com/datasets/uciml/default-of-credit-card-clients-dataset

---

## Objective

To apply SQL for exploring and answering business-critical questions in a fintech environment, focusing on:

- App usage and user activity
- Customer engagement and churn
- Credit scoring and default risk
- Operational bottlenecks

---

## Database Structure

The datasets were adapted into relational tables and imported into a MySQL database. Key tables include:

- `customers`: general customer information
- `accounts`: account type and usage status
- `transactions`: transaction history by customer
- `loans`: loan applications and status
- `credit_scores`: credit risk levels and payment behavior

---

## Columns Description

- **ID** – Client identifier  
- **LIMIT_BAL** – Credit limit (NT dollars)  
- **SEX** – Gender (1 = male, 2 = female)  
- **EDUCATION** – Education level (1 = graduate school; 2 = university; 3 = high school; 4 = others; 0/5/6 = unknown)  
- **MARRIAGE** – Marital status (1 = married; 2 = single; 3 = others)  
- **AGE** – Client age (years)  
- **PAY_0 … PAY_6** – Repayment status for the last 6 months (-1 = pay duly; 1 = one month delay; up to 8 = eight months delay)  
- **BILL_AMT1 … BILL_AMT6** – Bill statement amounts for the last 6 months  
- **PAY_AMT1 … PAY_AMT6** – Amount of previous payments for the last 6 months  
- **default_payment_next_month** – Target variable (1 = default next month, 0 = no default)  

---

## Objective

To apply SQL and data exploration techniques to **business-critical questions in fintech**, focusing on:

- Customer engagement and churn  
- Credit scoring and default risk  
- Operational bottlenecks (repayment delays)  
- Risk segmentation  

---

## SQL Challenges

Each of the following questions is designed to simulate real operational analysis tasks in a fintech context. SQL was used to retrieve insights directly from the relational database.

**1. Identify the top 10% most active customers based on transaction frequency.**

**2. Calculate the average number of days between account creation and first transaction.**

**3. Determine the monthly churn rate (customers who stopped transacting) in the last 6 months.**

**4. Find the correlation between credit score and default status based on historical data.**

**5. Identify peak transaction hours to detect potential system overload periods.**

---

## Tools Used

- MySQL Workbench
- Jupyter Notebook (for SQL execution and documentation)
- pandas (for additional data exploration)
- Markdown (for documentation)

---

## Author

This project was developed as part of a personal portfolio, combining practical SQL challenges and business reasoning tailored to the fintech industry with real case scenarios relevant to fintechs such as Revolut, Nubank, Wave, Wise, and so on.


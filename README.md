# SaaS Business Analytics & Prediction Platform

A full-stack SaaS Analytics Platform built with **Python**, **Streamlit**, **Supabase**, and **Machine Learning** that helps businesses analyze customer behavior, predict churn, segment customers, monitor retention, and generate actionable insights through an interactive dashboard.

---

## Overview

Modern SaaS companies generate large volumes of customer and business data. Extracting meaningful insights from this data is often challenging and time-consuming.

This platform combines **Business Intelligence (BI)** and **Machine Learning (ML)** to provide a complete analytics solution that enables organizations to:

- Monitor business performance
- Analyze customer behavior
- Predict customer churn
- Segment customers intelligently
- Track retention trends
- Analyze custom datasets
- Generate data-driven business insights

---

## Features

### Authentication & User Management

- Email Registration
- Email Verification
- Email Login
- Google OAuth Authentication
- Session Management
- Secure Logout
- User Profile Management
- Supabase Authentication Integration

---

### Executive Dashboard

Key business metrics at a glance:

- Total Customers
- Active Customers
- Churn Rate
- Retention Rate
- Total Revenue
- Customer Lifetime Value (CLTV)

#### Interactive Visualizations

- Contract Distribution
- Revenue Distribution
- Churn Breakdown
- Customer Value Analysis

---

### Upload & Analyze Datasets

Upload and analyze:

- CSV Files
- Excel Files (`.xlsx`)

#### Automated Dataset Analysis

##### Dataset Summary

- Total Rows
- Total Columns
- Missing Values
- Duplicate Records

##### Data Exploration

- Dataset Preview
- Column Information
- Data Types
- Statistical Summary

##### Advanced Analytics

- Correlation Heatmap
- Distribution Analysis
- Missing Value Analysis
- Categorical Analysis
- Automated Insights

##### Export Results

- Download Processed Analytics Reports

---

### 🔮 Customer Churn Prediction

Machine Learning-powered churn prediction system.

#### Customer Information Inputs

- Demographics
- Contract Information
- Service Usage
- Billing Information
- Customer Lifetime Value

#### Prediction Outputs

- Churn Probability
- Retention Probability
- Risk Category

#### Smart Retention Recommendations

The platform automatically generates personalized retention strategies based on customer risk levels and behavioral patterns.

---

### 👥 Customer Analytics

Comprehensive customer intelligence dashboard.

#### Filters

- Contract Type
- Gender
- Internet Service
- Churn Status

#### Metrics

- Total Customers
- Active Customers
- Churned Customers
- Churn Rate
- Average CLTV

#### Visualizations

- Contract Distribution
- Churn Distribution
- Monthly Charges Distribution
- CLTV Distribution
- Revenue vs CLTV Analysis

#### Additional Features

- Customer Search
- Interactive Filtering
- Data Export

---

### 🎯 Customer Segmentation

Machine Learning-based customer clustering.

#### Techniques Used

- K-Means Clustering
- Feature Scaling
- Behavioral Segmentation

#### Customer Segments

- Budget Customers
- Premium Customers
- Loyal Customers

#### Segment Insights

- Segment Distribution
- Customer Value Analysis
- Segment Exploration
- Segmented Data Export

---

### 🔄 Retention Analysis

Analyze and monitor customer retention patterns.

#### Metrics

- Overall Retention Rate
- Churn Percentage
- Average Customer Tenure

#### Visualizations

- Retention by Tenure Group
- Churn by Tenure Group

#### Reports

- Retention Summary Tables
- Exportable Retention Reports

---

### User Profile

Display authenticated user details:

- Name
- Email
- Authentication Provider
- Account Status

---

##  System Architecture

```text
Frontend (Streamlit)
        │
        ▼
Authentication (Supabase Auth)
        │
        ▼
Backend Services
        │
        ▼
Supabase PostgreSQL Database
        │
        ▼
Analytics & Machine Learning Layer
        │
        ▼
Visualizations & Business Insights
```

---

##  Technology Stack

### Frontend

- Streamlit
- Plotly
- HTML/CSS

### Backend

- Python

### Database

- Supabase PostgreSQL

### Authentication

- Supabase Auth
- Google OAuth

### Machine Learning

- Scikit-Learn
- K-Means Clustering
- Churn Prediction Models

### Data Processing

- Pandas
- NumPy

### Visualization

- Plotly Express
- Plotly Graph Objects

---

##  Project Structure

```text
saas-analytics/
│
├── frontend/
│   ├── app.py
│   ├── pages/
│   ├── components/
│   └── auth/
│
├── backend/
│   ├── database.py
│   ├── services.py
│   ├── auth.py
│   └── supabase_client.py
│
├── ml/
│   ├── predict.py
│   ├── segmentation.py
│   ├── feature_engineering.py
│   ├── config.py
│   └── churn_model.pkl
│
├── assets/
├── requirements.txt
└── README.md
```

---

##  Machine Learning Pipeline

### Customer Churn Prediction

#### Input Features

- Gender
- Senior Citizen
- Partner
- Dependents
- Tenure Months
- Phone Service
- Multiple Lines
- Internet Service
- Online Security
- Online Backup
- Device Protection
- Tech Support
- Streaming TV
- Streaming Movies
- Contract Type
- Paperless Billing
- Payment Method
- Monthly Charges
- Total Charges
- CLTV

#### Feature Engineering

Generated Features:

- Revenue_Per_Month
- Long_Term_Customer
- High_Value_Customer
- Annual_Contract

#### Model Outputs

- Churn Probability
- Risk Classification
- Retention Recommendations

---

##  Security Features

- Secure User Authentication
- Google OAuth Integration
- Password-Based Authentication
- Session Management
- Protected Routes
- Secure Environment Variables

---

##  Business Value

This platform helps organizations:

- Reduce Customer Churn
- Improve Customer Retention
- Identify High-Value Customers
- Enhance Customer Engagement
- Support Data-Driven Decisions
- Monitor Business Performance
- Discover Customer Behavior Patterns

---

##  Installation

### 1️ Clone the Repository

```bash
git clone https://github.com/your-username/saas-analytics.git
cd saas-analytics
```

### 2️ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️ Configure Environment Variables

Create a `.env` file in the project root:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

### 4️ Run the Application

```bash
streamlit run frontend/app.py
```

---

##  Future Enhancements

- Revenue Forecasting
- Automated Report Generation
- PDF Export
- Real-Time Analytics
- Email Alerts
- Advanced User Roles & Permissions
- AI-Powered Business Insights
- Multi-Tenant SaaS Architecture

---

##  Learning Outcomes

This project demonstrates expertise in:

- Full-Stack Development
- SaaS Product Development
- Business Intelligence
- Data Analytics
- Machine Learning
- Customer Intelligence
- Authentication Systems
- Database Management
- Data Visualization

---

##  License

This project is intended for educational, research, and portfolio purposes.

---

##  Author

### Sumanth Manda

**SaaS Business Analytics & Prediction Platform**

Built using:

- Python
- Streamlit
- Supabase
- Machine Learning

---

⭐ If you found this project useful, consider giving it a star on GitHub!

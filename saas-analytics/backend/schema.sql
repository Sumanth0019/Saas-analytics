DROP TABLE IF EXISTS churn_predictions, transactions, subscriptions, customers, app_users CASCADE;

CREATE TABLE app_users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(120) UNIQUE,
    password VARCHAR(200),
    role VARCHAR(20) DEFAULT 'admin',
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(120),
    plan VARCHAR(20),
    signup_date DATE,
    status VARCHAR(20),
    monthly_charges NUMERIC(10,2),
    tenure INT,
    last_login_days INT,
    support_tickets INT,
    feature_adoption NUMERIC(4,2),
    payment_failures INT,
    contract_type VARCHAR(20),
    churned INT
);

CREATE TABLE subscriptions (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    plan VARCHAR(20),
    amount NUMERIC(10,2),
    start_date DATE,
    status VARCHAR(20)
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    amount NUMERIC(10,2),
    type VARCHAR(20),
    status VARCHAR(20),
    created_at TIMESTAMP
);

CREATE TABLE churn_predictions (
    id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    probability NUMERIC(5,3),
    risk_level VARCHAR(10),
    predicted_at TIMESTAMP DEFAULT NOW()
);
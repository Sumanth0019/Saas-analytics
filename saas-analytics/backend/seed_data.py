"""Creates schema and populates the database with realistic synthetic data."""
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from faker import Faker
from sqlalchemy import text
from backend.database import engine

fake = Faker()
random.seed(42)
np.random.seed(42)


def create_schema():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "schema.sql"), "r") as f:
        sql = f.read()
    with engine.begin() as conn:
        for stmt in sql.split(";"):
            if stmt.strip():
                conn.execute(text(stmt))
    print("✅ Schema created")


def generate_customers(n=500):
    plans = ["Basic", "Pro", "Enterprise"]
    plan_price = {"Basic": 29, "Pro": 99, "Enterprise": 299}
    contracts = ["Monthly", "Yearly"]
    rows = []
    for _ in range(n):
        plan = random.choices(plans, weights=[0.5, 0.35, 0.15])[0]
        tenure = random.randint(1, 48)
        last_login = random.randint(0, 60)
        tickets = int(np.random.poisson(2))
        adoption = round(random.uniform(0.1, 1.0), 2)
        pay_fail = int(np.random.poisson(0.5))
        contract = random.choices(contracts, weights=[0.6, 0.4])[0]

        churn_score = (
            (last_login / 60) * 0.4
            + (pay_fail / 5) * 0.25
            + (1 - adoption) * 0.25
            + (1 if contract == "Monthly" else 0) * 0.1
        )
        churned = 1 if (churn_score + random.uniform(-0.15, 0.15)) > 0.5 else 0
        status = "Churned" if churned else "Active"

        rows.append({
            "name": fake.name(),
            "email": fake.email(),
            "plan": plan,
            "signup_date": fake.date_between(start_date="-4y", end_date="-1M"),
            "status": status,
            "monthly_charges": plan_price[plan],
            "tenure": tenure,
            "last_login_days": last_login,
            "support_tickets": tickets,
            "feature_adoption": adoption,
            "payment_failures": pay_fail,
            "contract_type": contract,
            "churned": churned,
        })
    df = pd.DataFrame(rows)
    df.to_sql("customers", engine, if_exists="append", index=False)
    print(f"✅ {n} customers inserted")


def generate_subs_and_txns():
    custs = pd.read_sql(
        "SELECT id, plan, monthly_charges, signup_date, status FROM customers",
        engine,
    )
    subs, txns = [], []
    for _, c in custs.iterrows():
        subs.append({
            "customer_id": int(c.id),
            "plan": c.plan,
            "amount": float(c.monthly_charges),
            "start_date": c.signup_date,
            "status": "Active" if c.status == "Active" else "Cancelled",
        })
        months = random.randint(1, 24)
        for m in range(months):
            txns.append({
                "customer_id": int(c.id),
                "amount": float(c.monthly_charges),
                "type": "Subscription",
                "status": random.choices(["Success", "Failed"], weights=[0.92, 0.08])[0],
                "created_at": datetime.now() - timedelta(days=30 * m),
            })
    pd.DataFrame(subs).to_sql("subscriptions", engine, if_exists="append", index=False)
    pd.DataFrame(txns).to_sql("transactions", engine, if_exists="append", index=False)
    print(f"✅ {len(subs)} subscriptions, {len(txns)} transactions inserted")


if __name__ == "__main__":
    create_schema()
    generate_customers(500)
    generate_subs_and_txns()
    print("🎉 Data generation complete!")
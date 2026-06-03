import pandas as pd
from predict import predict_proba, risk_label

df = pd.read_excel("data/telco_churn.xlsx")

sample = df.sample(10, random_state=42)

probs = predict_proba(sample)

for idx, prob in enumerate(probs):
    print(
        f"Customer {idx+1}: "
        f"{prob:.4f} "
        f"{risk_label(prob)}"
    )
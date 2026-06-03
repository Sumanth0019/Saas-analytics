from services import get_customers

df = get_customers()

print(df.columns.tolist())
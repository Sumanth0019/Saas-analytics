import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

from ml.preprocessing import preprocess
from ml.evaluate import evaluate_model

DATASET_PATH = "data/telco_churn.xlsx"


def train():

    print("Loading dataset...")

    df = pd.read_excel(DATASET_PATH)

    X, y = preprocess(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        stratify=y,
        random_state=42
    )

    models = {
        "Logistic Regression": LogisticRegression(
            max_iter=1000,
            random_state=42
        ),

        "Random Forest": RandomForestClassifier(
            n_estimators=300,
            random_state=42
        ),

        "XGBoost": XGBClassifier(
            n_estimators=300,
            max_depth=5,
            learning_rate=0.05,
            eval_metric="logloss",
            random_state=42
        )
    }

    results = []

    best_model = None
    best_auc = 0

    print("\nTraining Models...\n")

    for name, model in models.items():

        print(f"Training {name}...")

        model.fit(X_train, y_train)

        metrics, cm = evaluate_model(
            model,
            X_test,
            y_test
        )

        results.append({
            "Model": name,
            "Accuracy": round(metrics["Accuracy"], 4),
            "Precision": round(metrics["Precision"], 4),
            "Recall": round(metrics["Recall"], 4),
            "F1": round(metrics["F1"], 4),
            "ROC-AUC": round(metrics["ROC_AUC"], 4)
        })

        print(f"\n{name}")
        print("-" * 40)

        for metric, value in metrics.items():
            print(f"{metric}: {value:.4f}")

        print("\nConfusion Matrix:")
        print(cm)

        if metrics["ROC_AUC"] > best_auc:
            best_auc = metrics["ROC_AUC"]
            best_model = model

    results_df = pd.DataFrame(results)

    print("\nModel Comparison")
    print(results_df)

    model_dir = os.path.dirname(os.path.abspath(__file__))

    joblib.dump(
        {
            "model": best_model,
            "columns": list(X.columns)
        },
        os.path.join(model_dir, "churn_model.pkl")
    )

    results_df.to_csv(
        os.path.join(model_dir, "model_comparison.csv"),
        index=False
    )

    print(f"\nBest Model Saved")
    print(f"Best ROC-AUC: {best_auc:.4f}")


if __name__ == "__main__":
    train()
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)


def evaluate_model(
    model,
    X_test,
    y_test
):

    preds = model.predict(X_test)

    probs = model.predict_proba(
        X_test
    )[:, 1]

    metrics = {
        "Accuracy":
            accuracy_score(y_test, preds),

        "Precision":
            precision_score(y_test, preds),

        "Recall":
            recall_score(y_test, preds),

        "F1":
            f1_score(y_test, preds),

        "ROC_AUC":
            roc_auc_score(y_test, probs)
    }

    cm = confusion_matrix(
        y_test,
        preds
    )

    return metrics, cm
"""Analisis dan prediksi keterlambatan pembayaran invoice."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, roc_auc_score, classification_report, ConfusionMatrixDisplay

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "invoices.csv"
OUTPUT_DIR = ROOT / "outputs"
TARGET = "late_payment"

def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError("Dataset belum ada. Jalankan dulu: python generate_data.py")

    OUTPUT_DIR.mkdir(exist_ok=True)
    df = pd.read_csv(DATA_PATH)

    print("=" * 62)
    print("STUDI KASUS: PREDIKSI KETERLAMBATAN PEMBAYARAN")
    print("=" * 62)
    print(f"Jumlah baris: {len(df)}")
    print(f"Jumlah data duplikat: {df.duplicated().sum()}")
    print(f"Jumlah nilai kosong: {int(df.isna().sum().sum())}")
    print("\nRingkasan target (0 = tidak terlambat, 1 = terlambat):")
    print(df[TARGET].value_counts().rename(index={0: "Tidak terlambat", 1: "Terlambat"}))
    print(f"Persentase invoice terlambat: {df[TARGET].mean() * 100:.2f}%")

    # Data preparation dasar: buang baris duplikat dan pisahkan fitur dari target.
    df = df.drop_duplicates().copy()
    X = df.drop(columns=[TARGET])
    y = df[TARGET]

    numeric_features = [
        "invoice_amount", "payment_terms_days", "customer_tenure_months",
        "previous_late_payments", "order_count_6m", "invoice_month"
    ]
    categorical_features = ["payment_method", "customer_segment"]

    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])
    categorical_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ])
    preprocessing = ColumnTransformer([
        ("numeric", numeric_pipeline, numeric_features),
        ("categorical", categorical_pipeline, categorical_features)
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000, class_weight="balanced", random_state=42),
        "Random Forest": RandomForestClassifier(
            n_estimators=250, max_depth=8, min_samples_leaf=4,
            class_weight="balanced", random_state=42
        )
    }

    results = []
    fitted = {}
    for name, model in models.items():
        pipe = Pipeline([("preprocessing", preprocessing), ("model", model)])
        pipe.fit(X_train, y_train)
        pred = pipe.predict(X_test)
        probability = pipe.predict_proba(X_test)[:, 1]
        result = {
            "model": name,
            "accuracy": accuracy_score(y_test, pred),
            "precision": precision_score(y_test, pred, zero_division=0),
            "recall": recall_score(y_test, pred, zero_division=0),
            "f1": f1_score(y_test, pred, zero_division=0),
            "roc_auc": roc_auc_score(y_test, probability)
        }
        results.append(result)
        fitted[name] = (pipe, pred, probability)
        print(f"\n--- {name} ---")
        for metric in ["accuracy", "precision", "recall", "f1", "roc_auc"]:
            print(f"{metric.upper():10s}: {result[metric]:.3f}")
        print(classification_report(y_test, pred, target_names=["Tidak terlambat", "Terlambat"], zero_division=0))

    results_df = pd.DataFrame(results).sort_values("recall", ascending=False)
    results_path = OUTPUT_DIR / "model_comparison.csv"
    results_df.to_csv(results_path, index=False)
    best_name = results_df.iloc[0]["model"]
    best_pipe, best_pred, best_probability = fitted[best_name]

    # Simpan prediksi untuk contoh invoice uji; tidak menyertakan identitas pribadi.
    predictions = X_test.copy()
    predictions["actual_late_payment"] = y_test
    predictions["predicted_late_payment"] = best_pred
    predictions["late_payment_probability"] = best_probability.round(4)
    predictions.to_csv(OUTPUT_DIR / "test_predictions.csv", index=False)

    # Grafik distribusi target
    counts = df[TARGET].value_counts().sort_index()
    plt.figure(figsize=(7, 4))
    plt.bar(["Tidak terlambat", "Terlambat"], [counts.get(0, 0), counts.get(1, 0)])
    plt.title("Distribusi Status Pembayaran")
    plt.ylabel("Jumlah invoice")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "distribusi_pembayaran.png", dpi=150)
    plt.close()

    # Confusion matrix model terpilih
    plt.figure(figsize=(6, 5))
    ConfusionMatrixDisplay.from_predictions(
        y_test, best_pred, display_labels=["Tidak terlambat", "Terlambat"], cmap="Blues"
    )
    plt.title(f"Confusion Matrix - {best_name}")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "confusion_matrix.png", dpi=150)
    plt.close()

    print("\n" + "=" * 62)
    print(f"Model dengan recall tertinggi pada pengujian ini: {best_name}")
    print(f"Hasil perbandingan disimpan di: {results_path}")
    print(f"Prediksi data uji disimpan di: {OUTPUT_DIR / 'test_predictions.csv'}")
    print("Grafik disimpan di folder outputs/.")
    print("\nPenting: ini demonstrasi dengan data sintetis. Hasilnya tidak boleh dianggap")
    print("sebagai kinerja nyata perusahaan. Keputusan penagihan tetap perlu ditinjau manusia.")

if __name__ == "__main__":
    main()

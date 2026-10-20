"""Membuat dataset sintetis untuk studi kasus keterlambatan pembayaran."""
from pathlib import Path
import numpy as np
import pandas as pd

SEED = 42
N = 1200

def main():
    rng = np.random.default_rng(SEED)
    tenure = rng.integers(1, 73, N)
    previous_late = rng.poisson(1.3, N).clip(0, 8)
    invoice_amount = np.round(rng.lognormal(mean=14.2, sigma=0.65, size=N), 0)
    payment_terms = rng.choice([7, 14, 30, 45, 60], N, p=[0.08, 0.18, 0.43, 0.21, 0.10])
    order_count = rng.integers(1, 35, N)
    payment_method = rng.choice(["Transfer", "Kartu", "Tunai", "E-Wallet"], N, p=[0.55, 0.16, 0.19, 0.10])
    customer_segment = rng.choice(["Reguler", "Silver", "Gold"], N, p=[0.55, 0.30, 0.15])
    month = rng.integers(1, 13, N)

    # Label sintetis: peluang terlambat meningkat dengan riwayat keterlambatan,
    # nilai invoice besar, dan masa menjadi pelanggan yang lebih singkat.
    score = (
        -2.15
        + 0.48 * previous_late
        + 0.000000035 * invoice_amount
        + 0.012 * payment_terms
        - 0.018 * tenure
        - 0.018 * order_count
        + np.where(payment_method == "Transfer", 0.12, 0)
        + np.where(customer_segment == "Reguler", 0.25, 0)
        + rng.normal(0, 0.45, N)
    )
    probability = 1 / (1 + np.exp(-score))
    late_payment = rng.binomial(1, probability)

    df = pd.DataFrame({
        "invoice_amount": invoice_amount.astype(int),
        "payment_terms_days": payment_terms,
        "customer_tenure_months": tenure,
        "previous_late_payments": previous_late,
        "order_count_6m": order_count,
        "payment_method": payment_method,
        "customer_segment": customer_segment,
        "invoice_month": month,
        "late_payment": late_payment
    })
    out = Path(__file__).resolve().parent / "data" / "invoices.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False)
    print(f"Dataset sintetis berhasil dibuat: {out}")
    print(f"Jumlah invoice: {len(df)}")
    print(f"Persentase terlambat: {df['late_payment'].mean() * 100:.1f}%")
    print("Catatan: data ini sintetis untuk pembelajaran, bukan data perusahaan nyata.")

if __name__ == "__main__":
    main()

import pandas as pd

# Carregar os dados
df = pd.read_csv("payments.csv")

# Converter a coluna de data
df["payment_date"] = pd.to_datetime(df["payment_date"])

# ==========================================
# VISÃO GERAL
# ==========================================

print("===== VISÃO GERAL =====")

print(f"Total de pagamentos: {len(df)}")

print(f"Valor total movimentado: R$ {df['amount'].sum():.2f}")

print(f"Ticket médio: R$ {df['amount'].mean():.2f}")


# ==========================================
# PAGAMENTOS POR STATUS
# ==========================================

print("\n===== PAGAMENTOS POR STATUS =====")

status_analysis = df.groupby("status").agg(
    quantidade=("payment_id", "count"),
    valor_total=("amount", "sum")
)

print(status_analysis)


# ==========================================
# PAGAMENTOS POR MÉTODO
# ==========================================

print("\n===== PAGAMENTOS POR MÉTODO =====")

method_analysis = df.groupby("payment_method").agg(
    quantidade=("payment_id", "count"),
    valor_total=("amount", "sum"),
    ticket_medio=("amount", "mean")
)

print(method_analysis)


# ==========================================
# TOP CLIENTES
# ==========================================

print("\n===== CLIENTES COM MAIOR VALOR =====")

customer_analysis = df.groupby("customer_id").agg(
    quantidade=("payment_id", "count"),
    valor_total=("amount", "sum")
).sort_values("valor_total", ascending=False)

print(customer_analysis)


# ==========================================
# PAGAMENTOS POR MÊS
# ==========================================

print("\n===== PAGAMENTOS POR MÊS =====")

df["month"] = df["payment_date"].dt.to_period("M")

monthly_analysis = df.groupby("month").agg(
    quantidade=("payment_id", "count"),
    valor_total=("amount", "sum")
)

print(monthly_analysis)


# ==========================================
# TAXA DE APROVAÇÃO
# ==========================================

print("\n===== TAXA DE APROVAÇÃO =====")

approved = (df["status"] == "Aprovado").sum()

approval_rate = (approved / len(df)) * 100

print(f"Taxa de aprovação: {approval_rate:.2f}%")

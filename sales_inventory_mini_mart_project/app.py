from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


DATA_PATH = Path(__file__).parent / "data" / "mini_mart_sales_inventory.csv"


@st.cache_data
def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH, parse_dates=["date"])

    numeric_columns = ["units_sold", "revenue", "current_stock", "reorder_level"]
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    df["stock_gap"] = df["reorder_level"] - df["current_stock"]
    df["stock_status"] = df.apply(classify_stock_status, axis=1)
    df["reorder_recommendation"] = df.apply(create_reorder_recommendation, axis=1)

    return df


def classify_stock_status(row: pd.Series) -> str:
    if row["current_stock"] <= row["reorder_level"]:
        return "Stockout Risk"
    if row["units_sold"] <= 10 and row["current_stock"] >= row["reorder_level"] * 2:
        return "Slow-moving"
    return "Healthy"


def create_reorder_recommendation(row: pd.Series) -> str:
    if row["stock_status"] == "Stockout Risk":
        return "Reorder immediately"
    if row["stock_status"] == "Slow-moving":
        return "Review demand before reordering"
    return "Maintain current stock level"


def format_currency(value: float) -> str:
    return f"${value:,.2f}"


st.set_page_config(
    page_title="Mini Mart Sales & Inventory Dashboard",
    page_icon=":bar_chart:",
    layout="wide",
)

st.title("Sales & Inventory Analytics Dashboard")
st.caption("Mini mart portfolio project focused on sales performance, stockout risk, and restocking decisions.")

df = load_data()

with st.sidebar:
    st.header("Filters")
    selected_categories = st.multiselect(
        "Category",
        options=sorted(df["category"].unique()),
        default=sorted(df["category"].unique()),
    )
    selected_stores = st.multiselect(
        "Store",
        options=sorted(df["store_id"].unique()),
        default=sorted(df["store_id"].unique()),
    )
    selected_promotions = st.multiselect(
        "Promotion Status",
        options=sorted(df["promotion_status"].unique()),
        default=sorted(df["promotion_status"].unique()),
    )

filtered_df = df[
    df["category"].isin(selected_categories)
    & df["store_id"].isin(selected_stores)
    & df["promotion_status"].isin(selected_promotions)
].copy()

stockout_risk_df = filtered_df[filtered_df["stock_status"] == "Stockout Risk"].copy()
slow_moving_df = filtered_df[filtered_df["stock_status"] == "Slow-moving"].copy()

kpi_1, kpi_2, kpi_3, kpi_4 = st.columns(4)
kpi_1.metric("Total Revenue", format_currency(filtered_df["revenue"].sum()))
kpi_2.metric("Total Units Sold", f"{filtered_df['units_sold'].sum():,.0f}")
kpi_3.metric("Stockout Risk Products", f"{stockout_risk_df['product_id'].nunique():,.0f}")
kpi_4.metric("Slow-moving Products", f"{slow_moving_df['product_id'].nunique():,.0f}")

st.divider()

chart_left, chart_right = st.columns(2)

top_products = (
    filtered_df.groupby("product_name", as_index=False)["units_sold"]
    .sum()
    .sort_values("units_sold", ascending=False)
    .head(10)
)

with chart_left:
    st.subheader("Top 10 Products by Units Sold")
    fig_top_products = px.bar(
        top_products,
        x="units_sold",
        y="product_name",
        orientation="h",
        text="units_sold",
        color_discrete_sequence=["#2563eb"],
        labels={"units_sold": "Units Sold", "product_name": "Product"},
    )
    fig_top_products.update_layout(yaxis={"categoryorder": "total ascending"}, height=420)
    st.plotly_chart(fig_top_products, use_container_width=True)

category_revenue = (
    filtered_df.groupby("category", as_index=False)["revenue"]
    .sum()
    .sort_values("revenue", ascending=False)
)

with chart_right:
    st.subheader("Revenue by Category")
    fig_category_revenue = px.bar(
        category_revenue,
        x="category",
        y="revenue",
        text=category_revenue["revenue"].map(lambda value: f"${value:,.0f}"),
        color="category",
        labels={"category": "Category", "revenue": "Revenue"},
    )
    fig_category_revenue.update_layout(showlegend=False, height=420)
    st.plotly_chart(fig_category_revenue, use_container_width=True)

st.divider()

table_columns = [
    "date",
    "store_id",
    "product_name",
    "category",
    "units_sold",
    "current_stock",
    "reorder_level",
    "stock_gap",
    "stock_status",
    "reorder_recommendation",
]

table_left, table_right = st.columns(2)

with table_left:
    st.subheader("Products at Stockout Risk")
    st.dataframe(
        stockout_risk_df[table_columns].sort_values(["stock_gap", "units_sold"], ascending=[False, False]),
        use_container_width=True,
        hide_index=True,
    )

with table_right:
    st.subheader("Slow-moving Products")
    st.dataframe(
        slow_moving_df[table_columns].sort_values(["current_stock", "units_sold"], ascending=[False, True]),
        use_container_width=True,
        hide_index=True,
    )

with st.expander("View prepared dataset with calculated columns"):
    st.dataframe(filtered_df.sort_values(["date", "store_id"]), use_container_width=True, hide_index=True)

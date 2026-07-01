# Project Summary: Sales & Inventory Analytics Dashboard for Mini Mart

## 1. Project Summary

This project analyzes a sample sales and inventory dataset for a mini mart chain. The main objective is to support store managers in making better inventory decisions by identifying:

- Best-selling products
- High-revenue products and categories
- Stores and products with stockout risk
- Slow-moving inventory
- Opportunities for smarter replenishment planning

The dataset contains 50 records across 5 stores and 12 products. It is suitable for beginner-level analysis using Excel, Power BI, Tableau, SQL, or Python.

## 2. Main Insights

### Insight 1: Bottled Water is the strongest product by sales volume

Bottled Water 500ml recorded **222 units sold**, making it the highest-volume product in the dataset. This suggests strong daily demand and a higher need for regular restocking.

### Insight 2: Rice Bag 5kg creates high revenue despite low unit sales

Rice Bag 5kg generated **$112.00** in revenue. Although the number of units sold is low, the product has a higher selling price, so it still contributes strongly to revenue.

### Insight 3: Stockout risk is concentrated in several stores

The stores with the most stockout-risk cases are:

| Store | Stockout-Risk Items |
|---|---:|
| S003 | 10 |
| S005 | 7 |
| S001 | 5 |
| S002 | 4 |
| S004 | 2 |


A stockout-risk item means `current_stock <= reorder_level`.

### Insight 4: Some products appear to be slow-moving

Several products have low sales but high current stock, especially:

- Shampoo 180ml
- Rice Bag 5kg
- Frozen Dumplings

These products may need promotion, better placement, lower reorder quantities, or a review of demand by store.

### Insight 5: Promotions are linked with higher sales volume

Promotion records sold an average of **36.7 units per record**, while non-promotion records sold an average of **16.1 units per record**. This suggests that promotion campaigns can help increase sales volume, especially for beverages and snacks.

## 3. Recommended Actions for Store Managers

### Recommendation 1: Create a restocking priority list

Products with `current_stock <= reorder_level` should be prioritized for replenishment. Managers should check these products daily, especially fast-moving items such as Bottled Water, Soft Drink, Instant Noodles, Snack Chips, and Sandwich Bread.

### Recommendation 2: Reduce overstock for slow-moving products

For products with high stock but low sales, managers should consider:

- Reducing reorder quantity
- Running small promotions
- Moving products to more visible shelves
- Reviewing whether the product is suitable for all stores

### Recommendation 3: Use promotion data to support inventory planning

Before launching promotions, stores should prepare extra inventory for promoted products. Promotion can increase sales volume, but without enough stock, the store may lose potential sales due to stockouts.

## 4. Portfolio Value

This project demonstrates practical data analytics skills including:

- Business problem framing
- Dataset understanding
- Sales performance analysis
- Inventory risk analysis
- Dashboard planning
- Insight writing and business recommendations

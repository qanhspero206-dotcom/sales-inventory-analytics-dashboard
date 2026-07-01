# Dashboard Plan: Sales & Inventory Analytics Dashboard for Mini Mart

## 1. Dashboard Goal

The dashboard should help mini mart managers quickly understand sales performance and inventory health. It should answer three practical questions:

1. What products are selling well?
2. Which products or stores are at risk of stockout?
3. Which products may be overstocked or slow-moving?

## 2. Suggested Dashboard Layout

### Top Section: KPI Overview

Place KPI cards at the top so users can understand the overall situation quickly.

Recommended KPI cards:

- Total Revenue
- Total Units Sold
- Number of Stores
- Number of Products
- Stockout Risk Items
- Average Units Sold per Record

### Middle Left: Sales Performance

Show which products and categories drive sales.

Recommended charts:

- Bar chart: Top 10 products by units sold
- Bar chart: Top 10 products by revenue
- Column chart: Revenue by category
- Donut chart or bar chart: Revenue share by category

### Middle Right: Inventory Health

Show products that need attention from store managers.

Recommended charts/tables:

- Table: Products where current_stock <= reorder_level
- Bar chart: Stockout-risk count by store
- Bar chart: Current stock vs reorder level by product
- Conditional formatting table: Highlight low-stock products

### Bottom Section: Store and Promotion Analysis

Compare store performance and promotion impact.

Recommended charts:

- Bar chart: Revenue by store
- Bar chart: Units sold by store
- Bar chart: Average units sold by promotion status
- Stacked bar chart: Units sold by category and promotion status

## 3. Suggested Dashboard Wireframe

```text
+----------------------------------------------------------------+
| KPI Cards: Revenue | Units Sold | Products | Stores | Risk Items |
+----------------------------------------------------------------+
| Top Products by Units Sold       | Revenue by Category          |
| Bar Chart                        | Bar/Donut Chart              |
+----------------------------------------------------------------+
| Stockout Risk Table              | Risk Count by Store          |
| Conditional Formatting Table     | Bar Chart                    |
+----------------------------------------------------------------+
| Revenue by Store                 | Promotion vs Non-Promotion   |
| Bar Chart                        | Bar Chart                    |
+----------------------------------------------------------------+
| Action Table: Store, Product, Stock, Reorder Level, Action       |
+----------------------------------------------------------------+
```

## 4. Suggested Calculated Fields

You can create these calculated fields in Excel, Power BI, Tableau, SQL, or Python.

### Stockout Risk Flag

```text
IF current_stock <= reorder_level THEN "At Risk" ELSE "Healthy"
```

### Stock Gap

```text
reorder_level - current_stock
```

A positive stock gap means the product is below reorder level.

### Sales Velocity Category

```text
High Sales: units_sold >= 30
Medium Sales: units_sold between 15 and 29
Low Sales: units_sold < 15
```

### Inventory Status

```text
At Risk: current_stock <= reorder_level
Watch: current_stock <= reorder_level * 1.5
Healthy: current_stock > reorder_level * 1.5
```

## 5. Recommended Dashboard Filters

- Date
- Store ID
- Category
- Product Name
- Promotion Status
- Inventory Status

## 6. Design Tips

- Use clear labels and simple chart titles.
- Place business-critical alerts near the top.
- Use conditional formatting for stockout risk.
- Keep the dashboard to one page if possible.
- Avoid too many colors; use color mainly to highlight risk or priority.

## 7. Suggested Action Table

Create an action table with these columns:

| Store | Product | Current Stock | Reorder Level | Status | Suggested Action |
|---|---|---:|---:|---|---|
| S003 | Bottled Water 500ml | 6 | 20 | At Risk | Reorder immediately |
| S005 | Bottled Water 500ml | 4 | 20 | At Risk | Reorder immediately |
| S005 | Soft Drink Can | 5 | 18 | At Risk | Reorder immediately |
| S004 | Rice Bag 5kg | 50 | 10 | Overstock Watch | Review reorder quantity |

## 8. Dashboard Preview Placeholder

After building the dashboard, export a screenshot and save it as:

```text
images/dashboard_preview.png
```

Then add the image to the README file:

```markdown
![Dashboard Preview](images/dashboard_preview.png)
```

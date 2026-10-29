# Factory-to-Customer Shipping Route Efficiency Analysis for Nassau Candy Distributor

## Project Overview

This project focuses on analyzing shipment data to understand how products are distributed from different factories to customer destinations. The goal is to explore shipping patterns, evaluate delivery lead times, and compare factory-to-customer routes using data analysis and interactive visualizations.

The project was developed using Python, Pandas, Plotly, and Streamlit to transform raw shipment data into meaningful insights through an interactive dashboard.

## Objectives

- Clean and validate the shipment dataset.
- Calculate shipment lead time to understand delivery duration.
- Map products to their respective factories.
- Analyze shipment volume and sales performance.
- Explore customer distribution across different states and regions.
- Compare factory-to-state shipping routes.
- Develop an interactive dashboard for exploring shipment data.
- Identify routes and shipment patterns that may require further investigation.

## Technologies Used

- **Python** – Data processing and analysis.
- **Pandas** – Data cleaning, validation, and manipulation.
- **Plotly** – Interactive charts and visualizations.
- **Streamlit** – Interactive dashboard development.

## Project Workflow

1. **Data Cleaning and Validation**  
   Prepared the dataset by cleaning and validating the available shipment records.

2. **Lead Time Calculation**  
   Calculated shipment lead time to analyze the duration between relevant shipment dates.

3. **Product-to-Factory Mapping**  
   Connected products with their corresponding factories to support route analysis.

4. **Shipment and Sales Analysis**  
   Examined shipment volumes, sales, customer regions, and distribution patterns.

5. **Route Analysis**  
   Analyzed factory-to-state routes to compare shipment distribution across customer destinations.

6. **Dashboard Development**  
   Built an interactive Streamlit dashboard to present the analysis through KPIs, charts, maps, filters, and downloadable data.

## Dashboard Features

- **KPI Cards:** Display key shipment and sales metrics.
- **Interactive Charts:** Explore shipment volume, sales, and distribution patterns.
- **Geographic Map:** Visualize customer destinations and shipment distribution.
- **Route Comparison:** Compare factory-to-state shipping routes.
- **Interactive Filters:** Filter the analysis based on available dataset attributes.
- **Downloadable Data Table:** Export filtered shipment data for further analysis.

## Key Outcomes

- Improved understanding of factory-to-customer distribution patterns.
- Better visibility into shipment volumes and sales across customer regions.
- Insights into delivery lead times and factory-to-state routes.
- An interactive platform for exploring shipment data and comparing routes.
- Identification of shipping patterns that may benefit from further investigation.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone "https://github.com/mr-rinshad/Factory-to-Customer-Shipping-Route-Efficiency-Analysis.git"
cd Factory-to-Customer-Shipping-Route-Efficiency-Analysis
```

### 2. Install the Required Libraries

```bash
pip install pandas plotly streamlit
```

Install any additional libraries required by your project.

### 3. Run the Streamlit Dashboard

```bash
streamlit run app.py
```

Replace `app.py` with your actual Streamlit application filename if it is different.

## Project Structure

```text
Factory-to-Customer-Shipping-Route-Analysis/
│
├── app.py                  # Streamlit dashboard application
├── data/                   # Dataset files (if included)
├── notebooks/              # Data cleaning and analysis notebooks
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

*Update the folder and file names to match your actual repository structure.*

## Future Improvements

- Incorporate more detailed delivery performance metrics.
- Investigate potential causes of longer shipment lead times.
- Add advanced route efficiency comparisons.
- Integrate updated shipment data for ongoing monitoring.
- Explore methods to identify potential shipping cost and delivery improvements.

## Conclusion

This project demonstrates how Python-based data analysis and interactive visualization tools can be used to understand factory-to-customer shipping operations. The dashboard enables users to explore shipment patterns, compare routes, and investigate areas where distribution efficiency may be improved.

The project provides a foundation for data-driven analysis of shipment performance and distribution operations.

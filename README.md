# Earthquake Magnitude Analysis by Continent (Python)

## Short Description
This project analyzes **average earthquake magnitudes across continents** using historical earthquake data (1995–2023).  
For example, the visualization helps answer questions like:
- Which continents experience stronger earthquakes on average?
- How do seismic intensity patterns compare globally?
- Are earthquake magnitudes relatively uniform or highly variable across regions?

---

## Tech Stack / Tools Used
- Python  
- Pandas (data loading, merging, aggregation)  
- Matplotlib (data visualization)  
- Seaborn (color palettes and styling)  

---

## Data Source
- Dataset sourced from **Kaggle**
- Earthquake data covering global seismic events from **1995 to 2023**
- Multiple CSV files merged to enrich earthquake records with regional (continent-level) information

---

## Features & Highlights

### Business / Analytical Problem
Earthquake data is often large and complex, making it difficult to identify **regional seismic patterns** at a global level.  
A clear aggregation and visualization is needed to compare **average earthquake intensity across continents**.

---

### Goal of the Analysis
- Aggregate earthquake data at the **continent level**
- Compute average earthquake magnitude per continent
- Visualize the comparison using a clean, readable bar chart
- Enable quick interpretation of global seismic trends

---

### Key Visual Walkthrough
- **Data Processing:**  
  - Two datasets are loaded and merged using Pandas  
  - Earthquake magnitudes are grouped by continent  
  - Mean magnitude is calculated for each continent  

- **Visualization:**  
  - Bar chart showing **average magnitude by continent**
  - Viridis color palette for clear visual distinction
  - Value labels displayed on top of each bar
  - Minimalist design with gridlines and removed chart clutter

---

### Insights & Interpretation
- Average earthquake magnitudes across continents fall within a relatively narrow range  
- Oceania and North America show slightly higher average magnitudes compared to other regions  
- Europe and Africa exhibit comparatively lower average magnitudes  
- The visualization provides a high-level global perspective rather than event-level volatility  

These insights can support **geographical risk assessment, academic research, and exploratory data analysis**.

---

## Screenshot
<img width="1328" height="734" alt="Screenshot 2025-12-31 165515" src="https://github.com/user-attachments/assets/d3aac509-19fd-4fbc-a057-7e20fa9f7963" />


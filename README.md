# 🚴‍♀️ Bike Sharing Dashboard ✨

This project contains a dashboard built with **Streamlit**, **Pandas**, **Matplotlib**, and **Seaborn** that visualizes bike rental data. The dashboard provides insights such as total rentals, daily rental trends, and average rentals based on weather conditions and whether it's a working day or not.

---

## ✨ Features

- **Total Rentals and Revenue**: Displays the total number of bike rentals and total revenue.
- **Daily Rental Trends**: Time series plot showing bike rental activity over a selected date range.
- **Best and Worst Performing Days**: Highlights the best and worst days in terms of bike rentals.
- **Average Rentals Based on Weather**: Visualizes the average number of rentals across different weather conditions.
- **Average Rentals Based on Working Day**: Compares bike rentals between working days and holidays.

---

## 🛠️ Setup Environment

### Anaconda Environment Setup
```bash
conda create --name bike-sharing-env python=3.9
conda activate bike-sharing-env
pip install -r requirements.txt
```
### Shell/Terminal
```bash
mkdir proyek_bike_sharing
cd proyek_bike_sharing
pipenv install
pipenv shell
pip install -r requirements.txt
```
### Run steamlit app
```bash
streamlit run dashboard.py
```

# sales_report.py

import csv
import datetime
import os

def sales_price(row):
    return float(row["sales price"])

def sales_report_str(date_str):
    date_object = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    formatted_date = date_object.strftime('%B, %Y')
    return "Sales Report for " + formatted_date

def monthly_sales_str(list):
    sales_sum_total = 0.0
    for row in list:
        sales_sum_total += float(row["sales price"])
    sales_sum_total = round(sales_sum_total, 2)
    return "Total Monthly Sales: $" + str(sales_sum_total)

def top_sales_str(list):
    top_sales_string = ""
    sorted_rows = sorted(list, key=sales_price)
    sorted_rows.reverse()
    for index in range(5):
        item = sorted_rows[index]
        sales_float = float(item["sales price"])
        sales_total = round(sales_float, 2)
        top_sales_string += str(index+1) + ") " + item["product"] + ": $" + str(sales_total)
        if index < 4:
            top_sales_string += ", "
    return top_sales_string


for filename in os.listdir("data"):
    with open("data/"+filename, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        items_list = list(reader)
        print(sales_report_str(items_list[0]["date"]))
        print(monthly_sales_str(items_list))
        print(top_sales_str(items_list))

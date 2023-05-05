import datetime
from flask import Flask, render_template, request
from functions import calculate_investment


app = Flask(__name__)

"""
# This is to clean the CSV file
input_file = "vfinx_div.csv"
output_file = "vfinx_data_cleaned.csv"

header = "Date,Dividend Per Share,Share Price\n"

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    outfile.write(header)
    for line in infile:
        cleaned_line = line.rstrip(",\n") + "\n"
        outfile.write(cleaned_line)

"""


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        birthday_str = request.form["birthday"]
        birthday = datetime.datetime.strptime(birthday_str, "%Y-%m-%d")
        final_value, dividends, table_data = calculate_investment(birthday)
        return render_template(
            "results.html",
            final_value=final_value,
            dividends=dividends,
            table_data=table_data,
        )
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

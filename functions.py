import csv
import datetime


def calculate_investment(birthday):
    table_data = []

    with open("vfinx_data_cleaned.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile)
        next(reader)  # Skip the header row
        initial_investment = 1000
        shares = initial_investment / float(next(reader)["Share Price"])
        dividends = 0

        for row in reader:
            date = datetime.datetime.strptime(row["Date"], "%m/%d/%y")
            if date > birthday:
                break

        for row in reader:
            date = datetime.datetime.strptime(row["Date"], "%m/%d/%y")
            if date >= birthday:
                # Calculate dividend amount for the current row
                dividend_amount = shares * float(row["Dividend Per Share"])
                dividends += dividend_amount
                new_shares = dividend_amount / float(row["Share Price"])

                # Reinvest the dividend amount by buying more shares at the current share price
                shares += dividend_amount / float(row["Share Price"])

                table_data.append(
                    {
                        "date": row["Date"],
                        "shares": shares,
                        "closing_price": row["Share Price"],
                        "dividend_per_share": row["Dividend Per Share"],
                        "total_dividend_amount": dividend_amount,
                        "new_shares_purchased": new_shares,
                    }
                )

        final_value = shares * float(row["Share Price"])
        return final_value, dividends, table_data

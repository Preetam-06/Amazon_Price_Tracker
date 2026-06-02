# Amazon Price Tracker

A Python-based Amazon price tracker that monitors the current price of a product and compares it against a user-defined budget. The application fetches product information from Amazon, extracts the current price, and notifies the user when the product price falls within the desired budget range.

## Features

* Track Amazon product prices.
* Compare the current price against a target budget.
* Display product name and current price.
* Simple command-line interface.
* Modular project structure for easier maintenance and future expansion.

## Project Structure

```text
Amazon_Price_Tracker/
├── README.md
├── requirements.txt
└── src/
    ├── main.py
    ├── auth/
    │   ├── __init__.py
    │   └── authorize.py
    └── data/
        ├── __init__.py
        └── data_scrap.py
```

## Technologies Used

* Python 3
* Requests
* BeautifulSoup4

## Requirements

* Python 3.9 or higher
* Internet connection

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd Amazon_Price_Tracker
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Before running the application, update the following values in the source code:

* Amazon product URL
* Product name
* Target budget

Example:

```text
Product URL: https://www.amazon.in/...
Product Name: ASUS Gaming V16
Target Budget: 70000
```

## Usage

Run the application:

```bash
python src/main.py
```

## Example Output

```text
Product: ASUS Gaming V16
Current Price: ₹68,999

Great news! The current price is within your budget.
```

## How It Works

1. Sends a request to the Amazon product page.
2. Extracts product information and price.
3. Compares the current price with the target budget.
4. Displays the result to the user.

## Limitations

* Amazon frequently updates its website structure, which may affect price extraction.
* Some product pages may block automated requests.
* The application currently tracks one product at a time.

## Future Improvements

* Email notifications for price drops.
* Support for tracking multiple products.
* Scheduled automatic price checks.
* Price history storage and analysis.
* Web-based dashboard.

## Troubleshooting

### Price Not Found

* Verify that the product URL is correct.
* Ensure the Amazon page is accessible.
* Check whether Amazon has changed its page structure.

### Request Errors

* Verify your internet connection.
* Retry after some time if Amazon temporarily blocks requests.

### Invalid Budget Input

* Enter numeric values only.

## Disclaimer

This project is intended for educational and personal use only. Amazon may modify its website structure or restrict automated access, which can affect the application's functionality.

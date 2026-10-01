# Google Maps Business Listing Scraper

A Python-based GUI application that searches Google Maps for businesses in a specified city, collects basic business information, and exports the results to a CSV file.

## Features

* Tkinter GUI for entering search parameters
* Default values for:

  * Business type
  * City
  * Minimum number of listings
  * Output CSV filename
* Automated Google Maps search using Selenium
* Automatically scrolls the results feed to load additional listings
* Extracts:

  * Business name
  * Phone number
  * Website
* Exports results to CSV
* Uses Chrome Incognito mode

## Requirements

* Python 3.10+
* Google Chrome
* Selenium

Install Selenium with:

```bash
pip install selenium
```

Recent Selenium versions can generally manage the appropriate Chrome driver automatically.

## Usage

Run the Python script:

```bash
python main.py
```

The GUI will ask for:

1. Business type
2. City name
3. Minimum number of listings
4. Output CSV filename

For example:

```text
Business type: Restaurant
City name: New York
Minimum number of listings: 10
Output CSV file name: business_listings.csv
```

The resulting CSV will contain:

```text
Name,Phone,Website
```

## Project Structure

```text
.
├── main.py
├── README.md
├── LICENSE.txt
└── business_listings.csv
```

## Notes

Google Maps pages can change their HTML structure and CSS selectors over time. If Google changes its interface, some selectors used by the scraper may need to be updated.

The scraper is intended for educational and personal automation purposes. Users are responsible for complying with applicable laws, website terms, and usage policies when collecting data.

## Author

**userAnonymous**

## License

This project is licensed under the MIT License. See `LICENSE.txt` for details.

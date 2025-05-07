# E-Commerce Web Test Suite

Automated tests for https://www.saucedemo.com/ using Selenium, Pytest, and POM.

## Setup
1. Install Python 3.9+.
2. Install dependencies: `pip install -r requirements.txt`.
3. Download ChromeDriver and add to PATH.
4. Run tests: `pytest tests/test_ecommerce.py --html=reports/report.html`.

## Project Structure
- `tests/`: Test cases.
- `pages/`: Page objects.
- `reports/`: Test reports.

## CI/CD
Tests run automatically via GitHub Actions. See workflow in `.github/workflows/tests.yml`.

![Tests](https://github.com/yourusername/ecommerce-web-tests/workflows/Run%20Pytest%20Suite/badge.svg)

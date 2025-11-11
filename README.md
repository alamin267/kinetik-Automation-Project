# Kinetik Automation Project

Automation framework using **Playwright** and **Python** for web application testing. Supports cross-browser testing, parallel execution, test parameterization, generates **Allure reports** and many more.

---

## ⚡ Features

- Cross-browser testing: Chromium, Firefox, Webkit
- Parallel execution using `pytest-xdist`
- Test parameterization for multiple inputs
- Page Object Model (POM) design
- WaitHelper utility for stable element interactions
- Allure report integration
- CI/CD with GitHub Actions

---

## 🛠️ Setup

1. **Clone the repo:**


```bash
git clone https://github.com/alamin267/kinetik-Automation-Project.git
cd kinetik-Automation-Project/src


Install dependencies:
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install pytest-playwright allure-pytest
pytest-playwright install

🚀 Running Tests
1. Run a single test file:
pytest tests/test_CaseNo_1.py --env qa --mybrowser chromium --alluredir=reports/allure-results

2. Run all tests in parallel:
pytest -n auto --env qa --mybrowser chromium --alluredir=reports/allure-results
-n auto will automatically use all available CPU cores.

📊 Generating Allure Report
allure generate reports/allure-results --clean -o reports/allure-report
allure open reports/allure-report


The report includes detailed results, screenshots, and test history.

🧪 Using Test Parameterization
Data-driven tests are supported via:
@pytest.mark.parametrize for multiple inputs
products.json file for dynamic test data

Example:

@pytest.mark.parametrize("search_term", ["Tshirt", "jeans", "Top"])
def test_home_page(page, config, search_term):
    ...

🔄 CI/CD with GitHub Actions

Workflow file: .github/workflows/python-playwright.yml

Runs tests on every push or pull request to main

Executes tests on multiple browsers

Generates Allure report and uploads as artifact

✅ Best Practices

Always use WaitHelper for stable element interaction

Use POM structure for page objects

Parameterize tests for different inputs

Run tests in parallel for faster execution


---

This README covers:

- Project overview  
- Folder structure  
- Features  
- Setup instructions  
- Running tests (including parallel)  
- Allure report generation  
- CI/CD workflow  
- Test parameterization  

---
If you want, I can also **add badges** at the top for **GitHub Actions CI status** and **Allure report link** to make it look more professional.  

Do you want me to add badges too?

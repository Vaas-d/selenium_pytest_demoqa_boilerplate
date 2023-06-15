# Selenium + Pytest boilerplate 

## Description:

Basic selenium + pytest testing framework. Framework displays how to test different UI elements
and scenarios utilising https://demoqa.com/ as a testing sandbox.

Framework utilises page object model to deal with locators. UI objets helper file is borrowed from [@ArturSpirin](https://www.youtube.com/@ArturSpirin).   
Allure is set up as a main reporter tool. Reports are stored and displayed via GitHub Pages.
The results of each test run are reported into a Slack Channel via GitHub Actions hook. 

### 1. Install environment:
```
  python -m pip install --upgrade pip
  pip install pipenv
  pipenv install --system
```

### 2. Run pytest tests:
Run all set of tests:
```
pytest
```
Run one particular test:
```
pytest -k <name of the test>
```
Run tests marked with a specific mark:
```
pytest -m <name of pytest mark>
```

### 3. Generate allure report:
Test report is generated automatically after each test run overriding the previous report. 
Use this command to see the report:
```
allure serve reports
```

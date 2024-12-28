# Altoro Mutual testing project example

## Description

The project implemented two information security test cases for checking input forms for the Altoro Mutual web resource:

- **test_password_form_masking** testing the password form for characters masking.

- **test_default_creds** testing the presence of default accounts in the system.

## Requirements

```bash
pip3 install -r requirements.txt
```

You need to install web-driver https://pypi.org/project/selenium/
The following drivers are supported: Firefox, Chrome, Edge.

## Install project

```bash
git clone https://github.com/Hramv/Altoro_test.git

cd Altoro_test

```

## Running

```bash

pytest test_auth_page.py

```

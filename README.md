# Altoro Mutual testing project example

## Description

The project implemented two information security test cases for checking input forms for the Altoro Mutual web resource:

- **test_password_form_masking** testing the password form for characters masking.

- **test_default_creds** testing the presence of default accounts in the system.

## Requirements

python 3.12

pytest 7.4

selenium 4.18

geckodriver 0.35

You need to install Firefox web-driver to "/usr/local/bin/geckodriver"

## Install project

```bash
git clone https://github.com/Hramv/Altoro_test.git

cd Altoro_test

```

## Running

```bash

pytest tests/test.py

```

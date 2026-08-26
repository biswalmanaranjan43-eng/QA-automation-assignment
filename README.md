# OrangeHRM QA Take-Home Automation Assignment

This project tests the public [OrangeHRM demo](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login). It was selected because it is publicly accessible and provides a realistic authenticated web workflow. The original workbook covered finance transactions only; after authorisation to create OrangeHRM-specific cases, the replacement cases are documented in [`test-cases/manual-test-cases.md`](test-cases/manual-test-cases.md).

The project uses Python, pytest, Selenium 4, and `requests`. UI tests use a Page Object Model: page-specific locators/actions live in `pages/`, and test files contain only scenario flow and assertions. Synchronisation uses Selenium explicit waits; there are no fixed delays or implicit waits. Assignment-required UI and API test files are in `ui-tests/` and `api-tests/` respectively.

## Setup and run

1. Create and activate a virtual environment.
2. Install dependencies: `python -m pip install -r requirements.txt`
3. Run all tests: `pytest`

Run UI or API tests independently with `pytest -m ui` or `pytest -m api`. Browser tests run headlessly by default; use `pytest -m ui --headed` to see Chrome. Selenium Manager obtains a compatible Chrome driver when Chrome is installed.

## Configuration

The public demo defaults are provided for convenience, but every value can be overridden without editing test code:

| Variable | Default |
| --- | --- |
| `ORANGEHRM_BASE_URL` | `https://opensource-demo.orangehrmlive.com` |
| `ORANGEHRM_USERNAME` | `Admin` |
| `ORANGEHRM_PASSWORD` | `admin123` |
| `ORANGEHRM_TIMEOUT` | `15` |
| `HEADLESS` | `true` |

## Assumptions and limitations

- The demo is shared, can be reset, rate-limited, or temporarily unavailable; tests do not create, edit, or delete records.
- Its `/api/v2` endpoints are internal endpoints authenticated by the web session rather than a documented public API. The API client first obtains the CSRF token from the public login page, then keeps the resulting session cookie. Endpoint paths, response fields, or exact unauthorised status may change when the demo is upgraded.
- UI text and locators are based on the public OrangeHRM 5.9 demo observed on 2026-08-26. Keep `ORANGEHRM_BASE_URL` configurable if testing another deployment.

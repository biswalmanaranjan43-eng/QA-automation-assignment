# OrangeHRM Manual Test Cases

**Core module:** Login and authenticated employee access. OrangeHRM is the selected HR/payroll workflow application. UI automation implements UI-001 through UI-003; API automation implements API-001 through API-003.

| ID | Type | Description | Steps | Expected result | Priority |
| --- | --- | --- | --- | --- | --- |
| UI-001 | UI, positive | Valid Admin login | 1. Open the login page. 2. Enter configured valid credentials. 3. Select **Login**. | The Dashboard page opens; its URL includes `/dashboard` and the Dashboard breadcrumb is visible. | High |
| UI-002 | UI, positive | Authenticated dashboard is displayed | 1. Log in with valid configured credentials. 2. Wait for the dashboard to load. | The Dashboard breadcrumb is visible and the dashboard URL is displayed. | Medium |
| UI-003 | UI, negative | Invalid password | 1. Open the login page. 2. Enter the configured username and an invalid password. 3. Select **Login**. | The page displays `Invalid credentials`; no dashboard is opened. | High |
| UI-004 | UI, negative | Required login fields | 1. Open the login page. 2. Leave Username and Password empty. 3. Select **Login**. | Both fields display `Required`. | Medium |
| API-001 | API, positive | Authenticated employee list | 1. Obtain the login CSRF token. 2. Authenticate with valid configured credentials. 3. Request `GET /api/v2/pim/employees?limit=10&offset=0`. | Login redirects to the dashboard. The API returns HTTP 200 with a list in `data` and a pagination object in `meta`. | High |
| API-002 | API, negative | Unauthenticated employee list | 1. Do not authenticate. 2. Request `GET /api/v2/pim/employees?limit=10&offset=0`. | HTTP 401 with a JSON response is returned. | High |
| API-003 | API, negative | Invalid login session | 1. Obtain the login CSRF token. 2. Submit invalid credentials. 3. Request the employee endpoint with that session. | Login redirects back to `/auth/login`; the protected endpoint returns HTTP 401. | High |
| API-004 | API, boundary | Single-record employee page | 1. Authenticate with valid configured credentials. 2. Request `GET /api/v2/pim/employees?limit=1&offset=0`. | HTTP 200; `data` contains at most one record and `meta.limit` is 1. | Medium |

# Flask Password Protection Lab

## Overview

This project is a Flask-based backend API that demonstrates **secure password handling** and **session-based authentication** using industry-standard tools. The core focus of the lab is ensuring that **user passwords are never stored or exposed in plaintext** while maintaining a clean, RESTful authentication flow.

The project emphasizes two foundational backend concepts:

1. **Password hashing and verification**
   - User passwords are hashed using `bcrypt` before being stored.
   - Password hashes are write-only and cannot be read back from the model.
   - Login attempts are validated by comparing hashes, not plaintext values.

2. **Session-based authentication**
   - Logged-in state is maintained using Flask sessions.
   - Session data persists across requests until explicitly cleared.
   - Authentication state is enforced entirely on the backend.

This lab is designed to mirror real-world backend authentication patterns while remaining intentionally small and focused.

---

## File Structure

The project follows a standard Flask application layout with testing support.

flask-password-protection-lab/.pytest_cache/

flask-password-protection-lab/client/

flask-password-protection-lab/server/instance/

flask-password-protection-lab/server/migrations/

flask-password-protection-lab/server/testing/__pycache__/

flask-password-protection-lab/server/testing/app_test.py

flask-password-protection-lab/server/testing/conftest.py

flask-password-protection-lab/server/app.py

flask-password-protection-lab/server/config.py

flask-password-protection-lab/server/models.py

flask-password-protection-lab/.gitignore

flask-password-protection-lab/CONTRIBUTING.md

flask-password-protection-lab/LICENSE.md

flask-password-protection-lab/Pipfile

flask-password-protection-lab/Pipfile.lock

flask-password-protection-lab/pytest.ini

flask-password-protection-lab/README.md

---

## Key Files

- `server/app.py`  
  Main Flask application. Defines RESTful authentication routes, session logic, and application startup configuration.

- `server/models.py`  
  SQLAlchemy `User` model and Marshmallow schema. Implements secure password hashing, authentication, and hash protection.

- `server/config.py`  
  Application configuration, database initialization, bcrypt setup, and Flask-RESTful wiring.

- `server/testing/app_test.py`  
  Pytest test cases covering authentication and session behavior.

- `server/testing/conftest.py`  
  Pytest fixtures for application setup and teardown.

---

## Functionality

### Authentication Flow

Authentication is handled using Flask-RESTful resources and Flask sessions.

- A user signs up with a username and password.
- The password is hashed immediately using bcrypt.
- The hashed password is stored in the database.
- During login, the provided password is verified against the stored hash.
- On success, `session['user_id']` is set.
- On logout, session data is cleared.

No plaintext passwords are ever stored or returned.

---

### Password Security

- Password hashes are stored in a private `_password_hash` column.
- The `password_hash` property is **write-only**.
- Attempting to read the password hash raises an exception.
- Authentication uses bcrypt’s secure hash comparison.

This ensures:
- No accidental password exposure
- No reversible password storage
- Industry-standard hashing practices

---

### Session Persistence

- Sessions persist across requests and page reloads.
- Each client maintains its own session state.
- Logging out removes all authentication-related session keys.
- Session logic is enforced server-side and cannot be bypassed by the client.

---

## API Endpoints

### Authentication Routes

#### `POST /signup`

Creates a new user account.

**Behavior**
- Accepts `username` and `password`
- Hashes the password using bcrypt
- Stores the new user in the database

**Response**
- `201 Created` with user data
- Password hash is never returned

---

#### `POST /login`

Logs a user in.

**Behavior**
- Retrieves the user by username
- Verifies the password against the stored hash
- Stores `user_id` in the session on success

**Response**
- `200 OK` with user data
- `401 Unauthorized` if credentials are invalid

---

#### `DELETE /logout`

Logs the user out.

**Behavior**
- Removes `user_id` and related session data

**Response**
- `204 No Content`

---

#### `GET /check_session`

Checks whether a user is currently authenticated.

**Behavior**
- If `user_id` exists in the session, returns the user
- If no session exists, returns an empty response

**Response**
- `200 OK` with user data
- `204 No Content` if not logged in

---

## Features

- Secure password hashing with bcrypt
- Write-only password storage
- Session-based authentication
- RESTful API design with Flask-RESTful
- SQLAlchemy ORM with Marshmallow schemas
- Backend-enforced authentication logic
- Pytest-based automated testing
- Clear separation of concerns

---

## How to Use

### Setup

- `pipenv install`
- `pipenv shell`

### Initialize the Database

- `cd server`
- `flask db upgrade`

### Run the Backend

- `python app.py`

The API will run on:

http://localhost:5555

---

## Testing

Run all tests with:

pytest

---

## Notes

- Passwords are never stored or transmitted in plaintext.
- Session data should never include sensitive information.
- This lab focuses on backend security fundamentals that scale to larger systems.

---

## License

Educational use only. Intended for learning secure authentication, password hashing, and Flask session management.

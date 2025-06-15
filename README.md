# TaskFlow

ProjectPulse – A smart and intuitive project management system designed to streamline workflows, enhance collaboration, and keep teams aligned. Stay on track, meet deadlines, and optimize productivity with ease. 🚀

## Features

- **User Authentication:** Secure login and registration system using Django forms and models.
- **User Management:** Admin interface for managing users (`Pessoa` model) via Django admin.
- **Session Handling:** Middleware to ensure only authenticated users can access protected routes.
- **Custom Forms:** Clean and user-friendly login and registration forms.
- **Error Handling:** Informative messages and validation for user actions.

## Project Structure

```
TaskFlow/
├── src/
│   ├── core/
│   │   ├── admin.py         # Registers Pessoa model in Django admin
│   │   ├── models.py        # Pessoa model and registration logic
│   │   └── views/
│   │       └── views.py     # Home view rendering
│   └── login/
│       ├── forms.py         # Login and registration forms
│       ├── middleware.py    # Middleware for login-required routes
│       └── core/
│           └── views/
│               └── views.py # Main views: index, home, login, register, success
├── README.md
```

## Key Components

### Models

- **Pessoa:** Represents a user with fields for username, hashed password, and email. Includes a class method for registration that hashes the password before saving.

### Forms

- **LoginForm:** Handles user login with username and password fields.
- **RegistrationForm:** Handles user registration with username, email, and password confirmation.

### Middleware

- **LoginRequiredMiddleware:** Ensures users are authenticated before accessing protected pages, redirecting unauthenticated users to the login page.

### Views

- **index:** Renders the index page with the registration form.
- **home:** Renders the home page.
- **login:** Handles user login, session management, and error messages.
- **registrer:** Handles user registration, validation, and error handling.
- **sucess:** Handles successful form submissions.

## Getting Started

1. **Clone the repository:**
   ```sh
   git clone <repository-url>
   cd TaskFlow
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

4. **Create a superuser (for admin access):**
   ```sh
   python manage.py createsuperuser
   ```

5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

6. **Access the application:**
   - Main site: [http://localhost:8000/](http://localhost:8000/)
   - Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

## License

This project is licensed under the Apache License 2.0.
See the [LICENSE](LICENSE) file for details.
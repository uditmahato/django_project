# Django To-Do Application

This is a simple To-Do application built with Django, utilizing SQLite as the database backend. It features CRUD operations, session management, cookies handling, an admin dashboard for administrative tasks, and a user portal for managing tasks.

## Features

- **User Registration and Authentication**: Users can create accounts and log in securely.
- **To-Do Management**: Create, read, update, and delete tasks.
- **Sessions and Cookies**: Utilize sessions for user management and cookies for a personalized experience.
- **Admin Dashboard**: Access the admin panel for managing users and tasks.
- **User Portal**: A dedicated user interface for managing tasks.
- **SQLite Database**: A lightweight, built-in database for data storage.

## Getting Started

To run this Django application, follow these steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/django-todo.git
    cd django-todo
    ```

2. **Set Up a Virtual Environment (Optional):**

    It's recommended to use a virtual environment. You can create one with:

    ```bash
    python -m venv venv
    ```

3. **Install Dependencies:**

    Install the required Python packages from the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations:**

    Run the following commands to apply the initial database migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a Superuser (Admin):**

    You can create an admin account to access the admin dashboard:

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server:**

    Start the Django development server:

    ```bash
    python manage.py runserver
    ```

7. **Access the Application:**

    Open your web browser and navigate to `http://localhost:8000/` to access the user portal and `http://localhost:8000/admin/` for the admin dashboard.

## Configuration

- Customize the application by updating the settings in `settings.py`.
- Secure the application by configuring `settings.py` for production use.
- Deploy the application to a web server of your choice for public access.

## Contributing

Contributions are welcome! If you'd like to improve this project, please open an issue or submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Django community for their valuable resources and documentation.


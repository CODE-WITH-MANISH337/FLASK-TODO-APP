# Flask Todo App

A simple web-based Todo application built with Flask, featuring user authentication, task management, and a clean UI.

## Features

- **User Authentication**: Register and login functionality with session management.
- **Task Management**: Add, view, toggle status (Pending → Working → Completed), and clear all tasks.
- **Database Integration**: Uses SQLite with SQLAlchemy for data persistence.
- **Form Validation**: WTForms for secure and validated user inputs.
- **Responsive UI**: Basic HTML templates with CSS styling.
- **Docker Support**: Containerized deployment using Docker.

## Technologies Used

- **Backend**: Flask 3.1.2
- **Database**: SQLAlchemy 2.0.44, SQLite
- **Forms**: Flask-WTF 1.2.2, WTForms 3.2.1
- **Frontend**: HTML, CSS, Jinja2 templates
- **Deployment**: Docker
- **Other**: Werkzeug, itsdangerous, etc.

## Installation

### Prerequisites
- Python 3.9 or higher
- pip (Python package installer)

### Local Setup
1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-todo-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python run.py
   ```

5. Open your browser and navigate to `http://localhost:5000`.

### Docker Setup
1. Build the Docker image:
   ```
   docker build -t flask-todo-app .
   ```

2. Run the container:
   ```
   docker run -p 5000:5000 flask-todo-app
   ```

3. Access the app at `http://localhost:5000`.

## Usage

1. **Register**: Create a new account at `/register`.
2. **Login**: Log in with your credentials at `/login`.
3. **View Tasks**: After login, view your tasks at `/tasks`.
4. **Add Task**: Use the form to add new tasks.
5. **Toggle Status**: Click on a task to cycle through Pending → Working → Completed.
6. **Clear Tasks**: Clear all tasks with the clear button.
7. **Logout**: Log out to end the session.

## Project Structure

```
flask-todo-app/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models.py            # Database models (User, Task)
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py          # Authentication routes (login, register, logout)
│   │   ├── task.py          # Task management routes
│   │   └── wtf.py           # WTForms definitions
│   ├── static/
│   │   └── css/
│   │       └── style.css    # CSS styles
│   └── templates/
│       ├── base.html        # Base template
│       ├── login.html       # Login page
│       ├── register.html    # Registration page
│       └── task.html        # Task management page
├── instance/
│   └── todo.db              # SQLite database
├── Dockerfile               # Docker configuration
├── requirements.txt         # Python dependencies
├── run.py                   # Application entry point
└── README.md                # This file
```

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -am 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask documentation
- SQLAlchemy ORM
- WTForms for form handling

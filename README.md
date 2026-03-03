# JobFlow - Job Tracker Application

A Python and Django-based web application for tracking job applications, managing job opportunities, and analyzing job search analytics.

## Overview

JobFlow is a comprehensive job tracking application built with Django that helps users manage their job search process efficiently. It provides features to track job applications, manage job opportunities, and gain insights through analytics.

## Tech Stack

- **Backend**: Python 3.x
- **Framework**: Django
- **Database**: SQLite (default)
- **Frontend**: HTML/CSS Templates

## Features

- Dashboard for job tracking overview
- Job application management
- Application analytics and insights
- Job listing and management
- User-friendly interface for organizing job opportunities

## Project Structure

```
jobflow/
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── db.sqlite3            # SQLite database
├── jobtracker/           # Main Django project
│   ├── settings.py       # Project settings
│   ├── urls.py          # URL routing
│   ├── wsgi.py          # WSGI configuration
│   └── jobs/            # Jobs app
│       ├── models.py    # Database models
│       ├── views.py     # View logic
│       ├── serializers.py # API serializers
│       ├── admin.py     # Admin configuration
│       └── migrations/  # Database migrations
└── templates/            # HTML templates
    ├── base.html        # Base template
    ├── dashboard.html   # Dashboard page
    ├── add_job.html     # Add job form
    ├── analytics.html   # Analytics page
    ├── applications.html # Applications page
    └── about.html       # About page
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Vaibhavp809/jobflow.git
cd jobflow
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create a superuser (admin account):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000/`

## Usage

- Access the dashboard at `/dashboard/`
- View job applications at `/applications/`
- Add new job opportunities
- Check analytics and insights
- Manage job listings through the admin panel

## Dependencies

See `requirements.txt` for all Python dependencies.

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.

## Contact

For more information, visit the repository: https://github.com/Vaibhavp809/jobflow.git

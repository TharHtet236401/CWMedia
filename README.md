# CWMedia

A Django-based social media platform for creative writers and content creators.

## Features

- User Authentication
- Blog Posts Management
- Template-based Frontend
- MySQL Database Integration

## Tech Stack

- Python 3.12.4
- Django 5.1.6
- MySQL Database
- HTML/CSS

## Prerequisites

- Python 3.12 or higher
- MySQL Server
- pip (Python package manager)

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/CWMedia.git
cd CWMedia
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure MySQL Database
- Create a MySQL database named 'CWMedia'
- Update database settings in `CWMedia/settings.py` with your credentials

5. Run migrations
```bash
python manage.py migrate
```

6. Start the development server
```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser.

## Project Structure

```
CWMedia/
├── templates/          # Global templates
│   ├── base.html
│   └── nav.html
├── CWMedia/           # Project configuration
├── blogs/             # Blog app
│   └── templates/
│       └── blogs/
└── manage.py
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
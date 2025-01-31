﻿# FAQ Project

##  Overview

This project is a **Django-based FAQ system** that provides an API for retrieving frequently asked questions in different languages. It uses **Redis for caching** to improve performance.

## Supported Languages
- Hindi (`hi`)
- Bengali (`bn`)
- Spanish (`es`)
- French (`fr`)
- German (`de`)
- Chinese (`zh`)
- Arabic (`ar`)
- Russian (`ru`)
- Japanese (`ja`)
- Portuguese (`pt`)
  
  
### Prerequisites

Ensure you have the following installed:

- Python 3.9+
- Docker & Docker Compose
- Redis (if not using Docker)

## 🚀 Features

- **Multi-language support**: Retrieve FAQs in different languages using the `lang` query parameter.
- **Redis Caching**: Optimized performance by storing API responses.
- **Docker Support**: Easily deploy the application using Docker and Docker Compose.
- **GitHub CI/CD**: Automated linting and testing using GitHub Actions.

##  Project Structure

```
faq_project/
│── faqs/                 # FAQ app containing models, views, serializers
│── faq_project/          # Main Django project configuration
│── requirements.txt      # Python dependencies
│── compose.yaml          # Docker Compose file
│── Dockerfile            # Docker configuration
│── entrypoint.sh         # Entry script for Docker container
│── manage.py             # Django management script
│── README.md             # Documentation
```


## Installation

## Running with Docker

To run the project using Docker:

```sh
docker-compose up --build
```

### Steps

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/faq-api.git
   cd bharatFD
   ```
2. Set up a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   cd faq_project/
   pip install -r requirements.txt
   ```
3. Apply database migrations:
   ```sh
   python manage.py migrate
   ```
4. Start the development server:
   ```sh
   python manage.py runserver
   ```
## Setting Up Redis for Caching

If you are using Redis for caching and need to run it separately, you can pull and run the Redis image using Docker:

```sh
docker pull redis
```

To run Redis as a container:

```sh
docker run --name redis-cache -d -p 6379:6379 redis
```



This will start both the Django application and Redis container.

## API Endpoints
**Example:**
```sh
  http://127.0.0.1:8000/admin
```
default id:- admin
default password:- admin
### Get FAQs

Retrieve FAQs in a specific language.

**Request:**

```sh
GET /api/faqs/?lang=<language_code>
```

**Example:**

```sh
GET /api/faqs/?lang=fr
```

**Response:**

```json
[
    {
        "id": 1,
        "question": "Quelle est votre politique de retour ?",
        "answer": "Nous acceptons les retours sous 30 jours."
    }
]
```


## Contribution Guidelines

1. Fork the repository and create a new branch.
2. Ensure your code follows PEP8 standards.
3. Run lint checks before submitting a pull request:
   ```sh
   flake8 .
   ```
4. Run tests to confirm functionality:
   ```sh
   python manage.py test
   ```
5. Submit a pull request with a detailed description of your changes.


## Assumptions & Design Choices

- The admin panel displays only questions in English for consistency and ease of management.
- Currently, pre-translation is supported only for Hindi and Bengali.
  
## License

This project is licensed under the MIT License.












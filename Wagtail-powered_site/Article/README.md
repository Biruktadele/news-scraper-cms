# Wagtail-Powered News Aggregator

This project is a news aggregator website built with Django and Wagtail. It includes a custom management command to scrape news articles from a target website and display them on the site.

## Prerequisites

- Python 3.8+
- pip

## Setup Instructions

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/Biruktadele/news-scraper-cms

    cd Wagtail-powered_site/Article
    ```

2.  **Create and Activate a Virtual Environment**

    For Windows:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

    For macOS/Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**

    Install all the required packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Database Migrations**

    Apply the database migrations to set up your database schema:
    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser**

    Create an admin user to access the Wagtail admin interface:
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to set a username, email, and password.

6.  **Run the Development Server**

    Start the Django development server:
    ```bash
    python manage.py runserver
    ```
    The site will be available at `http://127.0.0.1:8000`, and the admin interface at `http://127.0.0.1:8000/admin`.

## Usage

### Scraping News Articles

The project includes a command to scrape news articles. To run it, use the following command:

```bash
python manage.py scrape_news
```

This will fetch the latest articles and add them to your database. You can then see them on the news list page.

### Wagtail Admin

Log in to the admin interface at `http://127.0.0.1:8000/admin` with the superuser credentials you created. Here, you can manage pages, including the news articles.

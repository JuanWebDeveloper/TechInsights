# **TechInsights**

Welcome to **TechInsights**, a dynamic and modern technology blog built using Django. This platform is designed to provide users with an engaging space to share, explore, and discuss the latest in technology trends.

TechInsights empowers users to:

- Create and manage blog posts with categorized content.
- Explore posts across various categories in a seamless and organized way.
- Engage with a user-friendly interface designed for simplicity and clarity.

This repository contains the complete source code for the TechInsights project, along with setup instructions to get the application running on your local machine or accessing the deployed version.

---

## **Access the Application**

The application is live and accessible at the following URL:

[https://techinsights-3kvb.onrender.com/](https://techinsights-3kvb.onrender.com/)

---

## **Getting Started Locally**

To get the TechInsights project up and running on your local machine, follow these steps:

---

### **1. Clone the Repository**

First, clone the repository to your local machine using the following command:

```bash
git clone https://github.com/JuanWebDeveloper/TechInsights.git
cd TechInsights
```

---

### **2. Set Up the Virtual Environment**

It’s recommended to use a virtual environment for Python projects to manage dependencies effectively. Follow these steps:

1. **Create the Virtual Environment**

   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**

   - On **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Install Required Dependencies**  
   Install the dependencies listed in the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

---

### **3. Configure Environment Variables**

To set up the local environment, you'll need to configure the environment variables. Create a `.env` file in the project root directory and add the following variables:

```env
SECRET_KEY=your_secret_key
DEBUG=True
```

- **SECRET_KEY**: You can generate a secret key by running:

```bash
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

- **DEBUG**: Set this to `True` during development. When deploying, set it to `False`.

For deployment, you should configure these variables directly on your hosting platform (e.g., Render).

---

### **4. Database Setup**

TechInsights uses **SQLite** as the default database, which is already configured. Follow these steps to set up your database:

1. **Apply Migrations**  
   Run the following commands to create the database and apply necessary migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Create a Superuser**  
   A superuser is required to manage categories and perform administrative tasks. Create one using:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to set a username, email, and password.

3. **Manage Article Categories**
   - Article categories can only be created and managed by the superuser.
   - Log in to the admin panel at `http://127.0.0.1:8000/admin/` to create and manage categories.

---

### **5. Running the Development Server**

To start the application locally, run the following command:

```bash
python manage.py runserver
```

Once the server is running, open your browser and visit:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## **Features**

- **User Authentication**: Secure login and registration for all users.
- **Dynamic Blog Management**: Users can create, view, edit, and delete posts.
- **Admin Controls**: Superusers can manage categories and oversee posts.
- **Responsive Design**: Optimized for both desktop and mobile use.

---

## **Additional Notes**

- **Python Version**: Ensure you have Python 3.8+ installed on your system.
- **For Production**: In a production environment, you will need to configure a production-ready web server like **Gunicorn** and **Nginx**, and consider switching to a more robust database (such as PostgreSQL).
- **Security Considerations**: Always keep your `SECRET_KEY` secure, especially in production environments. It's recommended to use environment variables to store sensitive data.
- **Static Files**: When deploying to production, make sure that your static files are collected and served properly. For local development, you can run `python manage.py collectstatic` to collect static files into a single directory.

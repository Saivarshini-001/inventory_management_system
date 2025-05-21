# Inventory Management System

A Django-based web application to manage inventory for small retail stores.

## 📦 Features
- Add, update, and delete inventory items
- Track stock levels
- Secure admin panel for managing users and data
- Simple interface using Django’s default admin dashboard

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/Saivarshini-001/inventory_management_system.git
cd inventory_management_system

# Create and activate virtual environment
python3 -m venv env
source env/bin/activate

# Install required packages
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Create superuser (optional but recommended)
python manage.py createsuperuser

# Start the server
python manage.py runserver
```

Then open your browser and go to `http://127.0.0.1:8000/`

## 🚀 Usage
Use the Django admin dashboard to manage your inventory at `http://127.0.0.1:8000/admin`.

## 🔒 Admin Access
Login using the credentials created via `createsuperuser` to manage inventory securely.

## 📌 Future Improvements
- Frontend UI with Bootstrap or React
- Reporting tools and export options
- User roles and permissions

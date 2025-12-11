## site link
link : https://sandeepcodes.pythonanywhere.com/

## ShopyWorld – Django E-Commerce Web Application

ShopyWorld is a full-stack e-commerce application built using Django, MySQL, and Bootstrap 5. It includes product browsing, cart management, checkout flow, payments, and admin controls.

🚀 Features
🛒 Store

## Product listing

Product detail page

Category filtering

Search functionality

 ## 🛍️ Cart

Add to cart

Update quantity

Remove items

Auto total calculation

## 💳 Payment

Checkout

Razorpay/Test payment integration

Order confirmation

## 👤 User & Admin

User login, register, logout

Order tracking

Django admin for product management

## ⚙️ System

Clean project architecture

Environment variables support

Static & media handling

Production-ready setup

## 📁 Project Structure
ShopyWorld_djangoProject/
│── core/
│── store/
│── cart/
│── payment_app/
│── templates/
│── static/
│── media/
│── ShopyWorld_djangoProject/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│── requirements.txt
│── .env.example
│── README.md

## 🔧 Tech Stack
Component	Technology
Backend	Django 5.x
Frontend	HTML, CSS, Bootstrap 5
Database	MySQL
Payments	Razorpay (test mode)
Deployment	PythonAnywhere
Environment	Virtualenv
## ⚙️ Installation Guide
## 1️⃣ Clone the repository
git clone https://github.com/SandeepR8/ShopyWorld_djangoProject.git
cd ShopyWorld_djangoProject

## 2️⃣ Create virtual environment
python3 -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows

## 3️⃣ Install requirements
pip install -r requirements.txt

## 4️⃣ Create .env file
DJANGO_SECRET_KEY=your_secret_key
PA_MYSQL_PASSWORD=your_mysql_password
RAZORPAY_KEY_ID=your_key
RAZORPAY_KEY_SECRET=your_secret

## 5️⃣ Apply migrations
python manage.py migrate

## 6️⃣ Create superuser
python manage.py createsuperuser

## 7️⃣ Run the server
python manage.py runserver

## 🌐 Deployment (PythonAnywhere)

Clone or upload project to PythonAnywhere

Create virtualenv and install requirements

Add .env file with secret key + DB password

Configure WSGI file

Set static and media file paths

Reload web app

## 🧪 Testing
python manage.py test

## 📌 Future Enhancements

Wishlist

Coupon system

Advanced filtering

Email notifications

Full order history UI

## 🤝 Contributing

Contributions are welcome.
Open an issue for major changes.

## 📜 License

Open-source. Free to use.

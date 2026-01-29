# 🛍️ E-Commerce Website using Django

An online shopping platform built with **Django** — a simple yet fully functional e-commerce website that allows users to browse products, add items to a cart, register/log in, and place orders. This project demonstrates how to build a basic e-commerce store with core features using the Django web framework.

## ✨ Features

* **User Authentication:** Secure registration and login functionality.
* **Product Management:** Detailed product listing and individual detail pages.
* **Shopping Cart:** Add, remove, and update item quantities in real-time.
* **Checkout System:** Streamlined order creation and checkout process.
* **Admin Dashboard:** Built-in Django interface to manage products, categories, and customer orders.

## 🧱 Tech Stack

| Component | Technology |
| :--- | :--- |
| **Backend** | Python, Django |
| **Database** | SQLite (Default) |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Templates** | Django Template Language (DTL) |

## 📂 Project Structure

```text
E-Commerce-Website-using-Django/
├── accounts/          # User authentication and profiles
├── assets/            # Global CSS, JS, and static images
├── templates/         # HTML templates for the UI
├── media/products/    # Uploaded product images
├── manage.py          # Django project entrypoint
├── db.sqlite3         # SQLite database (Development)
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
🚀 Installation & Setup
Prerequisites
Python 3.x

pip (Python package manager)

Steps
Clone the Repository

Bash
git clone [https://github.com/Arman-dev123/E-Commerce-Website-using-Django.git](https://github.com/Arman-dev123/E-Commerce-Website-using-Django.git)
cd E-Commerce-Website-using-Django
Create a Virtual Environment (Optional but Recommended)

Bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
Install Dependencies

Bash
pip install -r requirements.txt
Apply Database Migrations

Bash
python manage.py makemigrations
python manage.py migrate
Create an Admin Account

Bash
python manage.py createsuperuser
Run the Server

Bash
python manage.py runserver
Access the App

Website: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/admin/

🧑‍💻 Usage
As a User: Browse the catalog, sign up for an account, manage your cart, and place mock orders.

As an Admin: Log in to the /admin portal to add new products, edit pricing, and view customer orders.

🤝 Contributing
Contributions make the open-source community an amazing place to learn and create.

Fork the Project.

Create your Feature Branch (git checkout -b feature/AmazingFeature).

Commit your Changes (git commit -m 'Add some AmazingFeature').

Push to the Branch (git push origin feature/AmazingFeature).

Open a Pull Request.

📄 License
This project is open-source. Feel free to use and modify it as you see fit. (Consider adding an MIT License for formal use).

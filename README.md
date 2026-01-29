# 🛍️ E-Commerce Website using Django

An online shopping platform built with **Django** — a simple yet fully functional e-commerce website that allows users to browse products, add items to a cart, register/log in, and place orders. This project demonstrates how to build a basic e-commerce store with core features using the Django web framework.

---

## ✨ Features

* **User Authentication:** Secure registration and login functionality.
* **Product Management:** Detailed product listing and individual product detail pages.
* **Shopping Cart:** Add, remove, and update item quantities in real time.
* **Checkout System:** Streamlined order creation and checkout process.
* **Admin Dashboard:** Built-in Django admin interface to manage products, categories, and customer orders.

---

## 🧱 Tech Stack

| Component     | Technology                     |
| ------------- | ------------------------------ |
| **Backend**   | Python, Django                 |
| **Database**  | SQLite (Default)               |
| **Frontend**  | HTML5, CSS3, JavaScript        |
| **Templates** | Django Template Language (DTL) |

---

## 📂 Project Structure

```text
E-Commerce-Website-using-Django/
├── accounts/          # User authentication and profiles
├── assets/            # Global CSS, JS, and static images
├── templates/         # HTML templates for the UI
├── media/products/    # Uploaded product images
├── manage.py          # Django project entry point
├── db.sqlite3         # SQLite database (development)
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

---

## 🚀 Installation & Setup

### Prerequisites

* Python 3.x
* pip (Python package manager)

### Steps

#### 1. Clone the Repository

```bash
git clone https://github.com/Arman-dev123/E-Commerce-Website-using-Django.git
cd E-Commerce-Website-using-Django
```

#### 2. Create a Virtual Environment (Optional but Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

#### 5. Create an Admin Account

```bash
python manage.py createsuperuser
```

#### 6. Run the Development Server

```bash
python manage.py runserver
```

---

## 🌐 Access the Application

* **Website:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🧑‍💻 Usage

### As a User

* Browse the product catalog
* Register and log in
* Add products to the shopping cart
* Proceed through checkout and place mock orders

### As an Admin

* Log in to the `/admin` panel
* Add, update, or delete products and categories
* Manage pricing and inventory
* View and manage customer orders

---

## 🤝 Contributing

Contributions are welcome and help make the open-source community a great place to learn and grow.

1. Fork the project
2. Create your feature branch

   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes

   ```bash
   git commit -m "Add some AmazingFeature"
   ```
4. Push to the branch

   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request

---

## 📄 License

This project is open-source and free to use. You are encouraged to add an **MIT License** or another license of your choice for formal or commercial use.

---

Happy coding! 🚀

from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db import connection
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from.models import Cart ,Product, Customer,Cart, Address, Order, OrderItem

# Register view
def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")  # Add a password field for simplicity

        # Check if the email is already registered
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM Customer WHERE email = %s
            """, [email])
            existing_user = cursor.fetchone()

        if existing_user:
            messages.warning(request, "This email is already registered. Please try another one.")
            return render(request, 'register.html')  # Show the registration page with warning message
        
        # If email is not registered, insert customer data into the Customer table
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Customer (first_name, last_name, email, phone_number, password)
                VALUES (%s, %s, %s, %s, %s)
            """, [first_name, last_name, email, phone_number, password])
        
        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')  # Redirect to login page
    
    return render(request, 'register.html')

# Login view
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        # Authenticate the user
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT * FROM Customer WHERE email = %s AND password = %s
            """, [email, password])
            user = cursor.fetchone()

        if user:
            # Log the user in
            request.session['user_id'] = user[0]  # Store user ID in session
            request.session['user_name'] = user[1]  # Store user name in session
            return redirect('home')  # Redirect to home page
        
        messages.error(request, "Invalid email or password.")
        return render(request, 'login.html')
    
    return render(request, 'login.html')

# Home view (index page)
def home(request):
    if 'user_name' in request.session:
        user_name = request.session['user_name']
    else:
        user_name = None
    return render(request, 'index.html', {'user_name': user_name})

def logout_view(request):
    try:
        # Remove user data from session
        del request.session['user_id']
        del request.session['user_name']
    except KeyError:
        pass  # Handle the case where the session doesn't have these keys
    return redirect('home')  


##### SHOP PAGE ####
from django.http import JsonResponse
from .models import Product, Category

# def shop(request):
#     categories = Category.objects.all()
#     products = Product.objects.all()  # Default: Show all products
    
#     if 'category' in request.GET:
#         category_name = request.GET['category']
#         products = Product.objects.filter(category__name=category_name)
    
#     context = {
#         'categories': categories,
#         'products': products
#     }
#     return render(request, 'shop.html', context)


#### \\\\\\\\\\\\\\\  SHOP  //////////////////////////////////////////

def shop(request):
    selected_category = request.GET.get('category')  # Get the selected category from the query parameter
    categories = Category.objects.all()

    if selected_category:
        products = Product.objects.filter(category__name=selected_category)
    else:
        products = Product.objects.all()

    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'shop.html', context)


#                            ******* CART *********


@login_required  
def add_to_cart(request, product_id):
  
    customer_id = request.session.get('user_id')  # Assuming you're storing the customer_id in the session
    
    if not customer_id:
        messages.error(request, "You must be logged in to perform this action.")
        return redirect('login')  

    query = """
        INSERT INTO cart (product_id, customer_id)
        VALUES (%s, %s);
    """
    
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, [product_id, customer_id])
            connection.commit() 
            messages.success(request, "Product added to your cart.")
    except Exception as e:
        messages.error(request, f"An error occurred: {e}")
        return redirect('home')  

    return render(request, 'add_to_cart.html', {'product_id': product_id, 'customer_id': customer_id})



def execute_raw_sql(query, params=None):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        return cursor.fetchall()

# def shop_cart(request):
#     # Retrieve the user_id from the session (if it's a session-based approach)
#     customer_id = request.session.get('user_id')
    
#     # Check if customer_id is available, else return to login or error page
#     if not customer_id:
#         return redirect('login')  # Or show an error if the session is lost
    
#     # Step 1: Get product_ids from the CART table for the specific customer
#     cart_query = "SELECT product_id FROM CART WHERE customer_id = %s"
#     product_ids = execute_raw_sql(cart_query, [customer_id])

#     # Step 2: Fetch product details (image, price, name) for each product_id
#     product_details = []
#     total_price = 0  # Initialize total_price
    
#     for product_id_tuple in product_ids:
#         product_id = product_id_tuple[0]
#         product_query = """
#             SELECT image, price, name 
#             FROM accounts_product 
#             WHERE id = %s
#         """
#         product = execute_raw_sql(product_query, [product_id])
#         if product:
#             product_details.append({
#                 'image': product[0][0],
#                 'price': product[0][1],
#                 'name': product[0][2],
#             })
#             total_price += product[0][1]  # Add product price to the total price

#     # Step 3: Pass the product details and total price to the template for rendering
#     context = {
#         'product_details': product_details,
#         'total_price': total_price,  # Add total_price to the context
#     }

#     return render(request, 'shop-cart.html', context)


def shop_cart(request):
    # Retrieve the user_id from the session (if it's a session-based approach)
    customer_id = request.session.get('user_id')

    # Check if customer_id is available, else return to login or error page
    if not customer_id:
        return redirect('login')  # Or show an error if the session is lost

    # Step 1: Get product_ids from the CART table for the specific customer
    cart_query = "SELECT product_id FROM CART WHERE customer_id = %s"
    product_ids = execute_raw_sql(cart_query, [customer_id])

    # If no products are in the cart, display a message
    if not product_ids:
        return render(request, 'shop-cart.html', {'message': 'Your cart is empty. Start shopping!'})

    # Step 2: Get product details (image, price, name) for each product_id
    product_ids_list = [product_id_tuple[0] for product_id_tuple in product_ids]  # Extract the product IDs

    # Fetch all product details in one query to optimize performance
    product_query = """
        SELECT id, image, price, name 
        FROM accounts_product 
        WHERE id IN %s
    """
    products = execute_raw_sql(product_query, [tuple(product_ids_list)])

    # Prepare product details and calculate total price
    product_details = []
    total_price = 0  # Initialize total_price

    for product in products:
        product_details.append({
            'id': product[0],
            'image': product[1],
            'price': product[2],
            'name': product[3],
        })
        total_price += product[2]  # Add product price to the total price

    # Step 3: Pass the product details and total price to the template for rendering
    context = {
        'product_details': product_details,
        'total_price': total_price,
    }

    return render(request, 'shop-cart.html', context)


# DELETE CART

def delete_cart_item(request, product_id):
    customer_id = request.session.get('user_id')

    if not customer_id:
        return redirect('login')  

    # SQL query to delete the product from the cart
    delete_query = "DELETE FROM CART WHERE customer_id = %s AND product_id = %s"
    execute_raw_sql(delete_query, [customer_id, product_id])

    return redirect('shop-cart')


####################################################################################################################################################################################################################################


def checkout_view(request):
    customer_id = request.session.get('user_id')
    if not customer_id:
        return redirect('login')

    # Fetch products in the cart
    cart_query = "SELECT product_id FROM CART WHERE customer_id = %s"
    product_ids = execute_raw_sql(cart_query, [customer_id])
    
    if not product_ids:
        return render(request, 'shop-cart.html', {'message': 'Your cart is empty. Start shopping!'})

    product_ids_list = [product_id_tuple[0] for product_id_tuple in product_ids]

    product_query = """
        SELECT id, image, price, name 
        FROM accounts_product 
        WHERE id IN %s
    """
    products = execute_raw_sql(product_query, [tuple(product_ids_list)])
    product_details = []
    total_price = 0

    for product in products:
        product_details.append({
            'id': product[0],
            'image': product[1],
            'price': product[2],
            'name': product[3],
        })
        total_price += product[2]

    return render(request, 'checkout.html', {
        'product_details': product_details,
        'total_price': total_price
    })



from django.http import HttpResponse

def submit_address_view(request):
    if request.method == 'POST':
        customer_id = request.session.get('user_id')
        if not customer_id:
            return redirect('login')

        # Get address details from form
        country = request.POST['country']
        city = request.POST['city']
        street = request.POST['street']
        house_number = request.POST['house_number']
        zip_code = request.POST['zip_code']

        # Insert address into the Address table
        insert_query = """
            INSERT INTO accounts_Address (country, city, street, house_number, zip_code, customer_id) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        execute_raw_sql(insert_query, [country, city, street, house_number, zip_code, customer_id])

        return redirect('checkout')
    return HttpResponse("Invalid request method.", status=405)


@login_required
def place_order(request):
    customer_id = request.session.get('user_id')

    if not customer_id:
        return redirect('login')

    # Step 1: Retrieve address ID
    address_id_query = """
        SELECT id FROM accounts_address WHERE customer_id = %s LIMIT 1
    """
    address_id_result = execute_raw_sql(address_id_query, [customer_id])

    if not address_id_result:
        messages.error(request, "No address found. Please add an address to proceed.")
        return redirect('add_address')

    address_id = address_id_result[0][0]

    # Step 2: Retrieve cart items and calculate total
    cart_items_query = """
        SELECT p.id, p.price, p.name 
        FROM accounts_product p 
        JOIN cart c ON c.product_id = p.id
        WHERE c.customer_id = %s
    """
    cart_items = execute_raw_sql(cart_items_query, [customer_id])

    if not cart_items:
        return render(request, 'shop-cart.html', {'message': 'Your cart is empty.'})

    total_amount = sum(item[1] for item in cart_items)

    # Step 3: Insert order
    insert_order_query = """
        INSERT INTO accounts_Order (customer_id, address_id, total_amount, status)
        VALUES (%s, %s, %s, 'Pending')
    """
    execute_raw_sql(insert_order_query, [customer_id, address_id, total_amount])

    # Retrieve the newly created order ID
    order_id_query = """
        SELECT order_id FROM OrderTable WHERE customer_id = %s ORDER BY order_id DESC LIMIT 1
    """
    order_id_result = execute_raw_sql(order_id_query, [customer_id])
    order_id = order_id_result[0][0] if order_id_result else None

    if not order_id:
        return HttpResponse("Failed to create order.", status=500)

    # Step 4: Insert order items
    for item in cart_items:
        product_id, price, _ = item
        insert_order_item_query = """
            INSERT INTO accounts_orderitem (order_id, product_id, quantity, price)
            VALUES (%s, %s, %s, %s)
        """
        execute_raw_sql(insert_order_item_query, [order_id, product_id, 1, price])

    # Step 5: Clear cart
    delete_cart_query = """
        DELETE FROM Cart WHERE customer_id = %s
    """
    execute_raw_sql(delete_cart_query, [customer_id])

    # Success message and redirect
    messages.success(request, "Order placed successfully!")
    return redirect('order_success')

# @login_required
# def place_order(request):
#     customer_id = request.session.get('user_id')
#     if not customer_id:
#         return redirect('login')

#     # Step 1: Retrieve address ID
#     address_id_query = """
#         SELECT id FROM accounts_address WHERE customer_id = %s LIMIT 1
#     """
#     address_id_result = execute_raw_sql(address_id_query, [customer_id])
#     if not address_id_result:
#         messages.error(request, "No address found. Please add an address to proceed.")
#         return redirect('add_address')

#     address_id = address_id_result[0][0]

#     # Step 2: Retrieve cart items and calculate total
#     cart_items_query = """
#         SELECT p.id, p.price, p.name
#         FROM accounts_product p
#         JOIN cart c ON c.product_id = p.id
#         WHERE c.customer_id = %s
#     """
#     cart_items = execute_raw_sql(cart_items_query, [customer_id])
#     if not cart_items:
#         return render(request, 'shop-cart.html', {'message': 'Your cart is empty.'})

#     total_amount = sum(item[1] for item in cart_items)

#     # Step 3: Insert order
#     insert_order_query = """
#         INSERT INTO OrderTable (customer_id, address_id, total_amount, status)
#         VALUES (%s, %s, %s, 'Pending')
#     """
#     execute_raw_sql(insert_order_query, [customer_id, address_id, total_amount])

#     # Retrieve the newly created order ID
#     order_id_query = """
#         SELECT order_id FROM OrderTable WHERE customer_id = %s ORDER BY order_id DESC LIMIT 1
#     """
#     order_id_result = execute_raw_sql(order_id_query, [customer_id])
#     order_id = order_id_result[0][0] if order_id_result else None
#     if not order_id:
#         return HttpResponse("Failed to create order.", status=500)

#     # Step 4: Insert order details
#     insert_order_details_query = """
#         INSERT INTO accounts_checkout (order_id, customer_id, customer_email, full_address,
#                                            product_id, product_name, quantity, price, total_price)
#         SELECT o.order_id, c.customer_id AS customer_id, c.email AS customer_email,
#                CONCAT(a.city, ' ', a.street, ' ', a.house_number, ' ') AS full_address,
#                p.id AS product_id, p.name AS product_name, oi.quantity, oi.price,
#                SUM(oi.price * oi.quantity) AS total_price
#         FROM OrderTable o
#         JOIN accounts_OrderItem oi ON o.order_id = oi.order_id
#         JOIN accounts_Product p ON oi.product_id = p.id
#         JOIN accounts_Address a ON o.address_id = a.id
#         JOIN Customer c ON o.customer_id = c.customer_id
#         WHERE o.customer_id = %s
#         GROUP BY o.order_id, c.customer_id, c.email, a.city, a.street, a.house_number, p.id, p.name, oi.quantity, oi.price
#         ORDER BY o.order_id, p.id
#     """
#     execute_raw_sql(insert_order_details_query, [customer_id])

#     # Step 5: Clear cart
#     delete_cart_query = """
#         DELETE FROM Cart WHERE customer_id = %s
#     """
#     execute_raw_sql(delete_cart_query, [customer_id])

#     # Success message and redirect
#     messages.success(request, "Order placed successfully!")
#     return redirect('order_success')


def order_success(request):
     return render(request, 'order_success.html')

# customer/views.py


def button_works(request):
    return HttpResponse("Button works")

def contact (request):
    return redirect ('contact.html')


from django.shortcuts import render, redirect, HttpResponse
secret_key = 'somekey'

def index(request):
    products= [
        {"id": 1, "name": "Dojo T-shirt", 'price': 19.99 },
        {"id": 2, "name": "Dojo Sweater", 'price': 29.99},
        {"id": 3, "name": "Dojo cup", 'price': 4.99},
        {"id": 4, "name": "Algorithm Book", 'price': 49.99}
    ]
    request.session['products'] = products
    request.session['order_count'] = request.session.get('order_count', 0)
    request.session['total'] = request.session.get('total', 0)
    request.session['price'] = request.session.get('price', 0)
    return render(request, 'amadon/index.html')


def process(request):
    product_id = request.POST['product']
    quantity = request.POST['amount']

    products = request.session['products']
    for product in products:
        if product['id'] == int(product_id):
            request.session['total'] += (product['price'] * int(quantity))
            request.session['price'] = (product['price'] * int(quantity))
    
    counter = request.session['order_count']
    request.session['order_count'] = counter +1
    print request.session['total']
    print request.session['price']
    print request.session['order_count']

    return redirect('/amadon/checkout')

def checkout(request):
    return render(request,'amadon/checkout.html')


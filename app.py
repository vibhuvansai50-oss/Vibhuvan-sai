from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    products_list = [
        {
            'id': 1,
            'name': 'Dark Chocolate Bar',
            'description': '70% pure dark chocolate with intense flavor',
            'price': '$12.99',
            'image': '🍫'
        },
        {
            'id': 2,
            'name': 'Chocolate Truffles',
            'description': 'Handcrafted truffles with premium ingredients',
            'price': '$18.99',
            'image': '🎁'
        },
        {
            'id': 3,
            'name': 'Chocolate Spread',
            'description': 'Creamy and luxurious chocolate spread',
            'price': '$9.99',
            'image': '🫙'
        },
        {
            'id': 4,
            'name': 'Chocolate Beans',
            'description': 'Roasted chocolate beans with premium quality',
            'price': '$15.99',
            'image': '🌰'
        }
    ]
    return render_template('products.html', products=products_list)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

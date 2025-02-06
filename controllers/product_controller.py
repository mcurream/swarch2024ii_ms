from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from services.product_service import ProductService

product_blueprint = Blueprint('products', __name__)
@product_blueprint.route('/products', methods=['POST'])
def create_product():
    data = request.form
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'error': 'Name is required'}), 400
    
    ProductService.create_product(name, description)
    return redirect(url_for('products.index'))

@product_blueprint.route('/products/<int:product_id>', methods=['POST'])
def update_product(product_id):
    data = request.form
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    updated_product = ProductService.update_product(product_id, name, description)
    
    if not updated_product:
        return jsonify({'error': 'Product not found'}), 404

    return redirect(url_for('products.index'))

@product_blueprint.route('/')
def index():
    return render_template('index.html')
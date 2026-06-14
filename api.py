from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# File paths
MEMBERS_FILE = 'member_data.json'
INVENTORY_FILE = 'inventory_data.json'
ACCOUNTING_FILE = 'accounting_data.json'
SALARY_FILE = 'salary_data.json'

# ═══════════════════════════════════════
# MEMBERS API
# ═══════════════════════════════════════

@app.route('/api/members', methods=['GET'])
def get_members():
    """Get all members"""
    try:
        with open(MEMBERS_FILE, 'r', encoding='utf-8') as f:
            members = json.load(f)
        return jsonify(members), 200
    except:
        return jsonify([]), 200

@app.route('/api/members', methods=['POST'])
def create_member():
    """Create new member"""
    try:
        data = request.json
        with open(MEMBERS_FILE, 'r', encoding='utf-8') as f:
            members = json.load(f)
        
        # Generate member ID
        member_id = f"M{len(members) + 1:03d}"
        
        new_member = {
            "id": member_id,
            "name": data.get('name'),
            "email": data.get('email'),
            "password": data.get('password'),
            "age": data.get('age', 0),
            "gender": data.get('gender', ''),
            "coupon": 0,
            "point": 0,
            "total_spending": 0,
            "level": "bronze"
        }
        
        members.append(new_member)
        
        with open(MEMBERS_FILE, 'w', encoding='utf-8') as f:
            json.dump(members, f, indent=4, ensure_ascii=False)
        
        return jsonify(new_member), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/members/<member_id>', methods=['PUT'])
def update_member(member_id):
    """Update member"""
    try:
        data = request.json
        with open(MEMBERS_FILE, 'r', encoding='utf-8') as f:
            members = json.load(f)
        
        for member in members:
            if member['id'] == member_id:
                member.update(data)
                break
        
        with open(MEMBERS_FILE, 'w', encoding='utf-8') as f:
            json.dump(members, f, indent=4, ensure_ascii=False)
        
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# ═══════════════════════════════════════
# INVENTORY API
# ═══════════════════════════════════════

@app.route('/api/inventory', methods=['GET'])
def get_inventory():
    """Get all products"""
    try:
        with open(INVENTORY_FILE, 'r', encoding='utf-8') as f:
            inventory = json.load(f)
        return jsonify(inventory), 200
    except:
        return jsonify([]), 200

@app.route('/api/inventory', methods=['POST'])
def create_product():
    """Create new product"""
    try:
        data = request.json
        with open(INVENTORY_FILE, 'r', encoding='utf-8') as f:
            inventory = json.load(f)
        
        product_id = f"P{len(inventory) + 1:03d}"
        
        new_product = {
            "id": product_id,
            "name": data.get('name'),
            "price": data.get('price'),
            "stock": data.get('stock'),
            "category": data.get('category', 'Electronics'),
            "date": datetime.now().strftime("%Y-%m-%d")
        }
        
        inventory.append(new_product)
        
        with open(INVENTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(inventory, f, indent=4, ensure_ascii=False)
        
        return jsonify(new_product), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/inventory/<product_id>', methods=['PUT'])
def update_product(product_id):
    """Update product"""
    try:
        data = request.json
        with open(INVENTORY_FILE, 'r', encoding='utf-8') as f:
            inventory = json.load(f)
        
        for product in inventory:
            if product['id'] == product_id:
                product.update(data)
                break
        
        with open(INVENTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(inventory, f, indent=4, ensure_ascii=False)
        
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# ═══════════════════════════════════════
# ACCOUNTING API
# ═══════════════════════════════════════

@app.route('/api/accounting/transactions', methods=['GET'])
def get_transactions():
    """Get all transactions"""
    try:
        with open(ACCOUNTING_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify(data.get('transactions', [])), 200
    except:
        return jsonify([]), 200

@app.route('/api/accounting/balance', methods=['GET'])
def get_balance():
    """Get current balance"""
    try:
        with open(ACCOUNTING_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return jsonify({"balance": data.get('total_balance', 0)}), 200
    except:
        return jsonify({"balance": 0}), 200

@app.route('/api/accounting/transactions', methods=['POST'])
def add_transaction():
    """Add new transaction"""
    try:
        data = request.json
        with open(ACCOUNTING_FILE, 'r', encoding='utf-8') as f:
            accounting = json.load(f)
        
        transaction_id = f"T{len(accounting['transactions']) + 1:04d}"
        
        new_transaction = {
            "transaction_id": transaction_id,
            "type": data.get('type'),
            "amount": data.get('amount'),
            "description": data.get('description', ''),
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "items": data.get('items', []),
            "member_id": data.get('member_id')
        }
        
        accounting['transactions'].append(new_transaction)
        accounting['total_balance'] += new_transaction['amount']
        
        with open(ACCOUNTING_FILE, 'w', encoding='utf-8') as f:
            json.dump(accounting, f, indent=4, ensure_ascii=False)
        
        return jsonify(new_transaction), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# ═══════════════════════════════════════
# SALARY API
# ═══════════════════════════════════════

@app.route('/api/salary', methods=['GET'])
def get_salaries():
    """Get all worker salaries"""
    try:
        with open(SALARY_FILE, 'r', encoding='utf-8') as f:
            salaries = json.load(f)
        return jsonify(salaries), 200
    except:
        return jsonify([]), 200

@app.route('/api/salary', methods=['POST'])
def create_salary():
    """Create new worker salary"""
    try:
        data = request.json
        with open(SALARY_FILE, 'r', encoding='utf-8') as f:
            salaries = json.load(f)
        
        new_salary = {
            "worker_id": data.get('worker_id'),
            "worker_name": data.get('worker_name'),
            "worker_role": data.get('worker_role'),
            "base_salary": data.get('base_salary'),
            "hours_worked": data.get('hours_worked', 0),
            "bonus": data.get('bonus', 0),
            "deductions": data.get('deductions', 0)
        }
        
        salaries.append(new_salary)
        
        with open(SALARY_FILE, 'w', encoding='utf-8') as f:
            json.dump(salaries, f, indent=4, ensure_ascii=False)
        
        return jsonify(new_salary), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/salary/<worker_id>', methods=['PUT'])
def update_salary(worker_id):
    """Update worker salary"""
    try:
        data = request.json
        with open(SALARY_FILE, 'r', encoding='utf-8') as f:
            salaries = json.load(f)
        
        for salary in salaries:
            if salary['worker_id'] == worker_id:
                salary.update(data)
                break
        
        with open(SALARY_FILE, 'w', encoding='utf-8') as f:
            json.dump(salaries, f, indent=4, ensure_ascii=False)
        
        return jsonify({"success": True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# ═══════════════════════════════════════
# HEALTH CHECK
# ═══════════════════════════════════════

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)

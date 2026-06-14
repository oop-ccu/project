# 🚀 Running the Smart Store System

## Option 1: Web UI Only (Current)
The web UI is already running at `http://localhost:5174`

**Data Storage**: Currently stored in **browser memory only** - data will be lost on refresh

---

## Option 2: Web UI + API (Persistent Data)

To enable **persistent data storage** to JSON files, start the API server:

### Step 1: Install Python Dependencies
```bash
cd "c:\Users\user\Downloads\project-main\project-main"
pip install -r requirements.txt
```

### Step 2: Start the API Server
```bash
python api.py
```

The API will run on `http://localhost:5000`

### Step 3: Access Web UI
The web UI will automatically connect to the API at `http://localhost:5174`

---

## API Endpoints

### Members
- `GET /api/members` - Get all members
- `POST /api/members` - Create new member
- `PUT /api/members/<member_id>` - Update member

### Inventory
- `GET /api/inventory` - Get all products
- `POST /api/inventory` - Create new product
- `PUT /api/inventory/<product_id>` - Update product

### Accounting
- `GET /api/accounting/balance` - Get current balance
- `GET /api/accounting/transactions` - Get all transactions
- `POST /api/accounting/transactions` - Record transaction

### Salary
- `GET /api/salary` - Get all salaries
- `POST /api/salary` - Create new salary
- `PUT /api/salary/<worker_id>` - Update salary

---

## How It Works

1. **Register Member**: 
   - Web UI registers "jay" → Sends to API → API saves to `member_data.json`

2. **Checkout**:
   - Web UI processes payment → Sends transaction to API → API updates `inventory_data.json` & `accounting_data.json`

3. **Worker Portal**:
   - Worker logs hours → API updates `salary_data.json`

---

## Data Persistence Flow

```
Web UI (React) 
    ↓
API Server (Flask) 
    ↓
JSON Files
    ├── member_data.json
    ├── inventory_data.json
    ├── accounting_data.json
    └── salary_data.json
```

**With API**: Data survives page refresh ✅  
**Without API**: Data lost on refresh ❌

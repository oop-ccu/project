

## 🚀 Quick Start
## unzip smart-store.zip

To start both the **API Server** and **Web UI** with a single command:



### Windows Users
**Option 1 - Batch File (Easiest)**
```bash
start-system.bat
```

**Option 2 - PowerShell**
```powershell
.\start-system.ps1
```

### macOS/Linux Users
```bash
python api.py &
cd smart-store && npm run dev
```

This will:
- ✅ Start API Server on `http://localhost:5000`
- ✅ Start Web UI on `http://localhost:5173`
- ✅ Data persists to JSON files
- ✅ Ready for sign in with `victor@gmail.com` / `12345678`

---



## 📋 Manual Setup (If Preferred)




預計系統架構：

```text
smart_store_system/
│
├── ui/
│   ├── owner_ui.py
│   ├── worker_ui.py
│   └── customer_ui.py
│
├── systems/
│   ├── member_system/
│   │   ├── member_system.py
│   │   └── member_data.json
│   │
│   ├── inventory_system/
│   │   ├── inventory_system.py
│   │   └── inventory_data.json
│   │
│   ├── accounting_system/
│   │   ├── accounting_system.py
│   │   └── accounting_data.json
│   │
│   ├── salary_system/
│   │   ├── salary_system.py
│   │   └── salary_data.json
│   │
│   └── checkout_system/
│       └── checkout_system.py
│
└── README.txt

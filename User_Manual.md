
## 📖 Smart Store System - User Manual

Welcome to the Smart Store System! This system features both a modern graphical Web User Interface (Web UI) and a Command Line Interface (CLI), providing dedicated interactive environments for three distinct roles: Customer, Worker, and Owner.


---

## 🛍️ 2. Customer Portal

The Customer Portal is designed for general consumers, providing features for browsing products, managing the shopping cart, and accessing the member profile.

### 2.1 Registration & Login

* **Register:** Click `Register` in the top right corner. Fill in your name, email, and password. The system will automatically verify if the email is already registered.
* **Sign In:** Click `Sign In` and enter your credentials.
*(Demo Account: `alice@demo.com` / Password: `1234`)*

### 2.2 Shopping & Checkout

1. **Browse Products:** Use the search bar or category filters (e.g., Electronics, Network) on the homepage to find items quickly.
2. **Add to Cart:** Click the `Add to Cart` button on any product card.
3. **Cart & Discounts:** Click `Cart` in the top right corner to open the side panel. If you are logged in, the system will **automatically apply your exclusive member discount** based on your tier:
* 🥉 Bronze: No discount
* 🥈 Silver: 5% off
* 🥇 Gold: 10% off
* 💎 VIP: 15% off


4. **Checkout:** Click `Proceed to Checkout`. Enter your payment amount; the system will calculate your change and automatically update your accumulated spending and reward points.

---

## ⚙️ 3. Worker Portal

The Worker Portal is tailored for store staff to manage daily inventory and track their personal payroll status. Switch to this view by clicking "⚙ Worker" at the bottom of the page.

### 3.1 Worker Login

* Please log in using your specific **Worker ID**.
*(Demo IDs: `W001`, `W002`, `W003`)*

### 3.2 Dashboard & Work Hours

* **View Salary:** The dashboard displays your Base Salary, Hours Worked, and the currently estimated "Net Salary" in real-time.
* **Log Work Hours:** Enter the number of hours worked today in the `Log Work Hours` section and submit. The system will instantly update your payroll object's state.

### 3.3 Inventory Management

* Navigate to the Inventory tab to view all current store products and stock levels.
* **Add New Item:** Fill in the Item Name, Category, Price, and Stock Qty, then click `Add Item` to immediately publish the new product to the customer storefront.

---

## 👔 4. Owner Dashboard

The Owner Dashboard is the highest-privilege control center of the system, offering comprehensive data analysis, financial ledgers, and HR management tools. Switch to this view by clicking "👔 Owner" at the bottom of the page.

### 4.1 System Login

* Log in using the administrator credentials: Username `admin` / Password `admin`.

### 4.2 Operations & Management

1. **Store Overview (Dashboard):**
* **Real-time Metrics:** Instantly monitor the current company Balance, Total Revenue, and Total Expense.
* **Store Indicators:** Displays the live count of Total Members, Product Types, and Workers.
* **Record Expense:** Manually input store expenses (e.g., utility bills, rent), which will automatically be deducted from the main balance.


2. **Transactions:**
* A complete ledger tracking all cash flows, including customer purchases (Checkout revenue) and salary/operational payouts (Expense). Every record includes a timestamp and detailed item descriptions.


3. **Members:**
* View the roster of all registered members, their current Level, Reward Points, and Total Amount Spent.


4. **Inventory:**
* Besides checking stock quantities, the system automatically calculates the "Total Value" for each product type, aiding in asset evaluation.


5. **Salary Management:**
* **Add Worker:** Create profiles for new employees by inputting their ID, Name, Role, and Base Salary.
* **One-Click Payroll (Safeguard Feature):** Click the `Pay` button next to an employee. The system will **automatically deduct the net salary from the company balance** and immediately **reset the worker's logged hours to zero**, preventing duplicate payroll errors.



---

## 💻 5. CLI Alternative (Terminal Mode)

If you are operating in an environment without a web browser, the system provides a fully functional, text-based Command Line Interface.

* **Customer System:** Open your terminal and run `python customer_ui.py`
* **Worker System:** Open your terminal and run `python worker_ui.py`
* **Owner System:** Open your terminal and run `python owner_ui.py`

All operations executed in the CLI mode (such as registering, checking out, or paying salaries) are persistently stored via `JSON` files and are 100% synchronized with the Web UI.

---

**🛡️ Data Consistency Statement:** This system features highly modular architecture and robust data consistency safeguards. Whether a checkout occurs on the Customer portal or a salary is distributed on the Owner dashboard, the system automatically triggers cross-module updates to the inventory and accounting databases, ensuring absolute reliability and data integrity.

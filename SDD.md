Here is the English translation of your system architecture document, formatted for readability:

## 1. System Architecture Design

This system adopts a modular and prototype microservices architecture. The system is divided into a pure backend logic layer, a terminal-based frontend interface layer, and a Flask API gateway responsible for external connections.

### 1.1 Core Modules

* **`accounting_system.py`**: Accounting module; handles total balance calculations, as well as adding and reading transaction records.
* **`salary_system.py`**: Salary module; contains the `Salary` class, responsible for updating work hours and calculating net salary (base salary + bonus - deductions).
* **`inventory_system.py`**: Inventory module; contains the `Item` class, managing product names, quantities, and total values.
* **`member_system.py`**: Member module (inferred from code); handles member authentication and discount logic.
* **`checkout_system.py`**: Checkout core; coordinates the inventory, member, and accounting systems to complete transactions.

### 1.2 UI Layer

* **`owner_ui.py`**: Calls the accounting, salary, member, and inventory modules to serve as an integrated dashboard for the store manager.
* **`worker_ui.py`**: Depends on `salary_system` to provide a terminal interface for employee self-management.
* **`customer_ui.py`**: Depends on `member_system` to provide a customer operation interface.

### 1.3 API Layer

* **`api.py`**: Implemented using Flask, it wraps JSON database read/write operations into HTTP endpoints and supports Cross-Origin Resource Sharing (CORS).

---

## 2. Database Design

The system uses local JSON files for data storage. The structural layout for each file is as follows:

* **`accounting_data.json`**
* `total_balance` (Float): Current total account balance.
* `transactions` (List): Array of transaction details, including `transaction_id`, `type` (revenue/expense/checkout revenue), `amount`, `description`, `date`, `items`, and `member_id`.


* **`salary_data.json`**
* Contains an array of employee objects: `worker_id`, `worker_name`, `worker_role`, `base_salary`, `hours_worked`, `bonus`, and `deductions`.


* **`inventory_data.json`**
* Contains an array of product objects: `id`/`name`, `quantity`/`stock`, `value`/`price`, `total_value`, and `date`.


* **`member_data.json`**
* Contains an array of member objects: `id`, `name`, `email`, `password`, `age`, `gender`, `level`, and `total_spending`.



---

## 3. System Interaction Flow Design (Sequence & Logic)

### 3.1 Checkout Flow

The `CheckoutSystem` acts as a Facade (Facade Pattern), hiding the complexity of multi-system interactions.

1. **Scan Item:** `scan_item()` calls `inventory_system.get_item()` to verify inventory availability; upon success, the item is added to the `cart`.
2. **Bind Member:** `set_member()` calls `member_system.get_member()` to retrieve member information and the applicable discount rate.
3. **Calculate Total:** `calculate_total()` calculates (`product unit price` * `quantity`) * `member discount rate`.
4. **Process Payment (`process_payment`):**
* Notifies `inventory_system` to decrease stock (`reduce_stock`).
* Encapsulates the transaction record and sends it to `accounting_system.add_transaction()`.
* Empties the shopping cart and returns the change amount.



### 3.2 Salary Payment Flow

1. The store manager enters the Worker ID in `owner_ui` to query the employee record (`ss.check_salary_data`).
2. Calls `worker.calculate_net_salary()` to retrieve the total amount to be paid.
3. Invokes `accounting.record_expense()` to log the salary as a store expense; the accounting system automatically updates the balance and saves it to the JSON file.
4. Resets the `hours_worked`, `bonus`, and `deductions` attributes within that employee's `Salary` object to `0`.
5. Calls `ss.save_salaries()` to overwrite `salary_data.json`, completing the payment process.

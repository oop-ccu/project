
# Smart Store System Project Document

### 1. Introduction

This document defines the functional and non-functional requirements of the "Smart Store System." The system aims to provide a lightweight, integrated management solution for physical or online stores, covering member management, inventory management, employee salaries, accounting, and checkout operations.

### 2. User Roles

* **Store Manager/Owner (Owner):** Possesses the highest permissions, responsible for viewing the overall operational status of the store, distributing salaries, and reviewing transaction details.
* **Employee (Worker):** Responsible for daily operational tasks (e.g., clocking in/reporting hours, checkout, inventory management).
* **Customer/Member (Customer):** The store's consumers, who can register accounts, log in, and maintain personal profiles.

---

### 3. Functional Requirements

#### 3.1 Owner Functions (Owner UI)

* **Secure Login:** The manager must log into the system using default credentials (`admin`/`admin`).
* **Store Overview (Dashboard):** Provides a one-click view of the store's total balance, total member count, total types of inventory items, and total employee count.
* **Accounting Management:**
* View the current total revenue and account balance.
* View historical transaction details (including income and expense records).


* **Salary Management:**
* Query salary details based on the Worker ID.
* Calculate and issue salaries; the system must automatically link salary payment records to the accounting system (recorded as an expense) and automatically reset the employee's monthly work hours and bonus/deduction records.



#### 3.2 Employee Functions (Worker UI)

* **Employee Login:** Employees must enter their unique Worker ID to log in.
* **Salary & Personal Profile:** View individual base salary, hours worked, bonuses, deductions, and the net salary to be paid this month.
* **Work Hour Reporting:** Employees can manually enter and update their work hours.
* *(Future Expansion)*: Access inventory management modules and the cash register checkout system.

#### 3.3 Customer/Member Functions (Customer UI)

* **Member Registration:** Create a new member profile.
* **Member Login:** Log in via Email and password.
* **Account Maintenance:** View personal profile, update personal information, and change passwords.

#### 3.4 Checkout System

* **Shopping Cart Management:** Supports scanning Item IDs to add to the cart and checks if there is sufficient stock based on the quantity.
* **Member Discounts:** Allows binding a Member ID during checkout; the system must automatically calculate discounts based on the member's tier.
* **Transaction Processing:**
* Calculate the total amount and verify if the payment amount is sufficient.
* Automatically deduct product inventory upon checkout completion.
* Automatically import transaction records and revenue into the accounting system.



#### 3.5 API Services (RESTful API)

* The system must provide a Flask-based REST API supporting CRUD (Create, Read, Update, Delete) operations by frontends or external systems for the following resources:
* `/api/members` (Member data)
* `/api/inventory` (Inventory data)
* `/api/accounting/...` (Accounting and transaction records)
* `/api/salary` (Employee salary data)



---

### 4. Non-Functional Requirements

* **Data Storage:** Utilizes lightweight JSON files as the local database, ensuring the system can run without the need to install an additional relational database.
* **User Interface:** Currently relies primarily on a text-based Command-Line Interface (CLI), providing a screen-switching experience through clear-screen commands (`cls` or `clear`).
* **System Architecture:** Adopts a modular design where each subsystem operates independently, with inter-system communication handled via dependency injection or APIs.

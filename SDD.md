
# Software Design Description (SDD) - Smart Store System

## 1. Introduction

### 1.1 Purpose
The purpose of this document is to provide a comprehensive architectural and detailed design description of the **Smart Store System**. It serves as a blueprint for developers to understand the system modules, data structures, and interactions between the frontend, backend, and persistence layers.

### 1.2 System Scope
The Smart Store System is an integrated retail management platform. It facilitates:
*   **Membership Management**: Registration, profile updates, and tiered loyalty discounts.
*   **Inventory Control**: Stock monitoring, product entry, and automatic stock reduction.
*   **Accounting & Finance**: Revenue tracking, expense recording, and real-time balance calculation.
*   **Human Resources**: Worker shift logging, salary calculation, and payroll integration.
*   **Checkout System**: Point-of-Sale (POS) logic integrating members, inventory, and accounting.

---

## 2. System Architecture

### 2.1 Architectural Overview
The system follows a **Modular Layered Architecture** with a decoupled frontend and backend.

1.  **Presentation Layer**: 
    *   **CLI UIs**: Python-based terminal interfaces for local management (`owner_ui`, `worker_ui`, `customer_ui`).
    *   **Web UI**: A modern React-based dashboard for customers and staff.
2.  **API Layer (Flask)**: `api.py` acts as the bridge, exposing RESTful endpoints for the web frontend to interact with the backend logic.
3.  **Business Logic Layer**: Core Python modules (`member_system`, `inventory_system`, etc.) containing the "brain" of the store.
4.  **Data Persistence Layer**: Lightweight JSON-based storage (`.json` files).

### 2.2 Component Interaction
The **Checkout System** serves as the central orchestrator. When a transaction occurs:
*   It queries the **Member System** for discount rates.
*   It updates the **Inventory System** to reduce stock levels.
*   It logs the final amount into the **Accounting System**.

---

## 3. Detailed Module Design

### 3.1 Member System (`member_system.py`)
*   **Class**: `member`
*   **Attributes**: `id`, `name`, `email`, `password`, `age`, `gender`, `level` (Bronze/Silver/Gold/VIP).
*   **Responsibilities**: 
    *   Authenticating users.
    *   Managing loyalty points and total spending history.
    *   Calculating tier-based discounts.

### 3.2 Inventory System (`inventory_system.py`)
*   **Class**: `item`
*   **Attributes**: `id`, `name`, `quantity`, `price`, `category`, `date`.
*   **Responsibilities**:
    *   Tracking product stock levels.
    *   Handling batch updates for item information.
    *   Providing product data to the Checkout module.

### 3.3 Accounting System (`accounting_system.py`)
*   **Class**: `AccountingSystem`
*   **Data Structure**: A ledger containing a `total_balance` and a list of `transactions`.
*   **Responsibilities**:
    *   `record_revenue()`: Adds positive cash flow.
    *   `record_expense()`: Deducts costs (Rent, Salaries, etc.).
    *   `add_transaction()`: Stores detailed purchase records including itemized lists.

### 3.4 Salary System (`salary_system.py`)
*   **Class**: `Salary`
*   **Attributes**: `worker_id`, `base_salary`, `hours_worked`, `bonus`, `deductions`.
*   **Responsibilities**:
    *   Calculating net pay: `(Base + Bonus - Deductions)`.
    *   Allowing workers to log hours.
    *   Interfacing with Accounting to deduct payroll from the store balance.

### 3.5 Checkout System (`checkout_system.py`)
*   **Functionality**: Orchestrates the POS flow.
*   **Logic Flow**:
    1.  **Scan**: Verify item exists and check stock.
    2.  **Identify**: Apply member discounts.
    3.  **Execute**: atomicaly update Stock (-), Member Spending (+), and Accounting Ledger (+).

---

## 4. Data Design (Persistence)

The system uses JSON files for persistence to ensure data survives application restarts.

| File Name | Purpose | Key Fields |
| :--- | :--- | :--- |
| `member_data.json` | Member database | email, password, total_spending, level |
| `inventory_data.json` | Product catalog | id, name, price, stock |
| `accounting_data.json` | Financial ledger | total_balance, transaction_history |
| `salary_data.json` | Employee payroll | worker_id, hours_worked, net_salary |

---

## 5. Interface Design

### 5.1 User Roles
1.  **Owner**: Access to the high-level dashboard, financial reports, and payroll management.
2.  **Worker**: Access to inventory management, hour reporting, and checkout processing.
3.  **Customer**: Access to product browsing, profile editing, and self-checkout.

### 5.2 API Design (REST)
*   `GET /api/members`: Fetch all member profiles.
*   `POST /api/inventory`: Add new stock items.
*   `POST /api/accounting/transactions`: Log a new revenue or expense entry.
*   `PUT /api/salary/<worker_id>`: Update work hours or bonus.

---

## 6. System Integrity & Maintenance

1.  **Data Synchronization**: Every module re-loads its JSON file before critical operations (Read-before-Write) to ensure multi-interface consistency.
2.  **Error Handling**: Built-in validation for `ValueError` (invalid amounts) and `JSONDecodeError` (corrupted files).
3.  **Initialization**: `database.py` ensures that all required JSON files exist upon system startup.

---
**Date:** May 2024  
**Version:** 1.0.0  
**Status:** Approved for Implementation

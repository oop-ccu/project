

# Software Requirements Specification (SRS)
## Smart Store Integration Platform

**Document Control**
| Document Information | |
| :--- | :--- |
| **Title** | Software Requirements Specification for Smart Store Integration Platform |
| **Date** | June 16, 2024 |
| **Status** | Draft |
| **Version** | 1.0 |


---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) document provides a comprehensive description of the **Smart Store Integration Platform**. The platform integrates membership loyalty, inventory control, automated accounting, and personnel payroll into a single ecosystem to enhance operational efficiency for retail businesses.

### 1.2 Document Conventions
This document follows these conventions:
| Term | Description |
| :--- | :--- |
| **SHALL** | Refers to a mandatory requirement that must be fulfilled in Phase 1. |
| **SHOULD** | Indicates a requirement for Phase 2 (Scalability). |
| **MAY** | Refers to an optional requirement anticipated for future phases. |
| **FR-XX** | Functional Requirements identifier. |
| **NFR-XX** | Non-Functional Requirements identifier. |

### 1.3 Project Scope
The platform serves as the core management system for a retail store, integrating:
*   **User Management**: Tiered membership and staff profiles.
*   **Inventory Management**: Real-time SKU tracking and automated updates.
*   **Accounting Ledger**: Automated revenue/expense logging and balance tracking.
*   **Personnel System**: Work hour reporting and payroll automation.
*   **Checkout Engine**: Cross-modular coordination of sales and data synchronization.

---

## 2. Overall Description

### 2.1 Product Perspective
The Smart Store Platform is a standalone system utilizing a Python backend and a React-based frontend. It interacts with lightweight JSON databases to ensure data persistence without the overhead of heavy SQL servers. It is designed to interface with:
*   **Internal Databases**: `member_data.json`, `inventory_data.json`, `accounting_data.json`, and `salary_data.json`.
*   **External APIs**: Future payment gateways (e.g., LINE Pay, Stripe).

### 2.2 Product Functions
1.  **Member Management**: Automated tier assignment (Bronze to VIP) based on spending.
2.  **Inventory Control**: CRUD operations for products and real-time stock deduction.
3.  **Transaction Processing**: POS logic that links customer data to accounting.
4.  **Payroll Automation**: Converts work hours into accounting expenses.

### 2.3 User Classes and Characteristics
*   **Customers**: Access profiles, view membership levels, and track spending history.
*   **Workers**: Manage inventory, process checkouts, and report work hours.
*   **Owners (Admin)**: Review financial dashboards, approve payroll, and manage system settings.

---

## 3. System Features and Functional Requirements

### 3.1 Member Management and Authentication
| ID | Requirement Description |
| :--- | :--- |
| **FR-01** | The system **SHALL** provide a self-registration process for customers via Email. |
| **FR-02** | The system **SHALL** automatically assign membership levels (Bronze, Silver, Gold, VIP) based on the `total_spending` attribute. |
| **FR-03** | The system **SHALL** calculate real-time discounts during checkout based on the member's tier. |
| **FR-04** | The system **SHALL** validate that no duplicate emails are used during registration. |

### 3.2 Inventory Management
| ID | Requirement Description |
| :--- | :--- |
| **FR-05** | The system **SHALL** support CRUD operations for inventory items (name, quantity, price, category). |
| **FR-06** | The system **SHALL** automatically reduce stock counts upon the completion of a checkout transaction. |
| **FR-07** | The system **SHOULD** provide an "Interested List" or favorites feature for items. |

### 3.3 Accounting and Checkout Integration
| ID | Requirement Description |
| :--- | :--- |
| **FR-08** | The system **SHALL** block transactions if the requested item quantity exceeds current inventory stock. |
| **FR-09** | The system **SHALL** record every successful checkout as a "Revenue" entry in the accounting ledger. |
| **FR-10** | The system **SHALL** generate a unique Transaction ID (e.g., T0001) for every record for audit purposes. |

### 3.4 Salary and Staff Management
| ID | Requirement Description |
| :--- | :--- |
| **FR-11** | The system **SHALL** allow workers to report work hours which are then stored in the salary database. |
| **FR-12** | When payroll is executed, the system **SHALL** deduct the amount from the store's total balance and reset the worker's monthly hours to zero. |

---

## 4. External Interface Requirements

### 4.1 User Interfaces
*   **Customer Portal**: Responsive web design showcasing featured products and member status.
*   **Owner CLI**: A terminal-based administrative interface for fast-access financial reporting.
*   **Dashboard**: A React-driven visual interface displaying Balance, Total Members, and Stock levels.

### 4.2 Software Interfaces
*   **RESTful API**: Communication between frontend and backend via Flask.
*   **JSON Schema**: All modules must adhere to standardized JSON formats for interoperability.

---

## 5. Non-Functional Requirements

### 5.1 Performance Requirements
*   **NFR-01**: The system **SHALL** process checkout operations and database updates within 2 seconds.
*   **NFR-02**: Page load times for the inventory dashboard **SHALL** be less than 3 seconds under normal load.

### 5.2 Security Requirements
*   **NFR-03**: The system **SHALL** implement Role-Based Access Control (RBAC) to differentiate Owner and Worker permissions.
*   **NFR-04**: Session management **SHALL** include configurable timeout settings for the web interface.

### 5.3 Reliability and Maintainability
*   **NFR-05**: The system **SHALL** maintain data integrity using "Read-before-Write" protocols to prevent data loss during concurrent access.
*   **NFR-06**: The system **SHALL** support modular architecture, allowing for the update of the Inventory module without affecting the Salary module.

---

## 6. Appendix: Analysis Models

### 1) Context Diagram (Level 0)
The **Smart Store Integration Platform** sits at the center, interacting with:
*   **Members**: Sending discount data, receiving payment.
*   **Accounting Ledger**: Receiving transaction logs.
*   **Inventory**: Sending stock reduction commands.

### 2) Process Flow Diagram: Checkout
1.  **Scan Item**: Verify stock in `inventory_data.json`.
2.  **Verify Member**: Fetch level from `member_data.json`.
3.  **Calculate**: Apply discount logic.
4.  **Finalize**: Update Inventory (-), Member Spending (+), and Accounting Ledger (+).





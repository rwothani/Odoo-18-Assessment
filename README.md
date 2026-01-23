# Odoo Multi-Vendor RFQ Module

## 1. Project Overview

This project involves the design and implementation of a **custom Odoo 18 module** that extends the existing **Purchases** application to support **multi-vendor Requests for Quotation (RFQs)**, bid management and structured purchase requests.

The module addresses a common procurement gap where organizations need to:

* Send a single RFQ to multiple vendors
* Receive and compare vendor bids
* Select a winning bid transparently
* Convert approved bids into Purchase Orders

The project is developed as part of a technical assessment and emphasizes **clean system design, correct data modeling and incremental progress** rather than feature completeness.

---

## 2. Objectives

The key objectives of this project are:

* Extend Odoo 18 Purchases functionality without modifying core modules
* Enable assignment of RFQs to multiple vendors
* Model and manage vendor bids linked to a single RFQ
* Allow selection of a single winning bid per RFQ
* Introduce a Purchase Request workflow that prepares RFQs internally

---

## 3. Functional Requirements

### 3.1 Purchase Request Module

* Users can create a **Purchase Request** internally
* A purchase request includes:

  * Requester
  * Department
  * Requested products
  * Quantities
  * Request status
* Purchase Requests can be converted into RFQs

### 3.2 Multi-Vendor RFQs

* A single RFQ can be assigned to **multiple vendors**
* Vendors are not required to all respond
* RFQs follow the standard Odoo workflow (Draft → Sent → Confirmed)

### 3.3 Vendor Bids

* Vendors submit **bids** in response to an RFQ
* Each RFQ can have **multiple bids** (one-to-many relationship)
* Each bid captures:

  * Vendor
  * Bid price
  * Delivery lead time
  * Bid status

### 3.4 Bid Selection

* Users can select **one winning bid per RFQ**
* The system prevents multiple winning bids
* The selected bid is used to proceed with Purchase Order creation

---

## 4. Non-Functional Requirements

* The module must be compatible with **Odoo 18**
* Code must follow Odoo development best practices
* The solution must be modular and extensible
* Partial functionality must remain stable and testable

---

## 5. Tools and Technologies

* **Operating System:** Ubuntu 22.__ WSL
* **ERP Framework:** Odoo 18
* **Database:** PostgreSQL
* **Language:** Python
* **Frontend:** XML (Odoo Views)
* **Version Control:** Git & GitHub

---

## 6. System Architecture (High-Level)

* Custom Odoo module extending `purchase` app
* New models for:

  * Purchase Request
  * Vendor Bid
* Existing models extended where necessary:

  * Purchase Order (RFQ)
* ORM-based relationships (Many2one, One2many)

---

## 7. Workflow Description

### Step 1: Purchase Request Creation

* Internal user creates a Purchase Request
* Request includes products and required quantities
* Request is reviewed and approved internally

### Step 2: RFQ Preparation

* Approved Purchase Request generates an RFQ
* RFQ is prepared internally before vendor assignment

### Step 3: Vendor Assignment

* Multiple vendors are assigned to the RFQ
* RFQ is sent to selected vendors

### Step 4: Bid Submission

* Vendors respond with bids
* Each bid is linked to the RFQ
* RFQ displays all received bids

### Step 5: Bid Evaluation & Selection

* User compares bids (price, delivery time)
* One bid is selected as the winning bid

### Step 6: Purchase Order Finalization

* Winning bid is used to generate a Purchase Order
* Standard Odoo post-PO workflows apply (delivery, invoicing)

---

## 8. Development Timeline (12-Day Plan)

### Day 1: Environment Setup

* Install Ubuntu 22.__WSL
* Install PostgreSQL
* Install and run Odoo 18

### Day 2: Odoo Familiarization

* Study Purchases module
* Review RFQ and PO workflows
* Identify extension points

### Day 3: Module Scaffolding

* Create custom module structure
* Define manifest and dependencies

### Day 4: Purchase Request Model

* Implement Purchase Request model
* Define fields and states

### Day 5: Purchase Request Views

* Create form and list views
* Add basic actions and buttons

### Day 6: RFQ Integration

* Implement RFQ preparation logic
* Link Purchase Requests to RFQs

### Day 7: Vendor Assignment Logic

* Enable multiple vendors per RFQ
* Update RFQ views accordingly

### Day 8: Bid Model Implementation

* Create Vendor Bid model
* Define relationships to RFQ and vendors

### Day 9: Bid Views & Data Entry

* Display bids on RFQ form
* Enable bid creation and editing

### Day 10: Bid Selection Logic

* Implement winning bid selection
* Enforce single-winner rule

### Day 11: Access Rights & Cleanup

* Define access control rules
* Clean up UI labels and workflows

### Day 12: Documentation & Final Review

* Write README and usage notes
* Commit final code
* Prepare repository for submission

---

## 9. Deliverables

* Fully functional Odoo custom module
* Source code hosted on GitHub
* README and technical documentation
* Clear commit history showing progress


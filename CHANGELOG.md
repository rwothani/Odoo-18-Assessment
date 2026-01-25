All notable changes to this project are documented in this file.

## Day 1 – Environment Setup
**Date:** 2026-01-23
- Installed Ubuntu 22.__ dependencies for Odoo 18
- Installed PostgreSQL and PostgreSQL client
- Set up Python tooling and build dependencies
- Verified development environment readiness
- Created README containing functional and Non-Functional requirements.
- Created PostgreSQL role for Odoo with createdb privileges


## Day 2 – Environment Correction
**Date:** 2026-01-23
- Identified Python 3.10 incompatibility with Odoo 18
- Installed Python 3.11
- Recreated virtual environment using Python 3.11
- Reinstalled Odoo 18 dependencies inside the new Python 3.11 environment.
- Verified that Odoo 18 now runs without Python-related import errors.
- Set PYTHONPATH permanently in virtual environment activation script for smooth Odoo startup.
- Successfully started Odoo 18 server using python odoo-bin -c ../odoo.conf 
- Observed PostgreSQL authentication errors; identified need to set proper database credentials.



## Day 3 – Environment Stabilization & Core App Setup
**Date:** 2026-01-24
- Verified Odoo server startup.
- Enabled Developer Mode in Odoo UI.
- Installed and activated the **Purchases** core module from Apps.
- Created initial project repository structure.
- modified `.gitignore` 
### Issues Encountered
- Purchase module initially unavailable until core dependencies were resolved.
- Odoo redirected to `/odoo/discuss` after module installation (expected behavior).
### Outcome
- Odoo backend and web interface fully operational.
- Purchase module successfully installed and accessible.
- Environment deemed stable for custom module development.



## Day 4 – Custom Module Scaffolding & Model Design
**Date:** 2026-01-25
- Created `custom_addons/` directory for custom development.
- Scaffolded custom module: **purchase_request**
- Implemented module structure:
custom_addons/purchase_request/
├── init.py
├── manifest.py
├── models/
│ ├── init.py
│ ├── purchase_request.py
│ └── purchase_request_line.py
├── views/
├── security/
└── data/

- Defined core business models:
- `purchase.request`
- `purchase.request.line`
- Implemented One-to-Many relationship:
- One Purchase Request → Multiple Request Lines
- Linked request lines to existing Odoo models:
- `product.product`
- `uom.uom`
- Declared dependency on the core `purchase` module in manifest.



## Day 5 – UI Enablement & Odoo 18 Compatibility
- Purchase Request user interface under the Purchase module
- List and Form views for `purchase.request`
- Menu item and window action for Purchase Requests
- Editable request lines embedded in the form view
- Access control rules for custom models

### Changed
- Updated view definitions to comply with **Odoo 18 view architecture**
  - Replaced deprecated `tree` view type with `list`
- Configured action window to support multiple view modes (`list,form`)
- Confirmed correct module metadata and dependencies in `__manifest__.py`

### Fixed
- Resolved `FileNotFoundError` caused by incorrect `addons_path` configuration
- Fixed XML `ParseError` due to invalid root view type (`tree`)
- Fixed frontend `UncaughtPromiseError` by aligning action view modes with available views
- Addressed server conflicts caused by running multiple Odoo instances simultaneously

### Verified
- Module installs successfully from Apps
- List view opens correctly under Purchases → Purchase Requests
- Form view loads and supports line item creation
- No registry, ORM, or JS errors after upgrade
- Odoo server restarts cleanly after changes

### Outcome
- Purchase Request feature is now visible and usable in the UI
- Stable foundation established for:
  - Workflow states
  - RFQ generation
  - Multi-vendor bidding logic




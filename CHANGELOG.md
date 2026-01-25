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


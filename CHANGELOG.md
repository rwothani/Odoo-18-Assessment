## Day 1 – Environment Setup
- Installed Ubuntu 22.__ dependencies for Odoo 18
- Installed PostgreSQL and PostgreSQL client
- Set up Python tooling and build dependencies
- Verified development environment readiness
- Created README containing functional and Non-Functional requirements.
- Created PostgreSQL role for Odoo with createdb privileges


## Day 2 – Environment Correction
- Identified Python 3.10 incompatibility with Odoo 18
- Installed Python 3.11
- Recreated virtual environment using Python 3.11
- Reinstalled Odoo 18 dependencies inside the new Python 3.11 environment.
- Verified that Odoo 18 now runs without Python-related import errors.
- Set PYTHONPATH permanently in virtual environment activation script for smooth Odoo startup.
- Successfully started Odoo 18 server using python odoo-bin -c ../odoo.conf 
- Observed PostgreSQL authentication errors; identified need to set proper database credentials.

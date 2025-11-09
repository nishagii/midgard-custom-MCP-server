"""
HR Management MCP Server (Full Mock Version)
--------------------------------------------
Run:
    uv run server hr_mcp stdio
"""

from mcp.server.fastmcp import FastMCP
from datetime import datetime

# Initialize the MCP server
mcp = FastMCP("HRManagement")

# Mock employee database
EMPLOYEES = [
    {
        "id": 1,
        "name": "Alice Johnson",
        "role": "Software Engineer",
        "department": "Engineering",
        "email": "alice@company.com",
        "salary": 80000,
        "leave_balance": 12,
        "last_updated": datetime.now().isoformat(),
    },
    {
        "id": 2,
        "name": "Bob Smith",
        "role": "HR Manager",
        "department": "Human Resources",
        "email": "bob@company.com",
        "salary": 90000,
        "leave_balance": 8,
        "last_updated": datetime.now().isoformat(),
    },
    {
        "id": 3,
        "name": "Charlie Brown",
        "role": "Data Analyst",
        "department": "Analytics",
        "email": "charlie@company.com",
        "salary": 75000,
        "leave_balance": 15,
        "last_updated": datetime.now().isoformat(),
    },
]


# ───────────────────────────────
# 🧰 TOOL 1: Get all employees
# ───────────────────────────────
@mcp.tool()
def get_all_employees() -> list:
    """
    Fetch a list of all employees.

    Returns:
        list: All employee records
    """
    return EMPLOYEES


# ───────────────────────────────
# 🧰 TOOL 2: Get employee by ID
# ───────────────────────────────
@mcp.tool()
def get_employee_by_id(emp_id: int) -> dict:
    """
    Retrieve employee details by ID.

    Args:
        emp_id (int): Employee ID

    Returns:
        dict: Employee data or error message
    """
    for emp in EMPLOYEES:
        if emp["id"] == emp_id:
            return emp
    return {"error": f"Employee with ID {emp_id} not found"}


# ───────────────────────────────
# 🧰 TOOL 3: Update employee role
# ───────────────────────────────
@mcp.tool()
def update_employee_role(emp_id: int, new_role: str) -> str:
    """
    Update an employee's role/title.

    Args:
        emp_id (int): Employee ID
        new_role (str): New job title

    Returns:
        str: Status message
    """
    for emp in EMPLOYEES:
        if emp["id"] == emp_id:
            old_role = emp["role"]
            emp["role"] = new_role
            emp["last_updated"] = datetime.now().isoformat()
            return f"✅ Updated {emp['name']}'s role from '{old_role}' to '{new_role}'."
    return "❌ Employee not found."


# ───────────────────────────────
# 🧰 TOOL 4: Add a new employee
# ───────────────────────────────
@mcp.tool()
def add_employee(
    name: str,
    role: str,
    department: str,
    email: str,
    salary: float,
    leave_balance: int = 10,
) -> dict:
    """
    Add a new employee record.

    Args:
        name (str): Full name
        role (str): Job title
        department (str): Department name
        email (str): Company email
        salary (float): Annual salary
        leave_balance (int): Remaining leave days (default: 10)

    Returns:
        dict: Created employee record
    """
    new_emp = {
        "id": len(EMPLOYEES) + 1,
        "name": name,
        "role": role,
        "department": department,
        "email": email,
        "salary": salary,
        "leave_balance": leave_balance,
        "last_updated": datetime.now().isoformat(),
    }
    EMPLOYEES.append(new_emp)
    return {"message": "✅ Employee added successfully!", "employee": new_emp}


# ───────────────────────────────
# 🧰 TOOL 5: Delete an employee
# ───────────────────────────────
@mcp.tool()
def delete_employee(emp_id: int) -> str:
    """
    Delete an employee by ID.

    Args:
        emp_id (int): Employee ID

    Returns:
        str: Status message
    """
    for emp in EMPLOYEES:
        if emp["id"] == emp_id:
            EMPLOYEES.remove(emp)
            return f"🗑️ Employee {emp['name']} (ID: {emp_id}) deleted successfully."
    return "❌ Employee not found."


# ───────────────────────────────
# 🧰 TOOL 6: Get employee metrics
# ───────────────────────────────
@mcp.tool()
def get_employee_metrics(emp_id: int) -> dict:
    """
    Retrieve performance metrics like salary and leave balance.

    Args:
        emp_id (int): Employee ID

    Returns:
        dict: Employee metrics or error
    """
    for emp in EMPLOYEES:
        if emp["id"] == emp_id:
            return {
                "name": emp["name"],
                "department": emp["department"],
                "salary": emp["salary"],
                "leave_balance": emp["leave_balance"],
                "last_updated": emp["last_updated"],
            }
    return {"error": f"Metrics not found for employee ID {emp_id}"}

import json
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()
FILE = "expenses.json"

# Load existing expenses
def load_expenses():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save expenses
def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=4)

# Add expense
def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (food, travel, shopping, etc.): ").strip()
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        console.print("[red]❌ Invalid amount. Please enter a number.[/red]")
        return
    description = input("Enter description: ").strip()

    expense = {"date": date, "category": category, "amount": amount, "description": description}
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    console.print("[green]✅ Expense added successfully![/green]")

# View expenses (with table)
def view_expenses():
    expenses = load_expenses()
    if not expenses:
        console.print("[yellow]⚠ No expenses found.[/yellow]")
        return

    table = Table(title="💸 All Expenses", box=box.ROUNDED, show_lines=True)
    table.add_column("Date", style="cyan", no_wrap=True)
    table.add_column("Category", style="magenta")
    table.add_column("Amount", style="green")
    table.add_column("Description", style="white")

    for e in expenses:
        table.add_row(e['date'], e['category'], f"₹{e['amount']}", e['description'])

    console.print(table)

# Show summary
def summary():
    expenses = load_expenses()
    if not expenses:
        console.print("[yellow]⚠ No expenses to summarize.[/yellow]")
        return

    total = sum(e['amount'] for e in expenses)
    console.print(f"\n[bold green]💰 Total Expenses: ₹{total}[/bold green]")

    categories = {}
    for e in expenses:
        categories[e['category']] = categories.get(e['category'], 0) + e['amount']

    table = Table(title="📊 Category-wise Breakdown", box=box.SIMPLE_HEAVY)
    table.add_column("Category", style="cyan")
    table.add_column("Amount", style="green")

    for cat, amt in categories.items():
        table.add_row(cat, f"₹{amt}")

    console.print(table)

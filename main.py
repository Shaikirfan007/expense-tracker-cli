import tracker
from rich.console import Console

console = Console()

def main():
    while True:
        console.print("\n[bold blue]==== Expense Tracker ====[/bold blue]")
        console.print("1. Add Expense")
        console.print("2. View Expenses")
        console.print("3. Summary")
        console.print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            tracker.add_expense()
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.summary()
        elif choice == "4":
            console.print("[bold red]👋 Exiting... Goodbye![/bold red]")
            break
        else:
            console.print("[red]❌ Invalid choice. Try again.[/red]")

if __name__ == "__main__":
    main()

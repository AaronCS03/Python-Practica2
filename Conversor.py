from rich.console import Console
from rich.table import Table

def exchange_money(budget, rates):
    results = {}
    for currency, rate in rates.items():
        results[currency] = round(budget * rate, 2)
    return results

def mostrar_resultados(budget, conversiones):
    console = Console()
    table = Table(title=f"Conversión de {budget} USD")

    table.add_column("Moneda", style="cyan", no_wrap=True)
    table.add_column("Equivalente", style="green")

    for moneda, valor in conversiones.items():
        table.add_row(moneda, str(valor))

    console.print(table)

def main():
    print("=== Conversor de Divisas Avanzado ===")
    try:
        budget = float(input("Ingrese su presupuesto en USD: "))

        tasas = {
            "JPY": 141.79,
            "EUR": 0.877,
            "MXN": 19.63,
            "COP": 3850.00
        }

        resultados = exchange_money(budget, tasas)
        mostrar_resultados(budget, resultados)

    except ValueError:
        print("⚠ Error: Debes ingresar un número válido.")

if __name__ == "__main__":
    main()

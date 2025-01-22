def calcular_area_triangulo(base, altura):
    """Calcula el área de un triángulo dado su base y altura."""
    area = (base * altura) / 2
    return area

def main():
    # Solicitar al usuario la base y altura
    try:
        base = float(input("Introduce la base del triángulo: "))
        altura = float(input("Introduce la altura del triángulo: "))

        # Calcular el área
        area = calcular_area_triangulo(base, altura)

        # Mostrar el resultado
        print(f"El área del triángulo es: {area}")
    except ValueError:
        print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    main()
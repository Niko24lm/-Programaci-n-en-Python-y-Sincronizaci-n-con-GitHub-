def calcular_descuento(monto_total, porcentaje_descuento=15):
    """
    Calcula el descuento basado en el monto total y el porcentaje de descuento.
    
    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento (por defecto 15%).
    :return: Monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

def main():
    # Primera llamada a la función con monto total
    monto1 = 150.00  # Monto total de la compra
    descuento1 = calcular_descuento(monto1)
    monto_final1 = monto1 - descuento1
    
    print(f"Monto total: ${monto1:.2f}")
    print(f"Descuento: ${descuento1:.2f}")
    print(f"Monto final a pagar: ${monto_final1:.2f}\n")
    
    # Segunda llamada a la función con monto total y porcentaje de descuento
    monto2 = 200.00  # Monto total de la compra
    porcentaje2 = 15  # Porcentaje de descuento
    descuento2 = calcular_descuento(monto2, porcentaje2)
    monto_final2 = monto2 - descuento2
    
    print(f"Monto total: ${monto2:.2f}")
    print(f"Descuento: ${descuento2:.2f}")
    print(f"Monto final a pagar: ${monto_final2:.2f}")

if __name__ == "__main__":
    main()
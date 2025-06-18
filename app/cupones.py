def aplicar_cupon(precio, cupon):
    descuentos = {
        "OFERTA10": 0.10,
        "SUPER20":   0.20,
        "BIENVENIDA":0.15
    }
    if cupon in descuentos:
        return round(precio * (1 - descuentos[cupon]), 2)
    return precio

def calcular_precio_final(precio_base, cupon, impuesto=0.19):
    precio_desc = aplicar_cupon(precio_base, cupon)
    return round(precio_desc * (1 + impuesto), 2)

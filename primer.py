import re
import unicodedata


def calculateDiscount(price: float, discount_percentage: float) -> float:
    """Devuelve el precio final tras aplicar un descuento positivo."""
    if price <= 0 or discount_percentage <= 0:
        raise ValueError("El precio y el porcentaje de descuento deben ser positivos.")

    return price * (1 - discount_percentage / 100)


def slugify(text: str) -> str:
    """Convierte un texto en un slug en minúsculas, sin acentos y con guiones."""
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", ascii_text.lower()).strip("-")

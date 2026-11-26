# AGENTS.md

Estas reglas aplican a todo el código dentro de `test/`.

## Código limpio

- Sigue PEP 8 y mantén un estilo consistente en todo el código.
- Usa nombres descriptivos y funciones pequeñas con una sola responsabilidad.
- Evita duplicación, código muerto e imports innecesarios.
- Usa type hints y docstrings cuando aporten claridad.

## Comentarios técnicos

- Comenta cada función y cada bloque técnico relevante explicando qué hace y por qué.
- Documenta supuestos, decisiones, casos límite y efectos secundarios.
- No escribas comentarios obvios que solo repitan el código.
- Actualiza los comentarios cuando cambie el código.

## Eficiencia

- Elige estructuras de datos y algoritmos adecuados al problema.
- Evita trabajo repetido, copias innecesarias y E/S redundante.
- Prioriza la legibilidad; mide antes de hacer microoptimizaciones.

## Reglas

Todo cambio lleva su test en tests/

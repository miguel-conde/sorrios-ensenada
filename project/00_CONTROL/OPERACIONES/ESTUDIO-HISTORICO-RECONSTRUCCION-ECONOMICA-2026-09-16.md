# Operación ESTUDIO-HISTORICO-RECONSTRUCCION-ECONOMICA-2026-09-16

- **Tipo:** reconstrucción económica integrada del expediente
- **Estado:** prepared
- **Fecha:** 16 de septiembre de 2026
- **Rama canónica:** `main`
- **Base SHA:** `0cdc9cc53575357d2aec00a521d25aa08f18a0bd`
- **Manual aplicado:** Manual Editorial v1.6
- **Edición base:** Edición Crítica v3.5
- **Análisis cuantitativo base:** v0.2
- **Fase:** `estudio_historico`
- **Aprobación:** el usuario ordenó avanzar con la reconstrucción económica integrada de Sorríos en 1752.

## Alcance

Se crea una reconstrucción económica integrada basada exclusivamente en la Edición Crítica validada y en el análisis cuantitativo v0.2 como documento derivado de apoyo.

El nuevo documento integra:

- estructura productiva agraria;
- ciclos de cultivo y calidad;
- ganadería, forraje y bienes comunales;
- red molinera y riesgo hidráulico;
- apicultura;
- organización doméstica del trabajo;
- flujos entre hogares, común, Iglesia, Conde de Luna e instituciones externas nombradas;
- rentas monetarias y en especie;
- equivalentes internos calculables sin conversiones externas;
- red parcial de activos y derechos;
- grado de monetización;
- restricciones, vulnerabilidades y límites de inferencia;
- un modelo económico integrado en cinco circuitos.

## Reglas metodológicas

- No se amplía el corpus documental.
- La Edición Crítica validada sigue siendo la única base documental primaria.
- El análisis cuantitativo v0.2 se usa solo como derivado de cálculo y control.
- Se distinguen dato documental, cálculo interno e interpretación.
- No se convierten unidades históricas a unidades modernas.
- No se introduce equivalencia entre medida principal de tierra y celemín.
- No se monetizan `cargas` de cereal por falta de equivalencia interna con quartales o fanegas.
- Solo se usan `4 quartales = 1 fanega` y `4 montones = 1 carro` cuando son necesarias.
- No se suman categorías sociales potencialmente solapadas.
- No se trata todo flujo institucional como salida geográfica de riqueza.
- No se estima PIB, renta per cápita, excedente neto, distribución completa de riqueza ni presión fiscal total.

## Cálculos nuevos incorporados

Entre otros, se documentan:

- composición de las medidas principales cultivadas: 93,13% centenales, 5,06% linares de regadío, 1,15% ferrañales y 0,66% linares de secano;
- índice anualizado de medidas cultivadas activas bajo el ciclo explícito de barbecho: 1.578,25, de las que el centenal representa aproximadamente 87,14%;
- índices ponderados de rendimiento por medida principal para comparar internamente clases y calidades;
- 5 fanegas de trigo = 20 quartales = 80 reales al precio regulado;
- 160 libras de lino = 160 reales + 960 maravedís al precio regulado;
- 26 quartales de primicia de centeno = 52 reales + 650 maravedís;
- 4 quartales de utilidad del molino venturero = 8 reales + 100 maravedís;
- 5 quartales de centeno del buey `dado arenta` = 10 reales + 125 maravedís;
- 4 quartales de la vaca `dado arenta` = 8 reales + 100 maravedís;
- 25 de los 233 reales de gastos comunes explícitos tienen destino geográfico externo inequívoco en Valladolid y León: 10,73% del subtotal conocido.

Todos estos valores se presentan como cálculos internos y no como cifras literales del manuscrito.

## Archivo creado

- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Reconstruccion_Economica_Integrada.md`

## Archivos no modificados

- `project/00_CONTROL/proyecto.yaml`;
- `project/00_CONTROL/estado.yaml`;
- `project/00_CONTROL/unidades.yaml`;
- `project/00_CONTROL/Manual_Editorial.md`;
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`;
- `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md`;
- `project/20_TRABAJO_EDITORIAL/Glosario.md`;
- los índices;
- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md`;
- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Analisis_Cuantitativo.md`;
- el PDF autoritativo de Drive.

## Verificación prevista

La publicación se realizará solo si `main` continúa en el Base SHA indicado. Después se comprobarán:

1. padre del commit;
2. lista exacta de dos archivos añadidos;
3. conservación de la Edición Crítica v3.5;
4. conservación del análisis cuantitativo v0.2;
5. conservación de `operation.status: clean`;
6. resultado del workflow de CI.

El registro conserva `Estado: prepared` como fotografía del paquete previo a la publicación; el commit, la comparación y CI determinan después el estado técnico efectivo.
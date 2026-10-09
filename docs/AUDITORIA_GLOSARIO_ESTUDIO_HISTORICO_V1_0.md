# Auditoría A — Glosario / Estudio Histórico

**Fecha:** 9 de octubre de 2026<br>
**Rama auditada:** `feature/quarto-book`<br>
**Baseline:** `8508bf358d720ca5f8f48cbb07d569d69750216f`<br>
**Naturaleza:** diagnóstico editorial; no constituye autorización de investigación ni de implementación<br>
**Cuestión principal:** `REV-020`

## 1. Objeto y alcance

Esta auditoría determina, para cada una de las 22 entradas vigentes del glosario, si su función actual es suficiente, si puede mejorarse con conocimiento ya consolidado en el proyecto, si requeriría una operación canónica interna o si una ampliación rigurosa exigiría investigación histórica externa nueva. También identifica posibles omisiones y compara tres arquitecturas conceptuales para el aparato.

La operación ha sido exclusivamente diagnóstica. No se ha investigado fuera del repositorio, no se han abierto las referencias externas ya citadas, no se ha redactado ninguna definición sustitutiva y no se han modificado fuentes canónicas, capítulos, generadores ni salidas de Quarto. La composición 0.6 tampoco actúa aquí como autoridad textual o histórica.

## 2. Fuentes auditadas

Se han contrastado las siguientes capas, respetando su autoridad:

- [Glosario histórico](../project/20_TRABAJO_EDITORIAL/Glosario.md), fuente de las 22 entradas auditadas.
- [Estudio Histórico 1.2](../project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md), síntesis canónica del contexto ya consolidado.
- [Registro de afirmaciones y cálculos 1.2](../project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md), con niveles D/C/I/E/L y cautelas.
- [Edición Crítica 3.6](../project/20_TRABAJO_EDITORIAL/Edicion_Critica.md), autoridad textual local.
- [Introducción contextual 1.3](../project/30_RESULTADOS/EDICION_DIVULGATIVA/Introduccion_Catastro_Ensenada_Sorrios.md), [índice rector 1.5](../project/30_RESULTADOS/EDICION_DIVULGATIVA/Indice_Referencia_Volumen_Final.md) y [Plan de composición 0.5](../project/30_RESULTADOS/EDICION_DIVULGATIVA/Plan_Composicion_Volumen_0_5.md).
- Índices vivos, en especial el [Índice de medidas](../project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md), además de los índices de instituciones y oficios.
- La vista derivada [glosario.qmd](../publication/generated/glosario.qmd), el [capítulo metodológico](../publication/content/01-catastro/04-manuscrito-volumen-actual.qmd) y los [capítulos 5–13](../publication/content/02-estudio/05-lugar-senorio-concejo-ordas.qmd), solo para comprobar qué recibe hoy el lector.

Las referencias externas resumidas en el Registro se han tratado como conocimiento ya incorporado. No se ha seguido ni abierto ninguno de sus enlaces.

## 3. Función actual del glosario

El glosario vigente es ante todo documental: registra la forma histórica, define su función en el expediente, localiza la primera aparición, remite a otras unidades y añade cautelas. Su propia norma excluye la interpretación histórica extensa. Esa restricción es valiosa porque preserva la separación entre testimonio local, contexto externo e inferencia.

La carencia observada no afecta por igual a las 22 voces. Las entradas léxicas o productivas suelen cumplir bien su función con una explicación local breve. Las voces institucionales, fiscales y sociales plantean más dificultades para el lector general: algunas pueden enriquecerse con contexto ya validado y otras no deberían ampliarse sin investigación específica. El problema es, por tanto, selectivo y arquitectónico; no demuestra que el glosario completo sea insuficiente.

## 4. Criterios G0–G4

| Estado | Criterio operativo |
|---|---|
| **G0 — suficiente** | La entrada cumple razonablemente su función; no requiere acción histórica antes de 1.0. |
| **G1 — mejora editorial con conocimiento ya disponible** | El proyecto ya contiene contexto suficiente; una operación editorial posterior podría aprovecharlo sin modificar el Estudio ni investigar. |
| **G2 — enriquecimiento canónico interno** | Faltaría consolidar el contexto en el Estudio, pero bastarían fuentes ya presentes; exigiría una operación canónica separada. |
| **G3 — investigación histórica externa necesaria** | Una explicación histórica rigurosa requiere responder una pregunta que las fuentes internas no resuelven. |
| **G4 — no ampliar deliberadamente** | La ampliación aportaría poco o elevaría el riesgo de falsa equivalencia, generalización o precisión. |

Solo G1–G3 reciben prioridad. La prioridad mide importancia para comprender el libro, no frecuencia textual ni urgencia automática de implementación.

## 5. Matriz completa de entradas

| ID | Término | Función actual | Contexto existente en Estudio | Otras fuentes internas | Estado G | Prioridad | Hueco concreto | Acción futura | Impacto |
|---|---|---|---|---|---|---|---|---|---|
| GLO-001 | Señorío | Mixta: condición jurisdiccional local y cautela contra reconstruir el régimen. | Explica Concejo, jurisdicción del conde de Luna, identificación del titular, derechos declarados y límites de R22. | JUR-005, JUR-006, JUR-008; caps. 5 y 10. | G1 | ALTA | Falta hacer explícita para el lector la diferencia entre dependencia jurisdiccional, propiedad y derechos concretos. | Sintetizar el contexto ya validado en una segunda capa breve, tras decisión GH. | Glosario; caps. 5 y 10 mediante enlaces, no contenido nuevo; índice institucional. |
| GLO-002 | medio vecino | Funcional/local: categoría de R21 y relación con vecinos, residentes y tributos. | Distingue vecindad fiscal, residencia, hogares y población; recoge el posible cómputo de viudas en otros lugares. | DEM-001, DEM-002, DEM-005; cap. 6. | G1 | ALTA | La entrada no orienta suficientemente sobre la naturaleza fiscal y variable de la categoría. | Incorporar síntesis ya autorizada sin convertirla en fracción fija de hogar o persona. | Glosario; cap. 6; índices de materias y oficios, si procede. |
| GLO-003 | propios | Funcional/local: recurso del común ausente en R23. | Sitúa propios y arbitrios como bases de la hacienda local y relaciona su ausencia con el repartimiento. | FIS-005–007, FIS-016, INT-006; cap. 11. | G1 | MEDIA | Falta una orientación institucional mínima que distinga recursos estables del común de otras cargas o ingresos. | Añadir contexto breve ya consolidado, coordinado con `arbitrio`. | Glosario; cap. 11; índice institucional y posible aparato fiscal. |
| GLO-004 | arbitrio | Funcional/local: categoría de recurso o ingreso ausente en R24. | Explica su lugar junto a propios y rentas en la hacienda local, con cautela frente a inferir pobreza absoluta. | FIS-005–007, FIS-016, INT-006; cap. 11. | G1 | MEDIA | La definición local no muestra bien su relación y diferencia con `propios`. | Presentar ambas voces coordinadamente con el contexto ya disponible. | Glosario; cap. 11; índice institucional y posible aparato fiscal. |
| GLO-005 | Ferrañales | Mixta: uso local y apoyo léxico agrario ya validado. | Explica cereal verde, cultivo sin interrupción y función forrajera dentro del sistema agrario. | AGR-001, AGR-013; cap. 7. | G0 | — | No hay hueco relevante para la comprensión del libro. | Conservar; evitar transferir detalles regionales adicionales. | Ninguno antes de 1.0. |
| GLO-006 | pelo | Mixta: número de aprovechamientos y contexto agrario regional controlado. | Distingue uno y dos aprovechamientos, `pelo y otoño`, riego, cierre y límites de generalización. | AGR-012; cap. 7. | G0 | — | La explicación vigente ya resuelve el sentido sin convertirlo en equivalencia universal. | Conservar. | Ninguno antes de 1.0. |
| GLO-007 | entreparedes | Documental/local: categoría y variantes internas, con ciclo declarado. | Conserva la categoría agraria y sus discordancias sin equivalencia externa segura. | TER-001, TER-002, TER-009; cap. 7. | G4 | — | No existe base interna para fijar una equivalencia agronómica general. | No ampliar; mantener variantes, localización y comportamiento documentado. | Evita una afirmación insegura en glosario y cap. 7. |
| GLO-008 | negrillos | Histórica léxica breve: identifica el término como olmos con cautela botánica. | Los integra en los sotos y recursos arbóreos. | Edición Crítica R4 y R10; caps. 7 y 8. | G0 | — | No hace falta una determinación botánica más precisa. | Conservar. | Ninguno antes de 1.0. |
| GLO-009 | pan | Histórica léxica breve: cereal o mies antes de la siega. | El sistema agrario aclara `tierras de pan llevar` y cultivos cerealistas. | AGR-001–007; cap. 7. | G0 | — | La acepción histórica necesaria ya está explicada. | Conservar. | Ninguno antes de 1.0. |
| GLO-010 | diezmos | Mixta: derecho eclesiástico local, perceptor y regulación de cantidades. | Distingue perceptor, especies, dinero, quinquenio y límites de agregación. | FIS-001–003; caps. 10 y 12. | G0 | — | Para la función del glosario no se necesita una historia general del diezmo. | Conservar; remitir al capítulo fiscal cuando se revise la navegación. | Ninguno histórico; posible enlace editorial. |
| GLO-011 | primicia | Funcional/local: derecho eclesiástico, receptor y cantidad documentada. | La sitúa junto a diezmos y boto, separando beneficiarios y bases. | FIS-001, FIS-002, FIS-004; cap. 10. | G0 | — | El contexto local basta; una historia institucional extensa sería desproporcionada. | Conservar. | Ninguno antes de 1.0. |
| GLO-012 | boto | Mixta: prestación local e identificación cauta con el Voto de Santiago. | Resume origen medieval, variantes y extensión desigual, sin completar el producto elidido. | FIS-001, FIS-002, FIS-004, FIS-013; cap. 10. | G1 | MEDIA | El contexto validado está en el Estudio, pero la entrada solo lo insinúa. | Añadir una capa histórica breve manteniendo `boto`, receptor y cuantía local. | Glosario; cap. 10; bibliografía ya registrada; índice institucional. |
| GLO-013 | fejes | Documental/local: unidad de cómputo del lino y relación interna de cuatro libras. | Permite calcular 160 libras solo para la partida documentada. | AGR-009, CAL-009; Índice de medidas; caps. 7 y 10. | G4 | — | No hay equivalencia general acreditada fuera de esa relación interna. | No ampliar ni convertir a una unidad moderna. | Evita falsa precisión metrológica. |
| GLO-014 | molino venturero | Funcional/local: molienda invernal condicionada por el agua y utilidad regulada. | Integra estacionalidad, río, ruedas, titulares y límites de la tipología. | HID-005, HID-008; cap. 9. | G0 | — | La caracterización interna basta para el lector; una tipología molinera amplia no es necesaria. | Conservar. | Ninguno antes de 1.0. |
| GLO-015 | esquilmo | Funcional/local extensa: producto o rendimiento ganadero regulado por especie. | Separa productos, cadencias, valores y ausencia de datos de producción efectiva. | GAN-001; cap. 8. | G0 | — | La entrada ya explica el uso específico y sus límites. | Conservar. | Ninguno antes de 1.0. |
| GLO-016 | añino | Documental/local: producto del cordero medido en quartarón y valorado. | Repite la relación local, pero no identifica con seguridad la naturaleza del producto. | GAN-001; Índice de medidas; cap. 8. | G3 | BAJA | ¿Qué designa exactamente `añino` en este contexto ganadero leonés y qué relación tiene con edad, lana o piel? Las fuentes internas no lo resuelven. | Si se decide ampliar, investigar léxico histórico ganadero y fuentes técnicas o documentales regionales; hasta entonces conservar la formulación local. | Estudio, Registro, glosario, cap. 8, bibliografía e índices; quizá recuadro ganadero de Auditoría B. |
| GLO-017 | pies de abejas | Documental/local: expresión de cómputo, titulares y utilidad regulada. | El libro usa cautamente `colmenas` para el activo, sin reconstruir tipología ni producción. | GAN-003–006, CAL-010, CAL-011, CAL-020; cap. 9. | G4 | — | Equiparar sin estudio `pie` con una categoría apícola moderna añadiría una precisión no documentada. | No ampliar; conservar la expresión y la ausencia de equivalencia moderna. | Evita extrapolación; mantiene estable cap. 9. |
| GLO-018 | alcavalas | Funcional/local: derecho fiscal enajenado, titular, pago anual y límite sobre el origen de la enajenación. | Distingue derecho señorial, pago de 633 reales, R22 y pozo de pesca; no explica el régimen general ni el título local. | JUR-005, JUR-006, FIS-009; caps. 5, 10 y 12. | G3 | ALTA | ¿Qué naturaleza fiscal tenía la alcabala en 1752 y por qué título concreto la percibía el conde en Ordás? El expediente declara el hecho, pero desconoce la causa de la enajenación. | Separar una eventual explicación general de la investigación específica del título; consultar historia fiscal y documentación jurisdiccional solo si el usuario lo autoriza. | Estudio, Registro, glosario, caps. 5, 10, 12 y 13, bibliografía, índices y posible esquema fiscal de Auditoría B. |
| GLO-019 | vecera | Funcional/local: turno vecinal de la taberna cuando no se arrienda. | Aporta paralelo de ordenanzas leonesas y limita la generalización a otras actividades. | TRA-005, TRA-006; caps. 8 y 11. | G1 | MEDIA | La entrada no muestra que el paralelo regional ya valida el sentido rotatorio del uso local. | Incorporar una explicación histórica breve con la cautela existente. | Glosario; caps. 8 u 11 mediante remisión; índice institucional. |
| GLO-020 | servicio ordinario y extraordinario | Documental/local: carga fiscal de la que el común declara no estar gravado. | Registra la ausencia y la separa de otros pagos, pero no explica la figura fiscal. | FIS-008; caps. 10 y 11. | G3 | MEDIA | ¿Qué comprendía esta figura fiscal en el marco aplicable en 1752 y qué significa exactamente su ausencia local? El material interno solo reproduce el dato negativo. | Investigar historia fiscal normativa o especializada antes de ampliar; no inferir exención general de otras cargas. | Estudio, Registro, glosario, caps. 10–12, bibliografía, índices y posible esquema fiscal de Auditoría B. |
| GLO-021 | hijo de familia | Funcional/local: jornalero que vive en compañía de sus padres. | Explica dependencia familiar, composición de los jornaleros y límites para inferir hogares o exclusividad laboral. | TRA-001, INT-008, DEM-005; caps. 6 y 12. | G1 | MEDIA | Puede aclararse que es una posición doméstica documentada, no una edad, estado civil o categoría laboral universal. | Sintetizar las cautelas internas en una nota breve. | Glosario; caps. 6 y 12; índices de oficios y materias. |
| GLO-022 | pobre de solemnidad | Documental/local: categoría aplicada a cinco personas en R36. | La sitúa entre las categorías sociales, pero no define su estatuto jurídico o asistencial. | Edición Crítica R36; caps. 6 y 13. | G3 | MEDIA | ¿Qué condiciones hacían reconocible esta categoría en el marco local de 1752 y qué efectos jurídicos o asistenciales tenía? Las fuentes internas solo dan el rótulo y el número. | Investigar historia jurídica y asistencial, con atención regional, antes de añadir contexto general. | Estudio, Registro, glosario, caps. 6 y 13, bibliografía, índices y posible recuadro social de Auditoría B. |

Recuento de control: **G0 8 + G1 7 + G2 0 + G3 4 + G4 3 = 22**. Entre los once casos G1–G3 hay **3 de prioridad alta, 7 media y 1 baja**.

## 6. Análisis de `Señorío`

### Lo que dice hoy el glosario

La entrada define `Señorío` como la condición jurisdiccional atribuida por los declarantes al lugar o concejo, perteneciente al conde de Luna. Localiza R2 y R22 y se abstiene expresamente de reconstruir un régimen señorial general. Es una definición mixta, aunque su capa histórica permanece implícita.

### Contexto ya disponible

El Estudio y el libro distinguen el lugar de Sorribos y Santibáñez, el Concejo de Ordás y el municipio posterior; presentan el señorío como marco jurisdiccional; identifican con evidencia externa ya registrada al XV conde de Luna; y separan la condición señorial de los derechos concretos. R22 solo declara que no se paga al señor por el concepto de establecimiento del suelo. Esto no autoriza a negar otros derechos: R28 documenta las alcabalas enajenadas y su pago anual de 633 reales al conde, y R29 documenta el pozo de pesca arrendado en nueve reales. `JUR-005`, `JUR-006` y `JUR-008`, junto con los capítulos 5 y 10, sostienen estas distinciones.

### Necesidad del lector general

El lector necesita una explicación corta de que `señorío` designa aquí una dependencia jurisdiccional e institucional del Antiguo Régimen y no implica que el señor sea propietario universal de tierras, recursos o rentas. También debe entender que los derechos se prueban por conceptos concretos y que ausencia de pago en R22 no equivale a ausencia de cargas señoriales.

### Qué está sustentado y qué falta

Esa explicación básica ya está sustentada y puede sintetizarse sin modificar el Estudio ni investigar: por eso la voz es **G1, prioridad ALTA**. Lo que no está resuelto es el título jurídico exacto, origen, alcance y evolución de cada derecho del conde en Ordás, en especial la causa de la enajenación de alcabalas y el título del pozo. Reconstruirlo sí exigiría investigación externa, pero no es necesario para corregir el hueco editorial básico de `Señorío` ni debe incorporarse de forma encubierta a esa voz.

## 7. Otros términos prioritarios

- **medio vecino — G1 ALTA:** el capítulo 6 y `DEM-005` permiten explicar mejor la categoría sin convertirla en media persona, medio hogar ni coeficiente demográfico fijo.
- **alcavalas — G3 ALTA:** es una carga cuantitativamente central y un derecho atribuido al conde; deben separarse la explicación fiscal general y la cuestión local del título de percepción.
- **propios / arbitrio — G1 MEDIA:** el proyecto ya permite explicar su función conjunta en la hacienda local y su relación con el repartimiento.
- **boto — G1 MEDIA:** `FIS-013` aporta el contexto suficiente para identificar con cautela el Voto de Santiago sin alterar la forma documental, el receptor ni la cuantía.
- **vecera — G1 MEDIA:** `TRA-006` valida el sentido rotatorio que ya muestra R29, sin autorizar su extensión a otros servicios.
- **servicio ordinario y extraordinario — G3 MEDIA:** la mera ausencia local no explica la figura fiscal.
- **hijo de familia — G1 MEDIA:** la información interna permite aclarar posición doméstica y dependencia sin atribuir rasgos no documentados.
- **pobre de solemnidad — G3 MEDIA:** la categoría social resulta relevante, pero su estatuto no está explicado internamente.
- **añino — G3 BAJA:** la duda léxica es real, aunque su resolución tiene impacto menor en la comprensión global del libro.

## 8. Candidatos a nuevas entradas

La lista es provisional y deliberadamente corta. No autoriza altas en el glosario.

| Término candidato | Capítulo o contexto | Por qué podría ser necesario | Fuente interna que lo respalda | Clasificación provisional |
|---|---|---|---|---|
| avitadores | Cap. 6; R21 | Es la suma fiscal explícita de vecinos y medios vecinos y puede confundirse con población total. | DEM-001, DEM-002, DEM-005; Estudio §§3–4. | G1 |
| utilidad | Caps. 8, 9 y 12; R17–R20, R29 | Es una regulación fiscal o pericial, no producción observada, beneficio empresarial ni ingreso efectivo. | GAN-001, HID-004–005, FIS-012; Introducción metodológica. | G1 |
| repartimiento | Cap. 11; R25 | Explica cómo se cubren gastos declarados al faltar propios, arbitrios y rentas. | FIS-005–007, INT-006. | G1 |
| establecimiento del suelo | Caps. 5 y 10; R22 | Es clave para no convertir una ausencia de pago concreta en ausencia general de derechos señoriales. | JUR-005; Estudio §2.3. | G1 |
| arenta | Cap. 8; R20 | La forma es opaca y el proyecto ya dispone de contexto leonés de renta o aparcería, con límites. | GAN-008; Estudio §9. | G1 |
| quartal | Caps. 7, 10 y 12 | Cumple varias funciones —sembradura, fruto, prestación y utilidad— y su relación interna no permite una conversión moderna. | TER-003–005; Índice de medidas. | G1 |

Resultado: **6 candidatos**, todos G1 provisional. `fanega`, `celemín`, `carga`, `quartaron`, `real` y `maravedís` ya tienen un aparato específico en el Índice de medidas; trasladarlos en bloque duplicaría funciones. Solo `quartal` supera provisionalmente ese umbral por su centralidad y pluralidad de usos. La decisión final depende del modelo GH elegido y de la política de enlaces entre aparatos.

## 9. Comparación GH-A / GH-B / GH-C

| Dimensión | GH-A — una definición local | GH-B — dos capas en una entrada | GH-C — dos recursos separados |
|---|---|---|---|
| Claridad general | Alta para consulta documental, limitada para voces institucionales. | Alta: distingue de forma visible uso local y contexto breve. | Potencialmente alta, pero exige que el lector salte entre aparatos. |
| Rigor | Muy alto por contención. | Alto si la segunda capa solo usa contexto validado y conserva D/E/I/L. | Alto, aunque la separación puede ocultar la relación exacta con el expediente. |
| Riesgo de extrapolación | Bajo. | Bajo-medio, controlable con selección y cautelas. | Medio si el aparato histórico adquiere autonomía enciclopédica. |
| Mantenimiento | Mínimo. | Moderado; una entrada conserva juntas las dos capas y sus fuentes. | Alto; requiere sincronizar dos recursos, enlaces y cobertura. |
| Relación con el Estudio | El lector debe buscarla por su cuenta. | La capa histórica sintetiza y remite, sin sustituir el Estudio. | El segundo recurso puede duplicar el Estudio. |
| Relación con bibliografía | Escasa y normalmente indirecta. | Selectiva y trazable en las voces que la necesitan. | Requiere aparato bibliográfico propio o compartido más complejo. |
| Duplicación | Baja. | Baja si el contexto es breve. | Alta: dos entradas o aparatos para un mismo término. |
| HTML/PDF | Simple, pero menos orientador. | Una misma entrada funciona bien en ambos formatos con jerarquía tipográfica. | HTML tolera el salto; en PDF aumenta navegación, páginas y riesgo de separación. |

## 10. Recomendación conceptual

Se recomienda **GH-B, aplicado de forma selectiva y sujeto a decisión del usuario**. La primera capa conservaría el sentido en el expediente; la segunda ofrecería contexto histórico breve solo en voces G1 y, después de la investigación y propagación autorizadas, en las G3 que se decida ampliar. G0 y G4 no necesitan una segunda capa automática.

GH-B responde al problema de `Señorío` sin dividir artificialmente la consulta ni convertir el glosario en una enciclopedia. También permite enlazar el Estudio y la bibliografía manteniendo visible qué procede del documento local. GH-A sigue siendo adecuado para muchas entradas, pero como modelo único deja sin resolver las voces institucionales más opacas. GH-C puede reservarse para un futuro aparato temático más amplio; para 1.0 introduce duplicación, mantenimiento y navegación innecesarios.

Esta recomendación no selecciona una implementación, una extensión máxima ni una lista definitiva de voces enriquecidas.

## 11. Términos que NO necesitan investigación nueva

No necesitan investigación externa los **15 casos G0, G1 o G2**; en esta auditoría son ocho G0, siete G1 y ningún G2:

- **G0:** Ferrañales, pelo, negrillos, pan, diezmos, primicia, molino venturero y esquilmo.
- **G1:** Señorío, medio vecino, propios, arbitrio, boto, vecera e hijo de familia.
- **G2:** ninguno.

Tampoco se recomienda investigar para ampliar los tres G4 —entreparedes, fejes y pies de abejas— porque la decisión diagnóstica es conservar su función documental/local y evitar equivalencias o generalizaciones inseguras.

## 12. Términos que podrían necesitar enriquecimiento interno

No se ha identificado ningún **G2**. Las fuentes internas no revelan una carencia que obligue a modificar el Estudio Histórico antes de actuar editorialmente. Los siete G1 contienen ya el conocimiento necesario en el Estudio, el Registro o los capítulos; su eventual trabajo sería una síntesis editorial posterior y no un enriquecimiento canónico.

Si en una revisión humana apareciera un nuevo G2, deberá tratarse como operación canónica separada: primero consolidación en el Estudio y, si procede, en el Registro; después se evaluaría la propagación. Esta auditoría no autoriza esa operación.

## 13. Términos que requerirían investigación externa

| Término | Pregunta de investigación | Insuficiencia actual | Tipo de fuente necesaria |
|---|---|---|---|
| añino | Naturaleza exacta del producto y alcance de la voz en el contexto ganadero leonés del XVIII. | El expediente solo da unidad y valor; el Estudio no define el producto. | Léxico histórico ganadero, tratados técnicos o documentación regional coetánea. |
| alcavalas | Régimen fiscal aplicable y título concreto por el que el conde percibía las alcabalas de Ordás. | El expediente declara enajenación, perceptor y cuantía, pero los declarantes desconocen su causa. | Historia fiscal normativa y documentación jurisdiccional, patrimonial o archivística del señorío. |
| servicio ordinario y extraordinario | Contenido de la figura fiscal en 1752 y alcance de la ausencia declarada. | Solo existe el dato negativo de R27. | Normativa e historia fiscal del Antiguo Régimen, preferiblemente contextualizada para León. |
| pobre de solemnidad | Criterios de reconocimiento y efectos jurídicos o asistenciales de la categoría. | Solo se conserva el rótulo local y el número de personas. | Historia jurídica, administrativa y asistencial, con contraste regional o local. |

No se propone aquí ninguna fuente concreta nueva ni se ha realizado la investigación.

## 14. Mapa de propagación al libro

La secuencia autorizable sigue siendo:

```text
investigación
→ fuente canónica correspondiente
→ Estudio Histórico
→ Registro D/C/I/E/L, si procede
→ glosario
→ capítulos afectados
→ bibliografía
→ índices
→ Quarto
```

No todas las capas cambian siempre. No hay G2 en el resultado actual. Para los G3, el impacto potencial es:

| Término G3 | Estudio y Registro | Glosario y capítulos | Bibliografía e índices | Quarto y posible Auditoría B |
|---|---|---|---|---|
| añino | Nueva síntesis ganadera; probable E/I y cautela L si persiste ambigüedad. | Voz y cap. 8; cap. 12 solo si afecta a la lectura del valor. | Fuente visible; índices de materias y medidas/productos según diseño. | Regeneración posterior; podría informar un recuadro ganadero, no necesariamente un gráfico. |
| alcavalas | Contexto fiscal y, por separado, resultado sobre el título local; E/I y actualización de L si se resuelve. | Voz; caps. 5, 10, 12 y quizá síntesis 13. | Bibliografía fiscal y documental; índices institucional y de materias. | Regeneración posterior; puede afectar a un esquema de derechos y cargas de Auditoría B. |
| servicio ordinario y extraordinario | Explicación fiscal y límite de la ausencia; nueva E/I. | Voz; caps. 10–12 según relevancia. | Bibliografía fiscal; índices institucional y de materias. | Regeneración posterior; posible inclusión en un esquema fiscal de Auditoría B. |
| pobre de solemnidad | Contexto social/jurídico; nueva E/I y cautela sobre efectos locales. | Voz; cap. 6 y, solo si aporta a la síntesis, cap. 13. | Bibliografía social/asistencial; índices de materias y quizá oficios/categorías. | Regeneración posterior; puede orientar un recuadro de categorías sociales de Auditoría B. |

Para los G1 bastaría una operación editorial posterior que reutilice conocimiento ya canónico. Podrían revisarse enlaces entre glosario y capítulos 5, 6, 10, 11 y 12, además de los índices institucional, de oficios y de materias. La bibliografía ya citada deberá hacerse visible si la futura redacción usa su contexto, cuestión relacionada con `REV-003`; el modo de presentar notas o remisiones se relaciona con `REV-004`. Los posibles esquemas fiscales, ganaderos o sociales se trasladan únicamente como insumo a `REV-021` y a la Auditoría B, sin prejuzgar su selección.

## 15. Riesgos editoriales

- Convertir todas las entradas a dos capas generaría contexto redundante y diluiría la función de consulta.
- Mezclar en una misma frase dato local y regla general haría invisible la diferencia D/E/I.
- Presentar `señorío` como propiedad, o R22 como ausencia de derechos, contradiría el registro canónico.
- Definir `medio vecino` mediante un coeficiente fijo produciría falsa precisión demográfica.
- Equiparar `entreparedes`, `fejes`, `pies de abejas`, medidas o monedas con unidades modernas sin prueba dañaría el rigor metrológico y léxico.
- Ampliar `alcavalas`, `servicio ordinario y extraordinario`, `añino` o `pobre de solemnidad` con conocimiento general no investigado ocultaría lagunas reales.
- Duplicar el Índice de medidas dentro del glosario aumentaría mantenimiento y riesgo de divergencia.
- Una bibliografía invisible debilitaría las capas históricas; una bibliografía excesiva en cada voz perjudicaría la consulta. Su resolución corresponde también a la Auditoría C.
- En PDF, segundas capas largas pueden romper la exploración alfabética; en HTML, enlaces indiscriminados pueden fragmentar la lectura.

## 16. Conclusión y siguientes decisiones

El glosario no presenta una carencia histórica general. Ocho entradas son suficientes; siete admiten una mejora editorial con conocimiento ya disponible; ninguna exige enriquecimiento canónico interno; cuatro requerirían investigación externa antes de una ampliación rigurosa; y tres deben conservarse deliberadamente en su función documental. `Señorío` es el caso de control: su hueco básico es G1, no G3.

La recomendación conceptual es GH-B selectivo. Quedan pendientes de decisión humana: aceptar o rechazar ese modelo; elegir qué G1 se enriquecerían para 1.0; decidir si algún G3 se investiga ahora, se difiere o conserva su forma actual; aprobar o descartar los seis candidatos; y fijar la extensión, citas y navegación de las dos capas. Nada de ello se decide ni implementa en esta auditoría.

La siguiente operación acordada es la Auditoría B. No debe usar las menciones de posibles esquemas o recuadros como aprobación de diseño: son únicamente dependencias que deberá evaluar junto con 0.6, el Plan 0.5 y la candidata.

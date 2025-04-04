
# 1. ¿Qué es una MT universal?
Una Máquina de Turing Universal (MTU) es una MT capaz de ejecutar cualquier otra. La MT U recibe como entrada una MT M (codificada mediante una cadena < M >) y una cadena w, y ejecuta M a partir de w.


# 2. Explicar cómo enumeraría los números naturales pares, los números enteros, los números racionales (o fraccionarios) y las cadenas de Ʃ* siendo Ʃ = {0, 1}.

Para enumerarlos **usaría la notación unaria**.

**Pares**:
1. Iniciar con cintas 1 y 2 en blanco.
3. Marcar el inicio de un n° en la cinta 2.
4. Escribir "1" en la cinta 2 por cada "1" en la cinta 1.
5. Agregar dos "1" en la cinta 1 y volver al primer símbolo.
6. Vuelve al paso 2.

**Enteros**:
1. Iniciar con cintas 1, 2 y 3 en blanco.
3. Marcar el inicio de un n° en la cinta 2 con 0.
4. Escribir "1" en la cinta 2 por cada "1" en la cinta 1.
4. Escribir un "0" en la cinta 3 (indicando que es un n° negativo) y luego un  "1" en la cinta 3 por cada "1" en la cinta 1.
5. Agregar un "1" en la cinta 1 para avanzar a la siguiente magnitud, o sea, tomar un número mas grande (para avanzar a la siguiente magnitud, o sea, tomar un número mas grande) y volver al primer símbolo.
6. Vuelve al paso 2.

<br>

### **Racionales**:

Idea General:

Utilizaremos una enumeración diagonal de pares de números naturales (p, q) con q > 0. Cada par se interpretará como la fracción p/q, representada en notación unaria (por ejemplo, "1^p # 1^q", donde "#" es un delimitador). Opcionalmente, podemos filtrar para obtener la forma canónica (p y q coprimos), pero la idea básica es la siguiente:

**Procedimiento:**

1. **Inicialización y Notación:**
   - La MT usa varias cintas.
   - En una cinta se mantiene un contador n que representará la suma p + q.
   - La fracción se representará como "1^p # 1^q" (por ejemplo, 3/2 se escribiría como "111#11" en notación unaria).

2. **Enumeración Diagonal:**
   - **Paso 1:** Inicializar n = 1.
   - **Paso 2:** Para cada n, considerar todos los pares (p, q) tales que:
     - p y q son números naturales.
     - p + q = n.
     - Se impone que q > 0 para que la fracción esté bien definida (en caso de que se quiera incluir el 0, se puede permitir p = 0).
   - **Paso 3:** Para cada par (p, q) con p + q = n:
     - Opcionalmente, si se requiere la forma reducida, calcular el máximo común divisor (MCD) de p y q. Si el MCD es 1, se acepta la fracción; si no, se descarta para evitar duplicados.
     - Escribir la fracción en la cinta de salida en la forma "1^p # 1^q".

3. **Iteración:**
   - Incrementar n en 1 y repetir el proceso.  
   - De este modo, se recorren sistemáticamente todos los pares (p, q) con q > 0.

**Ejemplo:**

- Para n = 1:
  - p = 0, q = 1 → Se escribe " (vacío)#1" (interpretado como 0/1, que representa el 0).

- Para n = 2:
  - p = 0, q = 2 → " (vacío)#11" (0/2; si queremos la forma canónica, 0 se representa de forma única, por ejemplo, como 0/1).
  - p = 1, q = 1 → "1#1" (representa 1/1).

- Para n = 3:
  - p = 0, q = 3 → " (vacío)#111" (0/3).
  - p = 1, q = 2 → "1#11" (representa 1/2).
  - p = 2, q = 1 → "11#1" (representa 2/1).

**Conclusión:**

La MT sigue un proceso de enumeración diagonal sobre los pares (p, q) con p + q constante. Así, al aumentar n, eventualmente se generan todas las posibles fracciones (o números racionales). Esta estrategia asegura que cada fracción (o su representación canónica, si se filtra por coprimalidad) se producirá en algún momento. De esta forma, la máquina de Turing logra enumerar todos los números racionales.


<br>

**Cadenas de Ʃ<sup>*</sup> (con Ʃ = {0, 1})**:
1. Iniciar con cintas 1 y 2 en blanco.
2. Marcar el inicio de una cadena en la cinta 2.
3. Copiar los símbolos de la cinta 1 en la cinta 2.
4. Si había un "0" en la cinta 1, escribir un "1" (como si sumáramos 1 en binario) y volver al primer símbolo.
    * Si había un "1" o un espacio en blanco, escribir un "0" (como si estuviéramos realizando una suma con acarreo en binario).
5. Volver al paso 2.


# 3. Dar la idea general de cómo sería una MT que, teniendo como cadena de entrada un número natural i, genera la i-ésima fórmula booleana satisfactible según el orden canónico. *Comentario: asumir que existen una MT M1 que determina si una cadena es una fórmula booleana, y una MT M2 que determina si una fórmula booleana es satisfactible.*

Idea General de la MT: recibe como entrada un número natural \(i\) y debe generar la \(i\)-ésima fórmula booleana satisfactible, siguiendo el orden canónico. Se asume la existencia de dos máquinas auxiliares:

- **M1:** verifica si una cadena es una fórmula booleana válida.
- **M2:** verifica si una fórmula booleana es satisfactible.

Procedimiento General:

1. **Entrada:** la MT recibe el número \(i\) (codificado, por ejemplo, en notación unaria o binaria).

2. **Enumeración de Cadenas:** la MT genera, en orden canónico (por ejemplo, orden lexicográfico), todas las posibles cadenas de símbolos.

3. **Filtrado de Fórmulas Booleanas:** para cada cadena generada, se utiliza M1 para determinar si es una fórmula booleana. Si la cadena NO es una fórmula booleana, se descarta.

4. **Verificación de Satisfactibilidad:** si la cadena es una fórmula booleana, se utiliza M2 para comprobar su satisfactibilidad. Si la fórmula NO es satisfactible, se descarta.

5. **Contador y Selección:** se mantiene un contador que se incrementa cada vez que se encuentra una fórmula booleana satisfactible. Cuando el contador alcanza \(i\), la MT detiene la búsqueda y devuelve la fórmula booleana satisfactible correspondiente.

### Resumen:

La MT realiza lo siguiente:
- **Genera** todas las cadenas en orden canónico.
- **Filtra** aquellas que sean fórmulas booleanas usando M1.
- **Filtra** las fórmulas resultantes para quedarnos solo con las satisfactibles usando M2.
- **Cuenta** las fórmulas válidas hasta encontrar la \(i\)-ésima.
- **Devuelve** la \(i\)-ésima fórmula booleana satisfactible.

Este es el esquema general de cómo una MT podría generar la \(i\)-ésima fórmula booleana satisfactible.

<br>

# 4. Sea M1 una MT que genera en su cinta de salida todas las cadenas de un lenguaje L. Dar la idea general de cómo sería una MT M2 que, usando M1, acepte una cadena w sii w ∈ L.

Idea General para la MT M2:

Dado que **M1** genera todas las cadenas de un lenguaje L en su cinta de salida, podemos construir una máquina M2 que acepte una cadena w si y solo si w ∈ L siguiendo estos pasos:

1. **Entrada:** M2 recibe la cadena w a evaluar.

2. **Simulación de M1:** M2 inicia una simulación de M1 de manera intercalada (o en paralelo) con el procesamiento de w. A medida que M1 genera cadenas, M2 las va capturando 1 x 1.

3. **Comparación:** cada vez que M1 produce una cadena x, M2 la compara con w. Si se encuentra que x = w, M2 acepta w.

4. **Resultado:**  si w ∈ L, eventualmente M1 generará w y M2 aceptará. Si w ∉ L, M1 nunca generará w y M2 no aceptará (es decir, puede rechazar o entrar en un loop infinito).

## Resumen

- **Simula M1:** M2 ejecuta M1 para obtener todas las cadenas de L.  
- **Compara:** cada cadena generada se compara con w.  
- **Acepta:** si se encuentra una coincidencia, M2 acepta w.  
- **No acepta:** si w no está en L, nunca se producirá la coincidencia.

Este enfoque utiliza la enumeración completa de L por M1 para decidir si w pertenece al lenguaje.

<br>

# 5. El lenguaje L<sub>U</sub> = {(< M >, w) | M acepta w} se conoce como lenguaje universal, y representa el problema general de aceptación. Probar que L<sub>U</sub> ∈ RE. Ayuda: construir una MT que acepte L<sub>U</sub>.

L<sub>U</sub> = { (< M >, w) | M acepta w }

Demostrar que L<sub>U</sub> ∈ RE.

Para probar esto se crea una MT U encargada de correr < M > a partir de la entrada `w`.

Como < M > se ejecutará sobre MT U, se puede garantizar que siempre que la entrada ∈ L<sub>U</sub> finalizará con el estado `qA`. Sin embargo, no se puede garantizar el resultado en el caso de que las cadenas no pertenezcan al lenguaje.

Al ejecutar < M > sobre MT U produce los siguientes resultados:
* Si (< M >, w) ∈ LU, < M > termina en qA<sub>< M ></sub>, por lo que MT U termina en `qA`.
* Si (< M >, w) ∈ LU, < M > termina en qR<sub>< M ></sub>, por lo que MT U termina en `qR`.
* Si < M > termina en bucle, MT U también lo hará.


<br>

# 6. Una función f : A ⟶ B se dice que es total computable, si existe una MT M<sub>f</sub> que computa f para todo elemento a ∈ A. Sea la función f<sub>01</sub>: Ʃ* ⟶ {0, 1}, tal que:
### f<sub>01</sub> (v) = 1, si v = (< M >, w) y M para a partir de w.
### f<sub>01</sub> (v) = 0, si v = (< M >, w) y M no para a partir de w, o bien v ≠ (< M >, w).

## Probar que la función f<sub>01</sub> no es total computable. *Ayuda: ¿con qué problema se relaciona dicha función?*

f<sub>01</sub> supone una MT<sub>f</sub> que siempre finaliza, por lo que podemos suponer que L(f<sub>01</sub>) ∈ R.

Por definición, f<sub>01</sub> debe retornar un valor "0" (qR) en el caso de que la MT < M > rechace la entrada `w` o no finalice a partir de ella.

Dado esto, encontramos una inconsistencia en la que f<sub>01</sub> debe retornar un resultado, incluso en el caso de que no finalice. Por lo tanto, MT<sub>f</sub> entraría en un bucle.

Por lo tanto, como no podemos asegurar la finalización de MT<sub>f</sub> para todas sus entradas, concluimos que L(f<sub>01</sub>) ∈ RE y entonces f<sub>01</sub> no es total comptable.

*// acá está explicado con la definición de HP, pero me parecía mejor tener la otra rta para entenderlo mejor*

Dada la función f<sub>01</sub>, al suponerla total computable se puede generar una MT<sub>f</sub>, la cual ∈ R.

Dicha MT<sub>f</sub> aceptaría las cadenas en las que f<sub>01</sub>(x) = 1, que por definición es: *"(< M >, w) y M para a partir de w"*.

Ese resultado de la función corresponde al lenguaje del Halting Problem (HP), el cual ∈ RE. Por lo tanto, se genera una falla lógica ya que M<sub>f</sub> no podría pertenecer a R al no poder garantizar la finalización de su ejecución en este caso.

Por lo tanto, MT<sub>f</sub> pertenecería a RE y f<sub>01</sub> no sería total computable.

**Resumen:**
- f₀₁ está definida para devolver 1 si y solo si M se detiene con w.
- Si f₀₁ fuera total computable, existiría una MT que decidiera el HT.
- Pero el HT es indecidible, por lo tanto, f₀₁ no puede ser total computable.

<br>

# 7. Responder breve y claramente cada uno de los siguientes incisos (en todos los casos, las MT mencionadas tienen **1** sola cinta):
## a. Probar que se puede decidir si una MT M, a partir de la cadena vacía λ, escribe alguna vez un símbolo no blanco. *Ayuda: ¿Cuántos pasos puede hacer M antes de entrar en un loop?*

**Idea:**  
- Al partir de la cadena vacía, la configuración de M (estado, posición de la cabeza y contenido relevante de la cinta) es finita.  
- Existe un n° max de pasos (= al n° de configuraciones posibles) antes de que M repita una config y entre en un ciclo.  
- Se simula M durante ese n° acotado de pasos; si durante la simulación se escribe algún símbolo no B, se acepta; de lo contrario, se rechaza.

**Conclusión:** es decidible, ya que el n° de pasos a simular es finito.

## b. Probar que se puede decidir si una MT M que sólo se mueve a la derecha, a partir de una cadena w, para. *Ayuda: ¿Cuántos pasos puede hacer M antes de entrar en un loop?*

La MT M siempre va a parar si la cadena `w` ∈ R.

**Idea:**
- Una MT que solo se mueve a la derecha nunca regresa a una celda anterior, por lo que, tras terminar la parte no vacía de w, siempre lee B.
- Una vez en la región de B, la única info relevante es el estado actual y el hecho de que se lee siempre el símbolo B.
- Esto implica que el n° de configuraciones posibles es finito.
- Se simula M por, a lo sumo, el n° finito de pasos (basado en el n° de configuraciones); si se repite alguna config sin haber detenido la máquina, se concluye que M entra en loop.

**Conclusión:** es decidible, ya que se puede acotar la simulación por el n° de configuraciones posibles.


## c. Probar que se puede decidir si dada una MT M, existe una cadena w a partir de la cual M para en a lo sumo 10 pasos. Ayuda: ¿Hasta qué tamaño de cadenas hay que chequear?

Si L(M) ∈ R, entonces se garantiza que M va a finalizar.

Para decidir si finalizará en 10 pasos o menos, podría ejecutarse < M > en una MT U con espacio limitado a 10 celdas.
* Si < M > finaliza, MT U finaliza en `qA`.
* Si no, finaliza en `qR`.

**Idea:**  
- Si M para en 10 pasos o menos, entonces la ejecución solo depende de lo que se lea en, como máximo, 10 celdas de la cinta.  
- Por lo tanto, para cada máquina M, solo es necesario considerar todas las cadenas de entrada de longitud hasta 10 (hay un n° finito de ellas).  
- Se simula M en cada una de estas cadenas durante 10 pasos.  
- Si alguna simulación termina en 10 pasos o menos, se responde afirmativamente; de lo contrario, se responde negativamente.

**Conclusión:** es decidible, porque solo hay que chequear finitamente muchas cadenas (todas de longitud ≤ 10) y cada simulación se limita a 10 pasos.



## d. ¿Se puede decidir si dada una MT M, existe una cadena w de a lo sumo 10 símbolos a partir de la cual M para? Justificar.

No es decidible, ya que implicaría resolver el HT para una cantidad finita pero indeterminada de pasos, lo que es indecidible.

**Idea:**  
- Aquí se pregunta: ¿existe alguna entrada, de longitud ≤ 10, para la que M se detenga (sin acotar el número de pasos)?
- Aunque el conjunto de entradas a considerar es finito, decidir si M se detiene en una entrada dada equivale al Halting Problem (HT), que es indecidible.
- No existe un algoritmo que, para cada entrada de longitud ≤ 10, determine siempre (en tiempo finito) si M se detendrá, ya que M podría tardar un número arbitrario de pasos antes de detenerse o nunca hacerlo.

**Conclusión:**  
No es decidible, ya que implica resolver (en forma global) el HT para una cantidad finita pero indeterminada de pasos, lo que es indecidible.













# 1. Considerando la reducción de HP a LU descripta en clase, responder:

## a. Explicar por qué la función identidad, es decir la función que a toda cadena le asigna la misma cadena, no es una reducción de HP a L<sub>U</sub>.

La función identidad se define como $f(x) = x$. Para que una función de reducción sea válida de HP a L<sub>U</sub> se deben cumplir las siguientes propiedades:
1. Para toda entrada $w$ ∈ HP, su $f(x)$ ∈ L<sub>U</sub>.
2. Para toda entrada $w$ ∉ HP, su $f(x)$ ∉ L<sub>U</sub>.
3. La función $f$ debe ser computable.

El problema de la reducción de HP a L<sub>U</sub> es que HP está contenido en L<sub>U</sub>, por lo tanto existen entradas $w$ que pertenecen al conjunto (L<sub>U</sub> - HP), en las cuales $w$ ∉ HP pero $f(x)$ ∈ L<sub>U</sub>.

Por lo tanto, la función identidad no es una reducción de HP a L<sub>U</sub>.

## b. Explicar por qué las MT M<sub>2</sub> generadas en los pares de salida (< M<sub>2</sub> >, w), o bien paran aceptando, o bien loopean.

Suponiendo una MT M que ejecuta M<sub>2</sub> para garantizar que ésta termina o no, independientemente de que acepte o rechace la entrada se considera que la MT terminó, por lo que finalizará con estado `qA`. Por otro lado, al entrar en bucle no hay manera de retornar un estado final, aunque este sea `qR`; por lo tanto, la máquina quedará en bucle.

GPT: las máquinas M<sub>2</sub> están diseñadas para tener un comportamiento único y predecible en función de la detención de M con w: o aceptan en todas sus entradas (paran aceptando) o nunca detienen su proceso (loopean).

## c. Explicar por qué la función utilizada para reducir HP a L<sub>U</sub> también sirve para reducir HP<sup>C</sup> a L<sub>U</sub><sup>C</sup>.

Porque la reducción cumple la propiedad de las reducciones en la que:
* Si L<sub>1</sub> <= L<sub>2</sub>
* Entonces L<sub>1</sub><sup>C</sup> <= L<sub>2</sub><sup>C</sup> con la misma función de reducción.

### GPT:

Dado que la función *f* ya garantizaba que:

- Si ⟨M, w⟩ ∈ HP → *M'* ∈ L<sub>U</sub>
- Si ⟨M, w⟩ ∉ HP → *M'* ∉ L<sub>U</sub>

Podemos inferir directamente que esta misma transformación mantiene la relación entre los complementos:

- Si ⟨M, w⟩ ∈ HP<sup>C</sup> → *M'* ∈ L<sub>U</sub><sup>C</sup>
- Si ⟨M, w⟩ ∉ HP<sup>C</sup> → *M'* ∉ L<sub>U</sub><sup>C</sup>

Por lo tanto, la función utilizada para reducir **HP** a **L<sub>U</sub>** también sirve para reducir **HP<sup>C</sup>** a **L<sub>U</sub><sup>C</sup>**.


## d. Explicar por qué la función utilizada para reducir HP a L<sub>U</sub> no sirve para reducir L<sub>U</sub> a HP.

Porque la reducción no garantiza la simetría de las funciones.

HP <= L<sub>U</sub> no garantiza L<sub>U</sub> <= HP con la misma función.

## e. Explicar por qué la siguiente MT M<sub>f</sub> no computa una reducción de HP a L<sub>U</sub>: dada una cadena válida (< M >, w), M<sub>f</sub> ejecuta M sobre w, si M acepta entonces genera la salida (< M >, w), y si M rechaza entonces genera la cadena 1.

No es una reducción porque la función representada por M<sub>f</sub> no es total computable, ya que no puede garantizar la finalización correcta de las entradas $w$ en HP.

### GPT

La máquina M<sub>f</sub> no computa una reducción válida de HP a L<sub>U</sub> porque:  

1. **No preserva correctamente la relación entre los lenguajes**, ya que su salida no necesariamente pertenece o no a L<sub>U</sub>.  
2. **No maneja el caso en el que M entra en un bucle**, lo que significa que la función de reducción no es computable en todos los casos.  
3. **Produce cadenas que no siempre representan máquinas de Turing válidas**, lo que impide que se pueda verificar correctamente su pertenencia a L<sub>U</sub>.  

Por estas razones, M<sub>f</sub> **no puede ser utilizada como una reducción de HP a L<sub>U</sub>**.

<br>



# 2. Sabiendo que L<sub>U</sub> ∈ RE y L<sub>U</sub><sup>C</sup> ∈ CO-RE:
## a. Probamos en clase que existe una reducción de L<sub>U</sub> a LƩ*. En base a esto, ¿qué se puede afirmar con respecto a la ubicación de LƩ* en la jerarquía de la computabilidad?

(CONSIGNA VIEJA: Justificar por qué una reducción de L<sub>U</sub> a L<sub>Ʃ*</sub> no sirve para probar que L<sub>Ʃ*</sub> ∉ RE.)

Supongamos una función de reducción $f(x) = < MƩ*>$, suponiendo una MT a partir de la cual se puede producir el lenguaje.

$f$ es una función computable, puesto que la MT puede producirse sin entrar en bucle. Esto se debe a que todo lenguaje tiene una MT que lo produce.

Sin embargo, pueden darse casos en los que haya una entrada $w$ ∉ L<sub>U</sub>, y $f(x)$ sí pertenezca a L<sub>Ʃ*</sub>. Por lo tanto, la función de reducción no es válida.

Como no puede realizarse la reducción, no puede usarse el teorema para demostrar que L<sub>1</sub> ∈ RE -> L<sub>2</sub> ∈ RE ni su contrarrecíproco. Sin embargo, como L<sub>Ʃ*</sub> es más complejo que L<sub>U</sub>, no pueden realizarse suposiciones sobre él.

### GPT:
La reducción de LU a L<sub>Σ*</sub> no sirve para probar que L<sub>Σ*</sub> ∉ RE porque L<sub>Σ*</sub> es trivialmente RE (incluso decidible), ya que contiene todas las cadenas. Una reducción se usa para transferir propiedades no RE de un lenguaje a otro, pero en este caso, L<sub>Σ*</sub> ya es recursivamente enumerable, por lo que la reducción no aporta ninguna demostración de no enumerabilidad.


## b. Se prueba que existe una reducción de L<sub>U</sub><sup>C</sup> a L<sub>⊘</sub>. En base a esto, ¿qué se puede afirmar con respecto a la ubicación de L<sub>⊘</sub> en la jerarquía de la computabilidad?

Si existe una reducción válida de L<sub>U</sub><sup>C</sup> a L<sub>⊘</sub>, se puede usar el teorema:

L<sub>U</sub><sup>C</sup> <= L<sub>⊘</sub> entonces L<sub>U</sub><sup>C</sup> ∉ RE -> L<sub>⊘</sub> ∉ RE.

Por lo tanto, como L<sub>U</sub><sup>C</sup> ∉ RE entonces **L<sub>⊘</sub> ∉ RE**.

En otras palabras, L<sub>⊘</sub> es, al menos, tan “difícil” como L<sub>U</sub><sup>C</sup> y por lo tanto **no es recursivamente enumerable**.

<br>

# 3. Sea el lenguaje D<sub>HP</sub> = {w<sub>i</sub> | M<sub>i</sub> para desde w<sub>i</sub>, según el orden canónico}. Encontrar una reducción de D<sub>HP</sub> a HP.

HP está formado por los pares (< M >, w) en los que M para sobre la entrada $w$.

D<sub>HP</sub> está formado por los pares (< M<sub>i</sub> >, w) generadas en orden canónico, en los que M para sobre la entrada $w$ generada en su mismo orden $i$.

Dado esto, se busca encontrar una función que reduzca D<sub>HP</sub> a HP. 

Supongamos una $f((<M_i>, w_i)) = (<M>, w)$:
* Si M<sub>i</sub> para sobre $w_i$, entonces ∈ D<sub>HP</sub> y $f(x)$ produce un par (< M >, w) que ∈ HP.
* Si M<sub>i</sub> no para sobre $w_i$, entonces ∉ D<sub>HP</sub> y $f(x)$ produce un par (< M >, w) que ∉ HP.

Por lo tanto, $f((<M_i>, w_i)) = (<M>, w)$ reduce D<sub>HP</sub> a HP.


### GPT:
Sea D<sub>HP</sub> = { w<sub>i</sub> | M<sub>i</sub> para desde w<sub>i</sub>, según el orden canónico }.

Definimos la función de reducción f de la siguiente manera: si w es la cadena que ocupa la posición i en el orden canónico (es decir, w = w<sub>i</sub>), entonces fijamos

    f(w) = < Mi, wi >

Observamos que:
- w está en D<sub>HP</sub> si y solo si M<sub>i</sub> se detiene sobre w<sub>i</sub>,
- lo cual es equivalente a que < M<sub>i</sub>, w<sub>i</sub> > esté en HP.

Por lo tanto, f es una reducción de D<sub>HP</sub> a HP.

<br>

# 4. Sean TAUT y NOSAT los lenguajes de las fórmulas booleanas sin cuantificadores tautológicas (satisfactibles por todas las asignaciones de valores de verdad) e insatisfactibles (insatisfactibles por todas las asignaciones de valores de verdad). Encontrar una reducción de TAUT a NOSAT. *Comentario: hay que definir la función de reducción y probar su total computabilidad y correctitud.*

VER JOACO


### GPT: Reducción de TAUT a NOSAT

### Definición de la función de reducción

Definimos la función de reducción **f** de la siguiente manera:

`f(φ) = ¬φ`

donde **f** toma una fórmula booleana sin cuantificadores **φ** y devuelve su negación.

---

### 1. Total computabilidad

- **Totalidad:** para cualquier fórmula **φ** en el lenguaje de fórmulas booleanas, **¬φ** es también una fórmula bien definida.
- **Computabilidad:** la función **f** es computable porque, dada cualquier fórmula **φ**, podemos obtener **¬φ** simplemente anteponiendo el operador de negación (agregando paréntesis si es necesario).

---

### 2. Correctitud de la reducción

Se debe demostrar que:

`φ ∈ TAUT  ⇔  f(φ) ∈ NOSAT`

donde:

- **TAUT** es el conjunto de fórmulas booleanas que son verdaderas para toda asignación (tautológicas).
- **NOSAT** es el conjunto de fórmulas booleanas que son falsas para toda asignación (insatisfacibles).

**(i) Supongamos que φ ∈ TAUT:**

- Por definición, **φ** es verdadera para todas las asignaciones.
- Entonces, para toda asignación **A**, se cumple que **A(φ) = verdadero**, lo que implica que **A(¬φ) = falso**.
- Por lo tanto, **¬φ** es insatisfacible y **f(φ) ∈ NOSAT**.

**(ii) Supongamos que φ ∉ TAUT:**

- Existe al menos una asignación **A** tal que **A(φ) = falso**, lo que implica que **A(¬φ) = verdadero**.
- Por lo tanto, **¬φ** es satisfacible y **f(φ) ∉ NOSAT**.

---

### Conclusión

La función **f(φ) = ¬φ** es total, computable y satisface que:

`φ ∈ TAUT  ⇔  ¬φ ∈ NOSAT`

Por lo tanto, **f** es una reducción válida de TAUT a NOSAT.

---
<br>

# 5. Se prueba que existe una reducción de L<sub>U</sub><sup>C</sup> a LƩ* (y así, como L<sub>U</sub><sup>C</sup> ∉ RE, entonces se cumple que LƩ* ∉ RE). La reducción es la siguiente. Para toda w: f((< M1 >, w)) = < M2 >, tal que M2, a partir de su entrada v, ejecuta |v| pasos de M1 a partir de w, y acepta sii M1 no acepta. Probar que la función definida es efectivamente una reducción de L<sub>U</sub><sup>C</sup> a LƩ*. Comentario: hay que probar su total computabilidad y correctitud.

VER JOACO


### GPT: Reducción de L<sub>U</sub><sup>C</sup> a LΣ*:

### Definición de la función de reducción

Para cada par (< M1 >, w) definimos la función  
`f((<M1>, w)) = <M2>`,  
donde la máquina M2 actúa de la siguiente manera en cualquier entrada v:

- Simula M1 sobre w durante |v| pasos.
- **Acepta** si y solo si M1 **no** acepta w en esos pasos.

---

### 1. Total computabilidad

- **Construcción efectiva:** dada < M1 > y w, es posible construir el código < M2 > mediante un procedimiento programable.
- **Simulación finita:** para cualquier entrada v, se realiza una simulación de M1 sobre w durante |v| pasos, lo cual es un proceso finito.

Por lo tanto, la función f es total y computable.

---

### 2. Correctitud de la reducción

Debemos demostrar:  
`(<M1>, w) ∈ LUC ⇔ <M2> ∈ LΣ*.`

- **Si M1 no acepta w (caso L<sub>U</sub><sup>C</sup>):**
  - La simulación de M1 en M2 nunca detecta una aceptación.
  - Por lo tanto, M2 acepta **todas** las entradas v, es decir, L(M2) = Σ*.

- **Si M1 acepta w (caso contrario):**
  - Existe un número n de pasos en que M1 acepta w.
  - Para cualquier v con |v| ≥ n, M2 simula suficientes pasos y detecta la aceptación, por lo que **no acepta** dichos v.
  - Esto implica que L(M2) ≠ Σ*.

---

### Conclusión

La función f es:

- **Total y computable:** se puede construir efectivamente < M2 > a partir de (< M1 >, w).
- **Correcta:** se cumple que `(<M1>, w) ∈ LUC` si y solo si `<M2> ∈ LΣ*`.

Por lo tanto, f es una reducción válida de LUC a LΣ*.  
Si `LUC ∉ RE`, se concluye que `LΣ* ∉ RE`.




<br>
<br>
<br>

# PUNTOS VIEJOS:

<br>



# 5. Construir un autómata finito que reconozca el lenguaje de todas las cadenas con 0 y 1, incluso la cadena vacía, tales que a todo 0 le siga un 1.

M = { Q, Ʃ, δ, q<sub>ini</sub>, qA, qR }

Q = {q<sub>ini</sub>, q0, q1, qA, qR }
* q<sub>ini</sub>: estado inicial.
* q0: buscando un símbolo "0".
* q1: buscando un símbolo "1".


Función de transición:
* δ(q<sub>ini</sub>, B): qA
* δ(q0, 0): q1
* δ(q0, 1): q0
* δ(q1, 1): q0
* δ(q1, 0): qR

# 6. Un autómata linealmente acotado (ALA) es una MT con una sola cinta, con la restricción de que su cabezal sólo puede moverse a lo largo de las celdas ocupadas por la cadena de entrada. Probar que el lenguaje aceptado por un ALA es recursivo.

**Ayuda: ¿en cuántos pasos se puede detectar que el ALA entra en loop?**

Dada una cadena de entrada con $w$ caracteres, se puede saber la cantidad de pasos que va a tomar una MT ALA antes de entrar en bucle.

Suponiendo que tiene Q estados y Ʃ símbolos, la MT puede realizar $|Q| * |Ʃ|^w$ pasos antes de entrar en bucle.

*// A partir de esto cómo se prueba que es recursivo?*

<br>

### GPT:

## Prueba de que el lenguaje aceptado por un ALA es recursivo

Un autómata linealmente acotado (ALA) es una máquina de Turing cuya cinta se limita a las celdas que contienen la cadena de entrada. Esto implica que, para una entrada de longitud n, la cinta que puede ser usada tiene un tamaño finito (acotado por una función lineal en n).

La configuración de un ALA se define por:
- El estado actual (conjunto finito de estados).
- El contenido de la cinta en las celdas acotadas (un alfabeto finito y un número fijo de celdas).
- La posición del cabezal (que solo puede estar en una de esas celdas).

Dado que tanto el conjunto de estados, como el alfabeto, como la cantidad de celdas son finitos, el número total de configuraciones posibles es finito.

Esto significa que, en cualquier cómputo, el ALA no puede generar una secuencia infinita de configuraciones distintas. Si el ALA no se detiene, eventualmente repetirá una configuración, lo que indica un ciclo. Por lo tanto, se puede construir un algoritmo de decisión que:

1. Simule el ALA sobre la entrada.
2. Registre las configuraciones visitadas.
3. Acepte si se alcanza un estado de aceptación.
4. Rechace si se detecta una repetición (ciclo) en las configuraciones.

Debido a que el número de configuraciones es finito, este proceso siempre terminará en un número finito de pasos, permitiendo decidir si la entrada es aceptada o no.

Por lo tanto, el lenguaje aceptado por un ALA es **recursivo** (decidible).


# 7. Construir una MT que genere todos los índices i tales que (< Mi >, wi) ∈ HP, según el orden canónico.
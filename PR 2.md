# 1. Responder breve y claramente los siguientes incisos:
## a. ¿En qué difieren entre sí los lenguajes recursivos, los lenguajes recursivamente numerables no recursivos, y los lenguajes no recursivamente numerables?

* Un lenguaje es **recursivo (R)** si existe una MT que lo acepte y se detenga en todos los casos. Son un subconjunto de los **recursivamente numerables**.
* Un lenguaje es **recursivamente enumerable (RE)** si existe una MT que lo acepte, pero no siempre se detenga.
* Los lenguajes **recursivamente enumerables no recursivos** son aquellos que forman parte del conjunto `RE - R`. Estos lenguajes tienen uma MT que los acepte, pero hay casos en los que no se detiene. Son un subconjunto directo de Ł (todos los lenguajes).
* Los lenguajes **no recursivamente numerables (CO-RE)** son aquellos que forman parte del conjunto RE<sup>C</sup> (o Ł - RE). Estos lenguajes pueden no tener una MT que los acepte.

### En resumen:
- R -> problema decidible, MT siempre para
- RE -> problema computable, MT NO siempre para
- Ł -> no tienen MT que los acepte

<br>

## b. Probar que R ⊆ RE ⊆ 𝔏.

Siguiendo las definiciones (w = la entrada):
* Para cualquier lenguaje L ∈ R:
    1. Si w ∈ L, la MT siempre para en `qA`.
    2. Si w ∉ L, la MT siempre para en `qR`.
* Para cualquier lenguaje L ∈ RE:
    1. Si w ∈ L, la MT siempre para en `qA`.
    2. Si w ∉ L, la MT **NO** siempre para en `qR`.
        - La MT se detendrá en el estado `qR`.
        - La MT entrará en bucle.
* Para cualquier lenguaje L ∈ 𝔏:
    1. Si w ∈ L, la MT **NO** siempre para en `qA`.
    2. Si w ∉ L, la MT **NO** siempre para en `qR`.

Los lenguajes que pertenecen a R son un subconjunto de RE formado por aquellos L que cumplan las propiedades `1` y `2.a`, por lo tanto R ∈ RE.

Por último, en 𝔏 se encuentran todos los lenguajes posibles, independientemente del estado final de sus MT o si entran en bucle o no; por lo tanto, RE es un subconjunto de 𝔏 formado por aquellos lenguajes que que sus MT siempre terminan si su entrada es aceptada, pero podrían no terminar cuando su entrada no pertenece al lenguaje.

<br>

## c. Dijimos en clase que el hecho de que si L es recursivo (L ∈ R) entonces L<sup>C</sup> también lo es, significa en términos de problemas que si un problema es decidible entonces también lo es el problema contrario. ¿Qué significa en términos de problemas que la intersección de dos lenguajes recursivos es también un lenguaje recursivo?

La intersección de 2 problemas decidibles es también decidible porque podemos construir un algoritmo que verifique ambas propiedades y, al hacerlo, siempre terminará con una respuesta correcta para cualquier entrada.

Además, si un problema y el problema contrario son *computables*, entonces ambos son **decidibles**.

Lo demuestro con una MT M con 2 MTs secuenciales a forma de AND.

<br>

## d. Explicar por qué no es correcta la siguiente prueba de que si L ∈ RE, también L<sup>C</sup> ∈ RE: dada una MT M que acepta L, entonces la MT M’, igual que M pero con los estados finales permutados, acepta L<sup>C</sup>.

Si L está en RE, entonces L<sup>C</sup> está en CO-RE.
Por ello, la prueba es incorrecta -> solo sería válida si M se pararía en todas las entradas, lo cual no es el caso (lenguaje recursivamente enumerables).

<br>

## e. ¿Qué lenguajes de la clase CO-RE tienen MT que los aceptan? ¿También los deciden?

1. El conjunto CO-RE está formado por los lenguajes resultantes de la operación RE<sup>C</sup> (o RE - Ł).
2. El conjunto R está formado por los lenguajes resultantes de la operación RE ⋂ CO-RE.
3. Por definición, los L ∈ R **siempre** tienen una MT que los acepte.

Por lo tanto, los lenguajes de CO-RE que tienen una MT que los acepte son aquellos pertenecientes a R.

**Sí, también los deciden**. Solo los lenguajes que pertenecen a la clase R (los lenguajes recursivos) son decididos por MTs. Una MT decide un lenguaje si lo acepta y siempre para para cualquier entrada (aceptando si la entrada está en el lenguaje y rechazando si no lo está).

Los lenguajes en CO-RE - R no son decidibles. Si un lenguaje L ∈ CO − RE − R, aunque su complemento L<sup>C</sup> sea aceptado por una MT que no siempre para, no existe una MT que siempre pare y decida L. Si existiera una MT que decidiera L, entonces L sería recursivo, lo que contradice el hecho de que L ∈ CO − RE − R.


## En resumen:
* Los lenguajes de la clase CO-RE que tienen MTs que los aceptan son precisamente los lenguajes recursivos (R), que son un subconjunto de CO-RE.
* Estos mismos lenguajes recursivos (R) son también los únicos en CO-RE que son decididos por MTs (porque la MT que los acepta siempre se detiene).
* Los lenguajes que están en CO-RE pero no son recursivos (CO-RE - R) no tienen MTs que los acepten.

<br>

## f. Probar que el lenguaje Ʃ* de todas las cadenas y el lenguaje vacío ∅ son recursivos. Alcanza con plantear la idea general. Ayuda: encontrar MT que los decidan

Ʃ* es recursivo, ya que basta con construir una MT que siempre responda `qA`.

∅ es recursivo, ya que basta con crear una MT que siempre responde `qR`.

<br>

Ʃ*: para que sea *recursivo*, para toda cadena w ∈ Ʃ*, la MT debe parar en `qA` o `qR`.
Ʃ* es recursivo porque, al incluir todas las cadenas posibles, su MT siempre aceptará y nunca loopeará. Por lo tanto, Ʃ* ⊆ R.

∅: para que sea *recursivo*, para toda cadena w ∈ Ʃ*, la MT debe parar en `qA` o `qR`.
∅ es recursivo porque, al no tener ninguna cadena, su MT siempre rechazará y no loopeará.

## g. Probar que todo lenguaje finito es recursivo. Alcanza con plantear la idea general. Ayuda: encontrar una MT que lo decida (pensar cómo definir sus transiciones para cada una de las cadenas del lenguaje).

Al tratarse de un lenguaje finito, la MT que lo genera NO lo hará de manera indefinida, sino que eventualmente terminará con un n° determ de cadenas.

Por definición, una MT debe aceptar aquellas cadenas que pertenezcan al lenguaje. Como se sabe exactamente cuáles son las cadenas que pertenecen a este y cuáles no, M siempre finalizará, ya sea como `qA` o `qR`.

Dado que la MT *siempre para*, se trata de un lenguaje recursivo.

## f. Justificar por qué si L1 ∈ CO-RE y L2 ∈ CO-RE, entonces (L1 ⋂ L2) ∈ CO-RE.

* Por definición de intersección, los elementos del conjunto L1 ⋂ L2 forma parte de L1 y de L2.
* Tanto L1 como L2 ∈ CO-RE, por lo tanto cada uno de sus elementos ∈ CO-RE.
* Por lo tanto, L1 ⋂ L2 ∈ CO-RE.

<br>

# 2. Considerando la Propiedad 2 estudiado en la Clase 2:
## a. ¿Cómo implementaría copiar la entrada w en la cinta 2 de la MT M?

**Propiedad 2: si L1 y L2 ∈ R, entonces L1 ⋂ L2 ∈ R**.

La copia de la entrada w de la cinta 1 a la cinta 2 se puede implementar mediante una secuencia de transiciones de la MT M de la siguiente manera:
* Inicialmente, la entrada w se encuentra en la cinta 1, y ambas cabezas de lectura/escritura están posicionadas al inicio de las cintas. La cinta 2 está inicialmente en blanco.
* La MT M entraría en un estado dedicado a la operación de copia.
* Mientras la cabeza de la cinta 1 lea un símbolo s (que no sea el símbolo blanco que indica el fin de la entrada):
    * La MT M escribirá el mismo símbolo s en la posición actual de la cabeza de la cinta 2.
    * Ambas cabezas (la de la cinta 1 y la de la cinta 2) se moverán una posición a la derecha.
    * La MT M permanecerá en el estado de copia.


## b. ¿Cómo implementaría borrar el contenido de la cinta 2 de la MT M?

El borrado del contenido de la cinta 2 se puede implementar con otra secuencia de transiciones de la MT M:

* Después de la ejecución de M1 sobre w en la cinta 2, la cabeza de la cinta 2 podría estar en cualquier posición. Para borrar el contenido, primero necesitamos posicionar la cabeza al inicio del contenido que se desea borrar. Esto podría implicar mover la cabeza hacia la izquierda hasta encontrar un símbolo blanco que indique el inicio de la región utilizada.
* Una vez que la cabeza de la cinta 2 esté posicionada al inicio del contenido a borrar, la MT M entraría en un estado dedicado al borrado.
* Mientras la cabeza de la cinta 2 lea un símbolo que no sea el símbolo blanco (indicando que aún hay contenido de la ejecución anterior):
    * La MT M escribirá el símbolo blanco en la posición actual de la cabeza de la cinta 2.
    * La cabeza de la cinta 2 se moverá una posición a la derecha.
    * La MT M permanecerá en el estado de borrado.

<br>

Implementación:

M = { Q, Γ, δ, q0, qA, qR }

Alfabeto Γ = (L2, B)

Estados: Q = { q0, qb, qA, qR }
* q0: estado inicial.
* qb: borrando contenido.

*// suponiendo "x" como cualquier símbolo ∈ Ʃ*

Función de transición: δ

* `δ(q0, (B,B))`: qb, (B, S), (B, L)
* `δ(qb, (B,x))`: qb, (B, S), (B, L)
* `δ(qb, (B,B))`: qA, (B, S), (B, S)


*// CONSULTAR: esto lo hice como si estuviese modelando la M1 y M2. Lo tendría que haber hecho modelando la M directamente? en ese caso habría que cambiar los estados nomás*

### RESOLUCION MATE
a- Explicar sin hacer MT que copia la entrada de la cinta 1 en la cinta 2 y luego viene otra MT: necesito usar un caracter como “#” delimitador por si quiero copiar espacios.

b- MT que borra el contenido de su cinta simplemente llenar en blancos lo que está entre los caracteres especiales.

Para ambos casos debo delimitar el espacio de trabajo, dejando “##” al inicio e irlo modificando mientras agrego o saco caracteres.

Al borrar puedo llegar a tener blancos en el medio de la cadena, no borrar hasta llegar a un blanco.

<br>

# 3. Probar:
## a. La clase R es cerrada con respecto a la operación de unión. Ayuda: la prueba es similar a la desarrollada para la intersección.

Para probar que la clase R (lenguajes recursivos) es cerrada con respecto a la operación de unión, debemos demostrar que si L1 y L2 son lenguajes recursivos, entonces su unión L1 ∪ L2 también es un lenguaje recursivo.

Dado que L1 ∈ R y L2 ∈ R, por definición, existen dos Máquinas de Turing:
* M1 que decide L1: para cualquier entrada w, M1 se detiene y acepta si w ∈ L1, y se detiene y rechaza si w ∉ L1.
* M2 que decide L2: para cualquier entrada w, M2 se detiene y acepta si w ∈ L2, y se detiene y rechaza si w ∉ L2.

Nuestro objetivo es construir una MT M que decida el lenguaje L1 ∪ L2 = w ∣ w ∈ L1 o w ∈ L2.

Idea General:

La MT M tomar una cadena de entrada w y simulará la ejecución de M1 y M2 sobre w. Si al menos una de ellas acepta, entonces w pertenece a L1 ∪ L2, y M debe aceptar. Si ambas rechazan, entonces w no pertenece a L1 ∪ L2, y M debe rechazar. Debido a que tanto M1 como M2 siempre se detienen (ya que deciden L1 y L2 respectivamente), nuestra MT M también siempre se detendrá, ya sea en el estado de aceptación o de rechazo. Por lo tanto, M decide L1 ∪ L2.

<br>

### OTRA:

Hay que probar que si L1 y L2 ∈ R, entonces L1 U L2 ∈ R. Para demostrar que ∈ a R tengo que hacer una MT que reconozca el lenguaje y pare siempre -> ***SIEMPRE* que hay que demostrar que algo ∈ R, debemos construir una máquina**.

Puedo construir una MT M que adentro tiene a MT1 y MT2 que aceptan L1 y L2 respectivamente, las ejecuto de forma secuencial y acepto la salida final si alguna de estas fue `qA`. Esto hace que para cualquier entrada, si es aceptada por MT1 o MT2 es aceptada, entonces siempre termina la máquina y L1 U L2 ∈ R.

<br>

### Demostración

Demostrar que L1 ∪ L2 ∈ R. Se suponen dos MT M1 y M2 que aceptan L1 y L2 respectivamente, dentro de una MT M que las ejecuta secuencialmente.

Al tratarse de una unión, con que sólo una de M1 o M2 acepte la entrada ya podemos suponer que forma parte del lenguaje L1 ∪ L2 (no es necesaria la verificación en ambas como en la intersección). Como ambos conjuntos ∈ R, por definición se sabe que su unión también.

Idea general:
1. Copiar la entrada en una segunda cinta.
2. La M1 itera sobre los elementos de la cinta.
    1. Si todos los símbolos ∈ L1, pasa al estado `qA1`.
    2. Si encuentra un elemento que no, pasa al estado `qR1`.
3. Una vez que terminó la ejecución de M1, pueden ocurrir dos casos según el estado con el que finalice:
    1. Si aceptó la entrada, se puede confirmar que la entrada pertenece a L1 ∪ L2.
    2. Si rechazó la entrada, se debe ejecutar M2 para saber si la entrada ∈ L2.
4. Al terminar de ejecutar M1 y M2, si al menos una de las 2 MT aceptó la entrada, se puede concluir que L1 ∪ L2 ∈ R.

M = { Q<sub>M</sub>, Γ<sub>M</sub>, δ<sub>M</sub>, q0, qA<sub>M</sub>, qR<sub>M</sub> }

M1 = { Q<sub>M1</sub>, Γ<sub>M1</sub>, δ<sub>M1</sub>, q0, qA<sub>M1</sub>, qR<sub>M1</sub> }

M2 = { Q<sub>M2</sub>, Γ<sub>M2</sub>, δ<sub>M2</sub>, q0, qA<sub>M2</sub>, qR<sub>M2</sub> }

Alfabeto Γ<sub>M</sub> = Γ<sub>M1</sub> ∪ Γ<sub>M2</sub>

Estados: Q<sub>M</sub> = Q<sub>M1</sub> ∪ Q<sub>M2</sub> ∪ { q0, qc, qr, qa<sub>Mi</sub>, qw, qA, qR }
* q0: estado inicial
* qc: copiando en cinta 2.
* qr: vuelve al inicio de la fila.
* qa<sub>Mi</sub>: la MT Mi revisa la cinta.

Función de transición: δ

* δ(q0(x, B)): qc(x, S), (B, S)
* δ(qc(x, B)): qc(x, R), (x, R)
* δ(qc(B, B)): q0<sub>M1</sub> (B, R), (B, R)
* δ(q0<sub>M1</sub>(x, x)): qa<sub>M1</sub>(x, R), (x, R) *// para todo "x" ∈ Ʃ<sub>M1</sub>*
* δ(qa<sub>M1</sub>(B, B)): qA<sub>M1</sub>(B, S), (B, S)
* δ(qA<sub>M1</sub>(B, B)): qA(B, S), (B, S)
* δ(qR<sub>M1</sub>(B, B)): q0<sub>M2</sub>(B, S), (B, S)
* δ(qA<sub>M2</sub>(B, B)): qA(B, S), (B, S)
* δ(qR<sub>M2</sub>(B, B)): qR (B, S), (B, S)


<br>
SOFIA:

* q0: estado inicial
* qc: copia x en cinta 2.
* qb: busca x en cada cinta.

Función de transición: δ

* δ(q0(x, B)): qc(x, S), (B, S)
* δ(qc(x, B)): qc(x, R), (x, R)
* δ(qc(B, B)): qb(B, L), (B, L)
* δ(qb(x, x)): qb(x, L), (x, L)
* δ(qb(B, B)): qAi(B, R), (B, S)

<br>
<br>
<br>

## b. La clase RE es cerrada con respecto a la operación de intersección. Ayuda: la prueba es similar a la desarrollada para la clase R.

Para probar que la clase RE (leng recurs enumerable) es cerrada con respecto a la operación de intersección, debemos demostrar que si L1 y L2 son L RE, entonces su intersección L1 ∩ L2 también es un L RE.

Dado que L1 ∈ RE y L2 ∈ RE, por definición, existen dos Máquinas de Turing:
* M1 que decide L1: para cualquier entrada w, M1 se detiene y acepta si w ∈ L1, y puede detenerse y rechazar si w ∉ L1 o puede no detenerse y quedarse loopenado.
* M2 que decide L2: para cualquier entrada w, M2 se detiene y acepta si w ∈ L2, y puede detenerse y rechazar si w ∉ L2 o puede no detenerse y quedarse loopenado.

Nuestro objetivo es construir una MT M que decida el lenguaje L1 ∩ L2 = w ∣ w ∈ L1 y w ∈ L2.

Idea General:

La idea general es simular la ejecución de M1 y M2 secuencialmente sobre una misma entrada w.

Dado una entrada w, la MT M operará de la siguiente manera:
1. Ejecutar M1 sobre la entrada w.
2. Si M1 rechaza w (se detiene en `qR`), entonces M también rechaza w. Si M1 no se detiene, entonces M tampoco se detiene en esta rama de la ejecución.
3. Si M1 acepta w (se detiene en `qA`), entonces M procede a ejecutar M2 sobre la misma entrada w. Para esto, podemos imaginar que M guarda la entrada w y reinicia o simula la ejecución de M2 con w. También se puede pensar en una MT con múltiples cintas donde una cinta contiene la entrada y las otras se usan para simular M1 y M2.
4. Si M2 acepta w (se detiene en `qA`), entonces M acepta w.
5. Si M2 rechaza w (se detiene en `qR`), entonces M rechaza w. Si M2 no se detiene, entonces M tampoco se detiene.

De esta construcción, podemos observar lo siguiente:
- M aceptará la entrada w si y solo si tanto M1 como M2 aceptan w. Esto se debe a que M solo llega al paso de ejecutar M2 si M1 ya aceptó. Si M2 también acepta, entonces M acepta.
- Si w no pertenece a L1, entonces M1 rechazará o no se detendrá, y en ambos casos, M no aceptará.
- Si w pertenece a L1 pero no a L2, entonces M1 aceptará, pero M2 rechazará o no se detendrá, y en ambos casos, M no aceptará.

Por lo tanto, M reconoce exactamente el lenguaje L1 ⋂ L2. Aunque M1 o M2 puedan no detenerse para entradas que no están en sus respectivos lenguajes, la construcción asegura que M acepta precisamente cuando ambas M1 y M2 aceptan, cumpliendo con la definición de que L1 ⋂ L2 es recursivamente enumerable.

<br>
<br>

### OTRA:

RE suele necesitar máquinas en paralelo por si alguna queda loopeando. Si L1 y L2 ∈ RE, puedo demostrar que L1 ⋂ L2 ∈ RE construyendo una MT M con MT1 y MT2 en paralelo que acepte la entrada si alguna lo hizo (solo se queda loopeando si ambas loopean).

<br>

Demostrar que L1 ⋂ L2 ∈ RE. Se suponen 2 MT, M1 y M2 que aceptan L1 y L2 respectivamente, dentro de una MT M que las ejecuta secuencialmente.

A diferencia del conjunto recursivo, con los lenguajes ∈ RE no se puede garantizar que las MT que los aceptan finalicen correctamente; con que una de las dos permanezca en bucle, M también lo hará.

Además, al tratarse de una intersección, la entrada debe pasar por las 2 MT para poder ser aceptada. 

<br>

# 4. Sean L1 y L2 dos lenguajes recursivamente numerables de números naturales codificados en unario (por ej, el número 5 se representa con 11111). Probar que también es recursivamente numerable el lenguaje L = {x | x es un número natural codificado en unario, y existen y, z, tales que y + z = x, con y ∈ L1, z ∈ L2}. *Ayuda: la prueba es similar a la vista en clase, de la clausura de la clase RE con respecto a la operación de concatenación.*

Para probar que el lenguaje L = x ∣ x es un número natural codificado en unario, y existen y, z, tales que y + z = x, con y ∈ L1, z ∈ L2, es recursivamente enumerable, dado que L1 y L2 son lenguajes recursivamente enumerables de números naturales codificados en unario, podemos construir una MT M que acepte L.
**VER JOACO**

## OTRA:

* L1 ∈ RE
* L2 ∈ RE
* L(M1) = L1
* L(M2) = L2
* L = L1 * L2
* Demostrar que L ∈ RE

Como L1 y L2 son números escritos en lenguaje unario, la suma de dos números sería lo mismo que la concatenación de símbolos 1. Se busca construir una máquina M que compruebe que L ∈ RE.

Al tratarse de lenguajes de RE, no se puede garantizar la finalización de L1 o L2; por lo tanto, tampoco se puede confirmar para L. Debido a esto la comprobación debe realizarse ejecutando M1 y M2 concurrentemente (en paralelo).

<br>

RES Mateo:

No estamos haciendo otra cosa que la concatenación de L1 con L2 (siempre una cadena de L1 seguida de otra de L2). Sabemos que si L1 y L2 pertenecen a RE, entonces L1.L2 también por el siguiente motivo:

- M1 acepta L1
- M2 acepta L2
- Puedo construir una M3 que ejecute en paralelo lo siguiente: dada una entrada de N caracteres;
    - no ejecuto ningún caracter en M1 y de 0 a N en M2. Si ambas aceptan entonces acepto, si no, voy al siguiente caso
    - ejecuto caracteres del 1 al 1 en M1 y del 2 a N en M2. Si ambas aceptan entonces acepto, si no, voy al siguiente caso
    - hasta el 2 en M1 y los N-2 restantes en M2 …
    - …
    - Si en ningún caso se acepta, entonces se RECHAZA la entrada.


<br>

# 5. Dada una MT M1 con alfabeto Ʃ = {0, 1}:
## a. Construir una MT M2 que determine si L(M1) tiene al menos una cadena.

## **VER JOACO**

Alfabeto {0, 1} → lenguaje {0, 1, 00, 01, 10, 000, …}

Solución a fuerza bruta: probar con MT1 con todos los casos.

Otra forma es ejecutar en paralelo (como M1 puede loopear no nos sirve la solución secuencial) cada entrada y ni bien reciba un qA M2 devuelve qA, si todas devuelven qR entonces devuelvo qR, si no hay ningún qA y hay alguna loopeando entonces me quedo loopeando.
Tengo que hacer un MT1 OR MT1 OR MT1 … de forma paralela.

## b. ¿Se puede construir además una MT M3 para determinar si L(M1) tiene a lo sumo una cadena? Justificar.

## **VER JOACO**

**NO** se puede, porque no puedo verificar todas las posibles infinitas entradas que darán F, e incluso la máquina puede quedar loopeando en alguna entrada y debería esperar infinitamente.













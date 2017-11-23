# Coeficiente-Jaccard-Tanimoto-Python-
El archivo chemicals.tsv contiene un listado de compuestos, expresados como secuencias de caracteres.
Cada línea del archivo corresponde a la información de un compuesto; dentro de cada línea, la primera 
columna asigna un identificador al compuesto, y la segunda columna indica la fórmula química del compuesto.

El archivo solution.tsv es un ejemplo de cómo se deben expresar los valores de similitud química entre compuestos.
Cada línea expresa la similitud entre un par de compuestos, así, en la primera columna se escribe el primer 
identificador de compuesto (compuesto a), la segunda columna expresa el segundo identificador de compuesto (compuesto b),
y la tercera columna expresa el valor del coeficiente Jaccard/Tanimoto entre los dos compuestos (valor T(a,b)). 

Donde T(a,b) es coeficiente de similitud entre el compuesto a y b, Na es el número de elementos en el compuesto a, Nb es 
el número de elementos en el compuesto b, y Nc es el número de elementos comunes entre los compuestos a y b. 

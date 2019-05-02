"""
    OBJETOS: em Python, são abstrações ou conceitos para data. Toda data num programa em
Python é representado por objectos ou por relações entre objetos. Todo objeto tem uma
identidade, um tipo e um valor.

    IDENTIDADE: a identidade dum objeto nunca muda uma vez que ele foi criado; que pode ser
pensado como um endereço dum objecto na memória. O operador << is >> compara a identidade de
dois objetos, enquanto que a função << id(objeto) >> retorna um número inteiro que representa
essa identidade.

    TIPO: o tipo dum objeto determina as operações que o objeto suporta (e. g. qual o tamanho
desse objeto (length)?) e também define as possibilidades de valores para objetos desse tipo.
A função << type() >> retorna o tipo dum objeto (que é um objeto em si mesmo). Como sua
identidade, o tipo dum objeto é também imodificável.

    VALOR: o valor dum objeto pode se modificar. Objetos cujos valores podem ser modificados são
chamados de << mutables >>; os que não podem ser modificados, uma vez criados, são << immutables >>.
    Valor << mutable >> significa que a identidade do objeto permanece a mesma, porém seu valor
se modifica; como, p. ex., em dicts e em lists.
    Valor << immutable >> significa que cada valor desse tipo de objeto tem uma identidade própria
e única; como, p. ex., em strings, numbers, tuples, bytes.

    DESTRUIÇÃO: objetos nunca são explicitamente destruídos; todavia, quando se tornam
inalcançáveis, eles podem estar em << garbage-collected >>. O garbage-collected é um
método automático de desalocação da memória assim que os objetos não são mais alcançáveis.
    É possível se prolongar o envio de objetos ao garbage collection ou omiti-lo completamente.
O uso de ferramentas como tracing ou debugging podem manter objetos vivos que normalmente já
estariam coletados; tal como o uso de exceptions - << try >> e << except >> blocks.
    Objetos externos como << open files >> ou << windows / gui >> são entendidos como livres a
partir do momento em que estão no garbage collection. Como tais objetos não oferecem garantias
de que serão movidos automaticamente para lá, usualmente eles providenciam um acessório para
libertá-los explicitamente; p. ex., um << close() >> método. Um excelente alternativa para o
fechamento de objetos externos está em declarações << try / finally >> e << with >>.

    CONTAINERS: são objetos que contêm referências a outros objetos; p. ex., tuples, lists e
dicts. As referências são partes de um valor do container. Na maioria dos casos, ao se referir
sobre o valor dum container, infere-se os valores mas não as identidades dos objetos contained;
entretanto, ao se referir sobre a mutabilidade dum container, somente as identidades dos objetos
imediatamente contained estão implicados. Portanto, se um immutable container, como um tuple,
contêm uma referência a um objeto mutable, seu valor muda se esse objeto mutable é mudado.

    COMPORTAMENTO DE OBJETOS: tipos afetam quase todos os aspectos do comportamento dum objeto.
Mesmo a importância da identidade do objeto é afetada em algum sentido; pois, em tipos imutáveis,
operações que computam novos valores podem verdadeiramente refletir uma referência a qualquer
objeto existente com o mesmo tipo e valor, enquanto que isso não é permitido para objetos mutáveis.
P. ex., depois de << a = 1 >> e << b = 1 >>, << a >> e << b >> podem ou não se referir ao mesmo
objeto com o valor << 1 >>, a depender da implementação; porém, após << c = [] >> e << d = [] >>,
<< c >> e << d >> referem-se categoricamente a dois objetos diferentes, únicos, embora sejam
do mesmo tipo. Nota-se que << c = d = [] >> aponta o mesmo objeto tanto para << c >> quanto
para << d >>.
"""

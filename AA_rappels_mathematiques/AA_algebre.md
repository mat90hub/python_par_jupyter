# À quoi sert l'algèbre ?

L'algèbre est un domaine d'exploration des mathématiciens, qui a pour objectif de clarifier les règles de généralisation des calculs sur les nombres à d'autres objets comme les vecteurs, les matrices, les polynômes, les fonctions...

# Une première structure algébrique, le groupe

En observant comment nos calculs numériques fonctionnent, les mathématiciens ont définis des structures algébriques, qui sont des ensembles d'objets ayant une ou deux opérations possibles entre deux d'entre eux (on dit aussi des lois). Ils ne se sont pas attachés à décrire ces objets, mais se sont concentrés sur les règles minimales que devaient suivre ces opérations pour que les résultats que nous connaissons puissent être retrouvés.

Une des première structures est le **groupe**. Un groupe est un ensemble d'objets avec une loi opérant sur les couples objets. Pour que cet ensemble soit qualifié de groupe, il faut que cette loi est les propriétés suivantes:

- la loi doit être interne, c'est-à dire que cette loi appliquée à deux éléments doit donner un élément qui reste dans cet ensemble. C'est le cas de l'addition entre deux nombres entiers : l'addition de deux nombres entiers donne toujours un nombre entier (et jamais un réel) ;
- la loi doit être associative. Si on applique la loi à trois éléments au lieu de deux, l'ordre dans lequel on constitue les couples ne doit pas avoir d'importance:
  $\hbox{(1 + 2) + 3 = 1 + (2 + 3)}$ ;
- la loi doit avoir un élément neutre. Un élément neutre est un élément qui n'influe pas l'opération. Par exemple, l'élément neutre de l'addition des entiers est le chiffre zéro :
  $\quad 1 + 0 = 1$ ;
- Chaque élément doit avoir un symétrique, c'est-à dire un élément tel que l'opération appliquée à ce couple d'éléments donne l'élément neutre. On a cette propriété avec les entiers relatifs :
  $\quad 2 + (-2) = 0$ ,

Par contre, si on veut se restreindre aux entiers positifs (les entiers naturels), ils n'ont pas de symétriques, donc on ne peut pas faire un groupe d'entiers positifs avec la seule addition naturelle.

Personnellement, je retiens ces règles avec les lettres IANS (Interne, Associatif, Neutre, Symétrique). Si en plus, l'ordre d'application de la loi n'a pas d'importance on dit que la loi est commutative et le groupe lui-même est qualifié de **groupe commutatif** (on trouve aussi le terme groupe abélien, qui veut dire la même chose). C'est le cas des entiers relatifs :
$\hbox{2 + 3 = 3 + 2}$

## L'exemple d'un groupe cyclique.

Nous avons vu que les entiers relatifs muni de l'addition est un groupe. C'est un groupe de taille infinie.

Si on veut un groupe de taille fini, le plus simple est de prendre comme groupe les restes de la division entière par un entier, par exemple 5 muni de de l'addition. Un tel groupe est qualifié de cyclique et ces éléments sont : { 0, 1, 2, 3, 4 }.

Quand on additionne deux éléments de ce groupe, si le résultat est supérieur à 5, on retire 5 autant de fois qu'il le faut pour retrouver un chiffre entre 0 et 4 (ce qui équivaut à prendre le reste de le division par 5).

Dans ce groupe : 3 + 4 = 2

*( 3 + 4 = 7, je retire 5, il reste 2 )*

Cette loi d'addition ainsi définie est bien  interne. Elle conserve le caractère  associatif de l'addition *normale*, l'élément neutre est toujours 0 et on trouve un symétrique pour chaque élément.

| nombre | symétrique |
| ------ | ----------- |
| 0      | 0           |
| 1      | 4           |
| 2      | 3           |

Le symétrique est simplement le complément à 5.

Ce groupe conserve aussi la commutativité qui existe pour l'addition *normale* des entiers relatifs.

Il existe des groupes cycliques bien connus comme les secondes et les minutes ou les heures. Si on ne tient pas compte de la retenu convertissant les secondes en minutes, les minutes en heures, il s'agit de groupe cycliques. On utilise couramment le symétrique quand on lieu de dire *trois- heures-moins-le-quart*, on dit *deux-heures trois-quart*.

Mais tout n'est pas un groupe. Par exemple, les entiers relatifs munis de la multiplication ne sont pas un groupe, car il n'existe pas d'inverse dans les entiers relatifs.

# Structures avec deux lois internes : les anneaux et les corps.

L'introduction d'une deuxième loi (qu'on appelle souvent la multiplication en analogie avec ce qu'on fait avec les nombres) va permettre de préciser d'autres structures intéressantes: l'anneau et le corps.

## Les anneaux.

Les anneaux demandent d'avoir les règles suivantes:

- L'ensemble est sa première loi (l'addition) est un groupe commutatif ;
- la deuxième loi est interne, associative et a un élément neutre (noté 1);
- la deuxième loi est distributive par rapport à la première loi :
  $2 \times ( 4 + 5) = 2 \times 4 + 2 \times 5$

Si la multiplication est commutative, l'anneau est commutatif.

Une première propriété qu'on peut déduire sur ces structure d'anneau est que l'élément neutre de l'addition est toujours un élément absorbant pour la multiplication :

$$
\forall a , \quad a \times 0 = a \times (1 - 1) = a - a = 0
$$

Cette démonstration utilise uniquement:

- l'élément neutre de l'addition ;
- l'existence d'un élément symétrique pour l'addition (un *opposé*) ;
- l'élément de la multiplication (mais on aurait pu prendre un autre élément) ;
- la distributivité de la multiplication sur l'addition.

Cette propriété sera donc toujours valable quelque soit l'ensemble, du moment que les lois vérifient les règles que nous avons énoncées.

Une structure d'anneau commutatif est déjà très utile. Elle permet par exemple d'utiliser les formules de développements du binôme.

$$
(x + y)^n = \sum_1^n C_n^k x^k\cdot y^{n-k}
$$

ainsi que les autres propriétés similaires comme celle ci :

$$
(x - y) (x + y) = x^2 - y^2
$$

On peut ainsi utiliser toutes les formules qui ne font pas intervenir de division, car dans un anneau, les éléments n'ont pas d'inverse.

Les exemples d'anneaux sont les entiers relatifs avec l'addition et la multiplication. Plus loin, nous verrons aussi les matrices avec l'addition et la loi de composition ou encore les transformations du plan.

## Les corps.

Les corps sont des anneaux pour lesquels les éléments (hormis l'élément neutre de l'addition) ont aussi des symétriques pour la multiplication (des *inverses*, en gardant l'analogie avec les nombres).

Nous avons vu que les entiers relatifs ne pouvaient avoir qu'une structure d'anneau. Pour avoir une structure de corps, il faut utiliser les rationnels, toujours avec l'addition et la multiplication. Les réels ont aussi une structure de corps comme les nombres complexes. Pour les éléments plus complexes, les matrices inversibles comme les transformations bijectives munies de l'addition et de la composition ont des structure de corps.

# Une structure avec une loi externe : l'espace vectoriel.

Jusqu'à présent, nous n'avons présenté que des lois internes faisant intervenir un couple de l'ensemble considéré pour donner un résultat toujours dans cette ensemble.

Mais il peut être intéressant de définir des lois qui ne sont plus des lois internes et c'est le cas des espaces vectoriels.

Un espace vectoriel E est tout d'abord un ensemble (de vecteurs) doté d'une loi interne (l'addition de deux vecteur) et cet ensemble muni de cette loi d'addition est un groupe commutatif. Ensuite, cet espace vectoriel E est associé à un corps K (par exemple l'ensemble des rationnels ou des réels) pour définir une loi externe qui est la multiplication d'un vecteur de l'ensemble E par un scalaire du corps K et cette multiplication doit avoir les propriétés suivantes:

- si $\lambda$ est un élément du corps K, A un vecteur de E, $\, \lambda A$ est toujours dans E
- la multiplication externe est distributive :

  $\lambda (A + B) = \lambda A + \lambda B$

  $(\lambda + \mu) A = \lambda A + \mu A$
- On peut aussi effectuer les opérations dans l'ordre qu'on veut:

  $(\lambda \mu) A = \lambda (\mu A)$
- enfin, l'élément neutre du corps est aussi un élément neutre pour cette multiplication externe.

  $1 \cdot A = A$

Les ensembles de vecteurs que nous connaissons sont des espaces vectoriels. Mais on peut aussi dire la même chose sur leur représentation sous forme de liste de coordonnées. La dimension de l'espace vectoriel n'a pas besoin d'être limitée à deux ou trois et on peut donc l'augmenter autant que l'on veut.

Nous avons vu plus haut que l'ensemble des matrices avec l'addition et la composition des matrices pouvait être considéré comme un anneau (ou un corps si on se restreint aux matrices inversibles). L'ensemble des matrices peut aussi être considéré comme un espace vectoriel en utilisant une règle de multiplication d'une matrice par un scalaire (qui serait la multiplication de tous les termes de cette matrice par le scalaire).

## Les familles libres, génératrice ou base

Dans un espace vectoriel, une famille de vecteurs est dite liée, s'il existe des scalaires du corps associé tel que:

$$
(V_i)_i \, \text{est liée} \Longleftrightarrow \exists (\lambda)_i \in K ,\quad \sum \lambda_i V_i = 0
$$

Une **famille libre** est une famille qui n'est pas liée : il n'existe pas de paramètres non nuls permettant de faire une combinaison linéaire aboutissant au vecteur nul.

Une **famille génératrice** est une famille de vecteurs $(V_i)_i$ tel que pour tout vecteur, on pourra le décomposer avec cette famille.

$$
(V_i)_i \, \text{est génératrice} \Longleftrightarrow\forall V \quad \exists (\lambda_i)_i \quad \sum \lambda_i V_i = V
$$

Une **base** est une famille libre et génératrice. Elle permet de faire une décomposition unique de tous les vecteurs de l'espace vectoriel.

Le nombre d'élément de la base caractérisera la dimension de l'espace vectoriel.

Ce qu'on peut retenir de ceci, c'est que quand on a une structure d'espace vectoriel, on peut alors toujours trouver une base qui permettra de générer tous les éléments de l'espace vectoriel.

# Rappel sur les applications.

Une [application](https://fr.wikibooks.org/wiki/Alg%C3%A8bre/Fonctions_et_applications) d'un ensemble $E$ dans un ensemble $F$ (ou de $E$ vers $F$) est une correspondance, qui à tout élément $x$ de $E$ associe un et un seul élément $y$ de l'ensemble $F$.

$$
\forall x \in E ,\quad \exists ! \, y \in F \quad \backslash \quad y = f(x)
$$

- $y$ est appelée l'image de $x$ par $f$ et se note $f(x)$.
- $x$ est un antécédent de $y$ par $f$.
- $E$ s'appelle l'ensemble de départ ou l'ensemble de définition de $f$
- $F$ est l'ensemble d'arrivée.

De part ses propriétés, une application peut se représenter par un graphe, l'ensemble des antécédents en abscisse et les images en ordonnées. C'est d'ailleurs ainsi qu'on peut reconnaître une application. Par exemple, une application ne peut pas représenter un cercle, mais seulement un demi-cercle, car il ne faut qu'une seule image pour chaque antécédent sur l'axe des abscisses.

## Application injective.

Une application est injective si quand deux antécédents sont différents alors leurs images sont différentes.

$$
\forall (x,y) \in E, \quad x \neq y \,\Longrightarrow \, f(x) \neq f(y)
$$

On peut aussi utiliser la contraposée de cette proposition (voir un cours de logique).

$$
\forall (x,y) \in E, \quad f(x) = f(y) \, \Longrightarrow \, x = y
$$

En représentation graphique, cela veut dire que le graphe ne coupera n'importe quelle droite horizontale qu'en un seul point. Par exemple, une parabole n'est pas un graphe d'application injective.

## Application surjective.

Une application est surjective si tout élément de l'ensemble d'arrivée a toujours un antécédent: l'ensemble $F$ est égal à l'ensemble des images de $E$.

Sur le graphe, cela veut dire qu'une droite horizontale rencontre toujours le graphe de l'application. Une parabole n'est pas le graphe d'une application surjective.

## Application bijective

Une application est bijective si et seulement si elle est injective et surjective. Cela veut dire que tout élément de $F$ a un et un seul antécédent dans $E$.

$$
\forall y \in F ,\quad \exists ! \, x \in E \quad \backslash \quad y = f(x)
$$

Cette expression est très similaire à celle d'une application et de fait, si une application est bijective, il existe alors toujours une application inverse $f^{-1}$.

# Les morphismes.

Une application est appelée un morphisme quand elle s'effectue d'une structure à une autre structure du même type et que leurs lois et leurs éléments neutre se conserve dans cette application.

Dans un morphisme de groupe, on aura donc.

$$
f: (E, *) \mapsto  (G, \times) \quad / \quad f(x * y) = f(x) \times f(y)
$$

Si $e$ est l'élément neutre de E, $\quad e'$ l'élément neutre de G, $\quad f(e) = e'$.

Pour les anneaux et les corps, le morphisme doit avoir ces propriétés pour les deux opérations, l'addition et la multiplication.

Pour les espaces vectoriels, cette propriété doit s'appliquer pour l'opération externe.

$$
f(\lambda \cdot x) = \lambda \circ f(x)
$$

En tant qu'application, un morphisme peut être injectifs, surjectifs ou bijectif. Les morphismes bijectifs sont très importants et on les nomme **automorphismes**.

Deux structures reliées par un **automorphisme** ont des comportements tellement semblables, qu'on peut en pratique les confondre. C'est le cas des transformations du plan et des matrices (2x2) qui les représentent. L'ensemble des matrices (2 x 2) est un espace vectoriel comme l'ensemble des transformations du plan et on peut utiliser l'une ou l'autre des représentations.

37

# Programming MAP REDUCE

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/588599b614f4382c55c019a5218e4832cdcbd2d0d11c148c692e46c938c85d61.jpg)

# Map-Reduce et programmation fonctionnelle

# Map

$\triangleright$  Applique une fonction sur chaque élément d'une liste  
$\triangleright$  Retourne une liste de résultats  
$\gg$ $\operatorname{Map}(\mathrm{f}(\mathrm{x}), \mathrm{X}[1:\mathrm{n}])$  à  $[\mathrm{f}(\mathrm{X}[1]), \dots, \mathrm{f}(\mathrm{X}[\mathrm{n}])]$

Example :

$$
\operatorname {M a p} \left(\mathrm {X} ^ {2}, [ 0, 1, 2, 3, 4, 5 ]\right) = [ 0, 1, 4, 9, 1 6, 2 5 ]
$$

# Reduce/fold

> Fait l'iteration d'une fonction sur une liste d'éléments  
$\triangleright$  Applique la fonction sur les résultats precedents et l'objet courant  
$\triangleright$  Retourne un et un seul résultat,

Example :

$$
\operatorname {R e d u c e} (\mathbf {x} + \mathbf {y}, [ 0, 1, 2, 3, 4, 5 ]) = (((((0 + 1) + 2) + 3) + 4) + 5) = 1 5
$$

# Map-Reduce: Example 1

# -Calcul des ventes-

Imaginons que vous ayez plusieurs magasins que vous gerez à travers le monde

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/505e6607a16df93f5e1cabc86444fa5efdd7f3bfdc3cb57ba2e39bcc4180aafe.jpg)

2018-01-01 Miami Clothes 25.99

2018-01-01 Miami Music 12.15

2018-01-02 NYC Toys 3.10

2018-01-02 Miami Clothes 50.00

2017-05-16 London Toys 25.19

Objectif

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/7d31c4038903c3ceb349498f72a6db322201c5c8600e1a9f6f893a07350870e4.jpg)

Calculer le total des ventes par magasin pour l'année 2018

Clef Valeur

Miami 88.14

NYC 3.10

BigData

# Map-Reduce: Example 1

# -Calcul des ventes-

# □ Approche traditionnelle

Si on utilise les hashtables sur 1To, Problèmes?

Ca ne marchera pas?  
Problème de mémoire?  
Temps de traitement long?  
Réponses erronées?

Le traitement sequential de toutes les données peut s'avérer très long  
Plus on a de magasins, plus l'ajout des valeurs à la table est long  
Il est possible de tomber à court de mémoire pour enregistrer cette table  
Mais cela peut marcher, et le résultat sera correct

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/2e947c76513a6f42a6349519a2edde224d17328b95c58d7e3392dd852c652926.jpg)

<table><tr><td>2018-01-01</td><td>Miami</td><td>Clothes</td><td>25.99</td></tr><tr><td>2018-01-01</td><td>Miami</td><td>Music</td><td>12.15</td></tr><tr><td>2018-01-02</td><td>NYC</td><td>Toys</td><td>3.10</td></tr><tr><td>2018-01-02</td><td>Miami</td><td>Clothes</td><td>50.00</td></tr><tr><td>2017-05-16</td><td>London</td><td>Toys</td><td>25.19</td></tr></table>

# Map-Reduce: Example 1

# -Calcul des ventes-

# □ Approche Big Data

On suppose que le livre sur HDFS est découvert en deux parties:

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/f6c22984dd56b26074b0c0e6f52f5e0f6cc700dae2ece43e51d0c21d937202f5.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/a6054b6defb798249990c08e13da75d421d591055a8b6a77e8418b5c9e3c13c6.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/8bfb57520696dd70ac85d246f8debbea94eb31815741e6dba5113f4723b43913.jpg)  
BigData

<table><tr><td>2018-01-01</td><td>Miami</td><td>Clothes</td><td>25.99</td></tr><tr><td>2018-01-01</td><td>Miami</td><td>Music</td><td>12.15</td></tr><tr><td>2018-01-02</td><td>NYC</td><td>Toys</td><td>3.10</td></tr><tr><td>2018-01-02</td><td>Miami</td><td>Clothes</td><td>50.00</td></tr><tr><td>2017-05-16</td><td>London</td><td>Toys</td><td>25.19</td></tr></table>

# Map-Reduce: Example 1

# -Calcul des ventes-

# Etape 1: MAP

Faire des petitstraitements en paralllellegne par ligne:Pas d'opérations de calculs entre plusieurs lignes.  
2 Types de filtrage dans cet exemple:

- Filtrage vertical : diminuer le nombre de colonnes: nom magasin, valeur des ventes .  
- Filtrage horizontal: supprimer les lignes non concernées (année autre que 2018).

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/89789817ee979a3ed4646a1dc12adc10ce1671cc3ade2355361557797ffc1c43.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/4b62b8b536e20ef63bd470130e77902bdb1e4f05e8145b75de0a74091aad2dd4.jpg)

(Miami,25.99)

(Miami,12.15)

Etape 1:Map

(Clef, Valeur)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/2667eca63e046f0b98e79e6cf5be3db0af97cbd0e1e637601bd5ceabc63c0446.jpg)  
BigData

(NYC,3.10)

(Miami,50.00)

2018-01-01 Miami Clothes 25.99

2018-01-01 Miami Music 12.15

2018-01-02 NYC Toys 3.10

2018-01-02 Miami Clothes 50.00

2017-05-16 London Toys 25.19

# Map-Reduce: Example 1

# -Calcul des ventes-

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/6d31acd03b26e19869763a92c2b456bbd9ef6e66f0310106849e922974a43264.jpg)

# Etape 2: Sort and Shuffle

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/cc9d2b19730589185ddb6c4cb6e251cc614499529378bf09a9dd9e75828f2705.jpg)

Etape faite automatiquement par Hadoop, composée de deux sous étapes:

Shuffle: Rasseblement des données dans la même machine  
Sort: Tri par clé pour regrouper les ventes de même magasin successivement

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/4ca98ef118b06763b71662cb00baa2e6309d7aad4c685913c4b7061278600532.jpg)

<table><tr><td>2018-01-01</td><td>Miami</td><td>Clothes</td><td>25.99</td></tr><tr><td>2018-01-01</td><td>Miami</td><td>Music</td><td>12.15</td></tr><tr><td>2018-01-02</td><td>NYC</td><td>Toys</td><td>3.10</td></tr><tr><td>2018-01-02</td><td>Miami</td><td>Clothes</td><td>50.00</td></tr><tr><td>2017-05-16</td><td>London</td><td>Toys</td><td>25.19</td></tr></table>

(Miami,25.99)

(Miami,12.15)

Etape 2: Shuffle

(Clef, Valeur)

(Miami,25.99)

(Miami,12.15)

(NYC,3.10)

(Miami,50.00)

(NYC,3.10)

(Miami,50.00)

BigData

Etape 2':

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/8990231783eec0442c7ab9845a52940dab21f5e19c6673d1c35d7f1f34ffdd9a.jpg)

(Miami,25.99)

(Miami,12.15)

(Miami,50.00)

(NYC,3.10)

# Map-Reduce: Example 1

# -Calcul des ventes-

# Etape 3: Reduce

Comme le mapper, le code de reducer doit etre écrit par l'utilisateur  
Ici; faire la somme des ventes par magasin.  
(Clef, Valeur)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/a6c77dbab35b3cd0279c7dd8941d10b512fdf44c7e5a2b76ad0d1bb8c41efbe5.jpg)

<table><tr><td>2018-01-01</td><td>Miami</td><td>Clothes</td><td>25.99</td></tr><tr><td>2018-01-01</td><td>Miami</td><td>Music</td><td>12.15</td></tr><tr><td>2018-01-02</td><td>NYC</td><td>Toys</td><td>3.10</td></tr><tr><td>2018-01-02</td><td>Miami</td><td>Clothes</td><td>50.00</td></tr><tr><td>2017-05-16</td><td>London</td><td>Toys</td><td>25.19</td></tr></table>

BigData

<table><tr><td>(Miami,25.99)</td></tr><tr><td>(Miami,12.15)</td></tr><tr><td>(Miami,50.00)</td></tr><tr><td>(NYC,3.10)</td></tr></table>

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/b26fa9496080c68cc95bff3927b3c6dea872e916ea3c7a33204b170efabefe55.jpg)

(Miami, 88.14) (NYC, 3.10)

# A retenir: L' étape MAP

# Paires (key, value) en entrée

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/ad85d455f8c48edef442971f365239c23ad9e9e6bcd90609ec2bccc8e3d250f4.jpg)

v1

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/c8e307e56a235da0b02f40acb793b533fe72ce99519622b8b738b62288de95fd.jpg)

v2

#

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/cbdb8a72ad64091390b50a49feee49e530c0c7908247763d02f30033ecc8eb5c.jpg)

vn

# Paires (key, value) intermediaries

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/ce83552d7aabb07e8a3e8cb8df3874927898b86c9aa7f49bf68d4a5d30ee2b2c.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/8be12be1cb18bf8f1fd37520043a6b6a9764ffbf958579b2c3785597ed6160a2.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/17ba56ea3a81c0bd6de78aa8f247792c5ce042625abeeb6032da87252ca6add2.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/af964604ad1167c822dcd6759ad05ad747f6286750b50c906f61d6cfbca9aadf.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/db3ee2552373ceb8e64230e00398910922b5031ec64d5ac2b71c97d43e68017c.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/4405284a3afe47bcf83b8ed6c7887efcba4fc5de0658607d1271eef838336980.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/493ce4e70fda4c60311b682c1169a18505bd2d9b6ed7dc1231fa1ed002bb7576.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/dd3227b3fc07cd086a5e0d2cfacc67ac2654d80596efa40d6c619eb88dbc9f7d.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/f597cadf99c9bcf00b1de3613c766dbff91bb7cf1b513d891ed7963e3e4d5621.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/e45df3d107a284be673904b1c4250ce371cfc27457bc283fd6929455f4e3a460.jpg)

Dans l' étape Map, le but est de partir d'un couple <clé, valeur> et d'y associé de nouveaux couples <clé, valeur>. Les clés en entrée sont différentes des clés générées par le Map.  
Le nombre de tâches Map ne dépend pas du nombre de nœuds, mais du nombre de blocs de données en entrée. Chaque bloc se fait assigner une seule tâche Map. BigData

# A retenir : L’étape Shuffle and Sort

Paires (key, value) intermediaries

Groupes (key, values)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/21d0db7ec737f524bda7df5b0dec758a298bb30aa4bca7a5939a337cd2d8f1b3.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/c3af74b996da027a05a561c675ae481cff4abd7d24e9cfd86ba0328c210b1913.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/7bf64d391b53829e5eee230791f781eaf26955162261c153ff7a4100b70e92fd.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/755c7949ff5f2fd92cb869a3a7b2554becf264468c889bb0c3215b675f034a28.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/5b799492e57405b0ef139237fcc0dac19515f4fc69573ad0fbbef320b6b250e5.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/b59815c35eb4293bb78101806052a3b865289470ee5bbab4b8c8e7c39104365d.jpg)

(\~SQL Group by)

#

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/cedf7ca936063bf82fafc32f371d7dc716c7eedb97145c81025a8950c5442272.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/cab8da6eb8dfc7fa7d435405161f4e69e5e331e49e9fd672e1dca0e19a989647.jpg)

C'est un étape automatique de regroupement et tri s'intègre entre MAP et REDUCE pour la redistribution des données afin que les paires produites par Map ayant les mêmes clés soient sur les mêmes machines.

# A retenir : L'étape REDUCE

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/b06c46cca052fa89c6597317ca26f67a306a977eee50ceec860761c47322a144.jpg)

Dans l'etape Reduce le but est d'associer toutes les valeurs correspondantes à la même clé. On souhaite donc rassembler tous les couples <clé, valeur>.  
Pour le traitement, les taches Reduce suivent le même schéma que les taches Map.  
Elles n'ont pas à s'exécuter parallèment et dés qu'un noéud fini son traitement un autre lui est aussi tôt assigné. BigData

# Map-Reduce: Example 2

# -Word Count-

□ Word Count: Comptage des occurrences des mots

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/08220b044dffbd48df58ac3deadafeef3148d78299cc8e73df73cb9a117002fb.jpg)

# Map-Reduce: Example 2

# -Word Count-

# Pseudocodes du map et du reduce

```python
map(key, text): # input: key=position, text=line  
for each word in text:  
    Emit(word, 1) # outputs: key/value  
reduce(key, list of values): # input: key == word, our mapper output  
count = 0  
for each v in values:  
    count += v  
Emit(key, count) # it is possible to emit multiple (key, value) pairs here
```

# Map-Reduce: Example 3

# - Graphe Social-

On administré un réseau social comptant des millions d'utilisateurs.  
Pour chaque utiliser, on a dans notre BD la liste des utilisateurs qui sont ses amis sur le réseau (via une requête SQL).  
On souhaite afficher quand un utiliser va sur la page d'un autre utiliser une indication Vous avez N amis en commun ;  
On ne peut pas se permettre d'effectuer une série de requêtes SQL à chaque fois que la page est accédée (trop lourd en traitement).

$\Rightarrow$  On va donc développper des programmes Map et Reduce pour cette opération et executer le traitement toutes les nuits sur notre BD, en stockant le résultat dans une nouvelle table.

# Map-Reduce: Example 3

# - Graphe Social-

Ici, nos données d'entrée sont sous la forme Utilisateur  $\Rightarrow$  Amis:

<table><tr><td>A⇒B,C,D</td></tr><tr><td>B⇒A,C,D,E</td></tr><tr><td>C⇒A,B,D,E</td></tr><tr><td>D⇒A,B,C,E</td></tr><tr><td>E⇒B,C,D</td></tr></table>

Puisqu'on est interessed par l'information amis en commun entre deux utilisateurs et qu'on aura a terme une valeur par clé, on va besoin pour clé la concatenation entre deux utilisateurs.  
Par exemple, la clé  $A - B$  désignera les amis en commons des utilisateurs  $A$  et  $B$ .  
On peut segmenter les données d'entrée la aussi par ligne.

# Map-Reduce: Example 3

# - Graphe Social-

# La phase MAP

$\triangleright$  Notre opération Map va se contenter de prendre la liste des amis fournie en entrée, et va générer toutes les clés distinctes possibles à partir de cette liste.  
La valeur sera simplement la liste d'amis, tellequelle.  
On fait également en sorte que la clé soit toujours triée par ordre alphabetique (clé  $B - A$  sera exprimée sous la forme  $A - B$ ).  
$\triangleright$  Ce traitement peut parairtre contre-intuitif, mais il va a terme nous permetre d'obtenir, pour chaque clé distincte, deux couples (key, value) : les deux listedes d'amis de chacun des utilisateurs qui compose nla cle.

# Map-Reduce: Example 3

# - Graphe Social-

# La phase MAP

Le pseudo code de notre operation Map est le suivant :

```txt
UTILISATEUR = [PREMIERE PARTIE DE LA LIGNE]  
POUR AMI dans [RESTE DE LA LIGNE], FAIRE:  
SI UTILISATEUR < AMI:  
    CLEF = UTILISATEUR + AMI  
SINON:  
    CLEF = AMI + UTILISATEUR  
GENERER COUPLE (CLEF; [RESTE DE LA LIGNE])
```

Par exemple, pour la première ligne :

```javascript
A  $\Rightarrow$  B, C, D
```

On obtienda les couples (key, value):

```lisp
("A-B"; "BCD")
```

```lisp
("A-C"; "BCD")
```

```lisp
("A-D"; "B C D")
```

# Map-Reduce: Example 3

# - Graphe Social-

# La phase MAP

Pour la seconde ligne :

```csv
B=>A,C,D,E
```

On obtienda ainsi :

```lisp
("A-B"; "ACDE")
```

```txt
("B-C"; "A C D E")
```

```txt
("B-D"; "A C D E")
```

```txt
("B-E"; "A C D E")
```

Pour la troisième ligne :

```csv
C => A, B, D, E
```

On aura :

```lisp
("A-C"; "ABDE")
```

```lisp
("B-C"; "ABDE")
```

```lisp
("C-D"; "ABDE")
```

```lisp
("C-E"; "ABDE")
```

# Map-Reduce: Example 3

# - Graphe Social-

# Entre la phase MAP et la phase REDUCE

Une fois l'opération Map effectue, Hadoop va recupérer les couples (key, valeur) de tous les fragments et les groupe par clé distincte. Le résultat sur la base de nos données d'entrée :

<table><tr><td>Pour la clef</td><td>&quot;A-B&quot;: valeurs</td><td>&quot;A</td><td>C</td><td>D</td><td>E&quot;</td><td>et</td><td>&quot;B</td><td>C</td><td>D&quot;</td><td></td></tr><tr><td>Pour la clef</td><td>&quot;A-C&quot;: valeurs</td><td>&quot;A</td><td>B</td><td>D</td><td>E&quot;</td><td>et</td><td>&quot;B</td><td>C</td><td>D&quot;</td><td></td></tr><tr><td>Pour la clef</td><td>&quot;A-D&quot;: valeurs</td><td>&quot;A</td><td>B</td><td>C</td><td>E&quot;</td><td>et</td><td>&quot;B</td><td>C</td><td>D&quot;</td><td></td></tr><tr><td>Pour la clef</td><td>&quot;B-C&quot;: valeurs</td><td>&quot;A</td><td>B</td><td>D</td><td>E&quot;</td><td>et</td><td>&quot;A</td><td>C</td><td>D</td><td>E&quot;</td></tr><tr><td>Pour la clef</td><td>&quot;B-D&quot;: valeurs</td><td>&quot;A</td><td>B</td><td>C</td><td>E&quot;</td><td>et</td><td>&quot;A</td><td>C</td><td>D</td><td>E&quot;</td></tr><tr><td>Pour la clef</td><td>&quot;B-E&quot;: valeurs</td><td>&quot;A</td><td>C</td><td>D</td><td>E&quot;</td><td>et</td><td>&quot;B</td><td>C</td><td>D&quot;</td><td></td></tr><tr><td>Pour la clef</td><td>&quot;C-D&quot;: valeurs</td><td>&quot;A</td><td>B</td><td>C</td><td>E&quot;</td><td>et</td><td>&quot;A</td><td>B</td><td>D</td><td>E&quot;</td></tr><tr><td>Pour la clef</td><td>&quot;C-E&quot;: valeurs</td><td>&quot;A</td><td>B</td><td>D</td><td>E&quot;</td><td>et</td><td>&quot;B</td><td>C</td><td>D&quot;</td><td></td></tr><tr><td>Pour la clef</td><td>&quot;D-E&quot;: valeurs</td><td>&quot;A</td><td>B</td><td>C</td><td>E&quot;</td><td>et</td><td>&quot;B</td><td>C</td><td>D&quot;</td><td></td></tr></table>

...on obtient bien, pour chaque clé  $USER1 - USER2$ , deux listes d'amis : les amis de  $USER1$  et ceux de  $USER2$ .

# Map-Reduce: Example 3

# - Graphe Social-

# La phase REDUCE

Il nous faut enfin écrire notre programme Reduce. Il va receivevoir en entree toutes les valeurs associées à une clé. Son role va être très simple : déterminer quels sont les amis qui apparaissent dans les listes (les valeurs) qui nous sont fournies.

```txt
LISTE_AMISCOMMUNs  $\equiv$  //Liste vide au depart.   
SI LONGUEUR(VALEURS)！  $= 2$  ，ALORS: //Ne devrait pas se produit. RENVOYER ERREUR   
SINON: POUR AMI DANS VALEURS[0]，FAIRE: SI AMI EGALEMENT PRESENT DANS VALEURS[1]，ALORS: //Present dans les deux listedes d'amis, on I'ajoute. LISTE_AMIS COMMUNs+=AMI   
RENVOYER LISTE AMIS COMMUNs
```

# Map-Reduce: Example 3

# -Graphe Social-

# La phase REDUCE

Aprèsexecutionde l'opération Reduce pour les valeurs de chaque clé unique, on obtendra donc, pour une cle  $A - B$  ,lesutilisateurs qui apparaisent dans la liste des amis de A et dans la liste des amis de  $B$  Autrement dit, on obtendra la liste des amis en commun des utilisateurs A et  $B$  .Le résultat est:

```csv
"A-B": "C, D"  
"A-C": "B, D"  
"A-D": "B, C"  
"B-C": "A, D, E"  
"B-D": "A, C, E"  
"B-E": "C, D"  
"C-D": "A, B, E"  
"C-E": "B, D"  
"D-E": "B, C"
```

On sait ainsi que  $A$  et  $B$  ont pour amis communs les utilisateurs  $C$  et  $D$ , ou encore que  $B$  et  $C$  ont pour amis communs les utilisateurs  $A, D$  et  $E$ .

# Map-Reduce: Example 3

# - Graph Social

# Synthese

En utilisant le modele MapReduce, on a ainsi pu creer deux programmes très simples (nos programmes Map et Reduce) de quelques lignes de code seulement, qui permettent d'effectuer un traitementsonsse toute assez complexe.  
Mieux encore, notre traitement est parallélisable: même avec des dizaines de millions d'utilisateurs, du moment qu'on a assez de machines au sein du cluster Hadoop, le traitement sera effectué rapidement. Pour aller plus vite, il nous suffit de rajouter plus de machines.  
Pour notre réseau social, il suffira d'effectuer ce traitement toutes les nuits à heures fixe, et de stocker les résultats dans une table.

Ainsi, lorsqu'un utilisateur visitera la page d'un autre utilisateur, un seul SE-LECT dans la BD suffira pour obtenir la liste des amis en commun - avec un poids en traitement très faible pour le serveur.

# Fonctionnement de Map Reduce

# Hadoop MapReduce: Fonctionnement

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/8cde918a4e2cc46387c4ea7b60a226285934942c505aaee97f3716e3e02830b2.jpg)  
BigData et NOSQL- MP2

# Hadoop MapReduce: Fonctionnement

Deux démons: Job Tracker et Task Tacker  
Job Tracker

S'exécate sur la même machine que le Namenode (machine master)  
Divise le travail sur les Mappers et Reducers s'excutant sur les différents nœuds.

Task Tacker

S'exécate sur chacun des noèuds pour exécuter les vraies tâches de MapReduce.  
Choisit detraiter (map et reduce) un bloc sur la même machine que lui affecté  
S'il est déjà occupé, la tâche revient à un autre tracker qui utilisera le réseau (rare).

# Hadoop MapReduce: Fonctionnement

69

Un job Map-Reduce est divisé en plusieurs tâches mappers et reducers  
□ Chaque tâche est executée sur un nœud du cluster  
□ Chaque nœud a un certain nombre de slots prédéfinis (Map Slots+ Reduce Slots).  
Un slot est une unité d'exécution qui représentée la capacité du Task Tracker à exécuter une tâche (map ou reduce) individuellement, à un moment donné.

Le Job Tracker se charge à la fois:

D'allouer les ressources (mémoire, CPU...) aux différentes tâches  
- De coordonnier l'exécution des jobs Map-Reduce  
- De réserver et ordonnancer les slots, et de gérer les fautes en réalisant les slots au besoin.

# Hadoop MapReduce: Fonctionnement

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/eb6c563d-b7f4-44e5-829f-03ced5787996/97af67e6e16f2a134bdc05dd2065d70ce5b5a4d1ec773b265d3c02e14825fd30.jpg)
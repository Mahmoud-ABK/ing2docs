# Pattern Bridge

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/72186d3f-4971-4d02-b02c-1d67b0de73b0/cd8385bf055578ffaac958ca9be1fb7dad41f30ad5c989a7d73de09ed49502cc.jpg)

# Définition

Le pattern Bridge a pour but de dissocier une abstraction de son implémentation, afin qu'elles poussent évolver indépendamment l'une de l'autre.  
En d'autres termes, on peut éviter de combiner plusieurs dimensions de variation pour une même hierarchie de classes.

# Problème typique

Supposons qu'on ait une classe Shape et des sous-classes comme Circle, Square. Et que chaque forme puisse etre dessinée soit en 2D, soit en 3D.

Sans Bridge, on aurait cette structure UML:

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/72186d3f-4971-4d02-b02c-1d67b0de73b0/03221f431aea33135b77574bf2a98af01cd1da1b56cf52b236b331580ed22739.jpg)

# Solution Bridge

Avec Bridge, on sépare les deux dimensions d'évolution :

<table><tr><td>Dimension 1</td><td>Dimension 2</td></tr><tr><td>Type de forme (abstraction)</td><td>Type de rendu (implémentation)</td></tr></table>

On obtient la structure suivante:

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/72186d3f-4971-4d02-b02c-1d67b0de73b0/41471989771a4833b523e81b7920464bfc0c32cd4b35723e4c3991d95769e7bc.jpg)

# Structure UML

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/72186d3f-4971-4d02-b02c-1d67b0de73b0/1e3b77da8c632f763a005e0e06400985e5f8afb9024fda40538f2193d8736c53.jpg)

# Avantages et inconveniens

# Avantages:

- Évite la prolifération de classes.  
- Abstraction et implémentation évoluent indépendamment.  
- Favorise la composition只不过 que l'héritage.

# Inconvénients:

- Plus de classes et d'indirections.  
- Complexité accrue pour les petits projets.

# Exercice 1— Messages avec différents canaux

# Objectif:

Créer un système où un Message peut être envoyé via différents canaux (Email, SMS, Push).

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/72186d3f-4971-4d02-b02c-1d67b0de73b0/a928bb602a1066939fd2ce090c8dd0c8e915262b58f13618947550859e4b6907.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/72186d3f-4971-4d02-b02c-1d67b0de73b0/9ff5836ed745de61dbeb9d52b5ffacf9e7f12067be424ec7a81ab459444de920.jpg)

# Exercice 2—Paialement en ligne

# Objectif:

Créer une hierarchie Payment indépendante du mode de paiement (PayPal, CreditCard).

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/72186d3f-4971-4d02-b02c-1d67b0de73b0/756f92eea69594583994c6145215134c3532f1892a17a54f1b26757fe019feec.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/72186d3f-4971-4d02-b02c-1d67b0de73b0/752056be198838a837fb2aa70b816f8917ad5f01b33bf1f6c06281328327b02b.jpg)

# Exercice de synthèse — Système de génération de rapports multi-format

# Objectif:

Une société d'analyse de données peut creator un système de génération automatique de rapport. Chaque type de rapport (ex : Rapport financier, Rapport de performance, Rapport RH) peut etre exporte dans plusieurs formats : HTML, PDF, Excel.

Actuellement, le système est conçu de manière naïve

:FinancialReportPDF, FinancialReportHTML, FinancialReportExcelPerformanceReportPDF, PerformanceReportHTML, PerformanceReportExcelHRReportPDF, HRReportHTML, HRReportExcel

# Exercice de synthèse — Système de génération de rapport multis-format

# Travail demandé:

1. Identifiez les problèmes de la solution actuelle  
2. Identifiez les deux dimensions d'évolution présentes dans ce système.  
3. Proposez une refactorisation qui permette :

$\succ$  d'ajouter un nouveau type de rapport (ex : Rapport d'audit) sans modifier les formats ;  
> d'ajouter un nouveau format (ex : JSON) sans modifier les rapportés existants.

4. Donnez un diagramme de classes conceptuel de la nouvelle architecture.  
5. Proposez une illustration en pseudo-code ou Java simplex

# Exercice de synthèse — Système de génération de rapporte multi-format

Problèmes de la solution actuelle :

- Chaque nouvelle combinaison type de rapport × format de sortie entraîne la création d'une nouvelle classe.  
- Les changements dans un format (ex : PDF → nouvelle librarianie)IMPÔNT des modifications dans toutes les classes concernées.  
Il devient impossible de faire évolver le système sans le casser.

# Pattern Proxy

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/72186d3f-4971-4d02-b02c-1d67b0de73b0/13cb0615b9da4a4cdaeb29725dc7e612ee132c4b1507c1db30c6529620870f10.jpg)

# Définition

Le design pattern Proxy est un modele de conception structurel qui fournit un substitut ou un intermédiaire a un autre objet pour contrôler l'accès à cet objet.  
En Java, un proxy peut être utilisé pour ajouter une couche d'indirection et d'interception, permettant de modifier ou de contrôler l'accès aux fonctionnalités d'un objet sans en ALTERER le code source.

# Problème typique

On dispose d'un objet RealSubject coupteux à créé ou à manipuler.

On désire:

- Retarder la création jusqu'àu moment où il est juste nécessaire (lazy loading).  
- Contrôler l'accès selon l'utilisateur ou le contexte (protection).  
- Ajouter des fonctionnalités comme le logging ou la mise en cache.

# Problème typique

Example:

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/72186d3f-4971-4d02-b02c-1d67b0de73b0/873ede2ebe459bad7237856b3e6077933845feb98133e435e9ec3862f3d26752.jpg)

Les requêtes sur la base de données sont parfois très lentes.

Sans Proxy, chaque client manipule directement l'objet reel et toutes les fonctionnalités supplémentaires doivent etre intégrées dans l'objet.

# Problème typique

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/72186d3f-4971-4d02-b02c-1d67b0de73b0/761dd51808e9a995eb98c7efed8aa2e71c4e2970418e36e31d2296a9cf4d3c1e.jpg)

- Proxy propose de creator une classeprocuration qui a la même interface que l'objet du service original.  
- L'objet procuration est passé à tous les clients de l'objet original.  
Lors de la réception d'une demande d'un client, la procuration creée l'objet du service original et lui délege la tâche.

# Structure UML

4 Le Client passe par la même interface pour travailler avec les services et les procurations. Il est ainsi possible de passer une procuration à n'importe quel code qui attend un objet service.  
3 La Procuration est une classe dotée d'un attribut qui pointe vers un objet service. Une fois que la procuration a lancé tous sestraitements (instanciation paresseuse, historisation des logs, verification des droits, mise en cache, etc.),elle envoie la demande à l'objet du service.  
En général, lesprocurations gerentle cycle de vie de leurs objets service.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/72186d3f-4971-4d02-b02c-1d67b0de73b0/0bb67b055a350e5a3c99234aa5b21af6e2b6cd6af390083e1e5a4a0cf28da1cf.jpg)

1 L'Interface Service déclare l'interface du service. La procuration doit implémenter cette interface afin de pouvoir se déguiser en objet du service.

2 Le Service est une classe qui fournit la logique métier dont vous poulez vous servir.

# Types de proxy

<table><tr><td>Type</td><td>Description</td></tr><tr><td>Virtual Proxy</td><td>Retarde la création d&#x27;un objet couâteux jusqu&#x27;à ce qu&#x27;il soit réellement utilisé.</td></tr><tr><td>Protection Proxy</td><td>Contrôle l&#x27;accès à l&#x27;objet selon les droits de l&#x27;utilisateur.</td></tr><tr><td>Remote Proxy</td><td>Permet d&#x27;accéder à un objet situé sur un autre serveur/machine.</td></tr><tr><td>Cache Proxy</td><td>Stocke les résultats d&#x27;appels couâteux pour éviter de recalculator.</td></tr><tr><td>Logging Proxy</td><td>Intercepte les appeals pour journaliser ou monitorer l&#x27;utilisation.</td></tr></table>

# Example 1—Virtual Proxy

```java
// Interface commune   
interface Image { void display();   
}   
// Objriel   
class Reallmage implements Image { private String filename; public Reallmage(String filename) { thisFilename  $=$  filename; loadFromDisk(); } private void loadFromDisk() { System.out.println("Chargement de "+filename); } public void display() { System.out.println("Affichage de "+filename); }
```

```java
// Proxy   
class Proxylmage implements Image{ private RealImage realImage; private String filename; public Proxylmage(String filename) { thisFilename  $\equiv$  filename; } public void display() { if (realImage  $= =$  null) { realImage  $\equiv$  new RealImage(filename); // lazy loading 1 realImage.display(); 1
```

# Example 1—Virtual Proxy

```java
// Test   
public class ProxyDemo { public static void main(String[] args) { Image img1 = new Proxylmage("photo1.jpg"); Image img2 = new Proxylmage("photo2.jpg"); img1.display(); // charge et affiche img1.display(); // affiche sans recharger img2.display(); // charge et affiche } }
```

# Avantages et inconveniens

# Avantages:

- Contrôle fin sur l'accès à l'objet réel.  
- Permet le lazy loading, le caching, la sécurité, le logging, etc.  
Le client ne vait pas la différence entre le Proxy et l'objet réel. Inconvénients:  
Complexifie légèrement le code.  
- Peut introduire une surcharge si le Proxy ajoute beaucoup de logique.

# Exercise 1

Une entreprise peut protégger l'accès à certaines fonctionnalités selon le role utilisateur (Admin, Guest).

Les composants utilisés :

- Account: interface avec la méthode access().  
RealAccount: implémentation réelle des fonctionnalités.  
- AccountProxy : contrôle si l'utilisateur a les droits pour acceder.

# Questions:

1. Quel est le contrôle du Proxy dans ce scenario?  
2. Quelle est la différence entre RealAccount et AccountProxy?

# Exercise 1

# Conception:

1. Dessinez un diagramme de classes montrant les relations entre Account, RealAccount et AccountProxy.  
2. Expliquez comment vous pouvez ajouter un nouveau role utilisateur (Manager) sans modifier RealAccount.

# Implémentation

1. Implémentez l'interface Account.  
2. Implémentez RealAccount pour afficher "Accès accordé" lors d'un accès.  
3. Implémentez AccountProxy pour vérifier le role de l'utilisateur et refuser l'accès si le contrôle n'est pas autorisé.

# Exercise 1

# Test

Créez des comptes pour Admin et Guest et testez access() pour chaque role.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/72186d3f-4971-4d02-b02c-1d67b0de73b0/a1eabc0dde8c1693f0f77245b6244b723a2f891011595ba97ad1e59068a3552b.jpg)

# Exercice 1

// 1. Interface commune

```typescript
interface Account {
    void access();
}
```

// 2. Objet réel

```txt
class RealAccount implements Account { public void access() { System.out.println("Accès accordé"); } }
```

// 3. Proxy

```java
class AccountProxy implements Account {
    private RealAccount realAccount;
    private String role;
```

```txt
public AccountProxy(String role) { this-role  $=$  role; }
```

```java
public void access() { if (role.equalsIgnoreCase("Admin")) { if (realAccount == null) { realAccount = new RealAccount(); // lazy instantiation } realAccount.access(); } else { System.out.println("Accès refusé pour le role : " + role); } } }
```

# Exercice 1

```txt
// 4. Test   
public class ProxyAccessTest { public static void main(String[] args) { Account adminAccount  $=$  new AccountProxy("Admin"); Account guestAccount  $=$  new AccountProxy("Guest"); adminAccount.access(); // Affiche: Acces accordé guestAccount.access(); // Affiche: Acces refusé pour le role : Guest } }
```

# Pattern Flyweight

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/72186d3f-4971-4d02-b02c-1d67b0de73b0/ae6dd57016ac1e257e228eeabaa3971b32e9a9c58ec2f46461a6409aa8bf88d9.jpg)

# Définition

Le pattern Flyweight est un patron de structure qui permet de partager des objets similaires afin de réduire la consommation mémoire et d'améliorer les performances.  
Il sépare les informations d'un objet en :  
État intrinsèque : commun, partagé entre plusieurs objets (stocké dans le Flyweight).  
$\succ$  État extrinsèque : propre à chaque contexte, non partagé (fourni lors de l'utilisation).

# Différence entre État Intrinsèque et État Extrinsèque

<table><tr><td>Type d&#x27;état</td><td>Définition</td><td>Stockage</td><td>Partage</td><td>Exemple général</td></tr><tr><td>État intrinsèque</td><td>Ensemble des informations internes et invariables de l&#x27;objet, communes à plusieurs instances.</td><td>Dans le Flyweight lui-même.</td><td>partagé entre plusieurs clients.</td><td>Forme, texture, police, type, configuration fixe.</td></tr><tr><td>État extrinsèque</td><td>Informations contextuelles et changeanges dépendant de l&#x27;utilisation de l&#x27;objet.</td><td>Dans le client (ou passé en paramètre).</td><td>propre à chaque usage.</td><td>Position, couleur, état, coordonnées, vitesse.</td></tr></table>

# Exemple de voiture de location

- Imaginons une société de location avec 100 voitures du même modele :

<table><tr><td>Élément</td><td>Type d&#x27;état</td><td>Pourquoi</td></tr><tr><td>Modèle, marque, puissance moteur, couleur du châssis</td><td>Intrinsèque</td><td>Ce sont des caractéristiques communes, identiques pour toutes les voitures de ce modele.</td></tr><tr><td>Plaque d&#x27;immatriculation, kilométrage, conducteur actuel, destination</td><td>Extrinsèque</td><td>Ce sont des informations propres à chaque voiture au moment de l&#x27;utilisation.</td></tr></table>

Le Flyweight correspond à “la fiche technique du modele de voiture”.  
L'etat extrinsèque est géré par le "client" (la location courante).

# Structure UML

Ce diagramme montre les trois actuurs principaux du pattern Flyweight :

FlyweightFactory  $\rightarrow$  fabrique et gère les objets partages (cache).  
Flyweight  $\rightarrow$  représentée l'objet léger contenant l'état intrinsèque.  
□ Context → représenté chaque utilisation spécifique, contenant l'etat extrinsèque.  
Client  $\rightarrow$  demande la création/utilisation d'un objet via la Factory.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/72186d3f-4971-4d02-b02c-1d67b0de73b0/96c9dc80337f47584cf8a47caf19e26e62077a56424abb27480493099e4fbde5.jpg)

Le but est de réduire la duplication en partageant l'état commun entre plusieurs contexts.

# Exemple : Editeur de texte

Dans un éditeur, chaque caractère (A, B, C...) a :

- des informations intrinsèques : forme, police, taille, etc.  
- des informations extrinsèques : position (x, y), couleur locale, etc.

<table><tr><td>Composant du pattern</td><td>Exemple</td></tr><tr><td>Flyweight</td><td>Objet représentant la dette “A” avec la police Arial.</td></tr><tr><td>repeatingState</td><td>“A”, Arial (identique pour toutes leslettres “A” dans le document).</td></tr><tr><td>Context</td><td>Chaque occurrence de “A” à une position donnée (x, y).</td></tr><tr><td>unicouple</td><td>Coordonnées du caractère à l&#x27;écran.</td></tr><tr><td>Client</td><td>Editeur du texte.</td></tr><tr><td>FlyweightFactory</td><td>Gère un cache delettres “A”, “B”, “C”, etc.</td></tr></table>

# Exemple : Editeur de texte

```java
import java.util.\*;   
// Flyweight interface Glyph { void draw(int x, int y);   
}   
// Concrete Flyweight class CharacterFlyweight implements Glyph { private final char symbol; // état intrinsique partagé public CharacterFlyweight(char symbol) { this.symbol = symbol; } public void draw(int x, int y) { // état extrinsque System.out.println("Caractere" + symbol + " à (" + x + ", " + y + ")"); }   
}
```

```java
// Factory   
class GlyphFactory{ private final Map<Character, Glyph> pool  $=$  new HashMap<>(); public Glyph getCharacter(char c){ if (!pool.containsKey(c)){ pool.put(c, new CharacterFlyweight(c)); } return pool.get(c); } // Client   
public class FlyweightDemo { public static void main(String[] args){ GlyphFactory factory  $=$  new GlyphFactory(); String text  $=$  "ABABAC"; int  $\mathbf{x} = 0$  for(char c : text.toArrayArray(){ Glyph g  $=$  factory.getCharacter(c); g.draw(x++,1); } System.out.println("Nombre d'objets créées:" + facto
```

```txt
Caractère A à (0,1)  
Caractère B à (1,1)  
Caractère A à (2,1)  
Caractère B à (3,1)  
Caractère A à (4,1)  
Caractère C à (5,1)  
Nombre d'objects créés : 3
```

# Exercice d'application

# Problématique:

Dans un jeu video ou une simulation 3D, on peut avoir des dizaines de milliers d'arbres.

Créer un objet complet pour chaque arbre (avec son image et sa texture) serait trop lourd en mémoire.

On applique le pattern Flyweight pour partager les données communes à tous les arbres d'une même espèce

# Exercice d'application

# Travail demandé:

Implémentez un système simple où :

$\succ$  Chaque arbre a un type partagé (TreeType) : espèce, couleur, texture.  
$\succ$  Chaque arbre a aussi des caractéristiques uniques : position X/Y, taille.  
> Une fabrique réutilise les TreeType déjà créés pour éviter les doublons.  
Le programme create plusieurs arbres et affiche combien d'objets partages ont ete crees.

# Exercice d'application

# Exemple de résultat attendu:

Affichage arbre [Chêne] couleur=Vert, texture=Texture1 à (10,20), taille=5  
Affichage arbre [Chêne] couleur=Vert, texture=Texture1 à (15,25), taille=6  
Affichage arbre [Pin] couleur=Vert Foncé, texture=Texture2 à (50,60), taille=8  
Affichage arbre [Chêne] couleur=Vert, texture=Texture1 à (70,80), taille=10

Nombre de Type créés : 2
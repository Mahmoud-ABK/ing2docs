# PatternSingleton

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/126c7859-597d-47c3-8222-834eb9b29fc1/ec928e16c2addfc5eb9384db846a37afecdde0af30fc3267963c5ff3c8e2d585.jpg)

# Définition

Le Singleton est un patron de création qui garantit qu'une classe ne possède qu'une seule instance dans tout le système, et fournit un point d'accès global à cette instance.

Singleton = une seule instance + accès global.

Très utile pour les ressources partagées.

# Objectifs

1. Contrôler l'unicité : empêcher la création de plusieurs instances d'une même classe.  
2. Fournir un point d'accès global : rendre l'instance accessible de manière centralisée.  
3. Réduire la consommation mémoire : éviter la duplication inutile d'objets couâteux.  
4. Assurer la cohérence : partager le même état dans tout le système.

# Structure UML

Etapes:  
$\succ$  RendrePrivéle constructeur,  
$\succ$  Construire une instance privée de la classe comme attribut statique de la classe,  
Fournir une méthode publique d'accès à cette instance.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/126c7859-597d-47c3-8222-834eb9b29fc1/5c892a20580cd2c08c8420390a1f6e109ea1d25e5dd629e2f4f168de3f69c084.jpg)

# Implémentation d'un Singleton

```java
public class Singleton {
    // Instance unique (stockée en隱私)
    private static Singleton instance;
    // Constructeur隱私 (empêche new Singleton())
    private Singleton() {}
    // Méthode d'accès global
    public static Singleton getInstance()
        if (instance == null) {
            instance = new Singleton();
        }
    return instance;
}
```

```java
public class Main { public static void main(String[] args) { Singleton s1 = Singleton.getInstance(); Singleton s2 = Singleton.getInstance(); // Vérification : s1 et s2 pointent vers la même instance System.out.println(s1 == s2); // true } }
```

# Cas typiques d'utilisation

- Gestionnaire de configuration (fichier de configuration charge une seule fois).  
- Gestionnaire de connexion à une base de données (une seule connexion partagée).  
- Logger (un seul journal d'événements utilisé dans toute l'application).  
- Gestionnaire de threads ou de cache.

# Exercice

Dans une application de gestion, plusieurs modules (facturation, clients, rapport) doivent acceder à la même base de données.

Pour des raisons de performance et de cohérence, il est interdit d'ouvrir plusieurs connexions. On souhaite donc créé une classe DatabaseConnection qui :

garantit qu'une seule instance de connexion est utilisé dans tout le programme,  
- permet d'ouvrir (connect()) et de fermer (disconnect())
la connexion,  
- affiche des messages pour indiquer l'etat de la connexion.

# Exercice

# Travail demandé

1. Implémentez la classe DatabaseConnection en appliquant le patron Singleton  
2. Ajoutez deux méthodes :

- connect(): affiche un message "Connexion à la base de données..." si aucune connexion n'est ouverte, sinon "Connexion déjà ouverte.«  
- disconnect(): affiche un message "Déconnexion de la base de données..." si une connexion est ouverte, sinon "Aucune connexion active.«

3. Dans une classe Main, testez votre implémentation en :

- récapérant deux objets db1 et db2 via getInstance(),  
verifiant quils pointent vers la meme instance,  
- appellant successivement connect() et disconnect() sur db1 et db2.

# Solution

```java
public class DatabaseConnection { // Instance unique private static DatabaseConnection instance; // Simule l'etat de la connexion private boolean connected; // Constructeur privé private DatabaseConnection() { connected = false; } // Accès global à l'instance public static DatabaseConnection getInstance() { if (instance == null) { instance = new DatabaseConnection(); } return instance; }
```

# Solution

```java
public void connect() { if (!connected) { System.out.println("Connexion à la base de données..."); connected = true; } else { System.out.println("Connexion déjà ouverte."; } }   
public void disconnect() { if (connected) { System.out.println("Déconnexion de la base de données..."); connected = false; } else { System.out.println("Aucune connexion active."; } }
```

# Solution

```txt
public class Main { public static void main(String[] args) { DatabaseConnection db1 = DatabaseConnection.getConnection(); DatabaseConnection db2 = DatabaseConnection.getConnection(); // Vérification System.out.println(db1 == db2); // true // Utilisation db1.connect(); db2.connect(); // même instance => message "déjà ouverte" db1 disconnect(); db2disconnect(); // même instance => message "aucune connexion active" } }
```

# Exercice

# Questions de réflexion:

1. Que se passé-t-il si deux threads différents appelent getInstance() en même temps avant que l'instance ne soit créé?

Si plusieurs threads entrent simultanément dans getInstance() alors que instance == null, il est possible que deux instances différentes de DatabaseConnection(soient créées.

Consequence : cela viole le principe du Singleton (unicité), et peut cause des incohérences (accès concurrents non contrôlés à la base).

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/126c7859-597d-47c3-8222-834eb9b29fc1/f1c7ae6f6747ccb9f453eb4de0c988a91bc0827fd2179cf9298997c5b5802605.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/126c7859-597d-47c3-8222-834eb9b29fc1/ea47621a1fe9b6f81aed23e66bd069ad8389ca6d95f85527d16595bc95d34141.jpg)

# Exercice

Questions de réflexion:

2. Proposez une solution pour rendre votre Singleton thread-safe.

```java
Synchroniser la methode getInstance()   
public static synchronized DatabaseConnection getInstance(){ if (instance  $= =$  null){ instance  $=$  new DatabaseConnection(); } return instance;
```

```java
Initialisation statique  
private static final DatabaseConnection instance = new DatabaseConnection();  
public static DatabaseConnection getInstance() {  
return instance;}
```

# Pattern Builder

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/126c7859-597d-47c3-8222-834eb9b29fc1/8069787a2f1d2b65c8314187c25aa0ee39402423392d581b8b1c76bbd00ed5d8.jpg)

# Définition

Le Builder est un patron de conception de création qui permet de construire des objets complexes étape par étape.

Il sépare la construction d'un objet de sa représentation finale, de sorte qu'un même processus de construction puisse créé différentes représentations.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/126c7859-597d-47c3-8222-834eb9b29fc1/4f1e3b4b70f8a62e045a126c7639d086f06cfc01d7f5781e4e4253231e9f37d7.jpg)

# Objectifs

1. Isoler la construction d'un objet complexe (ex. un objet avec de nombreux paramètres optionnels).  
2. Éviter les constructeurs trop longs (avec trop d'arguments  $\rightarrow$  problème du telescoping constructor).  
3. Améliorer la lisibilité du code (approche fluide/chainée).  
4. Permettre de creator des variantes d'un même objet en réutilisant le même processus de construction.

# Structure UML

1 L'interface du Monteur déclare les étapes communés de la construction du produit entre tous les monteurs.  
2 Les Monteurs Concrets fournissant différentes implementations des étapes de la construction. Ils peuvent creer des produits qui ne reconnent pas l'interface commune.  
3 Les Produits sont les résultats retournés. Les produits construits par les différents monteurs ne sont pas obligés d'appartenir à la même hierarchie de classes ni d'avoir la même interface.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/126c7859-597d-47c3-8222-834eb9b29fc1/69597502108acb9732154bf333a8cfd7003467957b9a545fcd6b4454b5ee2f36.jpg)

4 Le Directeur indique l'ordonnancement des étapes de construction et offre la possibilité de creator et de réutiliser des configurations spécifiques pour les produits.  
Le Client doit associer l'un des monteurs au directeur. En général cette association n'est réalisée qu'une seule fois, grâce aux paramétres du constructeur du directeur. Pour toute construction ultérieure, le directeur utilise l'objet monteur. En guise d'alternative, le client peut passer l'objet monteur à la méthode de production du directeur. Dans ce cas, vous pouvez utiliser un monteur différent chaque fois que vous lancez une production avec le directeur.

# Conception sans Builder

Imaginons qu'on veuille creator un Burger sans Builder.

On utilise un constructeur avec beaucoup de paramètres.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/126c7859-597d-47c3-8222-834eb9b29fc1/6b33dd9b32d9cfe06f9b6fec255d2a14fe2a677e3a5a04bedb68922074ab6b52.jpg)

```java
public class Burger { private String bread; private String meat; private boolean cheese; private boolean salad; private boolean tomato;
```

```java
// Constructeur avec tous les parametes   
public Burger(String bread, String meat, boolean   
cheese,boolean salad,boolean tomato){ this.bread  $=$  bread; this.meat  $\equiv$  meat; this.chese  $\equiv$  cheese; this.salad  $\equiv$  salad; this.tomato  $\equiv$  tomato; } @Override public String toString(){ return "Burger [bread  $= 1$  +bread  $+$  ",meat  $= 1$  +meat  $^+$  ",cheese  $= 1$  +cheese  $+$  ",salad  $= 1$  +salad  $+$  ", tomato  $= 1$  +tomato  $+1$  ]; } }
```

# Conception sans Builder

# Problème

Créons deux burgers.

```java
public class Main { public static void main(String[] args) { Burger burger1  $=$  new Burger("Pain complet,"Poulet",true, true,false); Burger burger2  $=$  new Burger("Pain brioché","Boeuf",false, true, true); System.out.println(burger1); System.out.println(burger2); }
```

# Inconvénients

1. Lisibilité faible: Quand on lit new Burger("Pain complet", "Poulet", true, true, false), on ne sait pas directement à quoi correspondent les true et false.  
2. Risque d'erreurs: Si on se trompe dans l'ordre des paramètres, la compilation ne détectera rien (ex. inverser salad et tomato).  
3. Scalabilité limitée: Si on ajoute un nouvel ingrédient (ex. sauce), il faut modifier le constructeur et donc casser du code existant.

# Conception avec Builder

Ancien code :

new Burger("Pain complet", "Poulet", true, true, false);

Nouveau code : Solution avec builder

new Burger.Builder() .bread("Pain complet") .meat("Poulet") .cheese(true) .salad(true) .tomato(false) .build();

C'est beaucoup plus lisible, flexible et sür.

# Conception avec Builder

# Code complet:

```java
public class Burger { private String bread; private String meat; private boolean cheese; private boolean salad; private boolean tomato;
```

```javascript
// Constructeur privé : seul le Builder peut créé un Burger   
private Burger(Builder builder) { this.bread  $=$  builder.bread; this.meat  $\equiv$  builder.meat; this.chese  $\equiv$  builder.chese; this.salad  $\equiv$  builder.salad; this.tomato  $\equiv$  builder.tomato;   
}   
@override   
public String toString() { return "Burger [bread  $= "$  +bread  $+$  ",meat  $= "$  +meat  $^+$  ",cheese  $= "$  +cheese  $+$  ",salad  $= "$  +salad  $+$  ",tomato  $= "$  +tomato  $+$  ],
```

// Classe interne statique : le Builder

```java
public static class Builder { private String bread; private String meat; private boolean cheese; private boolean salad; private boolean tomato;
```

```java
public Builder bread(String bread) { this.bread  $=$  bread; return this;   
}
```

```java
public Builder meat(String meat) { this.meat  $\equiv$  meat; return this;
```

```javascript
public Builder cheese(boolean cheese) { this.chese  $=$  cheese; return this;
```

```javascript
public Builder salad(boolean salad){ this.salad  $=$  salad; return this; public Builder tomato(boolean tomato){ this.tomato  $=$  tomato; return this; // Methode de construction finale public Burger build() { return new Burger(this); }
```

# Conception avec Builder

Test Builder:

```java
public class Main { public static void main(String[] args) { // Creation fluide et lisible Burger burger1 = new Burger.Builder() .bread("Pain complet") .meat("Poulet") .cheese(true) .salad(true) .tomato(false) .build();
```

```txt
Burger burger2 = new Burger.Builder()
.bread("Pain brioché")
.meat("Boeuf")
.chese(false)
salad(true)
.tomato(true)
.build();
```

```txt
System.out.println(burger1); System.out.println(burger2); }
```

# Application de Builder avec Director

- Builder (interface/abstraite) : définit les étapes de construction.  
ConcreteBuilder : implémente les étapes et construit le produit final.  
- Product: l'objet complexe à construire.  
Director : orchestre l'ordre de construction en appelant les méthodes du Builder.  
- Client : demande la construction au Director et récapère le produit.

# Exercice 1 : Application de Builder avec Director

# Enoncé:

Vous devez modéliser un système de commande de pizzas personnalisées. Une Pizza doit être composée de certains éléments obligatoires et d'autres optionnels. Chaque client doit pouvoir creer facilement une pizza enCHOISSSANT ses ingrédients.

Une Pizza peut contenir les éléments suivants :

Pâté (dough) → obligatoire  
- Sauce  $\rightarrow$  obligatoire  
Fromage (cheese)  $\rightarrow$  optionne  
Garniture (topping)  $\rightarrow$  optionnel

# Exercice 1 : Application de Builder avec Director

# Travail demandé :

Ecrire un programme qui permet de construire trois builders correspondants aux trois types de pizzas suivants:

- Margherita : pâté fine, sauce tomate, fromage mozzarella.  
- Pepperoni : pâté épaisse, sauce tomate, fromage cheddar, garniture pepperoni.  
Végétarienne : pâté complète, sauce pesto, fromage de chèvre, garniture légumes.

```java
public class Pizza { private String dough; private String sauce; private String cheese; private String topping;
```

```java
public void setDough(String dough) { this.dough = dough; }  
public void setSauce(String sauce) { this.sauce = sauce; }  
public void setCheese(Stringcheese) { this.chesese = cheese; }  
public void setTopping(Stringtopping) { this.topping = topping; }
```

```java
@override   
public String toString() { return "Pizza:\n" + "Dough: " + dough + "\\n" + "Sauce:" + sauce + "\\n" + "Cheese:" + (cheese != null ? cheese : "None") + "\\n" + "Topping:" + (topping != null ? topping : "None"); } }
```

```java
public interface PizzaBuilder {  
    void buildDough();  
    void buildSauce();  
    void buildCheese();  
    void buildTopping();  
    Pizza getPizza();  
}
```

```java
// Margherita Builder
public class MargheritaBuilder implements PizzaBuilder {
    private Pizza pizza = new Pizza();
    public void buildDough() { pizza.setDough("Thin Crust"); }
    public void buildSauce() { pizza.setSauce("Tomato"); }
    public void buildCheese() { pizza.setCheese("Mozzarella"); }
    public void buildTopping() { /* pas de topping */ }
    public Pizza getPizza() { return pizza; }
} // Pepperoni Builder
public class PepperoniBuilder implements PizzaBuilder
    private Pizza pizza = new Pizza();
    public void buildDough() { pizza.setDough("Thin Crust"); }
    public void buildSauce() { pizza.setSauce("Tomato"); }
    public void buildCheese() { pizza.setCheese("Cerrihye"); }
    public void buildTopping() { pizza.setTopping("Pasta"); }
    public Pizza getPizza() {
        // processus de creation
        this.buildDough(); this.buildSauce(); this.buildChees;
        this.buildTopping();
        return pizza; }
```

```java
public class PizzaDirector { private PizzaBuilder builder; public PizzaDirector(PizzaBuilder builder) { this.builder  $=$  builder; } /\* on peut defineir ce processus de creation dans la classe Builder\*/ /\* Methode optionnelle \*/ public void constructPizza() { builder.buildDough(); builder.buildSauce(); builder.buildCheese(); builder.buildTopping(); } public Pizza getPizza(){ return builder.getPizza(); }
```

```java
public class Main { public static void main(String[] args) { // Pizza Margherita PizzaBuilder margheritaBuilder  $\equiv$  new MargheritaBuilder(); PizzaDirector director1  $=$  new PizzaDirector(margheritaBuilder); director1constructedPizza(); Pizza margherita  $\equiv$  director1.getPizza(); // Pizza Pepperoni PizzaBuilder pepperoniBuilder  $\equiv$  new PepperoniBuilder(); PizzaDirector director2  $\equiv$  new PizzaDirector(pepperoniBuilder); director2 ConstructsPizza(); Pizza pepperoni  $\equiv$  director2.getPizza(); // Affichage System.out.println("=== Margherita==="); System.out.println(margherita); System.out.println("\n=== Pepperoni==="); System.out.println(pepperoni); } }
```

# Exercice 2 : Application de Builders sans Director

Vous devez modéliser un système qui permet de configurer un ordinateur sur mesure (PC).

Un ordinateur peutContainir plusieurs éléments :

- Proesseur (obligatoire)  
- Mémoire RAM (obligatoire)  
Disque dur (optionnel)  
- Carte graphique (optionnel)  
- Carte mère (obligatoire)  
- Alimentation (optionnel)

# Exercice 2 : Application de Builders sans Director

# Travail demandé:

1. Créez une classe Computer avec les attributs ci-dessus.

- Les champs doivent être privés.  
- Le constructeur de Computer doit être privé, afin de force l'utilisation du Builder.

2. Ajoutez une classe interne statique Builder qui contient:

- Des attributs identiques à ceux de Computer.  
- Des méthodes chainées (processor(String p), ram(int r), disk(String d), etc.) pour initialiser les champs.  
- Une méthode build() qui returne l'objet final Computer.

# Exercice 2 : Application de Builders sans Director

# Travail demandé:

3. Dans une classe Main, créez deux configurations d'ordinateurs:

- Un PC Gamer (proCESseur puissant, 16 Go RAM, carte graphique, disque SSD).  
- Un PC Bureau (proceseur moyen, 8 Go RAM, sans carte graphique, disque dur classique).
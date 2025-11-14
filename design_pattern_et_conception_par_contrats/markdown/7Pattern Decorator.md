# Pattern Decorator

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/1a91a8cd-065c-494c-a93b-4f17b6bf7962/8c09d003c6fa470afb9f9795dd97bd98ecf0f077ab5c10fb706181d37669ffc2.jpg)

# Définition

# Le décorateur:

- est un patron structurel qui permet d'ajouter dynamiquement des fonctionnalités à un objet sans modifier sa classe.  
Il consiste à “enveloppper” un objet dans une autre classe (appelée décorateur) qui implémente la même interface (meme comportement).

# Structure UML

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/1a91a8cd-065c-494c-a93b-4f17b6bf7962/d25acaa082c5819baeeceb732756cc7437795d79110f7c61eb5f456e67286c58.jpg)

Le Compositant déclaré l'interface commune pour les décorateurs et les objets décorés

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/1a91a8cd-065c-494c-a93b-4f17b6bf7962/cab6f2e9e44e22b72a1d57488f20255957f36627f4f93524f4ce29b35bc6e42b.jpg)

Le Compositant Concret est une classe contenant des objets qui sont étremballes. Il définit le comportement par défaut qui peut être modifié par les décorateurs.

Les Décorateurs Concrets définissent des comportements supplémentaires qui peuvent être ajoutes dynamiquement aux composants. Les décorateurs concrets redéfinissent les méthodes du decorator de base et exécutent leur traitement avant ou après l'expérience à la méthode du parent.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/1a91a8cd-065c-494c-a93b-4f17b6bf7962/b4ad067e2075b942b3847bc4018d20b6f8217429a45365e7f045749ec7d35274.jpg)

Le Client peut emballer les composants dans plusieurs couches de décorateurs, tant qu'il manipule les objets à laide de l'interface du composant.

Le Décorateur de Base possède un attribut pour référencer un objet emballe L'attribut doit être déclaré avec le type de l'interface du composant afin deContaining à la fois les composants concrets et les décorateurs. Le décorateur de base délégue toutes les opérations à object émballe

remplacer l'héritage par l'agrégation ou la composition.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/1a91a8cd-065c-494c-a93b-4f17b6bf7962/c0b20731836f8e35d03f8fb5aa736213a08b9cc83da5f476fbb42066b8377a64.jpg)

# Exemple d'implémentation du pattern décorator: gestion d'un Coffee Shop

Imaginons un système de gestion d'un Coffee Shop. Chaque boisson (café simple, cappuccino, etc.) possède un coût et une description.

Au départ, nous avons une seule boisson :

- Un café simple à 2€.

Mais, réellement, un client peut pouvoir ajouter :

du lait,  
du sucre,  
du chocolat, ou  
- même plusieurs combinaisons (ex. café + lait + sucre).

# Exemple d'implémentation du pattern décorator: gestion d'un Coffee Shop

Avec l'héritage classique, nous aurions besoin de définir plusieurs classes comme :

- CaféAvecLait  
- CaféAvecSucre  
- CaféAvecLaitEtSucre  
- CaféAvecChocolatEtLait  
Etc  
$= >$  Explosion de classes, code rigide et difficile à maintainir.

# Exemple d'implémentation du pattern décorator: gestion d'un Coffee Shop

# Objectifs :

Le patron Décorateur permet de :

- Ajouter dynamiquement des options (lait, sucre, chocolat...) à une boisson existante.  
- Éviter la multiplication des sous-classes.  
- Combiner librement les options à l'exécution.  
- Respecter le principe Ouvert/Fermé (OCP) :on étend le comportement sans modifier les classes existantes.

# Exemple d'implémentation du pattern décorator: gestion d'un Coffee Shop

# Principe du decorator:

Chaque option de coffe est un décorateur (lait, sucre, chocolat...) qui :

- implémente la même interface Beverage que la boisson de base.  
enveloppe un objet de type Beverage

Exemple: si on désirecréer un : “Café simple, avec lait, avec sucre”

On aura: Beverage deluxe = new SugarDecorator(new MilkDecorator(new SimpleCoffee()));

# Structure UML

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/1a91a8cd-065c-494c-a93b-4f17b6bf7962/db635bac891a4b943c42d241e5889d21eff851184618c810c034c644cca78a15.jpg)

```java
public class SimpleCoffee implements Beverage { @Override public String getDescription() { return "Café simple"; } @Override public double cost(){ return 2.0; } }
```

```txt
public abstract class BeverageDecorator implements Beverage { protected Beverage beverage; public BeverageDecorator(Beverage beverage) { this.beverage = beverage; } }
```

```java
public class MilkDecorator extends BeverageDecorator { public MilkDecorator(Beverage beverage) { super(beverage); } @Override public String getNameDescription() { return beverage.getName() + ", lait"; } @Override public double cost(){ return beverage.cost() + 0.5; } }
```

```java
public class SugarDecorator extends BeverageDecorator {
    public SugarDecorator(Beverage beverage) {
        super(beverage);
    }
}
```

```java
public class Main { public static void main(String[] args) { Beverage coffee  $=$  new SimpleCoffee(); System.out.println(coffee_Description() + " = " + coffee.cost(  $\vDash$  "€")); Beverage milkCoffee  $=$  new MilkDecorator(coffee); System.out.println(milkCoffee_Description(  $\vDash$  " = " + milkCoffee.cost(  $\vDash$  "€")); Beverage deluxe  $=$  new SugarDecorator(new MilkDecorator(new SimpleCoffee())); System.out.println(deluxe_Description(  $\vDash$  " = " + deluxe.cost(  $\vDash$  "€")); } }
```
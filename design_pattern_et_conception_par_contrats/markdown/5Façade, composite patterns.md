# Cours

# Design Patterns et conception par contrats ING 2 - Génie Logiciel

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/f786fc0d-96e5-4163-83b5-bfdfba1135dc/5c1d7c2bace2116325601921907bb1a63100ba94413ff9d2c078eb77d56d7df9.jpg)

# 03

# Patterns de Structure

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/f786fc0d-96e5-4163-83b5-bfdfba1135dc/a34c28c339227d641a22c42acb993048875fa9bb55c5990079ba0936087a73aa.jpg)

# Objectifs des patterns de structure

- Les patterns de structure ont pour objectif de composer des classes et des objets pour former des structures plus grandes, tout en gardant ces structures flexibles et extensibles.  
Ils se concentrent sur la maniere dont les objets sont reliés entre euxs(composition,héritage,agrégation,délégation, etc.)plutôtque sur leur comportement interne.

# Objectifs des patterns de structure

Réutiliser le code existant sans le modifier (principe Open/Closed).  
- Simplifier les relations entre objets (réduire la complexité des dépendances).  
- Permettre des extensions futures sans casser le code existant.  
- Encapsulator les variations structurelles (par exemple, remplaçer une bibliothèque ou un composant sans tout réécrite).  
□ Faciliter la maintenance grâce à une architecture claire et découlée.

# Pattern Façade

# Définition

- Façade est un patron de conception structurel qui procure une interface offrant un accès simplifié à une librarianie, un framework ou à n'importe quel ensemble complexe de classes.  
- Le patron façade masque la complexité du système et fournit une interface au client à l'aide de laquelle il peut acceder au système.  
- Une façon ne se limite pas à simplifier une interface : elle découple le client d'un sous-système de composants (principe de faible couplage).

# Principe

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/f786fc0d-96e5-4163-83b5-bfdfba1135dc/4c0d6a737e286b2bd1c5dcc9b54dfd90470c0224923c04d02f55dbe02f21fe71.jpg)

# Structure UML

La Façade procure un accès pratique aux différentes parties des fonctionnalités du sous-systeme. Elle sait où diriger les requêtes du client et comment utiliser les différentes parties mobiles.

2 Une classe Façade Supplémentaire peut être créé pour éviter de polluer une autre façade avec des fonctionnalités qui pouraient la rendre trop complexe. Les façades supplémentaires peuvent être utilisées à la fois par le client et par les autres façades.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/f786fc0d-96e5-4163-83b5-bfdfba1135dc/5c3c1d358cb4d9b7ffaf114c841de772743f1fa1a06eb96fde150e93985c2f64.jpg)

Le Sous-système Complexe est composé de dizaines d'objets variés. Pour leur donner une réelle'utilité, vous doivent plonger au cœur des détails de l'implementation du sous-système, comme initiailler les objets dans le bon ordre et leur fournir les données dans le bon format.

Les classes du sous-systeme ne sont pas conscientes de l'existence de la façon. Elles opèrent et interagissent directement à l'intérieur de leur propre système.

# Cas d'utilisation typiques

- Interface simplifiée pour une bibliothèque complexe (ex. JavaFX, JDBC).  
- Point d'entrée unique pour un module applicatif.  
- API d'un framework ou SDK.  
- Couche intermédiaire entre le frontend et le backend (par ex., dans une architecture MVC).

# Exemple d'implémentation: Façade dans un système bancaire

Un client souhaite effectuer un virement bancaire. Mais en réalité, plusieurs sous-systèmes doivent coopérer :

Vérification du compte  
Vérification du solde  
- Système de transfert  
- Notification au client

Sans faucade, le client devrait interagir avec toutes ces classes.

Solution: Créer la Façade BankService avec une seule méthode transfer() qui invoque tous les sous-systèmes.

# Architecture du système

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/f786fc0d-96e5-4163-83b5-bfdfba1135dc/07c3313ef24c302fdd530f67a61efd23caf616329ce8d08157a4d2088e5425a7.jpg)

# Implémentation des sous-systèmes

```java
class AccountVerification {
    public boolean verifyAccount(String accountNumber) {
        System.out.println("Vérification du compte: " + accountNumber);
        return true;
    }
}
```

# Implémentation des sous-systèmes

```groovy
class TransferSystem { public void makeTransfer(String from, String to, double amount) { System.out.println("Transfert de " + amount + "€ de " + from + " vers " + to); } }   
class NotificationService { public void sendNotification(String accountNumber, String message) { System.out.println("Notification envoye à " + accountNumber + ": " + message); } }
```

# Implémentation de la façade

class BankService {  
```txt
// Récérances aux sous-systèmes
private AccountVerification verifier = new AccountVerification();
private BalanceChecker balanceChecker = new BalanceChecker();
private TransferSystem transferSystem = new TransferSystem();
private NotificationService notifier = new NotificationService();
```

// Implémentation de la méthode transfer() qui encapsule l'essay aux sous-systèmes  
```java
public void transfer(String from, String to, double amount) { // Appel aux sous-systèmes if (verifyAccount(from) && verifier.confirmAccount(to)) { if (balanceChecker.hasSufficientBalance(from, amount)) { transferSystem.makeTransfer(from, to, amount); notifier.sendNotification(from, "Vous avez transféré" + amount + "€ à" + to); notifier.sendNotification(to, "Vous avez reçu" + amount + "€ de" + from); } else { System.out.println("Solde insufficient!");
} else {
System.out.println("Compte invalide!");
} }
}
```

# Implémentation de la façade

class BankService {  
```txt
// Récérances aux sous-systèmes
private AccountVerification verifier = new AccountVerification();
private BalanceChecker balanceChecker = new BalanceChecker();
private TransferSystem transferSystem = new TransferSystem();
private NotificationService notifier = new NotificationService();
```

// Implémentation de la méthode transfer() qui encapsule l'essay aux sous-systèmes  
```java
public void transfer(String from, String to, double amount) { // Appel aux sous-systèmes if (verifyAccount(from) && verifier.confirmAccount(to)) { if (balanceChecker.hasSufficientBalance(from, amount)) { transferSystem.makeTransfer(from, to, amount); notifier.sendNotification(from, "Vous avez transféré" + amount + "€ à" + to); notifier.sendNotification(to, "Vous avez reçu" + amount + "€ de" + from); } else { System.out.println("Solde insufficient!");
} else {
System.out.println("Compte invalide!");
} }
}
```

# Avantages et inconvenients

# Avantages

- Simplifie l'utilisation du système.  
- Cache la complexité technique.  
- Réduit le couplage entre client et sous-systèmes.  
- Facilité la maintenance et l'évolution.

# Inconvénients

- Peut devenir une façon "trop grossse" si elle regroupe trop de responsabilités.  
- Masque parfois les fonctionnalités avancées disponibles dans les sous-systèmes.

# Exercice d'application

# Problème :

Une entreprise développée une application de maison intelligente (SmartHome). Elle possède déjà plusieurs sous-systèmes indépendants :

- LightSystem: contrôle des lumières,  
- HeatingSystem : contrôle du chauffage,  
SecuritySystem : alarme et caméras,  
MusicSystem: lecture musicale.

Les utilisateurs trouvent le système trop compliqué, car ils doivent appeler plusieurs classes pour exécuter une seule action.

# Exercice d'application

# Questions

Implémenter la façon SmartHomeFacade avec les méthodes suivantes:

$\succ$  leaveHome()  $\rightarrow$  prépare la maison quand on sort.  
$\succ$  arriveHome()  $\rightarrow$  prépare la maison quand on rentre.  
$\succ$  nightMode()  $\rightarrow$  active le mode nuit.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/f786fc0d-96e5-4163-83b5-bfdfba1135dc/49213955e40c14ede5d7e85a212f1ff1b655bdef711ed0bf18c8d1405242754e.jpg)

# Implémentation des sous-systèmes:

```groovy
class LightSystem {
    public void on() { System.out.println("Lumières allumées"); }
    public void off() { System.out.println("Lumières éteintes"); }
}  
class HeatingSystem {
    public void on() { System.out.println("Chauffage activé"); }
    public void off() { System.out.println("Chauffage éteint"); }
}  
class SecuritySystem {
    public void arm() { System.out.println("Système de sécurité activé"); }
    public void disarm() { System.out.println("Système de sécurité désactivé"); }
}  
class MusicSystem {
    public void play() { System.out.println("Musique lancée"); }
    public void stop() { System.out.println("Musique arrêtée"); }
}
```

# Programme Client :

```java
public class Main { public static void main(String[] args) { SmartHomeFacade home  $=$  new SmartHomeFacade(); home.arriveHome(); home.nightMode(); home离去Home(); }
```

# Pattern Composite

# Objectif

- Permettre de composer des objets en structures hierarchiques (arborescentes) et de Traits uniformément les objets simples et les objets composés.

# Example :

- Un dossier contient des fichiers ou d'autres dossiers. On peut pouvoir afficher, supprimer ou déplacer un dossier exactement comme un fichier, sans se soucie s'il contient d'autres éléments.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/f786fc0d-96e5-4163-83b5-bfdfba1135dc/5d03112e0b42f3ce00f7499c53fabf46e6e7ccac65ccdaab8528d9e0d4b1a156.jpg)

Le pattern Composite rend cela possible entraitant objets simples et composites de façon uniforme.

# Structure UML

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/f786fc0d-96e5-4163-83b5-bfdfba1135dc/59d68ed9f1159c9cfa1d9fc8f27f9def5e16d0f4055725688b4799a4049fcd27.jpg)

<table><tr><td>Élément</td><td>Rôle</td></tr><tr><td>Component</td><td>Interface commune (déclare les opérations communes)</td></tr><tr><td>Leaf</td><td>Élément de base (objet simple, sans enfants)</td></tr><tr><td>Composite</td><td>Objet composé (contient d&#x27;autres Components)</td></tr><tr><td>Client</td><td>Utilise les objets via l&#x27;interface Component, sans savoir s&#x27;il s&#x27;agit d&#x27;un Leaf ou d&#x27;un Composite</td></tr></table>

# Exemple d'implémentation: Système de fichiers

On modélise des dossiers et des fichiers :

Un fichier est une Leaf.  
- Un dossier est un Composite (il contient d'autres fichiers ou dossiers). Le client manipule les deux avec la même méthode showDetails().

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/f786fc0d-96e5-4163-83b5-bfdfba1135dc/89a27fc9ae1f1ff15389a3019a0ca0ca717bd38981b16fc1c153adf94437b7c2.jpg)

```java
import java.util.ArrayList;   
import java.util.List;   
interface FilesystemComponent{ void showDetails();   
}   
class FileItem implements FilesystemComponer private String name; public FileItem(String name) { this.name  $=$  name; } @Override public void showDetails() { System.out.println("Fichier:" +name); 1
```

```java
class Directory implementsFileSystemComponent {
    private String name;
    private List<FileSystemComponent> children = new ArrayList<>();
    public Directory(String name) {
        this.name = name;
    }
    public void add(FileSystemComponent component) {
        children.add(component);
    }
    public void remove(FileSystemComponent component) {
        children.remove(component);
    }
}
```

# Avantages et inconvenients

# Avantages

- Simplifie le code client (traitement uniforme).  
- Permet de creator des structures hiéarchiques dynamiques.  
- Facilité l'ajout de nouveaux types d'éléments (principipe Open/Closed).

# Inconvénients

- PeutAMD le système trop général (le client peut manipuler un fichier comme un dossier sans distinction).

# Exercice d'application

On veut modéliser un menu hierarchique pour un restaurant.  
Chaque éléments de menu doit pouvoir être :

soit un Plat (élément simple : nom + prix),

soit un Menu ( éléments composé contenant d'autres plats ou sous-menus).

Travail demandé :

1. Créez une interface MenuComponent avec une méthode showDetails().

# Exercice d'application

2. Créez deux classes :

- Dish (Feuille)  
- Menu (Composite)

Un objet Menu doit pouvoir :

- ajouter un élément (add( MenuComponent item))  
- supprimer un élément (remove( MenuComponent item))  
- afficher tout son contenu récursivement.

# Exercice d'application

3. Dans la classe principale, créez la hierarchie suivante :

Menu principal : "Menu Restaurant"

> Menu "Entrées"  
Plat : "Soupe du jour" - 5.5€  
Plat : "Salade verte" - 4.0€  
> Menu "Plats principales"  
Plat : "Steak frites" - 12.0€  
Plat : "Pâtes carbonara" - 10.0€  
> Menu "Desserts"  
Plat : "Assiette fruits de saison" - 6.0€
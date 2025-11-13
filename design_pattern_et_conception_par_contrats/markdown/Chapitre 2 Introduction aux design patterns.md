# Cours

# Design Patterns et conception par contrats ING 2 - Génie Logiciel

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/164f522c-9c98-4877-a766-7a19f6ed2d97/5c1d7c2bace2116325601921907bb1a63100ba94413ff9d2c078eb77d56d7df9.jpg)

# 02

# Introduction aux Design Patterns

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/164f522c-9c98-4877-a766-7a19f6ed2d97/cfef24f2ece78dc9444d088a20121cb6e0b832366972adb9aa4a2c4e41a870b9.jpg)

# Objectifs de ce chapitre

Comprétre les défis du développement logiciel  
□ Identifier les problèmes liés à la maintenance, l'évolution et la réutilisabilité du code.  
- Expliquer pourquoi une bonne conception est essentielle en génie logiciel.  
Définir ce qu'est un Design Pattern  
- Classer les Design Patterns selon la classification GoF (Gang of Four)

# Enjeu du Génie Logiciel

□ Produire des conceptions extensibles, maintainables et réutilisables

Il ne faut pas chercher à résoudre un problème en partant de ses mécanismes de base, mais il vaut mieux réutiliser des solutions qui ont déjà fait leurs préuves.

Il faut s'aider du savoir-faire des concepteurs OO   
expérimentés

# Design Pattern-Définition

Un Design Pattern est :

« Une solution réutilisable, éprouvée et documentée à un problème de conception qui se pose fréquement dans le développement logiciel. »

# Design Pattern-Caractéristiques

Réutilisable : peut être appliqué dans différents projets.  
- Abstract: ce n'est pas du code prét à l'emploi, mais un modele de solution.  
- Commun : fournit un vocabulaire partagé entre développpeurs et architectes.  
- Documenté : décrit de manière standardisée (nom, problème, solution, conséquences).

« Les patrons de conception vous aient à apprendre des succès des autres只不过 que de vos propres échecs. »

Mark Johnson

# Historique des Design Patterns

1977 – Christopher Alexander (architecture)

Architecte en bâtiment.

Public “A Pattern Language”.

Introduit l'idée des patterns : solutions réutilisables à des problèmes récurrents d'urbanisme et d'architecture.

Années 1980 - Début en génie logiciel

Leschercheurs en génie logiciel reconnent l'idée d'Alexander.

Utilisation de patterns pour décrire des solutions conception logicielle réutilisables.

# Historique des Design Patterns

1994 - GoF (Gang of Four):

Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides.

Publient "Design Patterns: Elements of Reusable Object-Oriented Software".

Définissant 23 Design Patterns classés en 3

catégories: Créationnels, Structurels et

Comportementaux

Ce livre devient la référence mondiale.

# Design Patterns

Elements of Reusable Object-Oriented Software

Erich Gamma  
Richard Helm  
Ralph Johnson  
John Vlissides

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/164f522c-9c98-4877-a766-7a19f6ed2d97/72c8409c2a8ff42bc2cbf6f01bc032547f8fc4c1c63767b31685ff1a949a1d78.jpg)  
Cort et al. 1976;Escher /Gordon-Ar -Barnard, Halland, All genus names Foreword by Brady Booch

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/164f522c-9c98-4877-a766-7a19f6ed2d97/9809b01ce83a1e453ce72d7c48489f6b470fdfaccf67e502e396f4e5dd61ea40.jpg)

# Historique des Design Patterns

# Depuis 2000 - Adoption massive des DP

Intégrés dans les frameworks Java, C#, C++.

Essentiels pour les architectes logiciels et développpeurs avancés.

De nouveaux patterns apparaiscent (ex. : Dependency Injection, MVC, Microservices).

# Structure d'un Design Pattern (GOF)

- Nom du pattern:

Unique, évocateur, facilité la communication entre développeurs.

Example : Observer, Strategy, Decorator

Problème:

Contexte dans lequel le pattern est utile.

Le type de difficulté de conception rencontre.

Exemple (Observer) : Comment notifies plusieurs objets lorsqu'un objet change d'etat, sans les coupler fortement.

# Structure d'un Design Pattern (GOF)

# Solution:

Description abstraite de la structure de classes/objects et de leurs collaborations.

Pas une implémentation unique  $\rightarrow$  un schéma générique.

Consequences (avantages / inconveniens):

Points forts : flexibilité, découvert, extensibilité.

Points faibles : complexité accrue, surcoût potentiel.

□ Implémentation:

Extrait de code (Java, Python, C++...).

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/164f522c-9c98-4877-a766-7a19f6ed2d97/7dad3c87510a64fbc0e19e7e21de0f3826115602ab4795da691dddc0d355c6a3.jpg)

# Avantages

□ Faciliter la communication entre les différents développpeurs.  
Réduire le couplage (interactions) entre les différentes classes(modules, composants) d'une application.  
Réduire le temps de développement d'une application.  
□ Faciliter la maintenance d'une application.

# Inconvénients

Difficulté à identifier quand un pattern s'applique.  
Nécessite un apprentice et de l'expérience.  
- Les patterns sont nombreux (23 patterns qui font l'unanimité, répertoriés dans un ouvrage de ↔reference (GoF)).  
La corrélation des patterns i.e Les patterns peuvent dépendre d'autres patterns.

# Classification des Design Patterns

- Les patrons de conception sont classés en trois catégories (GoF).  
1. Patterns de Creation (5)  
S'intéressent à la construction des objets : Comment organiser et déléguer la création dynamique d'instances ?  
Patterns FactoryMethod, AbstractFactory, Builder, Singleton

# Classification des Design Patterns

# 2. Patterns de Structure (7)

- Permettent d'organiser les classes d'une application : Comment composer classes et objets pour obtenir des structures plus complexes ?  
Travaillent essentiellement sur des aspects statiques, à «l'extérieur»des classes  
Bridge, Adapter et Composite (etc.)

# Classification des Design Patterns

# 3. Patterns de Comportement (11)

□ Expliquent comment organiser les objets pour qu'ils collaborent entre eux:Comment faire collaborer classes ou objets pour construire une partie de l'application et destraitements?  
Travaillent essentiellement sur des aspects dynamiques, à «l'intérieur»des classes et parfois au niveaux des instances  
Strategy, Decorator, Observer, Visitor (etc.)

# Principes communs aux patrons

4principles:

Principe 1. Réduire l'accessibilité des membres de classe  
Principe 2. Encapsuler ce qui varie  
Principe 3. Programmer pour une interface et non pour une implémentation  
Principe 4. Privilégier la composition à l'héritage

# Principe 1. Réduire l'accessibilité des membres de classe

L'accès direct aux donnéesés membres d'une classe devrait être limité à la classe elle-même  
Éviter d'exposer les détails d'implémentation pour facilitier l'évolution future sans aucune conséquence sur la classe

# Principe 1. Réduire l'accessibilité des membres de classe

# Solution : encapsulation

Faire des attributs privés  
Réduire l'utilisation des accessesurs ( getters) et mutateursurs (setters): Leur utilisation suggère que l'objet est un fournisseur de données, alors qu'il faut considérer l'objet comme un fournisseur de services

# Principe 2. Encapsulator ce qui varie

# Principe:

Isoler ce qui change de ce qui reste stable.

# Example:

interface PaymentStrategy {void pay(int amount);} class CreditCardPayment implements PaymentStrategy {...} class PayPalPayment implements PaymentStrategy {...}

```txt
class ShoppingCart{ privatePaymentStrategypayment; publicvoidsetPayment(PaymentStrategyp) { payment  $=$  p;} publicvoidcheckout() {payment/pay(total);}
```

l'algorithm de paiement peut changer sans modifier ShoppingCart.

# Règle 3. Programme pour une interface et non pour une implémentation

# Principe:

Dépendre d'abstractions, pas de classes concrètes

# Example (Pattern Observer):

```txt
interface Observer{void update();}   
class ConcreteObserver implements Observer{...}   
class Subject{ private List<Observer> observers; void notifyObservers() {for(Observero:observers) o.update();}
```

Le Subject ne connait pas les classes concretes, seulement l'interface Observer

# Règle 4. Privilégier la composition à l'héritage

# Principe:

Les objets collaborent只不过 que créé une hierarchie complexe.

L'héritage cree une relation "est-un" (is-a) : rigide et difficile à changer.

La composition creée une relation “a-un” (has-a) : flexible remplaçable et extensible

# Règle 4. Privilégier la composition à l'héritage

# Mauvais exemple (héritage): Problèmes:

```groovy
class EmailNotifier {
    void sendEmail(String msg) {
        System.out.println("Email: " + msg); }
}
```

```groovy
class SMSNotifier extends EmailNotifier {
    void sendSMS(String msg) { System.out.println("SMS: " + msg); }
}
```

Problèmes :

SMSNotifier n'est pas un EmailNotifier, la hierarchie est artificielle.

Ajouter PushNotifier ou combiner plusieurs méthodes devient compliqué.

# Règle 4. Privilégier la composition à l'héritage

# Bon example (Composition)

interface Notifier {

void send(String msg);

}

class EmailNotifier implements Notifier {

public void send(String msg) {

System.out.println("Email: "+msg);

}

class SMSNotifier implements Notifier {

public void send(String msg) {

System.out.println("SMS: " + msg); }

}

class NotificationService implements Notifier{

private List< Notifier> notifiers = new ArrayList<>();

public void addNotifier(Notifier n) { notifiers.add(n); }

public void send(String msg) {

for (Notifier n : notifiers) n.send(msg);

// Utilisation

NotificationService service = new NotificationService();

service.addNotifier(new EmailNotifier());

service.addNotifier(new SMSNotifier());

service.send("Hello world!");

# Example pratique

# Système de gestion de commandes

□ Contexte: L'application doit:gérer différents types de commandes : Commandes en ligne, Commandes en magasin.  
- Les commandes peuvent être payées par différentes méthodes : carte, PayPal, crypto.  
Le système doit pouvoir notificationier le client par email, SMS ou push.

# Example pratique

# Encapsulation des variations

On isole le comportement variable (methode de paiement)

interface PaymentStrategy {void pay(double amount);} class CreditCardPayment implements PaymentStrategy {...} class PayPalPayment implements PaymentStrategy {...}

Avantage : ajouter un nouveau mode de paiement ne modifie pas le reste du code.

# Example pratique

# Programmer pour une interface

Les notifications passent par une interface abstraite :

interface Notifier {void send(String msg);} class EmailNotifier implements Notifier{class SMSNotifier implements Notifier{

Le code qui envoie les notifications dépend de Notifier, pas des classes concretes.

# Example pratique

# Programmer pour une interface

Les notifications passent par une interface abstraite :

interface Notifier {void send(String msg);} class EmailNotifier implements Notifier{class SMSNotifier implements Notifier{

Le code qui envoie les notifications dépend de Notifier, pas des classes concretes.
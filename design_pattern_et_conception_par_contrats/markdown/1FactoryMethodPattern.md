![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/a8e46ba2-0744-4b4a-8df7-47521c27effc/0e98b63e38f38b1495941e3f9fbb9ba8e57892a45c6f3e8014a01a3111908b9c.jpg)

Université de Monastir

Institut Supérieur d'Informatique et de Mathématiques

Département Informatique

# Cours

# Design Patterns etconception par contratsING 2 - Génie Logiciel

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/a8e46ba2-0744-4b4a-8df7-47521c27effc/29df14084907cfd7ee0469f026437d2cd03d9d8b8c26021091a055d9d104ea65.jpg)

# 03

# Patterns de création

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/a8e46ba2-0744-4b4a-8df7-47521c27effc/b7db801a8fbbfbee5d9e36f77efc289f2d75078aebabcbacbbb502370086e076.jpg)

# Objectifs de ce chapitre

Comprendre les enjeux de l'instanciation d'objects

Pourquoi la création d'objects est une source fréquence de problèmes de conception.  
$\succ$  Différence entre instanciation directe (new) et via un pattern.

- Identifier les limites de l'instanciation classique

$\succ$  Couplage fort aux classes concretes.  
Difficulté à changer le type d'objets créés.  
> Complexté croissant avec la multiplicité objets.

# Objectifs de ce chapitre

Découvrir les principaux patterns de création (GoF)  
□ Appliquer les patterns à des cas pratiques

> Simplifier l'instanciation d'objets complexes.  
Découpler le code client de la logique de création.  
> Améliorer la flexibilité et la testabilité des applications.

# Limits de l'instantiation classique

1. Couplage fort aux classes concretes

Le code client dépend directement d'une implémentation précise.

Example :

Report report = new PDFReport(); // Coupled to PDF

$\rightarrow$  Si on veut générer un ExcelReport, il faut modifier le code client partout.

# Limites de l'instanciation classique

2. Manque de flexibilité

- Impossible de changer facilement le type d'objet créé à l'exécution (runtime).  
- On est bloqué par le choix fait dans le code.

3. Difficulté à gérer des familles d'objects

- Quand plusieurs objets liés doivent être créé ensemble, le code devient vite complexe.  
- Exemple : créé une UI Windows ou UI MacOS plusieurs composants (boutons, menus, fenêtre

# Limites de l'instantiation classique

# 4. Maintenance couâteuse

- Chaque ajust de type d'objet impose des modifications dans plusieurs classes.  
- Risque de duplication de logique de création.

new  $\rightarrow$  simple mais rigide.

Patterns de création  $\rightarrow$  apportent flexibilité, extensibilité et testabilité.

# Pattern Factory Method

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/a8e46ba2-0744-4b4a-8df7-47521c27effc/34db727bf5e3cda46eb45264e8112cce5f23334c2968adbe50c3a7794e069efb.jpg)

# Définition

- Le Factory Method est un patron de création qui délege l'instanciation des objets à une méthode spécifique (la "factory method")只不过 qu'à un appel direct à new.  
- Il permet à une classe de laisser ses sous-classes decide du type d'objet à créé, améliorant ainsi la flexibilité et l'extensibilité du code.

# Objectifs

- Encapsulator l'instanciation des objets concrets  
- Libérer le code source de toute responsabilité concernant l'instanciation et la configuration des objets.  
- Respecter le principe SRP en séparant les responsabilités: définir une Factory Method pour la création des objets concrets.  
- Augmenter la flexibilité et la réutilisation du code.

# Structure UML

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/a8e46ba2-0744-4b4a-8df7-47521c27effc/e54313a4b57cfabc681058886e62cc1fbc353f1491d2f64054d8a0119a680550.jpg)

Creator (abstract) : définit la Factory Method (create().

CreatorImpl : implémente la Factory Method pour returner un type précis.

Product (abstract) : définit l'interface commune des objets créés.

ProductImpl : implémentation concrète des objets créés.

# Exemple d'implémentation

```groovy
// Produit   
interface Document { void open();   
}   
//Produits concrets   
class PDFDocument implements Document { public void open() { System.out.println("Ouverture d'un document PDF"); }   
}   
class WordDocument implements Document { public void open() { System.out.println("Ouverture d'un document Word"); }   
}
```

# Exemple d'implémentation

// Créateur  
```txt
abstract class Application {
    // Factory Method
    public abstract Document createDocument();
}
```

```cs
// Test   
public class Main { public static void main(String[] args) { Application app  $=$  new PDFApplication(); // Choix flexible Document doc  $=$  app.createDocument(); doc.open(); }   
}
```

# Avantages et inconvenients

# Avantages

- Réduit le couplage aux classes concrétes.  
- Facilite l'ajout de nouveaux produits sans modifier le client.  
- Améliore la maintainabilité et la testabilité.

# Inconvénients

- Plus de classes à gérer (surcharge structurelle).  
- Peut semble complexe pour de petits projets.

# Exercice d'application

# Problème :

Une application doit envoyer des notifications (Email, SMS, Push) à ses utilisateurs. On peut permettre d'étendre l'application par d'autres types de notifications stèle que WhatsAppNotification.

1. Proposez une solution à ce problème en appliquant le patron Factory Method.  
2. Ajoutez un nouveau type WhatsAppNotification sans modifier le code existant.

# Exercice d'application

```cs
// Produit   
interface Notification { void notifyUser();   
}   
//Produits concrets   
class EmailNotification implements Notification { public void notifyUser() { System.out.println("Envoi d'un email..."); }   
}   
class SMSNotification implements Notification { public void notifyUser() { System.out.println("Envoi d'un SMS..."); }   
}
```

# Exercice d'application

# // Créateur

abstract class NotificationFactory { public abstract Notification createNotification(); }

# // Créateurs concrets

class EmailFactory extends NotificationFactory { public Notification createNotification() { return new EmailNotification(); } }

class SMSFactory extends NotificationFactory { public Notification createNotification() { return new SMSNotification(); } }

// Utilisation   
public class Main { public static void main(String[] args) { NotificationFactory factory  $=$  new EmailFactory(); Notification notification  $=$  factory.createNotification(); notification.notifyUser(); } }

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/a8e46ba2-0744-4b4a-8df7-47521c27effc/a28ccdbfd41e4720967b5ffd8523686f1a1f0abd8cbf036469fed93a15adee63.jpg)

# Travail à domicile

On souhaite créé une classe Logger permettant à des utilisateurs d'afficher des informations sur un programme lors de son exécution.

Un Logger est un objet possédant trois méthodes :

- logInfo(String message)  
- logDebug(String message)  
- logError(String message)

Un Logger est construit avec un état qui peut être :

- LogLevel.INFO  
- LogLevelDebug  
- LogLevel.ERROR

# Travail à domicile

Implémentez le système suivant :

1. Définir une enumeration LogLevel.  
2. Créer une interface Logger avec les trois méthodes ciderissus.  
3. Implémenter trois classes concretes :

InfoLogger : n'affiche que les messages INFO.

DebugLogger : affiche DEBUG et INFO.

ErrorLogger : affiche seulement ERROR.

4. Créer une factory (LoggerFactory) avec une méthode createLogger(LogLevel level).Cette méthode retourne le logger correspondant au niveau demandé.  
5. Écrire un programme de test qui create un Logger via la factory et affiche des messages avec différents niveaux.

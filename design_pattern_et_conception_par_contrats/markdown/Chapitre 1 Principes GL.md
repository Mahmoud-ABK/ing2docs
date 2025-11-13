# Cours

# Design Patterns et conception par contrats ING 2 - Génie Logiciel

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/77ca89a5-e019-438c-99d0-434ecbd731e9/5c1d7c2bace2116325601921907bb1a63100ba94413ff9d2c078eb77d56d7df9.jpg)

# Responsible du cours

Nom & Prénom : Dr. Sameh HBAIEB

Grade: Maitre Assistant

Département : Informatique

Université : ISIMM-Université de Monastir

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/77ca89a5-e019-438c-99d0-434ecbd731e9/ad86c149175c32ec05152a35eb989dee5cf1a354deb9710af46bd6cb35646bb6.jpg)

Email: samehhbaieb11@gmail.com

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/77ca89a5-e019-438c-99d0-434ecbd731e9/8ad66a86d360ab50a4cdfa8a8ba1e480bb86970ddec57c38a1d5e55cb19aacdf.jpg)

LinkedIn: https://www.linkedin.com/in/sameh-hbaieb-b6aab61b9/

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/77ca89a5-e019-438c-99d0-434ecbd731e9/b7dd9fb60bfc6790b25284e5f14740af353f7a56107664595d83437c96574f1d.jpg)

Facebook: https://www.facebook.com/sameh.hbaieb06

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/77ca89a5-e019-438c-99d0-434ecbd731e9/db222fe470b6c05fc63115fa74e95d68d3f2c604206c9ee2ae4af5f6e7234083.jpg)

Bureau : [A38, Bloc A]

Disponibilités :

- Permanence pédagogique : Mardi et heute  
- Rendez-vous par email

# Plan du cours

01

Principes de conception
Orientée Objects

02

Introduction aux Design Patterns

03

Patterns de Création

04

Patterns

Structurels

05

Patterns

Comportementaux

"Ce cours est unconçu pour vous aider à accouérir une maîtrise pratique des Design Patterns et des principales SOLID. N'hésitez pas à poser des questions et à demander des exemples supplémentaires"

# 01

# Principes de conception Orientée Objects

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/77ca89a5-e019-438c-99d0-434ecbd731e9/4fc7bdb49188279887aac88cb5f4cf07bbd93b8ae98e642f0e5044f5571f5885.jpg)

# Objectifs de ce chapitre

Réviser les fondamentaux de la conception orientée objet.  
- Comprendre les notions de couplage, cohésion, abstraction, responsabilité unique.  
□ Introduire les principes SOLID qui guideront l'utilisation des Design Patterns.

# Qu'est ce que le génie logiciel?

Le génie logiciel est l'ensemble des méthodes, outils et bonnes pratiques permettant de conceiveir, développer, tester, déployer et maintainir des systèmes logiciels complexes, fiables et évolutifs.

# Les grands principes du génie logiciel

# 1. Modularité

Principe : Diviser le logiciel en modules indépendants avec une responsabilité unique.

Example :

Dans une application e-commerce :

Module Paiement  $\rightarrow$  gère uniquement les transactions.

Module Catalogue  $\rightarrow$  gère uniquement la liste des produits.

Module Utilisateur  $\rightarrow$  gere l'inscription, l'authentication profil.

Avantage : Chaque module peut être développé et testé indépendamment.

# Les grands principes du génie logiciel

# 2. Abstraction

Principe : Masquer les détails d'implémentation et ne montré que l'essentiel.

Example :

interface PaymentMethod { void pay(double amount); }

class CreditCardPayment implements PaymentMethod { ..} class PaypalPayment implements PaymentMethod { ...}

Avantage : L'utilisateur du module Payment n’a pas besoin de connaître les détails de CreditCardPayment

# Les grands principes du génie logiciel

# 3. Cohésion et Couplage

Cohésion : Chaque module/fonction a une seule

responsabilité

Couplage : Minimiser les dépendances entre modules.

Example :

Mauvais design :

class UserManager {

void saveUser() {...}

void sendEmail() {...}

void logActivity({...})

# Les grands principes du génie logiciel

Bon design :   
class UserManager \{void saveUser(   ) \{...\} \}   
class EmailService \{void sendEmail(   ) \{...\} \}   
class Logger \{void logActivity(   ) \{...\} \}

Avantage : Les modules sont cohérents et indépendants, donc facies àMAINIPR.

# Les grands principes du génie logiciel

# 4. Réutilisabilité

Principe : Créer des composants qui peuvent être utilisés dans plusieurs projets.

Example :

Une librarianie de gestion des dates (DateUtils) ou un composant graphique réutilisable (CustomButton) pour plusieurs applications.

# Les grands principes du génie logiciel

# 5. Portabilité

Principe : Le logiciel doit fonctionner sur plusieurs plateformes.

Example :

Application Java : fonctionne sur Windows, Linux et MacOS grâce à la JVM.

Application web : compatible avec Chrome, Firefox et Edge.

# Les grands principes du génie logiciel

# 6. Extensibilité

Principe : Ajouter de nouvelles fonctionnalités sans modifier le code existant.

Example :

Ajouter un nouveau moyen de paiement à une application ecommerce.

# Les grands principes du génie logiciel

# 7. Maintenabilité

Principe : Faciliter la correction, l'évolution et l'adaptation du logiciel.

Example :

Un code clair et commenté, avec tests unitaires (JUnit) et suivi de version (Git) permet de corriger un bug rapidement.

# Les grands principes du génie logiciel

# 8. Fiabilité

Principe : Logiciel qui fonctionne correctement même en cas d'erreurs ou d'utilité inattendu.

Example :

Une application bancaire : vérifie les soldes avant de transférer l'argent et gère les exceptions réseau.

Utilisation de try/catch, tests automatisés et contrôle des entrées.

# Les grands principes du génie logiciel

# 9. Sécurité

Principe : Protégier le logiciel contre les accès non autorisés et les fuites de données.

Example :

Stockage des mots de passer avec hachage (ex. bcrypt).

Authentication à deux facteurs (2FA) pour un compte utilisé.

# Les grands principes du génie logiciel

# 10. Économie et Efficacité

Principe : Développper un logiciel en optimisant les coûts et lesressources.

Example :

Utilisation de méthodes agiles pour livrer rapidement un MVP. Intégration continue (CI/CD) pour éviter les retardes et réduire les coûts de correction.

# Les grands principes du génie logiciel

En conclusion:

Le génie logiciel fournit des principes généraux :

- Cohésion forte, couplage faible  
Modularité, réutilisabilité  
- Abstraction et encapsulation  
- Séparation des préoccupations

"Chaque原則 que vous découvert est une arme contre la complexité logicielle."

"L'objectif n'est pas seulement de coder... mais de coder intelligemment et durablement.."

# Des grands principes aux principes SOLID

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/77ca89a5-e019-438c-99d0-434ecbd731e9/8aeeb6972b3a1bf5de1c372ed273073b391622396751ffc26b2fdd392004406e.jpg)

Comment appliquer concrètement les principes OO

Dans le développement logiciel?

# S.O.LID.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/77ca89a5-e019-438c-99d0-434ecbd731e9/cde4d5c089d8276ad4483cd28a3e6eb19811aaa1b26d8ec67d4dbd325fb4c76a.jpg)

SOLID = 5 principales proposés par Robert C. Martin

$\mathbf{S} \rightarrow$  Single Responsibility Principle (SRP)  
$\mathrm{O} \rightarrow \mathrm{Open} / \mathrm{Closed Principle}(\mathrm{OCP})$  
$\mathsf{L} \to \mathsf{Liskov Substitution Principle (LSP)}$  
$\mathsf{I} \to$  Interface Segregation Principle (ISP)  
D → Dependency Inversion Principle (DIP)

# Principe 1. Responsabilité unique

Définition : Une classe doit avoir une seule raison de changer.

But : améliorer la cohésion, faciliter la maintenance.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/77ca89a5-e019-438c-99d0-434ecbd731e9/4ddab876d174c52d22d7e88dd9d3bc3281f8fed70b2dc311ecc46ca55c5cc3a0.jpg)

# Example :

```groovy
class Report {
    void calculateStatistics() {
        // Calculate des stats
    }
    void printReport() {
        // Impression du rapport
    }
    void saveToFile(){
        // Sauvegarde dans un fichier
    }
}
```

# Principe 1. Responsabilité unique

# Problèmes :

3 responsabilités différentes : calcul, impression, persistence.  
- Toute modification (nouveau format d'impression, nouvelle base de données, changement de logique métier) implique de modifier la même classe.  
- Forte probabilité d'erreurs et faible maintenabilité.

$\Rightarrow$  Respect du SRP:

On sépare les responsabilités en plusieurs classes cohésives : StatisticsCalculator, ReportPrinter, ReportSaver

# Principe 2. Ouverture / Fermeture

Définition : Une classe doit être ouverte à l'extension, mais fermée à la modification.

# But :

On doit pouvoir ajouter de nouvelles fonctionnalités sans modifier le code existant.  
On favorise l'héritage, le polymorphisme ou les interfaces au lieu de modifier directement une classe.

# Principe 2. Ouverture / Fermeture

# Example: Violation OCP

```javascript
class Rectangle{ double width; double height; public Rectangle(double w,double h){ this.width  $\equiv$  w; this.height  $\equiv$  h; }   
}   
class Circle{ double radius; public Circle(double r){ this.radius  $=$  r; } }
```

```txt
class AreaCalculator {
public double calculate(Object[]) shapes) {
    double area = 0;
    for (Object shape : shapes) {
        if (shape instanceof Rectangle) {
            Rectangle r = (Rectangle) shape;
            area += r.width * r.height;
        } else if (shape instanceof Circle) {
            Circle c = (Circle) shape;
            area += Math.PI * c radians * c radians;
        }
    }
}
```

# Principe 2. Ouverture / Fermeture

# Respect OCP

```txt
// Abstraction commune   
interface Shape{ double area();   
1   
// Rectangle   
class Rectangle implements Shape{ double width, height; public Rectangle(double w, double h) { this.width  $=$  w; this.height  $=$  h; } public double area(){ return width \* height; 1
```

```txt
//Cercle   
class Circle implements Shape{ double radius; public Circle(double r){ this.radius  $=$  r; } public double area(){ return Math.PI \* radius \* radius; }   
//Calculateur qui respecte OCP   
class AreaCalculator{ public double calculate(Shape[] shapes){ double area  $= 0$  . for (Shape shape : shapes) { area  $+ =$  shape.area(); } return area; }
```

# Principe 3. Substitution de Liskov

Les sous classes doivent pouvoir être substituées à leur classe de base sans modifier la logique métier du programme (transparence vis-à-vis les utilisateurs)  
Cela signifie qu'il ne faut pas lever d'exception imprévue ( comme UnsupportedOperationException par exemple), ou modifier les valeurs des attributs de la classe principale d'une manière inadaptée, ne respectant pas le contrat définir par la méthode.

# Principe 3. Substitution de Liskov

# Example: Violation de LSP

class Rectangle {

protected int width;

protected int height;

public void setWidth(int w) \{ this.width = w; \}

public void setHeight(int h) { this.height = h; }

public int getArea() { return width * height; }

}

class Square extends Rectangle {

@Override

public void setWidth(int w) {

this.width = w;

this.height = w; // forcer un carré

}

@Override

public void setHeight(int h) {

this.width = h;

this.height = h; // force un carré

}

# Principe 3. Substitution de Liskov

# Problème :

- Square hérite de Rectangle, mais ne respecte pas son comportement attendu.

# Exemple d'utilisation :

Rectangle r = new Square();

r.setWidth(5);

r.setHeight(10);

System.out.println(r.getArea()); // On s'attend à 50, mais on obtient 100

LSP violé : un Square ne peut pas toujours se substituer à un Rectangle.

# Principe 3. Substitution de Liskov

# Respect LSP:

```txt
interface Shape { int getArea(); }
```

// Rectangle indépendant  
```javascript
class Rectangle implements Shape{ private int width; private int height; public Rectangle(int w, int h) { this.width = w; this.height = h; } public int getArea() { return width \* height; }
```

// Carré indépendant  
```txt
class Square implements Shape { private int side;
```

```txt
public Square(int s) { this_side = s; }
```

```txt
public int getArea() { return side \* side; }
```

# Principe 3. Substitution de Liskov

# Avantages :

- Chaque classe respecte son comportement attendu.  
- Square et Rectangle sont au même niveau hierarchique.  
- On peut utiliser :

```txt
Shape[] shapes = { new Rectangle(5, 10), new Square(7) };  
for (Shape s : shapes) {  
    System.out.println(s.getArea());  
}  
// Résultats corrects pour chaque forme
```

# Principe 4. Ségrégation d'interface

Définition : Mieux vaut plusieurs interfaces spécifiques qu'une interface générale trop large.

Le principe stipule que le client ne doit voir que les services dont il a besoin.  
Autrement dit, la dépendance d'une classe vers une autre doit être restreinte à l'interface la plus petite possible.

# Principe 4. Ségrégation d'interface

# Violation de l'ISP :

// Interface trop large   
interface Worker{ void work(); void eat(); void sleep();   
}

class HumanWorker implements Worker {
    public void work() { System.out.println("L'humain travaill...")); }
    public void eat() { System.out.println("L'humain mange...")); }
    public void sleep() { System.out.println("L'humain mort...")); }
}

class RobotWorker implements Worker {
    public void work() { System.out.println("Le robot travaill..."); }
}

// Probleme : un robot ne mange pas et ne dort pas   
public void eat() {throw newUnsupportedOperationException("Le   
robot ne mange pas");}   
public void sleep() {throw newUnsupportedOperationException("Le   
robot ne dort pas");}

# Principe 4. Ségrégation d'interface

Respect de l'ISP : On segmente l'interface en plusieurs petites interfaces cohérentes :

```aidl
// Interfaces spécialisées  
interface Workable {  
    void work();  
}  
interface Eatable {  
    void eat();  
}  
interface Sleepable {  
    void sleep();  
}
```

# Principe 4. Ségrégation d'interface

```txt
// Implementations   
class HumanWorker implements Workable, Eatable, Sleepable { public void work() { System.out.println("L'humain travaill...");} public void eat() { System.out.println("L'humain mange...");} public void sleep() { System.out.println("L'humain mort...");}   
}   
class RobotWorker implements Workable { public void work() { System.out.println("Le robot travaill...");}
```

# Principe 5. Inversion des dépendances

Dépendre des abstractions, pas des implémentations.  
- Ce principe vise principalement à réduire les dépendances entre les modules de code (faible couplage).

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/77ca89a5-e019-438c-99d0-434ecbd731e9/94c5718bf9dfdf69ea39589db5eff35e007a706c330ad0207c13f2c0e3c1a3a1.jpg)

# Principe 5. Inversion des dépendances

Exemple avec dépendance forte:

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/77ca89a5-e019-438c-99d0-434ecbd731e9/de8dba3ca7967ea4edb9c9a717470aa28f43dd40542a920281c2124adc788f9c.jpg)

public class ReservationSalleService { private ReservationSalleDao reservationSalleDao;

```java
public ReservationSalleService() {
    reservationSalleDao = new MySqlReservationSalleImpl();
} 
public void resolver(ReservationSalle reservationSalle) {
    // faire un traitement nécessaire
    // (par exemple la validation de la réservation)
    // sauegarder la réservation
    reservationSalleDao.save(reservationSalle);
}
```

ReservationSalleService dépend de ReservationSalleDao

Création d'une instance de  
ReservationSalleDao dans le  
constructeur. La classe doit  
connaître le type  
d'implémentation (objet  
concrét)  
A éviter l'instanciation de l'objet  
reservationSalleDao

# Principe 5. Inversion des dépendances

□Cette solution est problèmeatique.

□ Il existe un couplage fort entre les objets: ReservationSalleService et ReservationSalleDao:  
□il n'est pas possible de considérer ReservationSalleDao comme une abstraction ou une interface puisque le service doit lui-même spécifier le type concret de l'attribut MySQLReservationSalleImpl.

# Principe 5. Inversion des dépendances

La création d'un objet de type MySqlReservationSalleImpl nécessite de passer des paramètres concrets comme par exemple l'adresse de la base de données, le login, le mot de passé d'accès... Tout un ensemble d'informations que la classe ReservationSalleService n'a sans doute pas à connaître.

# Principe 5. Inversion des dépendances

Solution: Inverser les dépendances pour réduire le couplage entre les classes

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/77ca89a5-e019-438c-99d0-434ecbd731e9/1792e864b4f9d525344e6feff48f73a96e2225faa5a77cd01243e88e95a68e98.jpg)

# Principe 5. Inversion des dépendances

public class ReservationSalleService {

private ReservationSalleDao reservationSalleDao;

public ReservationSalleService (ReservationSalleDao reservationSalleDao) { this.reservationSalleDao = reservationSalleDao; }

public void resolver(ReservationSalle reservationSalle) {

// faire un traitement nécessaire  
// (par exemple la validation de la réservation)

// sauvegarder la réservation reservationSalleDao.save(reservationSalle); } }

Injection de la dépendance par le constructeur:  
ReservationSalleService ne dépend plus d'un objet concret  
ReservationSalleDao.  
On fait passer comme paramètre un objet abstraction qu'on ne connait pas son type

# Les principales SOLID

<table><tr><td>Principe</td><td>Idée clé</td><td>Objectif</td></tr><tr><td>SRP</td><td>Une seule responsabilité</td><td>Cohésion</td></tr><tr><td>OCP</td><td>Ouvert à l&#x27;extension, fermé à la modification</td><td>Extensibilité</td></tr><tr><td>LSP</td><td>Remplaçabilité des sous-classes</td><td>Polymorphisme correct</td></tr><tr><td>ISP</td><td>Interfaces spécifiques</td><td>Faible couplage</td></tr><tr><td>DIP</td><td>Dépendances sur abstractions</td><td>Flexibilité</td></tr></table>
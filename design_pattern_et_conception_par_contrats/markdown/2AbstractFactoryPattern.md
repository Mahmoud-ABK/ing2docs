# Pattern Abstract Factory

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/7a2a307f-ec3c-4c18-94ef-8aad73364cff/b5f482360feef9d53f5d01ec102311395451574f0e7b691806708589b9bcabe9.jpg)

# Définition

- L'Abstract Factory est un pattern de création qui fournit une interface pour creer des familles d'objects liés ou dépendants, sans spécifiqueurs classes concretes.  
- Contrairement au Factory Method, qui create un seul type d'objet, l'Abstract Factory create plusieurs objets qui sont cohérents entre eux.  
- Il est souvent utilisé lorsque le système doit être indépendant de la façon dont ses objets sont créés composés et représentés.

# Objectifs

- Encapsulator la création d'objets : Permet de creator des objets sans exposer la logique de création au client.  
Assurer la cohérence : Garantir que les objets créés appartiennent à la même famille ou respectent des contraintes communes.  
- Séparer le client des classes concretes : Le client utilise uniquement les interfaces abstraites, ce qui facilité l'extension et la maintenance.  
- Faciliter l'extensibilité : Ajouter de nouvelles familles de produits ne nécessite pas de modifier le code client existant.

# Structure UML

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/7a2a307f-ec3c-4c18-94ef-8aad73364cff/3e829432c7377017357c54ee60c6c6717d8abcefce3f0392e40106549d94e5b6.jpg)

# Exemple d'implémentation

Imaginons que nous développons une application qui doit pouvoir fonctionner aussi bien sur Windows que sur MacOS.

Selon le système, les boutons et les cases à cocher doivent avoir un style différent. Au lieu de mélanger du code spécifique à chaque système un peu partout dans l'application, nous allons utiliser Abstract Factory pour centraliser la création de ces composants.

# Exemple d'implémentation

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/7a2a307f-ec3c-4c18-94ef-8aad73364cff/18ae3fb76f4a626f495a14241578648f191803c29863c7efc8e9a3e8e5d90b81.jpg)

# Exemple d'implémentation

# // Abstract Products

interface Button {void paint();}

interface Checkbox{void paint();}

# // Concrete Products

class WindowsButton implements Button {

public void paint() {

System.out.println("Windows Button");

}

class MacButton implements Button {

public void paint() {

System.out.println("Mac Button");}

class WindowsCheckbox implements checkbox {

public void paint() {

System.out.println("Windows checkbox");}

class MacCheckbox implements checkbox {

public void paint() {

System.out.println("Mac checkbox");}

# Exemple d'implémentat // Cie

# // Client

// Abstract Factory  
```txt
interface GUIFactory {
Button createButton();
Checkbox createCheckbox();
}
```

// Concrete Factories  
```java
class WindowsFactory implements GUIFactory {
    public Button createButton() { return new WindowsButton(); }
    public checkbox createCheckbox() { return new WindowsCheckbox(); }
}
```

```java
class MacFactory implements GUIFactory {
    public Button createButton() { return new MacButton(); }
    public checkbox createCheckbox() { return new MacCheckbox(); }
}
```

```java
public class Application {
    private Button button;
    private checkbox checkbox;
    public Application(GUIFactory factory) {
        button = factory.createButton();
        checkbox = factory.createCheckbox();
    }
    public void render() {
        buttonpaint();
        checkbox Painting;
    }
    public static void main(String[] args) {
        GUIFactory factory = new WindowsFactory(); // ou MacFactory
        Application app = new Application(factory);
        app.render();
    }
}
```

# Avantages et inconvenients

# Avantages

- Créer des familles cohérentes d'objects.  
Le client est indépendant des classes concretes.  
- Facilité l'extension du code à de nouvelles familles de produits.

# Inconvénients

- Ajouter un nouveau type de produit (nouvelle interface) demande de modifier toutes les factories concretes.  
- Peut devenir complexe si le nombre de produits et familles est élevé.

# Exercice d'application

# Problème :

Une entreprise de produits veut développer un système pour générer différents thèmes graphiques de son interface utilisateur.

Chaque thème définit un style pour deux éléments :

Fenêtre (Window) et Bouton (Button)

L'entreprise souhaite pouvoir changer facilement le thème graphique (ex. Dark ou Light) sans modifier le code principal du jeu.

# Exercice d'application

# Travail demandé :

1. Définir une modélisation de ce système en appliquant le pattern Abstract Factory  
2. Implémenter les interfaces/classes définies  
3. Tester en exécutant le jeu avec les deux thèmes (Dark et Light).
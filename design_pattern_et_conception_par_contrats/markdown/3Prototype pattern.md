# Pattern Prototype

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/706bc0cb-d76c-4a37-b28a-29857f7aba9b/3139b20207dea1ac6d4dbf3395f0479d4a1e9e23f6e24111acbe9382a09f3727.jpg)

# Définition

- Le Pattern Prototype est un patron de conception qui permet de copier des objets existants只不过 que de les créé à partir de zéro.  
- Il repose sur le principe que la création d'un objet peut être couhteuse ou complexe, et qu'une duplication d'un prototype existant est plus efficace.  
Principe clé :

"Créer de nouveaux objets en clonant un objet prototype existant."

# Objectifs

1. Réduire le coût de création d'objets complexes ou lourds à instancier.  
2. Permettre la duplication d'objects avec leurs états actuels, en conservant les attributs configurés.  
3. Fournir un mécanisme flexible pour créé des objets sans dépendre de leurs classes concretes.  
4. Faciliter la création d'objects dérivés à partir d'un modele commun.

# Structure UML

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/706bc0cb-d76c-4a37-b28a-29857f7aba9b/9985edaa6f235f54fb657cd566bbd52c25e3dae6e30615d7e3da1053fc2d91db.jpg)

# Exercice

Vous développpez un jeu de gestion d'animaux dans un zoo.

Chaque animal a des attributs comme :

- nom (String)  
espece (String)  
- âge (int)  
- santé (String)

Au lieu de créé chaque animal à partir de zéro, vous foulez cloner des animaux existants pour créé rapidement de nouveaux individus.

# Exercice

# Travail demandé

1. Créer une classe Animal qui implémente le pattern Prototype (méthode clone).  
2. Créer 2 prototypes d'animaux : un lion et un éléphant.  
3. Cloner ces animaux pour创建工作 de nouvelles instances avec eventuellement des attributs modifiés (nom, âge).  
4. Afficher les informations de chaque animal pour vérifier que le clonage fonctionne correctement.

# Solution

class Animal implements Cloneable {

private String nom;

private String espece;

private int age;

private String sante;

public Animal(String nom, String espece, int age, String sante) {

this.nom = nom;

this.espece = espece;

this.age = age;

this.sante = sante;

this.maladies = new ArrayList<>();

// Méthode clone pour Prototype (clonage profond)

@Override

public Animal clone() {

try{

Animal clone = (Animal) super.clone();

// Clonage profond de la liste

return clone;

} catch (CloneNotSupportedException e) {

e.printStackTrace();

return null;

}

// Affichage des infos

public void afficherInfos() {

System.out.println("Nom: " + nom);

System.out.println("Espèce: " + espèce);

System.out.println("Age: " + age);

System.out.println("Santé: " + sante);

System.out.println("Maladies: " + maladies);

System.out.println("");

}

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/706bc0cb-d76c-4a37-b28a-29857f7aba9b/a4d0e634d8be6a2c43d25854dfdbfd1af6e3ac14040dbdd435fae8538735a982.jpg)

# Solution

```java
public class ZooPrototypeDemo { public static void main(String[] args) { // Creation des prototypes Animal lionPrototype = new Animal("Lion Prototype", "Lion", 5, "Bon");
```

```javascript
Animal elephantPrototype = new Animal("Éléphant Prototype", "Éléphant", 10, "Bon");
```

```javascript
// Clonage des animaux  
Animal lion1 = lionPrototype.clone();  
lion1.setNom("Simba");  
lion1.setAge(3);
```

```javascript
Animal elephant1 = elephantPrototype.clone();  
elephant1.setNom("Dumbo");  
elephant1.setAge(8);
```

```javascript
// Affichage lionPrototype.afficherInfos(); lion1.afficherInfos(); elephantPrototype.afficherInfos(); elephant1.afficherInfos();
```

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/706bc0cb-d76c-4a37-b28a-29857f7aba9b/04418ab92752aa45b6e52e9c6e1ee3881530ec9206f7045fbc28820cbd5066bd.jpg)
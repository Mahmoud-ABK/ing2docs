# Pattern Adapter

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/e4bb64a3-f6f6-4d99-9bf6-d6be4c1a4258/808f48cf476c9705d46efb0ca376253edae6ad0fc517413bb705d3f6ca3bd0e1.jpg)

# Définition

# L’Adaptateur :

- Est un patron de conception structurel qui permet de faire collaborer des objets ayant des interfaces incompatibles.  
- Fonctionne comme un pont entre deux interfaces incompatibles.  
- Permet de combiner la capacité de deux interfaces indépendantes.

# Objectif

- Convertir l'interface d'une classe en une autre interface attendue par le client (interface cible) afin de permettre à des classes incompatibles d'interagir ensemble.  
□ Souvent motive par la réutilisation de code: le code réutilisé doit être conforme à une interface requise

# Structure UML

Adaptateur de classe: par heritage multiple/interfaces

Adaptateur de classe par heritage multiple (quand c'est possible) :

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/e4bb64a3-f6f6-4d99-9bf6-d6be4c1a4258/01ec44ef193a963d3c59114c6b078f7fba01ada563fb456e3ec390db7a7bb785.jpg)

Adaptateur d'objet: par composition d'objets

Adaptateur d'objet par composition d'objets :

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/e4bb64a3-f6f6-4d99-9bf6-d6be4c1a4258/53556256139c77a3f08b7853f2cc1b09e82af80d6a2b6ce5163efea56ad87e96.jpg)

# Exemple d'implémentation

On dispose d'une interface MediaPlayer et une classe concrète AudioPlayer implémentant l'interface MediaPlayer.

AudioPlayer peut dire les fichiers audio au format mp3 par défaut.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/e4bb64a3-f6f6-4d99-9bf6-d6be4c1a4258/08c0eb3b14b63c11e529693e7b47f3a9d8962e65854fef813b1680e3823c82e1.jpg)

```groovy
class AudioPlayer implements MediaPlayer{   
public void play(String filename) { System.out.println("Lecture de MP3 + filename + " via AudioPlayer..."); }   
}
```

# Exemple d'implémentation

# Problème:

Nos voulons faire en sorte qu'AudioPlayer puisse également dire d'autres formats VLC et mp4.

Les méthodes ne sont ni

homogenes  
- interchangeables

```txt
class Mp4Player { public void playMp4(String filename) \{...\}   
class VlcPlayer { public void playVlc(String filename) \{...\}
```

# Exemple d'implémentation

# Solution:

On intègre à la solution existante un autre composant: interface AdvancedMediaPlayer et des classes concrètes MP4Player et VLCPlayer implémentant l'interface AdvancedMediaPlayer qui permettent de dire des fichiers aux formats mp4 et VLC, respectivement.  
On doit creer aussi une classe d'adaptateur MediaAdapter qui implémente l'interface MediaPlayer et utilise des objets AdvancedMediaPlayer pour dire le format requis  
→Adaptateur d'objets (composition)

# Exemple d'implémentation

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/e4bb64a3-f6f6-4d99-9bf6-d6be4c1a4258/9bf53623e2d4ee40d5175f8761af016fe6b1cb0e4b2fca2242bf6af5a0e30c52.jpg)

# MediaAdapter

```java
public class MediaAdapter implements MediaPlayer { private AdvancedMediaPlayer advancedPlayer; public MediaAdapter(String extension) { if (extension.equalsCase("v1c")) { advancedPlayer = new V1cPlayer(); } else if (extension.equalsCase("mp4")) { advancedPlayer = new Mp4Player(); } }   
@override   
public void play(String filename) { String extension  $=$  getExtension(filename); if (extension.equalsCase("v1c")) { advancedPlayer.playV1c(filename); } else if (extension.equalsCase("mp4")) { advancedPlayer.playMp4(filename); } }
```

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/e4bb64a3-f6f6-4d99-9bf6-d6be4c1a4258/43a7dcee4bc5755de33060d810d3d36a241239870c0edc70562810c00ba65d5e.jpg)

# AudiPlayer

```java
public class VideoPlayer implements VideoPlayer { private MediaAdapter adapter; @Override public void play(String filename) { String extension  $=$  getExtension(filename); if (extension.equalsCase("mp3")){ System.out.println("Lecture du MP3:" + filename); } else if (extension.equalsCase("v1c") || extension.equalsCase("mp4")) { adapter  $=$  new MediaAdapter(extension); adapter.play(filename); } else { System.out.println("Format non supporté:" + extension); } }
```

# Le client (programme principal)

```java
public class Main { public static void main(String[] args) { MediaPlayer player  $=$  newAudioPlayer(); player.play("musique.mp3"); player.play("clip.mp4"); player.play("film.vlc"); player.play("document.avi"); } }
```

# Avantages des adaptateurs

<table><tr><td>Avantage</td><td>Explication</td></tr><tr><td>Découplage total</td><td>Le client ne dépend pas des classes concrètes (Mp4Player, VLCPlayer), juste de MediaPlayer.</td></tr><tr><td>Extensibilité</td><td>Il est possible d&#x27;ajouter un AviPlayer ou FlacPlayer sans changer le code client.</td></tr><tr><td>Encapsulation</td><td>Le client ignore tout de la logique interne d&#x27;adaptation (création de MediaAdapter).</td></tr><tr><td>Substitution</td><td>Il est possible de remplacer AudioPlayer par une autre implémentation (SmartPlayer, StreamingPlayer) sans casser le code du client.</td></tr></table>

# Problématique et solution des registres dynamiques

L'utilisation de if/else: rend le système rigide (OCP pas juste respecté)  
$\Rightarrow$  Solution: utiliser un registre dynamique des adaptateurs afin de permettre d'enregistrer dynamiquement de nouveaux formats multimédias, sans modifier le code existant.  
Principe:

AudioPlayer n'a plus besoin de connaître les types (mp4, VLC, etc.).  
- Les adaptateurs sont déclarés dans un registre (une Map) au démarrage.  
- Chaque adaptateur est créé à la volée avec une fabrique (Supplier<AdvancedMediaPlayer>).

# L'interface fonctionnelle Supplier

# Qu'est-ce que Supplier<T>?

- Supplier<T> est une interface fonctionnelle du package java.util.function introduite avec Java 8.  
- Elle représentée une “fabrique” d'objets (une fonction sans argument qui returne une valeur de type T).

# Définition :

```java
@FunctionallInterface   
public interface Supplier<T> { T get(); // produit une instance de T}
```

# MediaAdapter avec registre dynamique

import java.util.Map;

import java.util.function.Supplier;

public class MediaAdapter implements MediaPlayer {

// Registre dynamique d'adaptateurs => map immuable (non modifiable)

private static final Map<String, Supplier<AdvancedMediaPlayer>> registry = Map.of(

" VLC", VLCPlayer::new, // Appel constructeur => new VLCPlayer()

"mp4", Mp4Player::new // Appel constructeur => new Mp4Player()

);

private AdvancedMediaPlayer advancedPlayer;

public MediaAdapter(String extension) {

Supplier<AdvancedMediaPlayer> supplier = registry.get(extensiontoLowerCase());

if (supplier != null) {

this.advancedPlayer = supplier.get();

}

}

# MediaAdapter avec registre dynamique

```txt
@override   
public void play(String filename) { if (advancedPlayer  $= =$  null) { System.out.println("Aucun adaptateur disponible pour : " + filename); return; } String extension  $=$  getExtension(filename); if (advancedPlayer instanceof VlcPlayer) { advancedPlayer.playVlc(filename); } else if (advancedPlayer instanceof Mp4Player) { advancedPlayer.playMp4(filename); } else { System.out.println("Format non reconnu : " + extension); } } private String getExtension(String filename) { int i  $=$  filename.lastIndexOf("\\."); return  $(\mathrm{i} > 0)$  ? filename.substring(i+1): ""; } }
```

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/e4bb64a3-f6f6-4d99-9bf6-d6be4c1a4258/db93ed0171f70631a0427de02948ea55e5283d84cd418ac06c721375df2a6036.jpg)

# AudioPlayer

```java
public class AudioPlayer implements MediaPlayer {   
@override   
public void play(String filename) { String extension  $=$  getExtension(filename); if (extension.equalsIgnoreCase("mp3")){ System.out.println("Lecture du MP3:" + filename); } else { MediaAdapter adapter  $=$  new MediaAdapter(extension); adapter.play(filename); }   
}   
private String getExtension(String filename){ int i  $=$  filename.lastIndexOf("\\."); return  $(\mathrm{i} > 0)$  ? filename.substring(i+1):";   
}
```

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-14/e4bb64a3-f6f6-4d99-9bf6-d6be4c1a4258/926c9b019ba872a5809e97c874c008fed8dfc3ff4b3c9f55f39b6635a831c385.jpg)

# Exercice : Convertisseur de messages

Une entreprise développue une application de messagerie interne. Elle peut intégrer un système de notification externe qui envoie des messages via différents canaux :

- Email  
SMS  
Slack (chat d'équipe)

Problème :le système existant appelle toujours une méthode send(String message), mais les classes des nouveaux canaux n'ont pas la même interface.

# Exercice : Convertisseur de messages

Soit l'interface du système existant : public interface MessageSender \{ void send(String message);}

```java
Et soit les nouvelles classes à intégrer:  
public class EmailService {  
public void sendEmail(String subject, String body) {  
System.out.println("Envoi Email: " + subject + " | " + body); }  
public class SmsService {  
public void sendSms(String phoneNumber, String text) {  
System.out.println("Envoi SMS à " + phoneNumber + ": " + text); }  
}
```

# Exercice : Convertisseur de messages

# Travail demandé:

1. Implémentez un Adapter (ou plusieurs) pour rendre ces classes compatibles avec l'interface MessageSender: un adapter pour chaque service (Email, SMS, Slack)  
2. Créez un MessageSenderFactory qui désisit dynamiquement le bon adapter selon un paramètre,  
3. Simuler l'envoi de messages depuis le client principal, sans changer le code client.
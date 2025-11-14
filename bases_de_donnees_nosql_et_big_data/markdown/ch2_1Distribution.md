# Cours : Big DATA

--Chapitre 2 : Traitement des données massives avec Hadoop--

# Objectifs

2

Au terme de ce chapitre, vous serez capable de:

Explainier le principe de localité de données  
Décrir la vue d'ensemble et architecture(s) d'Hadoop  
Décrire le fonctionnement de HDFS  
Ecrire des algorithms Map-Reduce  
Comprendre la gestion de ressource avec YARN

# Motivation

# Too much data

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9827eccc-90d4-42a3-b576-1bb51249f0ce/76d6a102fa0b974a90ebf917fd911ddb342762bdc9564b4b036108ba6f75b5fb.jpg)

Not enough compute power, storage or infrastructure

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9827eccc-90d4-42a3-b576-1bb51249f0ce/c449339095c7042fc10026eb3a1a19964c19875ebee18ba4152dda4643d02095.jpg)

# Plan

□ Contexte d' apparition  
□ Présentation d'Hadoop  
Ecosystème d'Hadoop  
Système de fichiers distribué d'Hadoop : HDFS  
Hadoop Map-Reduce  
□ Allocation et gestion de ressources avec Yarn  
□ API JAVA d’Hadoop

5

# Contexte

C'est quoi?

Comment le programmermer?

# Distribution des données ettraitements

# - Centre de données -

6

Dans un centre de données, les serveurs sont empilés dans des baies (Rack) équipées pour leur fournir l'alimentation, la connexion réseau vers la grappe de serveur, la ventilation.  
- Une baie contient environ 40 serveurs. Un centre de données contient quelques centaines de baies. Ordre de grandeur : quelques milliers de serveurs par centre.  
- Combien des centres chez Google, Facebook, Amazon ...? Des millions de serveurs.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9827eccc-90d4-42a3-b576-1bb51249f0ce/47688f767a3faf65817e0316ae0860be6078084c8733abe033e79c228745d4b9.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9827eccc-90d4-42a3-b576-1bb51249f0ce/71e17ab865a61d7914358fee450f511962ea9e24579398262d9eca32ba8e1101.jpg)  
BigData  
Data Center

# Distribution des données ettraitements

# - Principe du Data Locality

C'est toujours l'accès aux données qui coute cher, pas le calcul lui-même une fois les données dans le cœur de calcul.  
□ Principe de data locality ou proximité des données.

# Classique:

Ramener les données au serveur pour les traiter

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9827eccc-90d4-42a3-b576-1bb51249f0ce/1a3864f34e37a66c0a08a273dbcf43e5db0b0d65633120594cae5fed6d43161b.jpg)

# Big Data:

Amener les codes detraitements aux données

data locality

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9827eccc-90d4-42a3-b576-1bb51249f0ce/f7b972c04ffa34c7af8a58885005698beeca7ab88b4f0a00cbbacc6702345aa3.jpg)

BigData

# Distribution des données ettraitements

# -Besoins du Big Data-

□ Besoins: Frameworks dédiés prénant en charge les enjeux du calcul distribué :

Optimisation des transferts disques et réseau en limitant les déplacements de données  
Tolerance aux pannes (fault tolerance).  
- Scalabilité pour permettre d'adapter la puissance au besoin (scalability)

# Distribution des données ettraitements

# -Scalabilité

9

□ Scalabilité: C'est la capacité d'un système à gérer des quantités croissantes de données, sans diminution significative de ses performances

# VERTICAL SCALING

Increase size of instance RAM, CPU etc.)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9827eccc-90d4-42a3-b576-1bb51249f0ce/d58aba1c64481feaff895fde3f1846a5dd10c4f77b685e347acd87cc63443c0d.jpg)

$\succ$  Plus facile de maintainir une seule machine.  
> Control centralisé sur les données et les calculs.

# HORIZONTAL SCALING

(Add more instances)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9827eccc-90d4-42a3-b576-1bb51249f0ce/f8669881980826a83a78c2e5d316d9a4994313de371cdad0bb3b67a481bf9f9c.jpg)

Mise à niveau illimitée de la puissance de calcul d'un système  
Tolerance aux pannes
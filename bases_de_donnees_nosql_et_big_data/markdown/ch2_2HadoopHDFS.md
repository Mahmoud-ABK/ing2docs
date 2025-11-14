# 10

# Hadoop: Présentation et écosystème

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/50b958d144f00d2e8566b67c4412f78bca2823d4b5f7fc73dd96a81d98f3de83.jpg)

# Présentation du Framework

11

Hadoop est un framework open source, écrit en Java et géré par la fondation Apache.  
□ Java est le langage de préférence pour écrire des programmes Hadoop natifs. Néanmoins, il est possible d'utiliser Python, Bash, Ruby, Perl ...  
Hadoop offre un rapport performance-prix très compétitif (Amazon EMS, réutilisation de PC existants, aucun coûts de licences ni de matériel spécialisé HPC).  
□ Le nom “Hadoop” était initialement celui d'un éléphant en peluche, jouet préfééré du fils de Doug Cutting.

Doug Cutting creator de Hadoop.

# Présentation du Framework

12

Le projet Hadoop consiste en deux grandes parties:

Stockage des données : HDFS (Hadoop Distributed File System)  
□Traitement des données : MapReduce / Yarn

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/f16a7e23835e0ccefe416e22f6c2f8d409ab9c072df9a5ce67bf769ed8b469ce.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/e408613b8b00bdebb282cd3ed244acf1c66177c031c5ec487fd46d888bf9f739.jpg)

Principe:

Diviser les données  
Les sauvégarder sur une collection de machines, appelée cluster  
□ Traiter les données directement là où elles sont stockées,只不过 que de les copier à partir d'un serveur distribué  
Il est possible d'ajouter des machines à votre cluster, au fur et à mesure que les données augmentent. Les machines peuvent être hétérogenes.

# Historique de Hadoop

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/03116793821c1f4fed9c5a6b00af8d69fc3a931db256d0b27bd381a772cd412e.jpg)

# Qui utilise Hadoop?

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/41ecbd28aef139992202d3f7b42e762f7c768a355faca1e344958682bc2dafce.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/3a2f1fc031937999ee28e762c9278bcfd32e892445d97bcb58d853d106d6335d.jpg)

rackspace

HOSTING

amazon.com

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/d6a389a9446ebb991d2ee682f044cb0528d341d9fde5ee7b8e5f50ad02aa473d.jpg)

NING

SAMSUNG

VISA

YAHOO!

# Ecosystème de Hadoop

Le système de fichiers distribués Hadoop (HDFS) est basé sur le système de fichiers Google (GFS).  
Il fournit un système de fichiers distribué concu pour fonctionner sur du matériel standard et presente de nombreuses similitudes avec les systèmes de fichiers distribués existants avec

certaines différences.

Il est hautementtolerant aux pannes et est concu pouretre déployé sur du matériel à faiblebout.

NB: Laiste presentee ci-dessus n'est pas exhaustive!

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/95356d36e8b51aeb718e9dcfc07ff45a35abf05eb7ba669a45d7a5491eb4cba5.jpg)

# Apache Hadoop Ecosystem

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/1aac9c245bc827c73a9e0da986449b7ee0284ab577779b0613f4805d4740c864.jpg)

# Ecosystème de Hadoop

- MapReduce est un modele de programmation parallèle pour l'ecriture d'applications distribuées concu par Google.  
Permet un traitement efficace de grandes quantités de données (plusieurs teraoctets) sur des grappes étendues (des milliers de nœuds) de matériel standard de manière fiable et tolérante aux

pannes.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/2286a8b8cb6364010702ed6fe1b8c7f4843495db12a837af898ab5be2ff1552d.jpg)

# Apache Hadoop Ecosystem

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/a2a940252399083eaf7f69e8281b0064615f8050581c1a3d782ee7df360771fe.jpg)

Ambari

Provisioning, Managing and Monitoring Hadoop Clusters

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/21aa5256fa590e321f568f559ff4e3986dccee2f6143240b0e1251f98d7a9c20.jpg)

Sooep

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/12509d5eeadb9c25ea614b4b2e64a6742b8aaa613e412c6bb656d3153264b476.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/f2bafe6f1c8534418584efcf6dbd7c3604c188382792c7d0c9fc18e18177e78b.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/e8f38758b87c055a6dc538dfd2e0372634a9996ca8916949ff7e3d91b911a6eb.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/0b8bc6ddd0cea86bc940ee1eafb91f548f58cbbb792f974667c6ae5484b96f86.jpg)

Rconnnns

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/ca95cf896a61d88dd40a268be1231dcbba25c3b4834a18aa8a323049446b8786.jpg)

Aenno TOS

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/2a6c89958f32b53f1db8c859716de418e540f03d90048bdc0756fc1f6ccc2393.jpg)

hneaae

Cannnnnne

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/38ed93591a7fee60162e034f168e7e43fd0328a1996ce7d1ebc2cf070b0f3779.jpg)

Fne eae

Zookeeper

$\left( {x - {2x}}\right) t - x{y}^{2} = \left( {x - {2x}}\right) {f}^{\prime }t$

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/9251c0503dad91af64f9b220a70903e64b6cd82a9e66c7da1505e8606d75d465.jpg)

YARN Map Reduce v2

Distributed Processing Framework

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/097e3a759164e7c883bdcef8219c81f51d789381a6d2089f982b2bf980b5e446.jpg)

NB: Laiste presentee ci-dessus n'est pas exhaustive!

HDFS

Hadoop Distributed File System

# Ecosystème de Hadoop

Plusieurs outils existent pour permettre:

L'extraction et le stockage des données de/sur HDFS  
La simplification des opérations de traitement sur ces données  
La gestion et coordination de la plateforme  
Le monitoring du cluster

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/5ccdf9e01d5cc9a92261958ee22c4dfe9680740f467eb89dc66ba0605c075791.jpg)

# Apache Hadoop Ecosystem

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/434111ce576b254e8be1b79994d014dee8fb23d2f48d31006d73fc7f924af5d4.jpg)

# HDFS: Hadoop Distributed File System

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/35bfbc4f9e76345fae832780b34af000a310424c48b8254478c015b091e62932.jpg)

# HDFS : Hadoop Distributed File System

# - Définition-

19

HDFS est un système de fichiers distribué et la couche native de stockage et d'accès à des données d'Hadoop.  
Conçu pour stocker et gérer des fichiers de très grande taille dans un cadre distribué de manière transparente comme s'ils étaient sur le disque dur local.  
HDFS est hautementtolerantaux pannes et concu avec un matériel a faiblecout.  
Pour garantir une tolération aux pannes, les blocs de chaque fichier sont répliqués, de manière intelligente, sur plusieurs machines.

# HDFS : Hadoop Distributed File System

# - Types des noeuds-

2 types de noeuds dans HDFS:

1 seul noeud pour les métá-données : les noms et blocs des fichiers ainsi que leur localisation dans le cluster (un gros annuaire).  
□ plusieurs noeuds pour sauvegarder les données réelles

# Data Node:

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/1ae8cda67c8d442c34ea0827ee14f0e486434d3a4679c717b59df6b9b47c04a8.jpg)

Exemple de configuration du Name Node

Processors: 2 Quad Core CPUs running @ 2 GHz

RAM: 128 GB

Disk: 6 x 1TB SATA

Network: 10 Gigabit Ethernet

# Name Node

Exemple de Configuration du Data Node

Processors: 2 Quad Core CPUs running 4 2 GHz

RAM: 64 GB

Disk: 12-24 x 1TB SATA Network: 10 Gigabit Ethernet

# HDFS: Hadoop Distributed File System

# - Architecture Hadoop 1.0 -

Topologie Maitre-esclave

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/e1776345e8f12839289364fc4e8635e1c07cd407c8a5e09b5c64db961e680211.jpg)  
BigData

# HDFS : Hadoop Distributed File System

# - Types des noeuds-

22

# □ NameNode

Une machine séparée sur lequel tourne un dénom appelé namenode  
Contient des métadonnées, pas de données user,  
Permet de retrouver les nœuds qui hébergent les blocs d'un fichier  
Cordonne l'accès aux données dans le système de fichiers.  
La responsabilité principale d'un Namenode est de stocker le namespace de HDFS :

L'arborescence des repertoires  
- Les permissions des fichiers  
Le mapping des fichiers aux blocs

□ Ces données sont stockées dans deux structures : FsImage et EditLog

NameNode

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/bae5b689b5fa21e45981b7bfaadaa90469ac370b11664fdce16bfb1d9808db77.jpg)

# HDFS : Hadoop Distributed File System

# - Types des noeuds-

- DataNode (nœud de données)

Uen machine sur laquelle tourne un démon esclave  
Il stocke les données réelles.  
Exécutés le demandes de lecture et décriture de bas niveau des clients du système de fichiers.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/5232096ee0ce95f80190c020b63b49fe31dc1e9d692b9b70ef82cd2a3b8e0928.jpg)

Il y a un DataNode pour chaque machine au sein du cluster.  
Les Datanodes sont sous les ordres du Namenode et sont surnommés les Workers (ou esclaves).  
$\Rightarrow$  Ils sont donc sollicités par les Namenodes lors des opérations de lecture et d'écriture!

# HDFS: Hadoop Distributed File System

# - Architecture Hadoop 2.0 -

□ Problème : Trop de charge sur le NameNode  
□ Solution: Ajout du Secondary NameNode: un assistant du NameNode pour réduire sa charge ( Ne le remplace pas)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/de4e383063430694992d2bba34e0e1e62ece72a74f555f6d1d1de34338f42dc6.jpg)

# HDFS: Hadoop Distributed File System

# - Rôle du Secondary Namenode

26

Responsible for accepting jobs from clients

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/c270457d262cf5145fcaee9d1c035dc21b922f84aa644858b959c0ce37361194.jpg)  
Sans Secondary NameNode

# HDFS: Hadoop Distributed File System

# - Rôle du Secondary Namenode-

27

Responsible for accepting jobs from clients

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/200c72e45596cf161b1a87a5bac80e955adf8fea81ec7a7169751a9983fa85bd.jpg)  
Avec Secondary NameNode

# HDFS: Hadoop Distributed File System

# - Rôle du Secondary Namenode-

Ce Nœud supplémentaire appelé Secondary-Namenode a été mis en place dans l'architecture Hadoop version2.  
□ le Secondary NameNode met à jour le fichier fsimage à intervalle régulier en y intégrant le contenu des editlogs.  
Le SecondaryNameNode intervient soit :

$\succ$  lorsquel fichier editlogsatteint une taille prédéfinie.  
à intervalle régulier (par exemple une fois par heures).

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/c0d24524d1080f329bb935f58e40181de521106b36c41d384346d9f46777aa07.jpg)

# HDFS: Hadoop Distributed File System

# - Architecture Hadoop 2.0 -

Problème : Le Namenode est un SPOF (Single Point Of Failure): Si ce service est arrêté, le cluster sera nom disponible!  
□ Solution: Possibilité de développer plusieurs instances du NameNode (un actif et un ou plusieurs StandBy : solution High Availability (HA) mais plus couteuse).

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/26ac3b5328461f768e5d2a8c8b26e1e1a96efa0a2e0420d9264d4bcf85dbebc6.jpg)

# HDFS: Hadoop Distributed File System

# -Décomposition en blocs

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/dedd6606625a3c178482ce00e21f13d3fa8d1142b39e392a58ba4831eed00b88.jpg)

Les fichiers sont physiquement decoupés en blocs d'octets de grande taille (64 Mo:

Hadoop 1.x et 128 Mo (Hadoop 2.x) ) pour optimiser les temps de transfert et d'accès

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/6e03d74583b46a1f03cceddd17a7a5d3479b366f2ad7f2472b6a140dc3b0076f.jpg)

Quand un fjichier mydata.txt est enregistré dans HDFS, il est décomposé en grands blocs chaque bloc ayant un nom unique: blk_1, blk_2...

mydata.txt (150 Mo)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/0efc43c3afa51cb5cf7b3928dfcdb77c17aa914c3860fd065e3bf59d0bbcc7a0.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/0f9497876d15f975d4c068b2279f42bdebe66e3d613bd772e838a61b7ca0cc2d.jpg)

Cluster Hadoop

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/3b638ffac43e1dbb3324813a1af9b574afcec6f4104eafe4ee6cdbb7dac98edd.jpg)

Ces blocs sont ensuite répartis sur plusieurs machines, permettant ainsi de Traitser un même fichier en parallèle.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/399b47e52babc7128d2f1cdda147ec90a4007a74e78d577f04997cd666a00c92.jpg)

Cela permet aussi de ne pas être limité par la capacité de stockage d'une seule machine pour au contraire tirer parti de tout l'espace disponible du cluster de machines ;

# HDFS: Hadoop Distributed File System

# -Réplication des données -

Si l'un des nœuds a un problème, les données seront perdues ?

Hadoop réplique chaque bloc 3 fois (par défaut)  
Le facteur de réplication par défaut peut être ajusté en modifiant la propriété dfs.replication dans le fichier de configuration hdfs-site.xml.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/7a7419c12e8c3b1a4978fab526b3bad955acd8a2703be4011dbb2563ba29ebe7.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/b394a176a8424f8d571ac7fb44c4f2017a8f8298c304748d66df6ff5cc41a430.jpg)

Cluster Hadoop

Si un nœud tombe en panne, les blocs qui y étaient hébergés seront répliqués pour avoir toujours 3 copies stockées.  
Application du concept de Rack-Awareness dans la réplication BigData

# HDFS: Hadoop Distributed File System

# - Principe du Rack Awarness

32

2 copies de chaque bloc se trouvent dans deux nœuds de données distincts du même rack afin de réduire la latence,  
La troisième copie est placée sur un autre rack pour améliorer la redondance et la disponibilité.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/35178b2d7043ed20c2b58aaaa3ec21792953f72c489e5013ff5b9f29f8fa7847.jpg)

Ne jamais perdre toutes les données si tout le rack tombe en panne.  
> Gardez les flux volumineux dans le rack lorsque cela est possible.  
> Répartition basée sur l'hypothèse que dans le rack la bande passante estILA et la latence est faible. BigData

# HDFS: Hadoop Distributed File System

# Ecriture/Lecture d'un fichier

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/f4ebca7321d74a08ef6dac432d5eefa83d7e0fd0c3b7871d281cee458609676f.jpg)  
BigData

# HDFS: Hadoop Distributed File System

# Ecriture/Lecture d'un fichier

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/9d384220-f369-42c5-897c-5612d1122757/e7cb5bd47f54185a1fb4e68638bb11f1bcdc7d1eec14ea11fc09660d3e23c4c4.jpg)

# HDFS: Hadoop Distributed File System

# Ecriture/Lecture d'un fichier

35

□ HDFS suit la philosophie Write Once – Read Many.  
Il n'est pas possible d'editor un fichier existant deja dans HDFS.  
Il est possible d'ajouter en fin de fichier (append)  
□ HDFS s'appuie sur le système de gestion de fichier natif. Sous linux sont ext3 ou ext4 le plus souvent.

# HDFS: Quelques commandes

Il y a deux possibilités pour manipuler HDFS :

> Soit via l'API Java  
$\succ$  Soit directement depuis un terminal via les commandes

$ hdfs dfs <commande hdfs="\" />

$ hadoop fs <commande HDFS>

En particulier, les commandes principales sont :

```txt
hdfs dfs -1s #listing home dir  
hdfs dfs -1s /user #listing user dir...  
hdfs dfs -mv <src><dst> #Moves files from source to destination.  
hdfs dfs -du -h /user #space used  
hdfs dfs -mkdir newdir #creating dir  
hdfs dfs -put myfile.csv . #storing a file on HDFS  
hdfs dfs -get myfile.csv . #getting a file from HDFS  
hdfs dfs -cat myfile.csv . #edit a file from HDFS
```
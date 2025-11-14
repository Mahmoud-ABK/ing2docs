# Institut Supérieur d'Informatique et Mathématiques Monastir

# Cours : Big DATA

# Chapitre 1: Introduction au Big Data

# Objectifs

2

Au terme de ce chapitre, vous serez capable de:

Définir le Big Data  
Définir les 3V  
Donner des exemples d'applications du Big DATA  
Donner des chiffres sur le données massives  
Comprendre la nature de ces données  
Situer les bases de données NOSQL dans le Big Data

# Plan

3

Data: c'est quoi?  
Typologie de données  
Explosion des données  
Définition du Big Data  
□ Les 3V, 4V, 5V  
Applications du Big Data  
$\square$  Big Data et NOSQL

# Data : C'est quoi ?

4

- Les données sont des symboles qui représentent les propriétés des objets et événements.

El n'a pas de sens en elle-même. Elle existe tout simplement.  
C'est la matière première sur laquelle la plupart des informations sont basées.  
Example:

Données:{«Ali»,«Ben Ahmed»,55}  
Information: Données +sens : {Prénom: « Ali », Nom: « Ben Ahmed », age: 55}

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/a3df55d3e7cb6352c333bf94495e83bdae785d27a3f78d1c33671141c3d54e40.jpg)

# Typologie des données

Données qualitatives/quantitatives:  
□ Quantitative: sont des données qui peuvent être mesurées (taille, poids...) ou repérées (température...)  
□Qualitative: sont des données auxquelles on ne peut pas attribuer une valeur ou une caractéristique (la couleur, la texture, le goût, l'odeur).

# Typologie des données

7

Données structurées/Semi-structurées/Non structurées

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/5ef88ed24b690265b5bb42a08f2fa1f67277e272d83cb49a12c3d4951504c1cc.jpg)

# D'ou viennent les données?

8

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/70df2199bffda4251a30d6aab402dd3a7117ce3560dfe0ab2bcdbad4559826b6.jpg)

# D'ou viennent les données?

10

Généralement, ce ne sont pas seulement des données structurées (comme dans les BD traditionnels) normalisées.  
Ce sont des données semi ou non structurées:

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/08bea525ee7569a61ef99216103cdd7e356b63fb94dde191b51c296b69f9a01c.jpg)

Tweets

$\square$  Logs des serveurs

Pages web

- Objects connectés

Fichiers CSV, JSON, etc. volumieux

{"hashtags": {"text":"TulsaAirport", "indices": [0,13]}, {"text":"Oklahoma", "indices": [14,23]}, "trends": [], "urls": ["url":"http://V/t.co/SnC8ST3gQC", "expanded_url":"http://V/bit.ly/188eNcw", "display_url":"bit.ly/V188eNcw", "indices": [93,115]}, "user Mentions": [], "symbols": [], "favorited":false,"retweeted":false,"possibly sensitive":false,"filter level":"low","lang":"en", "timestamp ms":"1421853664710"} {"created at":"WedJan 21 15:2T:04 +0000 2015", "id": 557920823877464064,"id str":"557920823877464064", "text":"An imeepisode updated: Kyoukaino Kanata: Mini Theater # 6 ( http://V/t.co/KjEPWveEHM)

# Explosion des données

13

Il n'y avait que 130 exaocets de données dans l'univers numérique en 2005.  
Il devrait y en avoir plus de 40 000 exaoctets à l'horizon 2020.  
En 2020, les données représentent l'équivalent de plus de 5 000 GO par

personne!

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/d8165889ea590767290cb4c3ac6d2262523779f02b2590350c09b0e54438d179.jpg)

# Explosion des données

14

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/d33e783a25b5adf55573d7fba403332dea3cdd3fc612d05c6d071fabb31e9c39.jpg)

# Encore des chiffres

15

□ Volumes de données estimées:

Google: 15000PB (=15 Exabytes)  
Facebook: 300PB  
Ebay: 90PB

90% of the data in the world today has been created in the last two years alone.

- IBM

□ Volumes de données par jour:

Google: 100 PB (5 milliards de requêtes par jour)  
Twitter: 100 TB (>200 millions de tweets par jour)  
Facebook: 600 TB

# Big Data: C'est quoi donc?

16

En français: Mégadonnées, Données massives  
C'est donc le volume de données??

Réponse: Non.  
Il n'y a pas que la dimension volume

□ Le Big Data représenté les collections de données caractérisées par un volume, une velocité et une variété si grands que leur transformation en valeur utilisable requiert l'utilisation de technologies et de méthodes analytiques spécifique. (d'après Gartner)

# Big data : 3V, 4V, 5V, ?V

18

□ 3V: Volume,

Variety, Velocity.

□ 4V: Volume,

Variety, Velocity, Value.

□ 5V: Volume,

Variety, Velocity,

Value, Veracity.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/931fa5991a53eb91037b0d0e9e684105862b36b896f25f729bac73becdb0980d.jpg)  
http://www.astosurf.com/luxorion/big-data-mining.htm

# Entreprise et Big Data

28

Big Data = Transactions + Interactions + Observations

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/1c09d6fc1d4dc9eb8c0fa751bef4c4d386b9657127b17ca67dcea78da54b2e01.jpg)

Increasing Data Variety and Complexity

# Entreprise et Big Data

# -Data Lake-

29

# Forget data warehousing, it's 'data lakes' now

Digital News Asia Mar 31, 2015

- Data Lakes becoming corporate priority because they fill a critical gap  
- Federation Business Data Lake simplifies complex task of building a data lake: EMC

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/6d26f906050c0b0562b831b004ecb3190d268633b8db9f69ae8a1db63f6974d6.jpg)  
BigData

# Entreprise et Big Data

# -Data Lake-

30

- Un data lake est un emplacement de stockage centralisé qui contient des big data sous un format brut et granulaire provenant d'un grand nombre de source.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/6ed8f5bdc12ca7eb8d24084a6904d78490ebc537889fe97c6a844fe17cada733.jpg)

# Applications du Big Data: Pour qui, pour quoi?

36

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/775c4546f114a2a1b03679aab9ef0d2c7818872f302282c6f2121ff062f2500c.jpg)  
La relation client avant tout, puis l'efficacité des processus et l'innovation

# Examples d'applications

37

Crowdsourcing  
![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/ed0bf8144c8a19e59e8b28efe1475f65486c9ffabb11a35f338bee4c9a356240.jpg)  
Realtimetrafficinfo

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/64e55320e7ef1fd91495528797ff8581ab8c2d1457216de81e29aed6725002e7.jpg)  
Sensing

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/fe11450df82bc9bad3cbdb67bc06bbf3e2c6cac0c2628a7ad85b34512189e0b7.jpg)  
Map data

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/78c2068887f53ca480c0a7bafad73fd96b2b064476b2a7598edd207d905869fe.jpg)

Computing  
![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/9cde8dd890a43677181642c542c691851cfdb6133faeabc0726143e638abad5a.jpg)  
Traveltime forecast/nowcast

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/b12e04edfd5d4b315d1f2ba29e839bd6598dca2b01ff637ad99bd4d8f17399f9.jpg)

# Examples d'applications

40

□ Recommendations basées sur les données utilisateur:

□ « There are 33 million different versions of Netflix. » (Joris Evers)  
75% des videos regardées viennent des suggestions de Netflix à ses utilisateurs.

□ Le Big Data a motivé l'achat des droits (pour 100 million US$) et le tournée de la série House of Cards (popularité de séries similaires,CHOIX du producteur, du réalisteur, des acteurs).

Bandeannounce personalisée en fonction du type d'utilisateur.  
House of Cards a amené 2 millions de nouveaux utilisateurs aux USA et 1 million en dehors des USA.

# NETFLIX

# Examples d'applications

41

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/8c1b325d3fd7809c5c32df31f75a722726b475845fd43a684ed67f6fd8f532a6.jpg)

PREDPOL

PredPol= « Predictive Policing »

□ prédire la probabilité des crimes et déliits (nature, localisation à quelques centaines de metres près, timing à 12h après)  
□ base d'apprentissage de 13 millions d'événements  
Los Angeles: diminution de  $33\%$  des agressions  
Santa Cruz : diminution de  $27 \%$ des cambriolages en moins d'un an.

D'autres applications:

Fraude (detection / prevention),  
Education, santé,  
Génomique,  
etc...

# Pipeline des données

42

- Système d'acheminement des données d'un point A vers un point B.  
Mis en place par un Data-Engineer.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/895f1bfc7287da28d9e71671e4b03e5a19992b225d64e5151ebd68dbe7e31669.jpg)

# Challenges du Big Data

43

- On s'intéresse dans ce cours à deux challenges: traitement des données et stockage.  
□ Traitement:

- Paralleliser le calcul sur les machines  
□ Framework de traitement distribuée (Hadoop /Spark)

Stockage:

Système de fichiers distribué  
Bases de données (relationnel/NoSQL) distribués

# NOSQL: C'est quoi?

45

- Nom exact: Bases de données non relationnelles.  
Privilégier NOSQL plutôt que NoSQL.  
Ce n'est pas du relationnel, et le contexte d'utilisation n'est donc pas ce lui désigné SGBDR.  
Ce n'est pas seulement l'opposition à SQL :  
ce lui dlesiona

- il s'agit de compléments aux SGBDR pour des besoines spécifique et non de solutions de remplacement.  
- experimentations, autres modèles de données très simples, nouveaux besoin, nouveaux outils!  
logiciels de stockage de données plutot que SGBD

# NOSQL: C'est quoi?

46

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/e990f2c979059fdef61cfd88151c9d2583d36fed85676b4dde0c041e2807307f.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/770807ede80c31f562b219e38e965b20b0246a4cf5a0a8d1ed45fad6db5bdec9.jpg)

"The whole point of seeking alternatives [to RDBMS systems] is that you need to solve a problem that relational databases are a bad fit for."

Eric Evans Rackspace

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/4526d154e2a1ade8333aff9c7de9f42fa8dfeaf3c283c8d91c1db565d65fc6dd.jpg)

- Un couple de concepteurs de bases de données entre dans un restaurant NoSQL. Une heures après, ils dessortent sans avoir réussi à manger.

Pourquoi?

# Types des bases NOSQL

4 types de bases NOSQL

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/fef56145933efe86f2a2cc20620c1bae14d3e4fd72dd1594c656420fb1190583.jpg)  
Key Value

Example:  
Riak, Tokyo Cabinet, Redis server, Memcached, Scalars

Clé valeur

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/634e4a754fb8fbfbf311a38b1ccf78429ce13d334fc9cdca2a0edd4cf949288e.jpg)  
Document-Based

Example:  
MongoDB, CouchDB, OrientDB, RavenDB

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/77c663a8bfcf6a0af2e844c951693d6ea838ad3d41a4139ec996a6415cf18a9b.jpg)  
Column-Based

Example:  
BigTable, Cassandra, Hbase, Hypertable

Orienté colonne

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/d0629169c9162a57bc7971bd2c18b6a646135a6f9e444fa35831ca9732f38743.jpg)  
Graph-Based

Example: Neo4J, InfoGrid, Infinite Graph, Flock DB

Orienté graphe

# Big Data et NOSQL

- Les bases de données NoSQL sont des outils Big Data qui permettent de stocker et récapérer de très gross volumes de données.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/23c5a56762dfb2fac371beb68c1e0f9d2a7ff0ed853c0e757e6bf6e0155462a5.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/ec9f9eb0-5714-49cc-9500-4f448be564ba/b4d3e456096381e37fba9d1a440c789b12861f8c62fb58566674651bc10eb932.jpg)

# Références

49

Laurent Jolia-Ferrier, Big Data - Concepts et mise en œuvre de Hadoop, Ed Eni, 2014.  
□ Pirmin Lemberger et al., Big Data et Machine Learning -Les concepts et les outils de la data science, Ed, Dunod, 2016.  
P. Lacomme, S. Aridhi, R. Phan, Bases de données NoSQL et Big Data: Concevoir des bases de données pour le Big Data, Cours et travaux pratiques Ellipses ~ Technosup, 2/12/2014, 336 p., 9782340002616.  
Rudi Bruchez, L. Les bases de données NoSQL et le Big Data: Compendre etMETRE en œuvre, Ed. Eyrolles, 2015.  
Cours Bases de données NOSQL de Raja CHIKY, Institut Mines Télecom: http://perso.isep.fr/rchiky/  
Cours Big Data et NoSQL de Lilia Sfaxi, INSAT, Tunisia: http://liliasfaxi.wixsite.com/liliasfaxi  
https://chewbii.com/  
Chaine Youtube Tech Wall, playlist Hadoop&cie.

50

Fin
72

# Gestion de Ressources d'Hadoop

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/64f3603746a7f083804f20fd7a19192fbbfbf9f0118c8b0a2853dde72da1034b.jpg)

# Hadoop MapReduce: Limits

Le Job Tracker s'exécute sur une seule machine, et fait plusieurs tâches (gestion de ressources, ordonnancement et monitoring des tâches...);  
Problème de scalabilité et de goulot d'étranglement : les nombreux datanodes existants ne sont pas exploités: max de 5000 noeuds et 40,000 tasks s'execuant simultanément (Yahoo).  
Si le Job Tracker tombe en panne, tous les jobs doivent redémarrer;  
Problème de disponibilité: SPoF (single point of failure)  
Le nombre de map slots et de reduce slots est prédéfini:  
Problème d'exploitation: si on a plusieurs map jobs à executer, et que les map slots sont pleins, les reduce slots ne peuvent pas être utilisés, et vice-versa.  
Le Job Tracker est fortement intégré à Map Reduce!  
Problème d'interoperabilité: impossible d'exécuter des applications non-MR sur HDFS BigData

# Solution: Hadoop 2.0

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/0b0841e3dce49238617940f79e6de654f2fbbe0a2e8809780e12d1cf7b1b1e45.jpg)

Hadoop v1.0

MapReduce

Data Processing

& Resource Management

HDFS

Distributed File Storage

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/e39f56b353942fcf101ac5ba4bae041dbc0b08651d89fcf437bcf1c18f7067ef.jpg)

Hadoop v2.0

MapReduce

Other Data

Processing

Frameworks

YARN

Resource Management

HDFS

Distributed File Storage

# YARN: C'est quoi?

Yarn: Yet Another Resource Negotiator.  
- Un framework permettant d'exécuter n'importe quel type d/application distribuée sur un cluster Hadoop, pas uniquement les applications MapReduce.  
Pas de notion de slots: Les nœuds ont des ressources (CPU, mémoire...) allouées aux applications à la demande.  
Idée clé: Séparer la gestion des ressources de celle des tâches MR.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/2235923e72ae295e4a6a0f5e21898a7318d256e8fbf1dd84571ec3b126f8d638.jpg)  
BigData

# YARN- Les démons

Resource Manager (RM)

Tournesur un nœud master  
Ordonnanceur global des ressources  
Permet l'arbitrage des ressources entre plusieurs applications.

Node Manager (NM)

S'exécutesurlesnœudsslaves  
□ Communique avec RM

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/1e1907c0bea11e0b4e12347a657945d89394fd5e200c6fcd41d1e4a7dc45607d.jpg)

NodeManager

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/7bb8df70cfa8fc31b41b4136db364823812fca12b143915e44c3c59aba2b88fd.jpg)

NodeManager

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/da49738290e0413e03f93874711240694a4536d76971c844d9e0bb1bb405a6ac.jpg)

# YARN- Les démons

# □ Containers

□ Crées par le RM à la demande  
Se voit allouer des ressources ( mémoire, CPU) sur le noeud slave: Il n'y a plus de slots prédéfinis.  
Les applications tournent sur un ou plusieurs containers.

# Application Master (AM)

Un seul par application  
S'exécutesur un container  
□Demande plusieurs containers pour executer les tâches d'applications.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/2da9f7a6af15ea0c0c211ceb5bca48e166adc3f288ed02e925e06961b187c7f3.jpg)

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/3ba83cbdef166f351dc36c224e3cacbdb02311995e9a7d2c327c857866aa9e36.jpg)

# YARN- Fonctionnement

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/231335d7fb29c99420dff5b79d61061ba05a88582addd325453b730f73f52bb7.jpg)

# Cluster YARN: Execution d'une application

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/9ef20ad4927b226f63af2de49f72696b82b9bea7e6196df063a76b83a921be54.jpg)  
BigData

# Cluster YARN: Execution d'une application

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/73b913a8fc7ad295b7da425fe58338fe7b1bead94f8b3e6829d6dcbb9a1f6c0f.jpg)  
BigData

# Cluster YARN: Execution d'une application

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/19115b52bdcd213b941d246f8c1678531a5cdcb566be046ad84cdb824da75119.jpg)

# Cluster YARN: Exécution d'une application

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/29eb66a550607ee6bf93b8b0edbf7c54bdde82d96ed577607dd973dbaa5fd81c.jpg)  
BigData

# Cluster YARN: Exécution d'une application

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/4fda53aafe78a6977cf04fb5882c3bd7a6589755cad73bd2c9bee7298d76fa42.jpg)  
BigData

# YARN et Map-Reduce v2

Yarn ne sait pas quel type d'application s'exécut: peut être MR ou autres applications non-MR comme:

Distributed Shell  
Impala  
Apache Giraph  
Spark  
Autres : https://cwiki.apache.org/confluence/display/HADOOP2/PoweredByYarn

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/0a98fc538f99eca79f2cc387327ee18dd2f7810ed8872a476315f6bcfbcfae9b.jpg)

# YARN et Map-Reduce v2

# □ MR2: C'est quoi?

Avec Yarn, il n'y a plus de l'unique JobTracker pour executer les jobs et des taskTracker pour executer les tasks des jobs.  
L'ancienne version MRv1 a eté écrit pour s'adapter avec YARN et a eté appelée MRv2.

$\square$  MR2 utilise Hadoop:

Hadoop inclus un MRAppMaster (MapReduce ApplicationMaster) pour gérer les jobs MR.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/8ca026ad67c328b7916feda1decb1e3827327dc748c6ef86e2a7b5e73d16a48d.jpg)

# Cluster YARN: Execution d'un job Map-Reduce

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/ba9d002942d458c5a5860bb6446e2d5a9fd136935eba6d7532af7a468a451152.jpg)  
BigData

# Cluster YARN: Execution d'un job Map-Reduce

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/e4b7c9444f47f7a1874e67cb551438fc90a0dfe91f350d807203c330dbc184bd.jpg)  
BigData

# Cluster YARN: Execution d'un job Map-Reduce

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/54741f60786d2bd5c556646cf3aa10ba89f949ed25d20e0fcf1c2ed7f1fc3ca0.jpg)  
BigData

# Cluster YARN: Execution d'un job Map-Reduce

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/7049b7b393a7080f943e078af36b1ded8a0ca2dd976d59c695c7a2a4bcbbf4b5.jpg)  
BigData

# Cluster YARN: Execution d'un job Map-Reduce

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/06ad9807bd5d20df653c443bc0851ca84fce67d207349af2959f14582162146e.jpg)  
BigData

# Cluster YARN: Execution d'un job Map-Reduce

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/62dac044f194c63a0be9b013875e78ae38507c9d36adc1d884210b5c55e1d98a.jpg)  
BigData

# Cluster YARN: Execution d'un job Map-Reduce

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/7c1c4ba61fd910aee19e4d08ee76efe79a00a2b46e357063cdedd7cb0fb5986c.jpg)  
BigData

# Cluster YARN: Execution d'un job Map-Reduce

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/9ef94851161fff9d9fd7e486cef5a187e45ad1cfc8f61be430f524265d113bc8.jpg)  
BigData

# Cluster YARN: Execution d'un job Map-Reduce

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/94e122f9e6da3ac7fd96a3568205b42c9c323d7a8bd88542e85cb1c10a8ce7ca.jpg)  
BigData

# Cluster YARN: Execution d'un job Map-Reduce

□ dans Yarn, Shuffle s'exécutecome un service auxiliaire

Il s'execute dans le NodeManager JVM comme un service

persistent.

![](https://cdn-mineru.openxlab.org.cn/result/2025-11-15/abbb9208-654e-4101-b3bc-9dce0a56b3a0/8280fed8bc8e336f5429a9e1fb84d4a8d7a2bf9e7bd849c41aea214fcbe304e8.jpg)
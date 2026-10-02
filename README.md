# 🤖 Robot Mobile — Détection d'obstacles avec YOLOv8

## Présentation

Projet de conception d'un système de détection d'obstacles en temps réel pour un véhicule autonome, basé sur le modèle de Deep Learning **YOLOv8**.

Le système a pour objectif d'identifier et de localiser les objets présents dans l'environnement de conduite à partir d'une caméra.

## Objectifs

- Détecter les obstacles dans l'environnement.
- Identifier les objets détectés.
- Localiser les objets dans l'image.
- Fournir des informations utiles à la navigation autonome.
- Préparer l'intégration avec un robot mobile.

## Technologies

- Python
- YOLOv8 / Ultralytics
- OpenCV
- Deep Learning
- Computer Vision
- Robotique mobile

## Architecture

```text
Caméra
   ↓
Acquisition de l'image
   ↓
YOLOv8
   ↓
Détection des objets
   ↓
Identification + localisation
   ↓
Analyse de l'environnement
   ↓
Prise de décision
   ↓
Robot mobile
```

## Code représentatif

Le fichier `src/detection.py` présente un exemple simple du principe de détection avec YOLOv8. Il s'agit d'un prototype documentaire destiné à illustrer l'étape logicielle.

## Étapes du projet

### 1. Acquisition
Utiliser une caméra pour récupérer des images de l'environnement.

### 2. Détection
Transmettre les images au modèle YOLOv8.

### 3. Identification
Le modèle identifie les catégories d'objets détectés.

### 4. Localisation
Les boîtes englobantes permettent de localiser les objets dans l'image.

### 5. Décision
Les informations de perception peuvent être utilisées par le système de navigation du robot.

### 6. Intégration
Prévoir l'intégration avec les moteurs, capteurs et contrôleur du robot mobile.

## Informations clés

**Entrée :** image ou flux vidéo de la caméra  
**Traitement :** modèle YOLOv8  
**Sortie :** objets détectés, classes et positions  
**Application :** robot mobile / véhicule autonome

## Perspectives

- Ajouter une caméra embarquée.
- Ajouter des capteurs ultrasoniques ou LiDAR.
- Mettre en place l'évitement automatique des obstacles.
- Contrôler les moteurs du robot.
- Ajouter la navigation autonome.
- Créer un jeu de données adapté à l'environnement ciblé.
- Adapter le modèle pour des situations spécifiques.

## Auteur

**Modeste LOKO**

Projet orienté Intelligence Artificielle, Computer Vision et Robotique.

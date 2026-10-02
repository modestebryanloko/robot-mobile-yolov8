# Architecture du système

## Chaîne principale

```text
[Caméra]
    |
    v
[Images de l'environnement]
    |
    v
[YOLOv8]
    |
    +--> Classe de l'objet
    |
    +--> Confiance
    |
    +--> Position / boîte englobante
    |
    v
[Analyse]
    |
    v
[Décision]
    |
    v
[Robot mobile]
```

## Rôle des composants

### Caméra
Capture l'environnement devant le robot.

### YOLOv8
Analyse les images et détecte les objets.

### Module d'analyse
Interprète les résultats de détection afin de fournir des informations exploitables.

### Robot mobile
Utilise les informations de perception pour adapter son déplacement.

## Résultat attendu

À terme, le système doit permettre au robot de percevoir son environnement et d'utiliser cette perception pour contribuer à une navigation autonome.

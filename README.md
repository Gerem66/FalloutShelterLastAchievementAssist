# 🏠 FalloutShelterLastAchievementAssist

Un assistant d'automatisation pour Fallout Shelter visant à faciliter l'obtention du dernier succès du jeu :

> Avoir 20 habitants légendaires dans l'abri.

Cet assistant permet d'obtenir le succès en farmant les 300~500 boîtes nécessaires en quelques dizaines de minutes / heures, ce qui aurais normalement dû coûter au choix :
- Plusieurs centaines d'euros en achats in-app
- Plusieurs mois de connexion quotidienne

## 🎯 Objectif

Ce projet permet d'automatiser les tâches répétitives dans l'obtention des résidents légendaires, notamment avec :
- La génération infinie de boîtes à butin (loot boxes)
  - Avec gestion automatique de la date système pour exploiter les mécaniques temporelles du jeu
- L'ouverture automatique de ces boîtes

## 📁 Structure du projet

```
├── test.py                   # Script de test interactif
├── farm_box.py               # Script principal - génération de boîtes
├── open_box.py               # Script principal - ouverture de boîtes
├── requirements.txt          # Dépendances Python
├── README.md                 # Documentation
└── src/
    ├── mouse.py             # Module de contrôle de la souris
    ├── date_manager.py      # Module de gestion de la date système
    └── tests.py             # Tests unitaires
```

## 🚀 Scripts principaux

### 0. `test.py` - Tests et débogage
Script interactif pour tester les fonctionnalités indépendamment :
- **Test 1** : Capture de position de souris
- **Test 2** : Test de clic automatique
- **Test 3** : Test d'ajout d'une semaine à la date
- **Test 4** : Test de restauration automatique de la date

```bash
python3 test.py
```

### 1. `farm_box.py` - Génération de boîtes infinies
Script principal qui automatise la génération de boîtes à butin dans Fallout Shelter :
- Manipule la date système pour avancer d'une semaine
- Ouvre Fallout Shelter
- Collecte les 7 loots quotidiens
- Ferme le jeu et restaure la date
- Répète le processus indéfiniment

```bash
python3 farm_box.py
```

### 2. `open_box.py` - Ouverture de boîtes infinies
Script pour ouvrir automatiquement les boîtes à butin accumulées :
- Clique continuellement sur le bouton d'ouverture de boîte
- Permet de traiter rapidement de grandes quantités de boîtes

```bash
python3 open_box.py
```

## 🔧 Installation

### Prérequis
- Python 3.7+
- Système Windows (pour la gestion de date)
- Fallout Shelter installé
- Accès aux permissions système pour modifier la date

### Installation des dépendances
```bash
pip install -r requirements.txt
```

### Dépendances principales
- `pyautogui` : Contrôle de la souris et du clavier
- `pynput` : Capture d'événements système

## ⚙️ Configuration

### Positions de souris
Les coordonnées sont prédéfinies dans les scripts pour une résolution spécifique. Vous devrez peut-être les ajuster selon votre configuration :

**Dans `farm_box.py` :**
```python
fallout_icon = [1245, 1056]           # Icône Fallout Shelter dans la barre des tâches
fallout_first_loot = [369, 617]       # Emplacement du premier loot
fallout_loot_padding = [90, 0]        # Espacement entre loots
fallout_loot_popup_close = [992, 185] # Bouton pour fermer popup
```

**Dans `open_box.py` :**
```python
fallout_open_box = [785, 452]         # Bouton d'ouverture de boîte (au centre de la zone de loot)
```

### Calibrage des positions
Utilisez `test.py` option 1 pour capturer les positions exactes sur votre écran.

## 🎮 Utilisation

### Étape 1 : Test et calibrage
```bash
python3 test.py
```
Testez chaque fonctionnalité et ajustez les coordonnées si nécessaire.

### Étape 2 : Génération de boîtes
```bash
python3 farm_box.py
```
Laissez le script tourner pour accumuler des boîtes à butin.

### Étape 3 : Ouverture des boîtes
```bash
python3 open_box.py
```
Ouvrez toutes les boîtes accumulées automatiquement.

## ⚠️ Précautions

- **Sauvegardez votre progression** avant d'utiliser ces scripts
- **Testez d'abord** avec le script de test
- **Surveillez le processus** - arrêtez avec `Ctrl+C` si nécessaire
- **Vérifiez les positions** - elles peuvent varier selon la résolution d'écran
- **Attention aux ToS** - vérifiez que l'automatisation est autorisée

## 📜 Licence

Ce projet est fourni "tel quel" à des fins éducatives. Utilisez-le de manière responsable et conformément aux conditions d'utilisation de Fallout Shelter.

---

**Note :** Ce projet a été créé pour faciliter l'obtention des derniers achievements de Fallout Shelter. Utilisez-le de manière responsable et à vos propres risques.

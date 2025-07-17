#!/usr/bin/env python3
"""
Script de test pour les fonctionnalités du projet FalloutShelter.
Menu interactif pour tester les différentes fonctions disponibles.
"""

from time import sleep
from src.mouse import click, wait_for_click
from src.date_manager import set_automatic_time, set_manual_time_plus_one_week, get_current_system_time

def test_get_pos():
    """Test de la fonction de capture de position de souris"""
    print("🖱️  === TEST CAPTURE POSITION SOURIS ===")
    print("Cliquez n'importe où pour capturer la position...")
    result = wait_for_click()
    if result:
        x, y = result
        print(f"✅ Position capturée: ({x}, {y})")
    else:
        print("❌ Aucune position capturée")
    print()

def test_click():
    """Test de la fonction de clic automatique"""
    print("🔄 === TEST CLIC AUTOMATIQUE ===")
    print("Le script va cliquer au centre de l'écran dans 3 secondes...")
    for i in range(3, 0, -1):
        print(f"⏳ {i}...")
        sleep(1)
    
    # Cliquer au centre approximatif d'un écran 1920x1080
    click(992, 186)
    sleep(0.1)
    click(992, 186)
    print("✅ Test de clic terminé")
    print()

def test_add_week():
    """Test d'ajout d'une semaine à la date système"""
    print("📅 === TEST AJOUTER UNE SEMAINE ===")
    print("Heure actuelle:")
    get_current_system_time()
    print()
    if set_manual_time_plus_one_week():
        print("✅ Date modifiée avec succès")
        print("Nouvelle heure:")
        get_current_system_time()
    else:
        print("❌ Échec de la modification de date")
    print()

def test_auto_time():
    """Test de restauration de l'heure automatique"""
    print("🔄 === TEST RESTAURATION AUTOMATIQUE ===")
    print("Heure avant restauration:")
    get_current_system_time()
    print()
    
    if set_automatic_time():
        print("✅ Synchronisation automatique restaurée")
        sleep(2)  # Attendre la synchronisation
        print("Heure après restauration:")
        get_current_system_time()
    else:
        print("❌ Échec de la restauration automatique")
    print()

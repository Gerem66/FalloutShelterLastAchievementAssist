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

def show_menu():
    """Affiche le menu principal"""
    print("🎯 === MENU DE TESTS ===")
    print("1. Tester 'get_pos' (capture position souris)")
    print("2. Tester 'click' (clic automatique)")
    print("3. Tester 'ajouter une semaine' (modifier date)")
    print("4. Tester 'Rétablir automatique' (restaurer date)")
    print("0. Quitter")
    print()

def main():
    """Fonction principale avec menu interactif"""
    while True:
        show_menu()
        try:
            choice = input("Votre choix (1-4, 0 pour quitter): ").strip()
            print()
            
            if choice == '0':
                print("👋 Au revoir !")
                break
            elif choice == '1':
                test_get_pos()
            elif choice == '2':
                test_click()
            elif choice == '3':
                test_add_week()
            elif choice == '4':
                test_auto_time()
            else:
                print("❌ Choix invalide. Veuillez entrer un nombre entre 1 et 4 (ou 0 pour quitter).")
                print()
                
        except KeyboardInterrupt:
            print("\n❌ Interruption par l'utilisateur")
            break
        except Exception as e:
            print(f"❌ Erreur: {e}")
            print()

if __name__ == "__main__":
    main()

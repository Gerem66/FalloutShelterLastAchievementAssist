#!/usr/bin/env python3
"""
Script de test pour les fonctionnalités du projet FalloutShelter.
Menu interactif pour tester les différentes fonctions disponibles.
"""

from src.tests import test_get_pos, test_click, test_add_week, test_auto_time

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

        # Demande de saisie utilisateur
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

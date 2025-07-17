#!/usr/bin/env python3
"""
Script de démonstration et de test pour les détecteurs de clics.
Permet de tester les deux versions et de comparer leurs performances.
"""

import sys
import os
import importlib.util

def load_module_from_file(module_name, file_path):
    """Charge un module Python depuis un fichier"""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def test_pyautogui_version():
    """Test de la version pyautogui"""
    print("🔍 Test de la version pyautogui...")
    try:
        detector = load_module_from_file("detector", "./mouse_click_detector.py")
        position = detector.get_mouse_click_position()
        if position:
            print(f"✅ pyautogui: Position capturée: {position}")
            return True
        else:
            print("❌ pyautogui: Aucune position capturée")
            return False
    except Exception as e:
        print(f"❌ pyautogui: Erreur - {e}")
        return False

def test_pynput_version():
    """Test de la version pynput"""
    print("🔍 Test de la version pynput...")
    try:
        detector_pynput = load_module_from_file("detector_pynput", "./mouse_click_detector_pynput.py")
        listener = detector_pynput.MouseClickListener()
        position = listener.wait_for_click()
        if position:
            print(f"✅ pynput: Position capturée: {position}")
            return True
        else:
            print("❌ pynput: Aucune position capturée")
            return False
    except Exception as e:
        print(f"❌ pynput: Erreur - {e}")
        return False

def check_dependencies():
    """Vérifie que les dépendances sont installées"""
    print("🔧 Vérification des dépendances...\n")
    
    dependencies = {
        'pyautogui': 'pyautogui',
        'pynput': 'pynput'
    }
    
    missing = []
    for name, module in dependencies.items():
        try:
            __import__(module)
            print(f"✅ {name} est installé")
        except ImportError:
            print(f"❌ {name} n'est pas installé")
            missing.append(module)
    
    if missing:
        print(f"\n📦 Pour installer les dépendances manquantes :")
        print(f"pip install {' '.join(missing)}")
        return False
    
    print("✅ Toutes les dépendances sont installées !\n")
    return True

def interactive_menu():
    """Menu interactif pour choisir le test à effectuer"""
    while True:
        print("\n" + "="*50)
        print("🖱️  Menu de Test des Détecteurs de Clics")
        print("="*50)
        print("1. Tester la version pyautogui")
        print("2. Tester la version pynput")
        print("3. Comparer les deux versions")
        print("4. Vérifier les dépendances")
        print("5. Quitter")
        print("="*50)
        
        try:
            choice = input("Choisissez une option (1-5): ").strip()
            
            if choice == '1':
                test_pyautogui_version()
            elif choice == '2':
                test_pynput_version()
            elif choice == '3':
                print("\n🔄 Comparaison des deux versions...")
                print("Première version: pyautogui")
                result1 = test_pyautogui_version()
                
                print("\nDeuxième version: pynput")
                result2 = test_pynput_version()
                
                print(f"\n📊 Résultats:")
                print(f"pyautogui: {'✅ Réussi' if result1 else '❌ Échec'}")
                print(f"pynput: {'✅ Réussi' if result2 else '❌ Échec'}")
                
            elif choice == '4':
                check_dependencies()
            elif choice == '5':
                print("👋 Au revoir !")
                break
            else:
                print("❌ Option invalide. Choisissez entre 1 et 5.")
                
        except KeyboardInterrupt:
            print("\n👋 Au revoir !")
            break
        except Exception as e:
            print(f"❌ Erreur: {e}")

def main():
    """Fonction principale"""
    print("🖱️ Testeur de Détecteurs de Clics de Souris")
    print("=" * 45)
    
    # Vérification initiale des dépendances
    if not check_dependencies():
        print("⚠️  Certaines dépendances sont manquantes.")
        install = input("Voulez-vous les installer maintenant ? (o/N): ").lower().startswith('o')
        if install:
            os.system("pip install -r requirements.txt")
            check_dependencies()
    
    # Lancement du menu interactif
    interactive_menu()

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Menu principal pour choisir le détecteur de clics approprié
selon l'environnement et les permissions disponibles.
"""

import os
import sys
import subprocess

def check_display():
    """Vérifie si un affichage graphique est disponible"""
    return os.environ.get('DISPLAY') is not None

def check_x11_access():
    """Vérifie si X11 est accessible"""
    try:
        import subprocess
        result = subprocess.run(['xauth', 'list'], 
                              capture_output=True, 
                              text=True, 
                              timeout=5)
        return result.returncode == 0
    except:
        return False

def test_pyautogui():
    """Test si pyautogui fonctionne"""
    try:
        import pyautogui
        # Test basique sans interface
        return True
    except Exception as e:
        return False, str(e)

def test_pynput():
    """Test si pynput fonctionne"""
    try:
        from pynput.mouse import Listener
        return True
    except Exception as e:
        return False, str(e)

def show_system_info():
    """Affiche les informations système"""
    print("📊 Informations Système")
    print("=" * 25)
    
    # Affichage
    display = os.environ.get('DISPLAY', 'Non défini')
    print(f"DISPLAY: {display}")
    
    # Session
    session = os.environ.get('XDG_SESSION_TYPE', 'Inconnu')
    print(f"Type de session: {session}")
    
    # X11
    x11_ok = check_x11_access()
    print(f"Accès X11: {'✅ OK' if x11_ok else '❌ Non accessible'}")
    
    # Tests des modules
    print(f"\n🐍 Modules Python:")
    
    pyautogui_result = test_pyautogui()
    if isinstance(pyautogui_result, tuple):
        print(f"pyautogui: ❌ {pyautogui_result[1]}")
    else:
        print(f"pyautogui: ✅ OK")
    
    pynput_result = test_pynput()
    if isinstance(pynput_result, tuple):
        print(f"pynput: ❌ {pynput_result[1]}")
    else:
        print(f"pynput: ✅ OK")

def run_script(script_name):
    """Lance un script Python"""
    try:
        print(f"🚀 Lancement de {script_name}...")
        print("=" * 40)
        subprocess.run([sys.executable, script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de l'exécution: {e}")
    except KeyboardInterrupt:
        print("\n👋 Script interrompu par l'utilisateur")
    except FileNotFoundError:
        print(f"❌ Script {script_name} non trouvé")

def show_recommendations():
    """Affiche les recommandations selon l'environnement"""
    print("\n💡 Recommandations:")
    print("=" * 20)
    
    has_display = check_display()
    x11_ok = check_x11_access()
    
    if not has_display:
        print("🖥️  Mode console détecté")
        print("   → Utilisez: simple_mouse_detector.py")
        print("   → Ou avec sudo pour plus de permissions")
    elif not x11_ok:
        print("🔐 Problème d'accès X11")
        print("   → Lancez: ./fix_x11.sh pour les solutions")
        print("   → Ou utilisez: simple_mouse_detector.py")
    else:
        print("✅ Environnement graphique OK")
        print("   → Tous les scripts devraient fonctionner")

def main_menu():
    """Menu principal interactif"""
    while True:
        print("\n" + "="*50)
        print("🖱️  Menu Principal - Détecteurs de Clics")
        print("="*50)
        
        print("1. Informations système")
        print("2. Version pyautogui (basique)")
        print("3. Version pynput (avancée)")
        print("4. Version simple (sans X11)")
        print("5. Script de test/comparaison")
        print("6. Corriger les problèmes X11")
        print("7. Recommandations")
        print("8. Quitter")
        print("="*50)
        
        try:
            choice = input("Choisissez une option (1-8): ").strip()
            
            if choice == '1':
                show_system_info()
                
            elif choice == '2':
                if test_pyautogui():
                    run_script('mouse_click_detector.py')
                else:
                    print("❌ pyautogui ne fonctionne pas dans cet environnement")
                    print("💡 Essayez l'option 4 (version simple)")
                    
            elif choice == '3':
                if test_pynput():
                    run_script('mouse_click_detector_pynput.py')
                else:
                    print("❌ pynput ne fonctionne pas dans cet environnement")
                    print("💡 Essayez l'option 4 (version simple)")
                    
            elif choice == '4':
                run_script('simple_mouse_detector.py')
                
            elif choice == '5':
                run_script('test_detectors.py')
                
            elif choice == '6':
                print("🔧 Lancement du script de correction...")
                try:
                    subprocess.run(['./fix_x11.sh'], check=True)
                except:
                    print("❌ Impossible de lancer fix_x11.sh")
                    print("💡 Lancez manuellement: ./fix_x11.sh")
                    
            elif choice == '7':
                show_recommendations()
                
            elif choice == '8':
                print("👋 Au revoir !")
                break
                
            else:
                print("❌ Option invalide. Choisissez entre 1 et 8.")
                
        except KeyboardInterrupt:
            print("\n👋 Au revoir !")
            break
        except Exception as e:
            print(f"❌ Erreur: {e}")

def main():
    """Fonction principale"""
    print("🖱️ Détecteurs de Clics de Souris")
    print("Détection automatique de l'environnement...")
    
    # Vérification initiale
    show_system_info()
    show_recommendations()
    
    # Menu principal
    main_menu()

if __name__ == "__main__":
    main()

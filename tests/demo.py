#!/usr/bin/env python3
"""
Script de démonstration des détecteurs de clics.
"""

print("🖱️ Projet Détecteur de Clics de Souris")
print("=" * 40)
print()
print("✅ Projet créé avec succès !")
print()
print("📁 Fichiers créés :")
print("  • mouse_click_detector.py         - Version pyautogui")
print("  • mouse_click_detector_pynput.py  - Version pynput") 
print("  • simple_mouse_detector.py        - Version système direct")
print("  • test_detectors.py               - Script de test")
print("  • fix_x11.sh                      - Correction problèmes X11")
print("  • requirements.txt                - Dépendances Python")
print("  • README.md                       - Documentation complète")
print()
print("🚀 Utilisation :")
print("  1. Version simple (recommandée):")
print("     python3 simple_mouse_detector.py")
print()
print("  2. Version avec pyautogui:")
print("     python3 mouse_click_detector.py")
print()
print("  3. Version avec pynput:")
print("     python3 mouse_click_detector_pynput.py")
print()
print("💡 En cas de problème X11/permissions :")
print("  ./fix_x11.sh")
print()

# Test des dépendances
print("🔧 État des dépendances :")
try:
    import pyautogui
    print("  ✅ pyautogui - OK")
except Exception as e:
    print(f"  ⚠️  pyautogui - {str(e)[:50]}...")

try:
    import pynput
    print("  ✅ pynput - OK")
except Exception as e:
    print(f"  ⚠️  pynput - {str(e)[:50]}...")

print()
print("🎯 Projet prêt ! Consultez README.md pour plus d'infos.")

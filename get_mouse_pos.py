#!/usr/bin/env python3
"""
Script simple pour détecter un clic de souris sur Windows.
Utilise pynput pour capturer la position du clic.
"""

from src.mouse import wait_for_click

def main():
    print("🖱️  Cliquez n'importe où pour capturer la position...")
    result = wait_for_click()
    if not result:
        print("❌ Aucun clic détecté ou erreur")
        exit(1)
    x, y = result
    print(f"✅ Position finale: ({x}, {y})")

if __name__ == "__main__":
    main()

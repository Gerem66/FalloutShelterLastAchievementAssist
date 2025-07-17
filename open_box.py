#!/usr/bin/env python3
"""
Script simple pour automatiser des clics de souris sur Windows.
Utilise pyautogui pour simuler les clics.
"""

from time import sleep
from src.mouse import click

fallout_open_box = [785, 452]

def main():
    print("🔍 Préparez vous, départ dans 5 secondes...")
    sleep(5)
    try:
        loop = 0
        while True:
            sleep(0.5)
            loop += 1
            click(fallout_open_box[0], fallout_open_box[1], f"Ouvrir le loot {loop}")

    except KeyboardInterrupt:
        print("❌ Processus annulé par l'utilisateur")
        return

if __name__ == "__main__":
    main()

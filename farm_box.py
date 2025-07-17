#!/usr/bin/env python3
"""
Script simple pour automatiser des clics de souris sur Windows.
Utilise pyautogui pour simuler les clics.
"""

import numpy as np
from time import sleep
from src.mouse import click
from src.date_manager import set_automatic_time, set_manual_time_plus_one_week

fallout_icon = [1245, 1056]             # Position de l'icône FalloutShelter
fallout_first_loot = [369, 617]         # Position du premier loot
fallout_loot_padding = [90, 0]         # Décalage pour les loots suivants
fallout_loot_popup_close = [992, 185]     # Position pour fermer la popup de loot

def main():
    steps = [
        # Loots
        fallout_first_loot,                                                 # Loot 1
        np.array(fallout_first_loot) + np.array(fallout_loot_padding),      # Loot 2
        np.array(fallout_first_loot) + np.array(fallout_loot_padding) * 2,  # Loot 3
        np.array(fallout_first_loot) + np.array(fallout_loot_padding) * 3,  # Loot 4
        np.array(fallout_first_loot) + np.array(fallout_loot_padding) * 4,  # Loot 5
        np.array(fallout_first_loot) + np.array(fallout_loot_padding) * 5,  # Loot 6
        np.array(fallout_first_loot) + np.array(fallout_loot_padding) * 6,  # Loot 7
    ]

    print("🔍 Préparez vous, départ dans 5 secondes...")
    try:
        loop = 0
        while True:
            sleep(2)
            print(f"🔁 Boucle {loop + 1}")
            loop += 1

            # Avancer la date
            set_manual_time_plus_one_week()
            sleep(2)

            # Ouvrir FalloutShelter
            click(fallout_icon[0], fallout_icon[1], "Ouvrir FalloutShelter")
            sleep(2)

            # Ouvrir, récupérer le loot, réduire
            i = 0
            for step in steps:
                i += 1
                x, y = step
                click(x, y, f"Ouvrir loot {i}")
                sleep(0.2)  # Pause pour laisser le temps au clic de s'effectuer
                click(x, y, False)
                sleep(0.2)  # Pause pour laisser le temps au clic de s'effectuer

            # Fermer la popup
            click(fallout_loot_popup_close[0], fallout_loot_popup_close[1], "Fermer la popup de loot")
            sleep(0.2)
            click(fallout_loot_popup_close[0], fallout_loot_popup_close[1], False)
            sleep(1)

            # Réduire FalloutShelter
            click(fallout_icon[0], fallout_icon[1], "Réduire FalloutShelter")

            # Reset la date
            set_automatic_time()
            sleep(1)

            # Ouvrir fallout pour reset puis réduire
            click(fallout_icon[0], fallout_icon[1], "Ouvrir FalloutShelter")
            sleep(2)
            click(fallout_icon[0], fallout_icon[1], "Réduire FalloutShelter")

    except KeyboardInterrupt:
        print("❌ Processus annulé par l'utilisateur")
        set_automatic_time()
        return

if __name__ == "__main__":
    main()

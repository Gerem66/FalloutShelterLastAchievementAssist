#!/usr/bin/env python3
"""
Version alternative utilisant pynput pour une détection plus précise des clics.
Cette version capture les événements système natifs.
"""

from pynput import mouse
import time
import threading

class MouseClickListener:
    def __init__(self):
        self.click_position = None
        self.listener = None
        self.waiting = False
        self.click_detected = False
    
    def on_click(self, x, y, button, pressed):
        """
        Callback appelé lors d'un clic de souris
        
        Args:
            x, y: Position du clic
            button: Bouton cliqué (left, right, middle)
            pressed: True si le bouton est pressé, False si relâché
        """
        if pressed and not self.click_detected:  # Seulement lors de l'appui
            self.click_position = (x, y)
            button_name = self.get_button_name(button)
            print(f"Clic {button_name} détecté à la position : x={x}, y={y}")
            self.click_detected = True
            self.waiting = False
            return False  # Arrête l'écoute
    
    def get_button_name(self, button):
        """Retourne le nom du bouton cliqué"""
        if button == mouse.Button.left:
            return "gauche"
        elif button == mouse.Button.right:
            return "droit"
        elif button == mouse.Button.middle:
            return "milieu"
        else:
            return "inconnu"
    
    def on_move(self, x, y):
        """Callback appelé lors du mouvement de la souris (optionnel)"""
        # Uncomment pour voir le mouvement en temps réel
        # print(f"Souris déplacée vers ({x}, {y})")
        pass
    
    def wait_for_click(self, show_movement=False):
        """
        Attend un clic et retourne la position
        
        Args:
            show_movement: Si True, affiche le mouvement de la souris
            
        Returns:
            tuple: (x, y) position du clic ou None si annulé
        """
        print("Cliquez n'importe où sur l'écran...")
        print("Appuyez sur Ctrl+C pour annuler")
        
        self.waiting = True
        self.click_position = None
        self.click_detected = False
        
        try:
            # Configure les callbacks
            callbacks = {'on_click': self.on_click}
            if show_movement:
                callbacks['on_move'] = self.on_move
            
            with mouse.Listener(**callbacks) as self.listener:
                while self.waiting:
                    time.sleep(0.1)  # Évite une utilisation excessive du CPU
            
            return self.click_position
            
        except KeyboardInterrupt:
            print("\nOpération annulée par l'utilisateur")
            return None

def get_current_mouse_position():
    """Retourne la position actuelle de la souris"""
    try:
        # Utilise pynput pour obtenir la position actuelle
        from pynput.mouse import Listener
        
        # Créer un listener temporaire pour obtenir la position
        position = None
        
        def on_move(x, y):
            nonlocal position
            position = (x, y)
            return False  # Arrête immédiatement
        
        # Déclenche un événement de mouvement en bougeant légèrement
        with Listener(on_move=on_move) as listener:
            listener.join(timeout=0.1)
        
        return position
    except:
        return None

def main():
    """Fonction principale"""
    print("=== Détecteur de Clics de Souris (Version pynput) ===\n")
    
    # Affiche la position actuelle
    current_pos = get_current_mouse_position()
    if current_pos:
        print(f"Position actuelle approximative : {current_pos}")
    
    # Demande à l'utilisateur s'il veut voir le mouvement
    try:
        show_movement = input("\nVoulez-vous voir le mouvement de la souris en temps réel ? (o/N): ").lower().startswith('o')
    except KeyboardInterrupt:
        print("\nAnnulé par l'utilisateur")
        return
    
    print()
    
    # Crée le listener et attend un clic
    listener = MouseClickListener()
    position = listener.wait_for_click(show_movement)
    
    if position:
        x, y = position
        print(f"\n✅ Position finale du clic : ({x}, {y})")
        
        # Informations supplémentaires
        print(f"📍 Coordonnées absolues : x={x}, y={y}")
    else:
        print("❌ Aucune position capturée")

if __name__ == "__main__":
    main()

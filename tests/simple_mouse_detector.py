#!/usr/bin/env python3
"""
Version simple du détecteur de clics qui fonctionne sans interface graphique.
Utilise la lecture de fichiers système Linux pour détecter les clics.
"""

import struct
import time
import os
import glob

class SimpleMouseDetector:
    def __init__(self):
        self.device_path = None
        self.find_mouse_device()
    
    def find_mouse_device(self):
        """Trouve le périphérique de souris dans /dev/input"""
        # Recherche les périphériques de souris
        mouse_devices = []
        
        # Recherche dans /dev/input/by-id pour les souris
        by_id_path = "/dev/input/by-id"
        if os.path.exists(by_id_path):
            for device in os.listdir(by_id_path):
                if "mouse" in device.lower():
                    device_path = os.path.join(by_id_path, device)
                    if os.path.exists(device_path):
                        mouse_devices.append(os.path.realpath(device_path))
        
        # Fallback: chercher dans /proc/bus/input/devices
        if not mouse_devices:
            try:
                with open('/proc/bus/input/devices', 'r') as f:
                    content = f.read()
                    # Simple parsing pour trouver les souris
                    devices = content.split('\n\n')
                    for device in devices:
                        if 'mouse' in device.lower() or 'Mouse' in device:
                            for line in device.split('\n'):
                                if line.startswith('H: Handlers='):
                                    handlers = line.split('=')[1]
                                    for handler in handlers.split():
                                        if handler.startswith('event'):
                                            mouse_devices.append(f"/dev/input/{handler}")
            except:
                pass
        
        # Dernier recours: essayer les périphériques event
        if not mouse_devices:
            mouse_devices = glob.glob("/dev/input/event*")
        
        if mouse_devices:
            self.device_path = mouse_devices[0]
            print(f"Périphérique de souris trouvé: {self.device_path}")
        else:
            print("Aucun périphérique de souris trouvé")
    
    def wait_for_click(self):
        """Attend un clic de souris via les événements système"""
        if not self.device_path:
            print("❌ Aucun périphérique de souris disponible")
            return None
        
        print("Cliquez n'importe où sur l'écran...")
        print("Appuyez sur Ctrl+C pour annuler")
        print(f"📱 Écoute sur {self.device_path}")
        
        try:
            with open(self.device_path, 'rb') as device:
                while True:
                    # Lire un événement (24 bytes sur la plupart des systèmes)
                    try:
                        data = device.read(24)
                        if len(data) == 24:
                            # Décomposer l'événement input_event
                            # struct input_event { time, type, code, value }
                            unpacked = struct.unpack('llHHI', data)
                            sec, usec, event_type, code, value = unpacked
                            
                            # Type 1 = EV_KEY (événements clavier/bouton)
                            # Code 272 = BTN_LEFT, 273 = BTN_RIGHT, 274 = BTN_MIDDLE
                            if event_type == 1 and code in [272, 273, 274] and value == 1:
                                button_names = {272: "gauche", 273: "droit", 274: "milieu"}
                                button = button_names.get(code, "inconnu")
                                print(f"Clic {button} détecté!")
                                
                                # On ne peut pas obtenir les coordonnées avec cette méthode
                                # mais on détecte bien le clic
                                return ("Clic détecté", button)
                    except struct.error:
                        continue
                        
        except PermissionError:
            print("❌ Permission refusée pour accéder au périphérique de souris")
            print("💡 Essayez de lancer le script avec sudo:")
            print("   sudo python3 simple_mouse_detector.py")
            return None
        except FileNotFoundError:
            print(f"❌ Périphérique {self.device_path} non trouvé")
            return None
        except KeyboardInterrupt:
            print("\n👋 Opération annulée par l'utilisateur")
            return None

def fallback_click_detector():
    """Détecteur de clics basique qui fonctionne partout"""
    print("=== Détecteur de Clics Simple ===")
    print("Cette version ne nécessite pas d'interface graphique")
    print()
    
    detector = SimpleMouseDetector()
    result = detector.wait_for_click()
    
    if result:
        print(f"✅ {result[0]} - Bouton: {result[1]}")
    else:
        print("❌ Aucun clic détecté")

def main():
    """Fonction principale avec instructions"""
    print("🖱️ Détecteur de Clics Simple (Sans X11)")
    print("=" * 40)
    print()
    print("Cette version fonctionne directement avec les périphériques système")
    print("et ne nécessite pas d'interface graphique.")
    print()
    
    # Vérifier si on est en mode graphique
    display = os.environ.get('DISPLAY')
    if not display:
        print("ℹ️  Pas d'affichage graphique détecté - utilisation du mode texte")
        fallback_click_detector()
    else:
        print("ℹ️  Affichage graphique détecté")
        print("Si les autres scripts ne marchent pas, vous pouvez:")
        print("1. Essayer: export DISPLAY=:0")
        print("2. Ou utiliser cette version simple")
        print()
        
        choice = input("Utiliser cette version simple ? (o/N): ").lower().startswith('o')
        if choice:
            fallback_click_detector()
        else:
            print("Utilisez les autres scripts avec les corrections suggérées.")

if __name__ == "__main__":
    main()

import sys
import signal
import pyautogui
from pynput import mouse
from pynput.mouse import Button, Listener

# Configuration pyautogui pour Windows
pyautogui.FAILSAFE = False  # Désactive la protection fail-safe
pyautogui.PAUSE = 0.1  # Petite pause entre les actions

def wait_for_click():
    """Attend et capture la position d'un clic de souris sur Windows"""

    def signal_handler(sig, frame):
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    clicked_position = None

    def on_click(x, y, button, pressed):
        nonlocal clicked_position
        if pressed:  # Seulement quand le bouton est pressé (pas relâché)
            clicked_position = (int(x), int(y))
            return False  # Arrête l'écoute

    try:
        # Écoute les clics de souris
        with Listener(on_click=on_click) as listener:
            listener.join()

        return clicked_position

    except KeyboardInterrupt:
        print("❌ Capture annulée par l'utilisateur")
        return None
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return None

def click(x, y, message = ""):
    """Effectue un clic de souris aux coordonnées spécifiées sur Windows"""
    try:
        if message is not False:
            print(f"🔄 Clic à ({x}, {y}) en cours", end="")

        try:
            mouse_controller = mouse.Controller()
            mouse_controller.position = (x, y)
            mouse_controller.click(Button.left, 1)
            if message is not False:
                print(f"\r✅ Clic effectué à ({x}, {y}) - {message}")
            return
        except Exception as pynput_error:
            print(f"\r ⚠️  pynput a échoué: {pynput_error}")

        raise Exception("Toutes les méthodes de clic ont échoué")

    except Exception as e:
        print(f"\r❌ Erreur lors du clic: {e}")

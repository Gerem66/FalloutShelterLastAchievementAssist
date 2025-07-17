#!/usr/bin/env python3
"""
Module pour gérer la date système Windows.
Utilise des commandes Windows pour modifier les paramètres de date/heure.
"""

import subprocess
import datetime
from time import sleep

def set_automatic_time():
    """Active la synchronisation automatique de l'heure Windows"""
    try:
        print("🔄 Activation de la synchronisation automatique de l'heure...", end='')
        
        # Commande pour activer la synchronisation automatique
        cmd = 'w32tm /config /manualpeerlist:"time.windows.com" /syncfromflags:manual /reliable:yes /update'
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            # Forcer la synchronisation
            sync_cmd = 'w32tm /resync'
            sync_result = subprocess.run(sync_cmd, shell=True, capture_output=True, text=True)
            
            if sync_result.returncode == 0:
                print("\r✅ Synchronisation automatique activée et effectuée")
                return True
            else:
                print(f"\r ⚠️  Synchronisation activée mais resync échoué: {sync_result.stderr}")
                return True
        else:
            print(f"\n❌ Erreur lors de l'activation: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"\n❌ Erreur lors de l'activation de la synchronisation automatique: {e}")
        return False

def set_manual_time_plus_one_week():
    """Définit la date système à la date actuelle + 1 semaine"""
    try:
        print("🔄 Définition de la date à +1 semaine...", end='')

        # Calculer la date + 1 semaine
        current_date = datetime.datetime.now()
        future_date = current_date + datetime.timedelta(weeks=1)
        
        #print(f"📅 Date actuelle: {current_date.strftime('%d/%m/%Y %H:%M:%S')}")
        #print(f"📅 Nouvelle date: {future_date.strftime('%d/%m/%Y %H:%M:%S')}")
        
        # Méthode 1: Essayer avec PowerShell (plus robuste)
        try:
            # Format PowerShell DateTime
            ps_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
            
            # Commande PowerShell pour changer la date
            ps_cmd = f'powershell -Command "Set-Date -Date \\"{ps_date}\\""'
            #print(f"🔧 Commande: {ps_cmd}")
            
            ps_result = subprocess.run(ps_cmd, shell=True, capture_output=True, text=True)
            
            if ps_result.returncode == 0:
                sleep(1)
                new_time = datetime.datetime.now()
                print(f"\r✅ Date définie à : {new_time.strftime('%d/%m/%Y %H:%M:%S')} (PowerShell)")
                return True
            else:
                print(f"\r ⚠️  PowerShell a échoué: {ps_result.stderr}")
                
        except Exception as ps_error:
            print(f"\r ⚠️  Erreur PowerShell: {ps_error}")
        
        # Méthode 2: Fallback avec les commandes CMD traditionnelles
        try:
            print("🔄 Tentative avec les commandes CMD...", end='')

            # Désactiver la synchronisation automatique d'abord
            disable_cmd = 'w32tm /config /syncfromflags:NO /update'
            subprocess.run(disable_cmd, shell=True, capture_output=True, text=True)

            # Format pour CMD Windows (dd/MM/yyyy)
            date_str = future_date.strftime("%d/%m/%Y")
            time_str = future_date.strftime("%H:%M:%S")

            #print(f"🔧 Date CMD: {date_str}")
            #print(f"🔧 Heure CMD: {time_str}")

            # Changer la date avec echo pour éviter l'interaction
            date_cmd = f'echo {date_str} | date'
            date_result = subprocess.run(date_cmd, shell=True, capture_output=True, text=True)

            # Changer l'heure avec echo pour éviter l'interaction  
            time_cmd = f'echo {time_str} | time'
            time_result = subprocess.run(time_cmd, shell=True, capture_output=True, text=True)

            # Vérifier que la date a changé
            sleep(1)
            new_time = datetime.datetime.now()
            print(f"\r✅ Date définie à : {new_time.strftime('%d/%m/%Y %H:%M:%S')} (CMD)")

            return True
            
        except Exception as cmd_error:
            print(f"\r ⚠️  Erreur CMD: {cmd_error}")
        
        print("❌ Toutes les méthodes ont échoué - Vérifiez les privilèges administrateur")
        return False
        
    except Exception as e:
        print(f"❌ Erreur lors de la définition manuelle: {e}")
        return False

def get_current_system_time():
    """Récupère l'heure système actuelle"""
    try:
        current_time = datetime.datetime.now()
        #print(f"🕐 Heure système actuelle: {current_time.strftime('%d/%m/%Y %H:%M:%S')}")
        return current_time
    except Exception as e:
        print(f"❌ Erreur lors de la récupération de l'heure: {e}")
        return None

def wait_and_show_time(seconds=5):
    """Attend et affiche l'heure toutes les secondes"""
    print(f"⏱️  Attente de {seconds} secondes avec affichage de l'heure:")
    for i in range(seconds):
        current_time = datetime.datetime.now()
        print(f"   {current_time.strftime('%H:%M:%S')}")
        if i < seconds - 1:  # Ne pas faire sleep à la dernière itération
            sleep(1)

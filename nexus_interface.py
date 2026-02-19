import os
import time

def draw_leds():
    state_path = os.path.expanduser("~/Desktop/nexus_project/.sys_state")
    os.system('clear')
    
    print("="*40)
    print("      NEXUS CORE - MONITORING SYSTEM")
    print("="*40)
    print("\n[ PROTOCOLLO ELENA/REFOSCO ATTIVO ]\n")

    if os.path.exists(state_path):
        # Stato: Boot completato
        print(" ●  B.R.A.I.N.  [ONLINE]")
        print(" ●  S.A.R.A.    [ONLINE]")
        print(" ●  V.E.D.O.    [ONLINE]")
        print(" ●  F.U.T.U.R.O. [ONLINE]")
        print("\n>>> STATUS: SISTEMA SCARICO E PRONTO.")
    else:
        # Stato: Attesa
        print(" ○  B.R.A.I.N.  [WAITING]")
        print(" ○  S.A.R.A.    [WAITING]")
        print(" ○  V.E.D.O.    [WAITING]")
        print(" ○  F.U.T.U.R.O. [WAITING]")
        print("\n>>> STATUS: IN ATTESA DI INIEZIONE...")

if __name__ == "__main__":
    try:
        while True:
            draw_leds()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nInterfaccia Nexus sospesa.")

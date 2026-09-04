# test_bot.py
import asyncio
# Wir importieren deine Methode aus der anderen Datei
from mcrequests import request_player_status

# Diese Liste simuliert später deine Datenbank-Abfrage
meine_test_datenbank_namen = ["SpeedyFabian", "Krieger249", "EinUngueltigerName123"]

async def main():
    print("Starte Abfrage der Live-Karte...")
    
    # Hier rufen wir deine Methode mit await auf – genau wie später im Bot!
    ergebnis = await request_player_status(meine_test_datenbank_namen)
    
    print("\n--- TEST-ERGEBNIS ---")
    print("Folgende registrierte Spieler sind gerade online:")
    print(ergebnis)

# Da wir hier ganz außen sind, wirft asyncio.run() den Motor an
asyncio.run(main())

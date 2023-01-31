#!/usr/bin/env python
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep

DEVICE_ID="98bb0735e28656bac098d927d410c3138a4b5bca"
CLIENT_ID="e6adc18f6e4247ab9a0478b66320bd21"
CLIENT_SECRET="cfa93cc0177943d4a7f4d57cb12096bd"

while True:
    try:
        reader=SimpleMFRC522()
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       redirect_uri="http://localhost:8080",
                                                       scope="user-read-playback-state,user-modify-playback-state"))
        
        # create an infinite while loop that will always be waiting for a new scan
        while True:
            print("Please scan a card...")
            id= reader.read()[0]
            print("ID of the card is:",id)
            sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
            
            if (id==16213434817):
                
                # BTS Butter
                # connecting sticker ID to spotfiy song ID
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:3VqeTFIvhxu3DIe4eZVzGq'])
                sleep(2)
                
            elif (id==426634469682):
             
                
                # New Jeans OMG
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:65FftemJ1DbbZ45DUfHJXE'])
                sleep(2)
                
            elif (id==840880644366):
                
                # New Jeans Hurt
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:5expoVGQPvXuwBBFuNGqBd'])
                sleep(2)
                
            elif (id==151655833961):
                
                # New Jeans Ditto
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:3r8RuvgbX9s7ammBn07D3W'])
                sleep(2)
                
            elif (id==703005417743):
                
                # BTS Run
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:69xohKu8C1fsflYAiSNbwM'])
                sleep(2)
                
            elif (id==357260550527):
                
                # Vannda Bong
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:7BalknaAGYtzUjIGOSkGBr'])
                sleep(2)
                
            elif (id==152729444783):
                
                # New Jeans Hype Boy
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:0a4MMyCrzT0En247IhqZbD'])
                sleep(2)
                
            elif (id==906479428062):
                
                # New Jeans Cookie
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:2DwUdMJ5uxv20EhAildreg'])
                sleep(2)
                
            elif (id==358418047264):
                
                # New Jeans Attention
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:2pIUpMhHL6L9Z5lnKxJJr9'])
                sleep(2)
                
            elif (id==429352051093):
                
                # DARARI
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:0dcnrLo8s1rhjm8euGjI4n'])
                sleep(2)
                
            elif (id==635579097470):
                
                # BTS Dynamite
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:0v1x6rN6JHRapa03JElljE'])
                sleep(2)
                
            elif (id==495673958658):
                
                # BTS Life goes On
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:5FVbvttjEvQ8r2BgUcJgNg'])
                sleep(2)
                
                
            elif (id==429135520144):
                
                # Taylor Swift All Too Well
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:3nsfB1vus2qaloUdcBZvDu'])
                sleep(2)
                     
                
                  
            elif (id==151858536800):
                
                # Lover
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:1dGr1c8CrMLDpV6mPbImSI'])
                sleep(2)
                
            elif (id==772464533873):
                
                # One Call Away
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:7soJgKhQTO8hLP2JPRkL5O'])
                sleep(2)
                
            elif (id==495103664430):
                
                # Marvin Gave
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:7rl1z4j7MurMDnn9rHh4M2'])
                sleep(2)
                
            elif (id==497335034275):
                
                # Left and Right
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:0mBP9X2gPCuapvpZ7TGDk3'])
                sleep(2)
                
            elif (id==769595761030):
                
                # Shut Down
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:0ARKW62l9uWIDYMZTUmJHF'])
                sleep(2)
                
            elif (id==909215752568):
                
                # Let her go
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:1KxwZYyzWNyZSRyErj2ojT'])
                sleep(2)
                
            elif (id==631653556639):
                
                # It's beginning to lok a lot like christmas
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:1Fiujre4Kze6NgSr5FXg02'])
                sleep(2)
                
            elif (id==84177412534):
                
                # Car Crash
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:2tlJ22iQwiO1CWBQSma23n'])
                sleep(2)
                
            elif (id==85804736980):
                
                # Visions
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:2pscAWkm3jAxcrpBwOtQmS'])
                sleep(2)
                
            elif (id==770952683790):
                
                # Anti Hero
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:0V3wPSX9ygBnCm8psDIegu'])
                sleep(2)
                
            elif (id==12924576061):
                
                # Nothing To Regret
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:3C2xQqHVkhA1Ht17SzPRke'])
                sleep(2)
                
            elif (id==84043194814):
                
                # JO
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:4WjrRCJDVJZ8reecQf9ts0'])
                sleep(2)
                
            elif (id==13964894589):
                
                # Mamacita
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:68PxsCDTqoPHRontE1Lh2b'])
                sleep(2)
                
            elif (id==1047156187394):
                
                # Love yourself
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:50kpGaPAhYJ3sGmk6vplg0'])
                sleep(2)
                
            elif (id==701679821309):
                
                # Pkor Lorn Pailen
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:5qje6kppOthWabkmEAlIuk'])
                sleep(2)
                
            elif (id==16011649414):
                
                # Austronaut
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:0h7QMc9ZRzA9QJrbEHytn2'])
                sleep(2)
                
            elif (id==631903248780):
                
                # BHeart Shaker
                sp.start_playback(device_id=DEVICE_ID, uris=['spotify:track:52FCAZn0YEkZfF0BtiAUMW'])
                sleep(2)
                
            
                
                
    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning  up...")
        GPIO.cleanup()
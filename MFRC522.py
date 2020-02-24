#-------------------------------------------------------------------------
#
#		Name: 		Eng. William R. Fröhlich
#
#		Project: 	MFRC552 - RFID
#
#		Date: 		2019.03.30
#
#-------------------------------------------------------------------------

# Import Library
import time
import RPi.GPIO as GPIO
import MFRC522
import signal
 
GPIO.setwarnings(False)

# UID of the Cards
CARTOES_LIBERADOS = {
    '72:AA:75:63:CE': 'Test',	
}
 
try:
    # Start the module RC522.
    LeitorRFID = MFRC522.MFRC522()
 
    print('Bring the card closer')
 
    while True:
        # Checks the existence of the card
        status, tag_type = LeitorRFID.MFRC522_Request(LeitorRFID.PICC_REQIDL)
 
        if status == LeitorRFID.MI_OK:
            print('Card detected!')
 
            # Read the UID
            status, uid = LeitorRFID.MFRC522_Anticoll()
 
            if status == LeitorRFID.MI_OK:
                uid = ':'.join(['%X' % x for x in uid])
                print('UID of the Card: %s' % uid)
 
                # If valid, release access
                if uid in CARTOES_LIBERADOS:
                    print('Release Access!')
                    print('Hi, %s.' % CARTOES_LIBERADOS[uid])
                else:
                    print('Access Denied')
 
                print('nBring the card closer')
 
        time.sleep(.25)
except KeyboardInterrupt:
    # If the user press Ctrl + C
    # End the code.
    GPIO.cleanup()
    print('nProgram Closed.')

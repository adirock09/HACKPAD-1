import board
import digitalio
import storage
import usb_cdc

boot_key = digitalio.DigitalInOut(board.GP26)
boot_key.direction = digitalio.Direction.INPUT
boot_key.pull = digitalio.Pull.UP

# If button pressed at boot
if not boot_key.value:
    # Enable USB drive so you can edit files
    storage.enable_usb_drive()
    usb_cdc.enable(console=True, data=True)
else:
    # Disable USB drive (normal keyboard mode)
    storage.disable_usb_drive()
    usb_cdc.enable(console=False, data=False)
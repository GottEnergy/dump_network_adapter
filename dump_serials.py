import platform
import wmi

def get_all_network_card_info():
    """Get detailed information about all network cards on Windows."""
    if platform.system() != "Windows":
        print("This script is designed to run on Windows systems.")
        return []

    network_info = []
    c = wmi.WMI()
    for nic in c.Win32_NetworkAdapter():
        card_info = {
            "DSN": nic.Name,  # Using Name as DSN equivalent
            "subSys IDs": nic.PNPDeviceID,  # Using PNPDeviceID as subSys ID's equivalent
            "Device ID": nic.DeviceID,
            "Vendor ID": nic.Manufacturer,  # Using Manufacturer as Vendor ID equivalent
            "BAR Address": nic.Description  # Using Description as BAR Address equivalent
        }
        network_info.append(card_info)
    return network_info

def display_all_network_card_info():
    """Display details of all network cards with custom labels."""
    all_network_cards = get_all_network_card_info()
    if not all_network_cards:
        print("No network cards found or script is not supported on this OS.")
        return

    for card in all_network_cards:
        print(f"DSN: {card['DSN']}")
        print(f"subSys IDs: {card['subSys IDs']}")
        print(f"Device ID: {card['Device ID']}")
        print(f"Vendor ID: {card['Vendor ID']}")
        print(f"BAR Address: {card['BAR Address']}")
        print('-' * 40)

if __name__ == "__main__":
    display_all_network_card_info()

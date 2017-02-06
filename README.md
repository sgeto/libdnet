
# Libdnet #
----------

Libdnet provides a simplified, portable interface to several low-level networking routines, including network address manipulation, kernel arp(4) cache and route(4) table lookup and manipulation, network firewalling, network interface lookup and manipulation, IP tunneling, and raw IP packet and Ethernet frame transmission.

This is a more or less personal fork I'm committed to maintain and keep up-to-date for educational proposes but any kind of help is greatly appreciated. The list of changes and "planned adjustments" pretty much matches that of upstream.

original: https://github.com/dugsong/libdnet
upstream: https://github.com/boundary/libdnet
nmap fork of libdnet: https://github.com/nmap/nmap/tree/master/libdnet-stripped

## Documentation

(coming soon)

## Build

For now, see INSTALL for various build instructions.

## Downloads

(coming soon)

## Bug report
Please report any bugs or issues here. If your issue occurs only on a specific OS, please mention it in the report.

## License
That's yet to be determined...

## Changes/Plans
----------
    * merged fixes and features from nmap fork of libdnet-stripped
        https://github.com/nmap/nmap/tree/master/libdnet-stripped
    * merged fixes from https://code.google.com/p/libdnet/issues/list
    * MinGW build compatibility
    * MSVC build compatibility (coming soon)
    * npcap compatibility (coming soon)
    * added os_intf_name and pcap_intf_name attributes
    * to intf.h for gaining access to the raw windows interface names
    * adds htonll/ntohll 64-bit endian conversions
    * various small build fixes

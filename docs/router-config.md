RUT200 Konfiguration
====================

#1. Reset Router

- Ausstecken
- Reset-Button mit Büroklammer gedrückt halten
- Wieder einstecken
- 2-3s warten
- Reset Button los lassen, LEDs blinken schnell

# 2. Router Firmware hochladen
- auf Routeroberfläche mit Browser: 192.168.1.1
- Firmware herunterladen auf teltonika Website (12MB, latest)
- Firmware uploaden
- Update drücken
- Warten, bis LEDs wieder statisch leuchten (neu gestartet)
- Browser neuladen

# 3. Router konfigurieren
- auf Routeroberfläche mit Browser: 192.168.1.1 anmelden

## 3.1 DHCP und IPV6 ausschalten
- Menu Netzwerk\LAN\Edit öffnen
- Tab General Settigns, Optionen: *Enable DHCPv4 server* und *Enable DHCPv6 server* auf *OFF* schalten
- Tab IPv6 Settigns, Option: *Delegate IPv6* auf *OFF* schalten
- mit *Save & Apply* bestätigen

## 3.2  Wirless ausschalten
- Menu Netzwerk\Wirless\SSIDs öffnen
- vorhandene SSID-Zeile auf *OFF* schalten
- mit *Save & Apply* bestätigen

## 3.3  APN einstellen für CAA
- Menu Netzwerk\Mobile\General öffnen
- Option *Auto APN* auf *OFF* schalten
- Eingabe bei APN *corporate.swisscom.ch*
- mit *Save & Apply* bestätigen

## 3.4 Dynamischer IP Dienst (DynDNS) einrichten

### 3.4.1  DynDNS installieren
- Menu System\Package Manager öffnen
- nach DDNS suchen
- DDNS Dienst installieren *install*
- warten bis Status *installed*


### 3.4.2 DynDNS auf einem Dienst-Provider erstellen (DuckDns, SPDNS)
- einloggen, und unter install mit openwrt:

	edit the config at /etc/config/ddns
	config service "duckdns"
			option enabled          "1"
			option domain           "bes1.duckdns.org"
			option username         "bes1"
			option password         "d73fa34a-eb90-49af-9f8c-ad3dbde0988b"
			option ip_source        "network"
			option ip_network       "wan"
			option force_interval   "72"
			option force_unit       "hours"
			option check_interval   "10"
			option check_unit       "minutes"
			#option ip_source       "interface"
			#option ip_interface    "eth0.1"
			#option ip_source       "web"
			#option ip_url          "http://ipv4.wtfismyip.com/text"
			option update_url       "http://www.duckdns.org/update?domains=[USERNAME]&token=[PASSWORD]&ip=[IP]"
			#option use_https       "1"
			#option cacert          "/etc/ssl/certs/cacert.pem"

### 3.4.3  DynDNS konfigurieren
- Menu Services\Dynamic DNS öffnen
- Neue Instanz erstellen "Add new instance"
- DDNS Name: Duckdns , oder Name des Providers
- Add drücken, Menu öffnet sich
- Enable: *ON* stellen
- LookUp-Hostname: *BESx.duckdns.org*
- DDNS service provider: duckdns.org auswählen
- Domain: *BESx.duckdns.org*
- Username gemäss 3.4.2 eingeben
- Passwort gemäss 3.4.2 eingeben
- Network: mob1s1a1
- mit *Save & Apply* bestätigen
- Status sollte nach einer Weile *UP* sein
- auf DynDNS Dienst kontrollieren ob die IP aktualisiert wurde

## 3.5 VPN Konfiguration

### 3.5.1  DynDNS konfigurieren
- Menu Services\Dynamic DNS öffnen
- Neue Instanz erstellen "Add new instance"

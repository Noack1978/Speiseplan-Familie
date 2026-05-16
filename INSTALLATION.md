# 🍽️ SPEISEPLAN – VOLLSTÄNDIGE INSTALLATION

## 📁 Datei 1: speiseplan.html
**Speicherort:** `config/www/speiseplan.html`

Die HTML-Datei ist bereits erstellt (siehe speiseplan.html).

**Installation:**
1. Öffne Home Assistant → File Editor (Add-on)
2. Navigiere zu `www/` (oder erstelle den Ordner, falls nicht vorhanden)
3. Lade `speiseplan.html` hoch

---

## 📋 Datei 2: Lovelace Dashboard-Karte
**Speicherort:** In deinem Dashboard (z.B. als Panel-Ansicht)

### Option A: Als Panel (empfohlen – volle Bildschirmhöhe)

1. In Home Assistant → Dashboard öffnen
2. Oben rechts → **Bearbeiten**
3. Oben rechts → **Ansicht hinzufügen**
4. Einstellungen:
   - **Titel:** Speiseplan
   - **Icon:** mdi:food
   - **Ansichtstyp:** Panel (1 Karte)
   - **URL:** speiseplan (optional für die URL-Leiste)
5. **Speichern**
6. In der neuen Panel-Ansicht → **Karte hinzufügen**
7. Folgendes YAML einfügen:

```yaml
type: iframe
url: /local/speiseplan.html
```

Das war's! Die Karte nimmt automatisch die volle Höhe ein.

---

### Option B: Als normale Karte (mit fester Höhe)

Falls du die App in einem normalen Dashboard einbetten willst:

```yaml
type: iframe
url: /local/speiseplan.html
aspect_ratio: 200%
```

Bei Bedarf `aspect_ratio` anpassen (150%, 200%, 250%).

---

## 🔧 Einrichtung beim ersten Start

Jedes Familienmitglied macht das **einmalig auf seinem Gerät**:

1. Speiseplan-Seite öffnen
2. Einrichtungsdialog erscheint automatisch
3. Eingeben:
   - **URL:** `http://homeassistant.local:8123` (oder deine IP)
   - **Token:** Das gemeinsame Token (siehe unten)
4. **Verbinden** klicken

---

## 🔑 Home Assistant Token erstellen

**Empfehlung:** Einen gemeinsamen Benutzer anlegen

1. **Einstellungen → Personen → Benutzer hinzufügen**
   - Name: `Speiseplan`
   - Passwort: beliebig
   - Rolle: Benutzer (kein Admin nötig)

2. Als dieser Benutzer einloggen → **Profil** (unten links)

3. Ganz nach unten scrollen → **Langfristige Zugriffstoken**

4. **Token erstellen**
   - Name: `Speiseplan App`
   - Token kopieren

5. Diesen einen Token an alle Familienmitglieder weitergeben

**Vorteil:** Wenn der Token mal kompromittiert ist, einfach den Speiseplan-Benutzer löschen statt deinen Admin-Token zurückzusetzen.

---

## ✅ Fertig! Keine weiteren Dateien nötig

Die App:
- ✅ Speichert Daten lokal im Browser (sofort verfügbar)
- ✅ Synchronisiert mit Home Assistant (alle sehen dasselbe)
- ✅ Überlebt HA-Neustarts (Daten bleiben lokal)
- ✅ Überlebt Dashboard-Wechsel (keine Ladezeit)
- ✅ Funktioniert offline (lokale Daten bleiben)

**Keine Helper, Sensoren oder Automationen nötig!**

---

## 🔄 So funktioniert die Synchronisation

1. **Person A** ändert eine Mahlzeit → sofort gespeichert
2. **Home Assistant** erhält die Änderung im Hintergrund
3. **Person B** sieht die Änderung nach max. 30 Sekunden

Bei HA-Neustart: Die lokalen Daten bleiben, beim nächsten Speichern wird HA wieder aktualisiert.

---

## 🛠️ Troubleshooting

**Seite zeigt nichts nach Dashboard-Wechsel**
→ Sollte mit der neuen Version nicht mehr passieren (localStorage)
→ Falls doch: Pull-to-refresh (nach unten ziehen)

**Daten weg nach HA-Neustart**
→ Sollte mit der neuen Version nicht mehr passieren (localStorage)
→ Falls doch: Im Browser-Cache gelöscht? Dann vom nächsten Familienmitglied synchronisiert

**Änderungen von anderen nicht sichtbar**
→ Warten bis zu 30 Sekunden (automatischer Sync)
→ Oder Pull-to-refresh erzwingen

**Token funktioniert nicht**
→ Prüfen: Richtiger Benutzer? Token vollständig kopiert?
→ Neu erstellen: ⚙️ Button oben rechts → Neu einrichten

---

## 📱 Mobile App optimiert

Die App ist für Handys optimiert:
- Kompakte Ansicht
- Touch-freundliche Buttons
- Automatisches Scrollen zu heute
- Swipe-Navigation zwischen Wochen

Viel Spaß beim Planen! 🍽️

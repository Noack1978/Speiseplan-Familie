# 🚀 Schnellstart

## Installation in 3 Schritten

### 1. Integration installieren

**Via HACS:**
1. HACS → Integrationen → ⋮ → Benutzerdefinierte Repositories
2. `https://github.com/DEIN-USERNAME/speiseplan` → Kategorie: Integration
3. "Speiseplan" installieren

**Manuell:**
1. Zip herunterladen und entpacken
2. `custom_components/speiseplan/` nach `/config/custom_components/` kopieren

### 2. Home Assistant neu starten

Nach Installation → **Einstellungen → System → Neu starten**

### 3. Dashboard-Karte hinzufügen

```yaml
type: iframe
url: /local/speiseplan.html
```

Bei Panel-Ansicht: Automatisch volle Höhe ✓

## Erste Benutzung

1. Seite öffnen → Einrichtungsdialog erscheint
2. **URL:** `http://homeassistant.local:8123` (oder deine IP)
3. **Token:** HA → Profil → Langfristige Zugriffstoken → erstellen
4. **Verbinden** klicken

Fertig! 🎉

## Token für alle

**Tipp:** Einen gemeinsamen HA-Benutzer "Speiseplan" anlegen:
1. Einstellungen → Personen → Benutzer hinzufügen
2. Name: `Speiseplan`, Rolle: Benutzer
3. Als dieser einloggen → Token erstellen
4. Token an alle Familienmitglieder verteilen

So kann jeder denselben Token verwenden.

## Wo sind die Daten?

`/config/www/speiseplan_data.json`

- Kann manuell editiert werden
- Wird in Backups mitgesichert
- Überlebt HA-Neustarts

## Probleme?

**Integration nicht gefunden**
→ Nach Installation HA neu starten

**Seite lädt nicht**
→ Entwicklerwerkzeuge → Dienste → Nach `speiseplan.save` suchen
→ Sollte vorhanden sein

**Keine Synchronisation zwischen Geräten**
→ Alle dasselbe Token verwenden?
→ Pull-to-refresh (nach unten ziehen)

---

Viel Spaß! 🍽️

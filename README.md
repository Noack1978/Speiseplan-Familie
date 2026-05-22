# 🍽️ Familien-Speiseplan für Home Assistant

Eine schöne, einfache Wochenplan-App für Home Assistant – perfekt für Familien.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2024.1+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## ✨ Features

- 📅 **Mehrwochen-Ansicht** – aktuelle Woche + 4 Wochen voraus + 8 Wochen zurück
- 🔄 **Automatische Synchronisation** – alle 10 Sekunden zwischen allen Geräten
- 💾 **Persistent** – überlebt Home Assistant Neustarts garantiert
- 👨‍👩‍👧‍👦 **Multi-User** – alle Familienmitglieder sehen und bearbeiten denselben Plan
- 📱 **Mobile-optimiert** – speziell für Smartphones designed
- 🎨 **Schönes Design** – warme Farben, intuitive Bedienung

## 📸 Screenshots

[Hier könnten deine Screenshots stehen]

## 🚀 Installation

### Über HACS (empfohlen)

1. HACS öffnen
2. **Integrationen** → **⋮** → **Benutzerdefinierte Repositories**
3. Repository hinzufügen:
   - **URL:** `https://github.com/DEIN-USERNAME/speiseplan`
   - **Kategorie:** Integration
4. **Speiseplan** suchen und installieren
5. **Home Assistant neu starten**

### Manuelle Installation

1. Dieses Repository herunterladen
2. Den Ordner `custom_components/speiseplan` nach `/config/custom_components/` kopieren
3. Home Assistant neu starten

## ⚙️ Konfiguration

**Keine YAML-Konfiguration nötig!** Die Integration läuft automatisch nach dem Neustart.

### Lovelace Dashboard-Karte

#### Als Panel-Ansicht (empfohlen)

1. Dashboard → **Bearbeiten** → **Ansicht hinzufügen**
2. Einstellungen:
   - **Titel:** Speiseplan
   - **Icon:** `mdi:food`
   - **Ansichtstyp:** Panel (1 Karte)
3. **Karte hinzufügen** → Manuell:

```yaml
type: iframe
url: /local/speiseplan.html
```

#### Als normale Karte

```yaml
type: iframe
url: /local/speiseplan.html
aspect_ratio: 200%
```

## 🔑 Erstes Setup

Beim ersten Öffnen erscheint ein Einrichtungsdialog:

1. **Home Assistant URL** eingeben (meist automatisch erkannt)
2. **Long-Lived Access Token** eingeben:
   - HA → Profil → Langfristige Zugriffstoken → Token erstellen
   - **Tipp:** Einen separaten Benutzer "Speiseplan" anlegen und dessen Token verwenden

Jedes Familienmitglied macht das einmalig auf seinem Gerät.

## 📁 Datenspeicherung

Die Daten werden in `/config/www/speiseplan_data.json` gespeichert:

- ✅ Überlebt HA-Neustarts
- ✅ Kann manuell bearbeitet werden (JSON-Format)
- ✅ Kann in Backups eingeschlossen werden
- ✅ Eine Datei = Single Source of Truth

## 🛠️ Services

Die Integration stellt zwei Services bereit:

### `speiseplan.save`

Speichert Speiseplan-Daten programmatisch:

```yaml
service: speiseplan.save
data:
  data:
    "2026-W20":
      Montag:
        Frühstück: "Müsli"
        Mittagessen: "Nudeln"
        Abendessen: "Pizza"
```

### `speiseplan.load`

Lädt die gespeicherten Daten (für Automationen):

```yaml
service: speiseplan.load
```

## 🔧 Troubleshooting

**Seite lädt nicht**
- Prüfe ob die Integration aktiv ist: `Einstellungen → Geräte & Dienste → Speiseplan`
- Home Assistant Logs prüfen: `Einstellungen → System → Logs`

**"Service speiseplan.save nicht gefunden"**
- Home Assistant neu starten nach Installation
- Prüfe ob `/config/custom_components/speiseplan/` existiert

**Änderungen nicht sichtbar bei anderen**
- Warte 10 Sekunden (Auto-Reload-Interval)
- Pull-to-refresh (nach unten ziehen)
- Prüfe ob alle dasselbe Token verwenden

## 🤝 Contributing

Beiträge sind willkommen! Bitte erstelle ein Issue oder Pull Request.

## 📄 License

MIT License - siehe [LICENSE](LICENSE) Datei

## ❤️ Support

Wenn dir diese Integration gefällt:
- ⭐ Gib dem Repo einen Stern auf GitHub
- 🐛 Melde Bugs als Issues
- 💡 Schlage neue Features vor

## 🙏 Credits

Erstellt mit Claude (Anthropic) für Home Assistant

---

**Made with ❤️ for families**

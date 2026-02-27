# Travel Exception Map - Project Documentation

**Live URL**: https://tcby04.github.io/travel-exception-map/

**GitHub**: https://github.com/Tcby04/travel-exception-map

**Last Updated**: 2026-02-23

---

## Project Overview

Interactive global map showing visa requirements with a focus on **special cases and exceptions** that normal visa charts miss. The key differentiator is highlighting nuanced entry rules like partial-entry zones, autonomous territories, and regional quirks.

---

## Features

### Core Map
- Color-coded countries: Green (visa-free), Yellow (VOA), Blue (eVisa), Red (required)
- Clickable countries with popup: stay duration, conditions, last_updated, source link
- Dark theme with clean Outfit font

### Special Zones Overlay (Toggle)
- 35+ special zones highlighted with purple markers
- Categories include:
  - **SARs**: Hong Kong, Macau
  - **COFA**: Micronesia, Marshall Islands, Palau
  - **Partial Entry**: Jeju Island (Korea), Hainan Island (China)
  - **UK Territories**: Guernsey, Jersey, Isle of Man, Gibraltar, Bermuda
  - **Schengen Territories**: Canary Islands, Madeira, Azores
  - **Nordic**: Faroe Islands, Greenland, Svalbard
  - **French Overseas**: French Polynesia, New Caledonia, Martinique, etc.
  - **India Restricted**: Ladakh, Arunachal Pradesh, Nagaland
  - **Indonesia**: Papua, Raja Ampat
  - **US Territories**: Guam, Northern Mariana Islands

---

## Data Model

```json
{
  "country": {
    "iso": "KOR",
    "name": "South Korea",
    "visa_status": "visa-free",
    "stay": "90 days",
    "conditions": "Visa-free entry",
    "lastUpdated": "2026-01-15",
    "specialZones": [
      {
        "name": "Jeju Island",
        "coords": [33.5, 126.5],
        "condition": "Some nationalities can visit Jeju without visa but not mainland"
      }
    ]
  },
  "specialZone": {
    "name": "Svalbard, Norway",
    "coords": [78.0, 16.0],
    "parentCountry": "NOR",
    "note": "UNIQUE: No visa required, unlimited stay (Svalbard Treaty)"
  }
}
```

---

## Tech Stack

- Single HTML file with embedded CSS/JS
- Leaflet.js for maps
- OpenStreetMap/CARTO dark tiles
- Country GeoJSON from CDN
- Hosted on GitHub Pages

---

## Research Sources (To Verify)

- IATA Timatic (industry standard)
- US State Department (travel.state.gov)
- UK FCDO (gov.uk/foreign-travel-advice)
- Schengen Visa Info (schengenvisainfo.com)

---

## Future Enhancements

- [ ] Per-nationality filtering (user selects their passport)
- [ ] Real-time API integration (IATA Timatic)
- [ ] More countries in dataset
- [ ] Search by country name
- [ ] Mobile optimizations
- [ ] Export functionality

---

## Files

- `index.html` - Main application
- `RESEARCH.md` - Detailed research notes
- `PROJECT.md` - This file

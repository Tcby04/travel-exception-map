#!/usr/bin/env python3
# Read the truncated file and complete it

with open('/home/alethia/.openclaw/workspace/travel-exception-map/index.html', 'r') as f:
    content = f.read()

# The file ends with the GRC entry closing }, 
# Replace trailing }, with }; to close countryData, then append rest
fixed = content.rstrip().rstrip(',') + ';\n'

rest = '''
        // ─── Map initialization
        var map = L.map("map", {center: [20, 0], zoom: 2, minZoom: 2, maxZoom: 8});
        L.tileLayer("https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png", {attribution: "&copy; <a href='https://www.openstreetmap.org/copyright'>OSM</a> &copy; <a href='https://carto.com/'>CARTO</a>", subdomains: "abcd", maxZoom: 20}).addTo(map);
        var colors = {visaFree: "#22c55e", visaOnArrival: "#eab308", eVisa: "#3b82f6", visaRequired: "#ef4444", specialZone: "#a855f7"};
        var currentPassport = "any";
        var geoJsonLayer = null;
        var specialZonesLayer = L.layerGroup().addTo(map);
        var showSpecialZones = true;
        var specialZones = [
            {name:"Hong Kong SAR", coords:[22.3,114.2], note:"Separate immigration from China"},
            {name:"Macau SAR", coords:[22.2,113.5], note:"Separate visa policy"},
            {name:"Micronesia (COFA)", coords:[7.5,150.5], note:"COFA: US citizens visa-free 30 days"},
            {name:"Marshall Islands (COFA)", coords:[7.0,171.0], note:"COFA: US citizens visa-free 90 days"},
            {name:"Palau", coords:[7.5,134.5], note:"Visa-free for US, PH, CN, IN, MX, UK citizens"},
            {name:"Jeju Island, Korea", coords:[33.5,126.5], note:"Some nationals can visit Jeju without mainland visa"},
            {name:"Hainan Island, China", coords:[19.5,109.5], note:"Visa-free for group tours from 59 countries"},
            {name:"Shenzhen SEZ, China", coords:[22.5,114.0], note:"5-day visa-free for cruise passengers"},
            {name:"Guernsey, UK", coords:[49.4,-2.5], note:"Common Travel Area with UK/Ireland"},
            {name:"Jersey, UK", coords:[49.2,-2.1], note:"Common Travel Area"},
            {name:"Isle of Man", coords:[54.2,-4.5], note:"Common Travel Area"},
            {name:"Gibraltar", coords:[36.1,-5.3], note:"British Overseas Territory"},
            {name:"Canary Islands, Spain", coords:[28.0,-15.5], note:"Part of Spain / Schengen"},
            {name:"Madeira, Portugal", coords:[32.7,-17.0], note:"Part of Portugal / Schengen"},
            {name:"Azores, Portugal", coords:[37.7,-25.7], note:"Part of Portugal / Schengen"},
            {name:"Faroe Islands", coords:[62.0,-7.0], note:"Part of Denmark"},
            {name:"Greenland", coords:[72.0,-40.0], note:"Part of Denmark"},
            {name:"Svalbard, Norway", coords:[78.0,16.0], note:"UNIQUE: No visa required, unlimited stay (Svalbard Treaty)"},
            {name:"French Polynesia", coords:[-17.6,-149.4], note:"French overseas - NOT Schengen"},
            {name:"New Caledonia", coords:[-20.9,165.6], note:"French overseas - NOT Schengen"},
            {name:"Martinique & Guadeloupe", coords:[15.6,-61.5], note:"French overseas - Schengen applies"},
            {name:"Ladakh, India", coords:[34.5,77.5], note:"Inner Line Permit required"},
            {name:"Arunachal Pradesh, India", coords:[28.0,94.0], note:"Restricted Area Permit required"},
            {name:"Nagaland & Sikkim, India", coords:[26.0,94.5], note:"Special Protected Area Permits"},
            {name:"Papua, Indonesia", coords:[-3.5,130.0], note:"Special permit required"},
            {name:"N. Mariana Islands", coords:[15.2,145.7], note:"US territory - CNMI-only entry for PH/CN"},
            {name:"Guam", coords:[13.4,144.8], note:"US territory - Guam-CNMI permit for PH/CN"},
            {name:"Bermuda", coords:[32.3,-64.7], note:"British Overseas Territory"}
        ];
        function addSpecialZones() {
            specialZones.forEach(function(z) {
                L.circleMarker(z.coords, {radius:8, fillColor:colors.specialZone, color:"#fff", weight:2, opacity:1, fillOpacity:0.8})
                    .bindPopup("<strong>"+z.name+"</strong><br><span style='color:#a855f7'>"+z.note+"</span>")
                    .addTo(specialZonesLayer);
            });
        }
        function toggleSpecialZones() {
            if (map.hasLayer(specialZonesLayer)) map.removeLayer(specialZonesLayer);
            else if (showSpecialZones) specialZonesLayer.addTo(map);
        }
        addSpecialZones();
        document.getElementById("toggleZones").addEventListener("click", function() {
            showSpecialZones = !showSpecialZones;
            this.classList.toggle("active");
            toggleSpecialZones();
        });
        function parseFlagData(s) {
            if (!s) return null;
            var p = s.split(":");
            return {status: p[0], stay: p[1], conditions: p[2] || ""};
        }
        function getStatusClass(s) {
            var m = {"visa-free":"status-free","visa-on-arrival":"status-arrival","evisa":"status-evisa","visa-required":"status-required","special":"status-special"};
            return m[s] || "status-required";
        }
        function getStatusLabel(s) {
            var m = {"visa-free":"Visa Free","visa-on-arrival":"Visa on Arrival","evisa":"eVisa","visa-required":"Visa Required","special":"Special"};
            return m[s] || s;
        }
        function getCountryColor(iso) {
            var c = countryData[iso];
            if (!c) return colors.visaRequired;
            if (currentPassport === "any") {
                if (c.flags) {
                    var vals = Object.values(c.flags);
                    for (var i = 0; i < vals.length; i++) {
                        var f = parseFlagData(vals[i]);
                        if (f) {
                            if (f.status === "visa-free") return colors.visaFree;
                            if (f.status === "evisa") return colors.eVisa;
                            if (f.status === "visa-on-arrival") return colors.visaOnArrival;
                        }
                    }
                }
                return colors.visaRequired;
            }
            var fl = parseFlagData(c.flags && c.flags[currentPassport]);
            if (!fl) return colors.visaRequired;
            var cm = {"visa-free":colors.visaFree,"visa-on-arrival":colors.visaOnArrival,"evisa":colors.eVisa,"visa-required":colors.visaRequired,"special":colors.specialZone};
            return cm[fl.status] || colors.visaRequired;
        }
        function getPopupHTML(iso) {
            var c = countryData[iso];
            if (!c) return null;
            var passportLabelMap = {"USA":"&#127482;&#127480; US","PHL":"&#127477;&#127469; Filipino","CHN":"&#127463;&#127466; Chinese","IND":"&#127470;&#127468; Indian","MEX":"&#127463;&#127465; Mexican","GBR":"&#127468;&#127463; British"};
            var emojiMap = {"USA":"&#127482;&#127480;","PHL":"&#127477;&#127469;","CHN":"&#127463;&#127466;","IND":"&#127470;&#127468;","MEX":"&#127463;&#127465;","GBR":"&#127468;&#127463;"};
            var labelMap = {"USA":"US Citizen","PHL":"Filipino","CHN":"Chinese","IND":"Indian","MEX":"Mexican","GBR":"British"};

            if (currentPassport === "any") {
                var rows = "";
                if (c.flags) {
                    var rowArr = [];
                    Object.keys(c.flags).forEach(function(pp) {
                        var f = parseFlagData(c.flags[pp]);
                        if (!f) return;
                        var em = emojiMap[pp] || "";
                        rowArr.push("<div class='info-row'><span class='info-label'>" + em + " " + pp + ":</span><span class='info-value'><span class='status-badge " + getStatusClass(f.status) + "' style='font-size:0.65rem;padding:0.1rem 0.4rem'>" + f.stay + "</span></span></div>");
                    });
                    rows = rowArr.join("");
                }
                var sp = "";
                if (c.specialZones) {
                    var zoneArr = [];
                    c.specialZones.forEach(function(z) {
                        zoneArr.push("<div class='zone-item'><strong>" + z.name + "</strong><br>" + z.condition + "</div>");
                    });
                    sp = "<div class='special-zones'><h4>&#10024; Special Zones</h4>" + zoneArr.join("") + "</div>";
                }
                return "<div class='country-info'><h2>" + c.name + " <span class='status-badge' style='background:#334155;font-size:0.65rem'>All passports</span></h2><p style='font-size:0.8rem;color:#94a3b8;margin-bottom:0.75rem'>Select a passport above to filter</p><div class='info-grid'>" + (rows || "<p style='color:#94a3b8;font-size:0.8rem'>No data</p>") + "</div>" + sp + "</div>";
            }
            var fl = parseFlagData(c.flags && c.flags[currentPassport]);
            if (!fl) return null;
            var pLabel = passportLabelMap[currentPassport] || currentPassport;
            var sp = "";
            if (c.specialZones) {
                var zoneArr = [];
                c.specialZones.forEach(function(z) {
                    zoneArr.push("<div class='zone-item'><strong>" + z.name + "</strong><br>" + z.condition + "</div>");
                });
                sp = "<div class='special-zones'><h4>&#10024; Special Zones</h4>" + zoneArr.join("") + "</div>";
            }
            return "<div class='country-info'><h2>" + c.name + " <span class='status-badge " + getStatusClass(fl.status) + "'>" + getStatusLabel(fl.status) + "</span> <span class='passport-tag'>" + pLabel + "</span></h2><div class='info-grid'><div class='info-row'><span class='info-label'>Max Stay:</span><span class='info-value'>" + fl.stay + "</span></div><div class='info-row'><span class='info-label'>Conditions:</span><span class='info-value'>" + fl.conditions + "</span></div></div>" + sp + "<a href='https://www.timaticweb.com/' target='_blank' class='source-link'>Source: IATA Timatic</a></div>";
        }
        document.getElementById("passportSelect").addEventListener("change", function() {
            currentPassport = this.value;
            var banner = document.getElementById("passportBanner");
            var bannerText = document.getElementById("passportBannerText");
            var labelMap = {"USA":"US Citizen","PHL":"Filipino","CHN":"Chinese","IND":"Indian","MEX":"Mexican","GBR":"British"};
            if (currentPassport === "any") {
                banner.classList.remove("visible");
            } else {
                bannerText.textContent = labelMap[currentPassport] || currentPassport;
                banner.classList.add("visible");
            }
            if (geoJsonLayer) geoJsonLayer.setStyle(styleCountry);
        });
        function styleCountry(feature) {
            var iso = feature.properties.ISO_A3;
            return {fillColor: getCountryColor(iso), weight: 1, opacity: 1, color: "#1e293b", fillOpacity: 0.75};
        }
        fetch("https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson")
            .then(function(r) { return r.json(); })
            .then(function(data) {
                geoJsonLayer = L.geoJSON(data, {
                    style: styleCountry,
                    onEachFeature: function(feature, layer) {
                        var iso = feature.properties.ISO_A3;
                        var h = getPopupHTML(iso);
                        if (h) layer.bindPopup(h);
                    }
                }).addTo(map);
            })
            .catch(function(e) { console.error("GeoJSON error:", e); });

        // Search functionality
        var searchBox = document.getElementById("searchBox");
        var searchResults = document.getElementById("searchResults");
        var searchClear = document.getElementById("searchClear");
        var highlightedIndex = -1;

        function doSearch(query) {
            if (query.length < 2) {
                searchResults.classList.remove("active");
                return;
            }
            var q = query.toLowerCase();
            var all = Object.keys(countryData).map(function(k) {
                return {iso: k, name: countryData[k].name, coords: countryData[k].coords};
            });
            var matches = all.filter(function(c) { return c.name.toLowerCase().indexOf(q) !== -1; }).slice(0, 8);

            if (!matches.length) {
                searchResults.innerHTML = "<div class='search-no-results'>No countries found</div>";
                searchResults.classList.add("active");
                return;
            }

            highlightedIndex = -1;
            var html = "";
            matches.forEach(function(m) {
                var c = countryData[m.iso];
                var badge = "";
                if (c) {
                    if (currentPassport !== "any") {
                        var fl = parseFlagData(c.flags && c.flags[currentPassport]);
                        if (fl) badge = "<span class='search-result-status " + getStatusClass(fl.status) + "'>" + getStatusLabel(fl.status) + "</span>";
                    } else {
                        badge = "<span class='search-result-status' style='background:#334155;color:#94a3b8'>All</span>";
                    }
                }
                html += "<div class='search-result-item' data-iso='" + m.iso + "' data-coords='" + m.coords + "' data-name='" + m.name + "'><span class='search-result-name'>" + m.name + "</span>" + badge + "</div>";
            });
            searchResults.innerHTML = html;
            searchResults.classList.add("active");

            searchResults.querySelectorAll(".search-result-item").forEach(function(item) {
                item.addEventListener("click", function() {
                    var coordStr = this.dataset.coords;
                    var coords = [parseFloat(coordStr.split(",")[0]), parseFloat(coordStr.split(",")[1])];
                    map.flyTo(coords, 6, {duration: 1.5});
                    searchBox.value = this.dataset.name;
                    searchResults.classList.remove("active");
                    if (geoJsonLayer) {
                        var iso = this.dataset.iso;
                        geoJsonLayer.eachLayer(function(layer) {
                            if (layer.feature && layer.feature.properties.ISO_A3 === iso) {
                                setTimeout(function() { layer.openPopup(); }, 1600);
                            }
                        });
                    }
                });
            });
        }

        searchBox.addEventListener("input", function(e) {
            searchClear.classList.toggle("visible", e.target.value.length > 0);
            doSearch(e.target.value);
        });
        searchBox.addEventListener("keydown", function(e) {
            var items = searchResults.querySelectorAll(".search-result-item");
            if (!items.length) return;
            if (e.key === "ArrowDown") {
                e.preventDefault();
                highlightedIndex = Math.min(highlightedIndex + 1, items.length - 1);
                items.forEach(function(it, i) { it.classList.toggle("highlighted", i === highlightedIndex); });
            } else if (e.key === "ArrowUp") {
                e.preventDefault();
                highlightedIndex = Math.max(highlightedIndex - 1, 0);
                items.forEach(function(it, i) { it.classList.toggle("highlighted", i === highlightedIndex); });
            } else if (e.key === "Enter" && highlightedIndex >= 0) {
                e.preventDefault();
                items[highlightedIndex].click();
            } else if (e.key === "Escape") {
                searchResults.classList.remove("active");
            }
        });
        searchClear.addEventListener("click", function() {
            searchBox.value = "";
            searchClear.classList.remove("visible");
            searchResults.classList.remove("active");
            searchBox.focus();
        });
        searchBox.addEventListener("focus", function() { if (searchBox.value.length >= 2) doSearch(searchBox.value); });
        document.addEventListener("click", function(e) {
            if (!e.target.closest(".search-wrapper")) searchResults.classList.remove("active");
        });

        // Legend
        var legend = L.control({position: "bottomright"});
        legend.onAdd = function() {
            var div = L.DomUtil.create("div", "legend");
            div.innerHTML = "<h3>Visa Status</h3>" +
                "<div class='legend-item'><div class='legend-color' style='background:" + colors.visaFree + "'></div><span>Visa Free</span></div>" +
                "<div class='legend-item'><div class='legend-color' style='background:" + colors.visaOnArrival + "'></div><span>Visa on Arrival</span></div>" +
                "<div class='legend-item'><div class='legend-color' style='background:" + colors.eVisa + "'></div><span>eVisa</span></div>" +
                "<div class='legend-item'><div class='legend-color' style='background:" + colors.visaRequired + "'></div><span>Visa Required</span></div>" +
                "<div class='legend-item'><div class='legend-color' style='background:" + colors.specialZone + "'></div><span>Special Zone</span></div>";
            return div;
        };
        legend.addTo(map);
    </script>
</body>
</html>
'''

complete = fixed + rest

with open('/home/alethia/.openclaw/workspace/travel-exception-map/index.html', 'w') as f:
    f.write(complete)

print("Done! New length:", len(complete))

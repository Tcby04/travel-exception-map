#!/usr/bin/env python3
"""Add missing countries to the travel exception map."""

with open('/home/alethia/.openclaw/workspace/travel-exception-map/index.html', 'r') as f:
    content = f.read()

# The file ends with GRC entry. Find it and add countries after.
# The GRC entry ends with "GBR:'visa-free:90 days:Visa-free; Schengen rules apply' }},\n"
# We need to replace that closing }, with the full list of remaining countries

missing_countries = '''
            'CHE': { name: 'Switzerland', coords: [46.8, 8.2],
                flags: { USA:'visa-free:90 days:Schengen area', PHL:'visa-required:0:Schengen visa required', CHN:'visa-required:0:Schengen visa required', IND:'visa-required:0:Schengen visa required', MEX:'visa-free:90 days:Visa-free; Schengen rules apply', GBR:'visa-free:90 days:Visa-free; Schengen rules apply' }},
            'AUT': { name: 'Austria', coords: [47.5, 14.6],
                flags: { USA:'visa-free:90 days:Schengen area', PHL:'visa-required:0:Schengen visa required', CHN:'visa-required:0:Schengen visa required', IND:'visa-required:0:Schengen visa required', MEX:'visa-free:90 days:Visa-free; Schengen rules apply', GBR:'visa-free:90 days:Visa-free; Schengen rules apply' }},
            'BEL': { name: 'Belgium', coords: [50.5, 4.5],
                flags: { USA:'visa-free:90 days:Schengen area', PHL:'visa-required:0:Schengen visa required', CHN:'visa-required:0:Schengen visa required', IND:'visa-required:0:Schengen visa required', MEX:'visa-free:90 days:Visa-free; Schengen rules apply', GBR:'visa-free:90 days:Visa-free; Schengen rules apply' }},
            'POL': { name: 'Poland', coords: [51.9, 19.1],
                flags: { USA:'visa-free:90 days:Schengen area', PHL:'visa-required:0:Schengen visa required', CHN:'visa-required:0:Schengen visa required', IND:'visa-required:0:Schengen visa required', MEX:'visa-free:90 days:Visa-free; Schengen rules apply', GBR:'visa-free:90 days:Visa-free; Schengen rules apply' }},
            'SWE': { name: 'Sweden', coords: [60.1, 18.6],
                flags: { USA:'visa-free:90 days:Schengen area', PHL:'visa-required:0:Schengen visa required', CHN:'visa-required:0:Schengen visa required', IND:'visa-required:0:Schengen visa required', MEX:'visa-free:90 days:Visa-free; Schengen rules apply', GBR:'visa-free:90 days:Visa-free; Schengen rules apply' }},
            'NOR': { name: 'Norway', coords: [60.5, 8.5],
                flags: { USA:'visa-free:90 days:Schengen area', PHL:'visa-required:0:Schengen visa required', CHN:'visa-required:0:Schengen visa required', IND:'visa-required:0:Schengen visa required', MEX:'visa-free:90 days:Visa-free; Schengen rules apply', GBR:'visa-free:90 days:Visa-free; Schengen rules apply' }},
            'DNK': { name: 'Denmark', coords: [56.3, 9.5],
                flags: { USA:'visa-free:90 days:Schengen area', PHL:'visa-required:0:Schengen visa required', CHN:'visa-required:0:Schengen visa required', IND:'visa-required:0:Schengen visa required', MEX:'visa-free:90 days:Visa-free; Schengen rules apply', GBR:'visa-free:90 days:Visa-free; Schengen rules apply' }},
            'FIN': { name: 'Finland', coords: [61.9, 26.0],
                flags: { USA:'visa-free:90 days:Schengen area', PHL:'visa-required:0:Schengen visa required', CHN:'visa-required:0:Schengen visa required', IND:'visa-required:0:Schengen visa required', MEX:'visa-free:90 days:Visa-free; Schengen rules apply', GBR:'visa-free:90 days:Visa-free; Schengen rules apply' }},
            'CZE': { name: 'Czech Republic', coords: [49.8, 15.5],
                flags: { USA:'visa-free:90 days:Schengen area', PHL:'visa-required:0:Schengen visa required', CHN:'visa-required:0:Schengen visa required', IND:'visa-required:0:Schengen visa required', MEX:'visa-free:90 days:Visa-free; Schengen rules apply', GBR:'visa-free:90 days:Visa-free; Schengen rules apply' }},
            'HUN': { name: 'Hungary', coords: [47.2, 19.5],
                flags: { USA:'visa-free:90 days:Schengen area', PHL:'visa-required:0:Schengen visa required', CHN:'visa-required:0:Schengen visa required', IND:'visa-required:0:Schengen visa required', MEX:'visa-free:90 days:Visa-free; Schengen rules apply', GBR:'visa-free:90 days:Visa-free; Schengen rules apply' }},
            'ROU': { name: 'Romania', coords: [45.9, 25.0],
                flags: { USA:'visa-free:90 days:not in Schengen; 90 in any 180-day period', PHL:'visa-required:0:Tourist visa required', CHN:'visa-required:0:Tourist visa required', IND:'visa-required:0:Tourist visa required', MEX:'visa-free:90 days:Visa-free for tourism', GBR:'visa-free:90 days:Visa-free for tourism' }},
            'BGR': { name: 'Bulgaria', coords: [42.7, 25.5],
                flags: { USA:'visa-free:90 days:not in Schengen; 90 in any 180-day period', PHL:'visa-required:0:Tourist visa required', CHN:'visa-required:0:Tourist visa required', IND:'visa-required:0:Tourist visa required', MEX:'visa-free:90 days:Visa-free for tourism', GBR:'visa-free:90 days:Visa-free for tourism' }},
            'HRV': { name: 'Croatia', coords: [45.1, 15.2],
                flags: { USA:'visa-free:90 days:not in Schengen; 90 in any 180-day period', PHL:'visa-required:0:Tourist visa required', CHN:'visa-required:0:Tourist visa required', IND:'visa-required:0:Tourist visa required', MEX:'visa-free:90 days:Visa-free for tourism', GBR:'visa-free:90 days:Visa-free for tourism' }},
            'SVN': { name: 'Slovenia', coords: [46.1, 14.8],
                flags: { USA:'visa-free:90 days:Schengen area', PHL:'visa-required:0:Schengen visa required', CHN:'visa-required:0:Schengen visa required', IND:'visa-required:0:Schengen visa required', MEX:'visa-free:90 days:Visa-free; Schengen rules apply', GBR:'visa-free:90 days:Visa-free; Schengen rules apply' }},
            'SVK': { name: 'Slovakia', coords: [48.7, 19.7],
                flags: { USA:'visa-free:90 days:Schengen area', PHL:'visa-required:0:Schengen visa required', CHN:'visa-required:0:Schengen visa required', IND:'visa-required:0:Schengen visa required', MEX:'visa-free:90 days:Visa-free; Schengen rules apply', GBR:'visa-free:90 days:Visa-free; Schengen rules apply' }},
            'TUR': { name: 'Turkey', coords: [38.9, 35.2],
                flags: { USA:'evisa:90 days:eVisa at evisa.gov.tr', PHL:'evisa:30 days:eVisa available', CHN:'evisa:30 days:eVisa available', IND:'evisa:30 days:eVisa available', MEX:'evisa:90 days:eVisa available', GBR:'evisa:90 days:eVisa available' }},
            'ARE': { name: 'UAE', coords: [23.4, 53.8],
                flags: { USA:'visa-free:90 days:Visa-free for tourism', PHL:'visa-on-arrival:30 days:VOA available', CHN:'evisa:30 days:eVisa available', IND:'evisa:30 days:eVisa available', MEX:'visa-free:90 days:Visa-free for tourism', GBR:'visa-free:30 days:Visa-free for tourism' }},
            'ISR': { name: 'Israel', coords: [31.0, 34.9],
                flags: { USA:'visa-free:90 days:Visa-free for tourism', PHL:'visa-free:90 days:Visa-free for tourism', CHN:'visa-required:0:Tourist visa required', IND:'visa-required:0:Tourist visa required', MEX:'visa-free:90 days:Visa-free for tourism', GBR:'visa-free:90 days:Visa-free for tourism' }},
            'IND': { name: 'India', coords: [20.6, 78.9],
                flags: { USA:'evisa:30 days:eVisa at indianvisaonline.gov.in', PHL:'evisa:30 days:eVisa available', CHN:'evisa:30 days:eVisa available', IND:'visa-free:0:Indian citizens', MEX:'evisa:30 days:eVisa available', GBR:'evisa:30 days:eVisa available' },
                specialZones: [{name:'Ladakh',condition:'Inner Line Permit required',coords:[34.5,77.5]},{name:'Arunachal Pradesh',condition:'Restricted Area Permit required',coords:[28.0,94.0]},{name:'Nagaland & Sikkim',condition:'Special Protected Area Permits',coords:[26.0,94.5]}]},
            'PAK': { name: 'Pakistan', coords: [30.4, 69.3],
                flags: { USA:'evisa:30 days:eVisa available', PHL:'visa-required:0:Tourist visa required', CHN:'evisa:30 days:eVisa available', IND:'visa-required:0:Tourist visa required', MEX:'visa-required:0:Tourist visa required', GBR:'evisa:30 days:eVisa available' }},
            'KAZ': { name: 'Kazakhstan', coords: [48.0, 66.9],
                flags: { USA:'evisa:30 days:eVisa available', PHL:'visa-required:0:Tourist visa required', CHN:'evisa:30 days:eVisa available', IND:'visa-required:0:Tourist visa required', MEX:'visa-required:0:Tourist visa required', GBR:'visa-required:0:Tourist visa required' }},
            'UZB': { name: 'Uzbekistan', coords: [41.4, 64.6],
                flags: { USA:'evisa:30 days:eVisa at evisa.gov.uz', PHL:'evisa:30 days:eVisa available', CHN:'evisa:30 days:eVisa available', IND:'evisa:30 days:eVisa available', MEX:'visa-required:0:Tourist visa required', GBR:'evisa:30 days:eVisa available' }},
            'ZAF': { name: 'South Africa', coords: [-30.6, 22.9],
                flags: { USA:'visa-free:90 days:Visa-free for tourism', PHL:'visa-required:0:Tourist visa required', CHN:'visa-required:0:Tourist visa required', IND:'visa-required:0:Tourist visa required', MEX:'visa-free:90 days:Visa-free for tourism', GBR:'visa-free:30 days:Visa-free for tourism' }},
            'EGY': { name: 'Egypt', coords: [26.8, 30.8],
                flags: { USA:'visa-on-arrival:30 days:VOA at airports', PHL:'visa-on-arrival:30 days:VOA available', CHN:'visa-on-arrival:30 days:VOA available', IND:'visa-on-arrival:30 days:VOA available', MEX:'visa-on-arrival:30 days:VOA available', GBR:'visa-on-arrival:30 days:VOA available' }},
            'MAR': { name: 'Morocco', coords: [31.8, -7.1],
                flags: { USA:'visa-free:90 days:Visa-free for tourism', PHL:'visa-free:90 days:Visa-free for tourism', CHN:'visa-free:90 days:Visa-free for tourism', IND:'visa-required:0:Tourist visa required', MEX:'visa-free:90 days:Visa-free for tourism', GBR:'visa-free:90 days:Visa-free for tourism' }},
            'KEN': { name: 'Kenya', coords: [-0.0, 37.9],
                flags: { USA:'evisa:90 days:eTA at evisa.go.ke', PHL:'evisa:90 days:eTA available', CHN:'evisa:90 days:eTA available', IND:'evisa:90 days:eTA available', MEX:'evisa:90 days:eTA available', GBR:'evisa:90 days:eTA available' }},
            'TZA': { name: 'Tanzania', coords: [-6.4, 34.9],
                flags: { USA:'visa-on-arrival:90 days:VOA at airports', PHL:'visa-on-arrival:90 days:VOA available', CHN:'visa-on-arrival:90 days:VOA available', IND:'visa-on-arrival:90 days:VOA available', MEX:'visa-on-arrival:90 days:VOA available', GBR:'visa-on-arrival:90 days:VOA available' }},
            'NGA': { name: 'Nigeria', coords: [9.1, 8.7],
                flags: { USA:'evisa:90 days:eVisa available', PHL:'evisa:90 days:eVisa available', CHN:'evisa:90 days:eVisa available', IND:'evisa:90 days:eVisa available', MEX:'visa-required:0:Tourist visa required', GBR:'evisa:90 days:eVisa available' }},
            'ETH': { name: 'Ethiopia', coords: [9.1, 40.5],
                flags: { USA:'evisa:90 days:eVisa available', PHL:'evisa:90 days:eVisa available', CHN:'evisa:90 days:eVisa available', IND:'evisa:90 days:eVisa available', MEX:'evisa:90 days:eVisa available', GBR:'evisa:90 days:eVisa available' }},
            'GHA': { name: 'Ghana', coords: [7.9, -1.0],
                flags: { USA:'visa-on-arrival:30 days:VOA available', PHL:'visa-on-arrival:30 days:VOA available', CHN:'visa-required:0:Tourist visa required', IND:'visa-required:0:Tourist visa required', MEX:'visa-on-arrival:30 days:VOA available', GBR:'visa-free:90 days:Visa-free for tourism' }},
            'SEN': { name: 'Senegal', coords: [14.5, -14.5],
                flags: { USA:'visa-free:90 days:Visa-free for tourism', PHL:'visa-free:90 days:Visa-free for tourism', CHN:'visa-free:90 days:Visa-free for tourism', IND:'visa-free:90 days:Visa-free for tourism', MEX:'visa-free:90 days:Visa-free for tourism', GBR:'visa-free:90 days:Visa-free for tourism' }},
            'RWA': { name: 'Rwanda', coords: [-1.9, 29.9],
                flags: { USA:'evisa:30 days:eVisa available', PHL:'evisa:30 days:eVisa available', CHN:'evisa:30 days:eVisa available', IND:'evisa:30 days:eVisa available', MEX:'evisa:30 days:eVisa available', GBR:'evisa:30 days:eVisa available' }},
            'AUS': { name: 'Australia', coords: [-25.3, 133.8],
                flags: { USA:'evisa:90 days:ETA via app', PHL:'evisa:90 days:eVisitor visa (free)', CHN:'evisa:90 days:eVisa (subclass 600)', IND:'evisa:90 days:eVisa (subclass 600)', MEX:'evisa:90 days:eVisa (subclass 600)', GBR:'evisa:90 days:eVisitor visa (free)' }},
            'NZL': { name: 'New Zealand', coords: [-40.9, 174.9],
                flags: { USA:'visa-free:90 days:NZeTA required', PHL:'evisa:90 days:eVisa required', CHN:'evisa:30 days:eVisa required', IND:'evisa:60 days:eVisa required', MEX:'visa-free:90 days:NZeTA required', GBR:'visa-free:90 days:NZeTA required' }},
            'FSM': { name: 'Micronesia', coords: [7.5, 150.5],
                flags: { USA:'visa-free:30 days:COFA - no visa required', PHL:'visa-required:0:Tourist visa required', CHN:'visa-required:0:Tourist visa required', IND:'visa-required:0:Tourist visa required', MEX:'visa-required:0:Tourist visa required', GBR:'visa-required:0:Tourist visa required' }},
            'MHL': { name: 'Marshall Islands', coords: [7.0, 171.0],
                flags: { USA:'visa-free:90 days:COFA - no visa required', PHL:'visa-required:0:Tourist visa required', CHN:'visa-required:0:Tourist visa required', IND:'visa-required:0:Tourist visa required', MEX:'visa-required:0:Tourist visa required', GBR:'visa-required:0:Tourist visa required' }},
            'PLW': { name: 'Palau', coords: [7.5, 134.5],
                flags: { USA:'visa-free:90 days:Visa-free for US citizens', PHL:'visa-free:90 days:Visa-free', CHN:'visa-free:90 days:Visa-free', IND:'visa-free:90 days:Visa-free', MEX:'visa-free:90 days:Visa-free', GBR:'visa-free:90 days:Visa-free' }},
            'MNP': { name: 'N. Mariana Islands (USA)', coords: [15.2, 145.7],
                flags: { USA:'visa-free:0:US territory', PHL:'visa-free:90 days:CNMI-only entry permit', CHN:'visa-free:21 days:CNMI-only visa waiver', IND:'visa-required:0:CNMI entry permit required', MEX:'visa-free:90 days:CNMI-only visa waiver', GBR:'visa-free:90 days:CNMI-only visa waiver' }},
            'GUM': { name: 'Guam (USA)', coords: [13.4, 144.8],
                flags: { USA:'visa-free:0:US territory', PHL:'visa-free:45 days:Guam-CNMI entry permit', CHN:'visa-free:45 days:Guam-CNMI entry permit', IND:'visa-required:0:Entry permit required', MEX:'visa-free:45 days:Guam-CNMI entry permit', GBR:'visa-free:45 days:Guam-CNMI entry permit' }},
            'RUS': { name: 'Russia', coords: [61.5, 105.3],
                flags: { USA:'visa-required:0:B tourist visa required', PHL:'evisa:16 days:eVisa available', CHN:'visa-free:30 days:Valid Chinese passport; group tours', IND:'evisa:16 days:eVisa available', MEX:'visa-required:0:B tourist visa required', GBR:'visa-required:0:B tourist visa required' }},
            'UKR': { name: 'Ukraine', coords: [48.4, 31.2],
                flags: { USA:'visa-free:90 days:Visa-free for tourism', PHL:'visa-free:90 days:Visa-free for tourism', CHN:'visa-required:0:Tourist visa required', IND:'visa-required:0:Tourist visa required', MEX:'visa-free:90 days:Visa-free for tourism', GBR:'visa-free:90 days:Visa-free for tourism' }},
'''

# The countryData object ends after GRC. We need to:
# 1. Change GRC's closing from "}};\n" (end of countryData) to "}},\n" (comma for next entry)
# 2. Insert missing_countries
# 3. Close countryData with "}};\n"

# Pattern: GRC entry ends with '}};\n\n' (closes countryData)
# We'll find that and insert countries in between
# But GRC is the LAST entry, so there's no "next entry" - the }; is the countryData closer
# Solution: find the }; that closes countryData and insert countries before it

# First, find the GRC entry and its flags closing
grc_start = content.find("'GRC':")
if grc_start == -1:
    print("ERROR: GRC not found")
    exit(1)

# Find the }; that closes countryData (it's right after GRC)
# We need to find the first }; after GRC that is followed by \n\n        //
# That is: GRC entry's }}; followed by \n\n        //
search_start = grc_start
# Find "};\n\n        //" pattern
end_pattern = "};\n\n        //"
end_pos = content.find(end_pattern, search_start)

if end_pos == -1:
    # Try variations of whitespace
    end_pos = content.find("};\n\n", search_start)
    if end_pos == -1:
        print("ERROR: Could not find countryData end")
        print("Around GRC:", repr(content[grc_start+100:grc_start+300]))
        exit(1)
    else:
        print("Found }; at:", end_pos)
        print("Context:", repr(content[end_pos-5:end_pos+50]))
else:
    print("Found countryData end at:", end_pos)
    print("Context:", repr(content[end_pos-5:end_pos+30]))

# Insert the missing countries before the closing };\n\n
new_content = content[:end_pos] + "},\n" + missing_countries + "};\n" + content[end_pos+len("};\n\n"):]
print("Inserted", len(missing_countries), "chars of country data")
content = new_content

with open('/home/alethia/.openclaw/workspace/travel-exception-map/index.html', 'w') as f:
    f.write(content)

print("New length:", len(content))

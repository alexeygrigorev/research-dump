"""Region rules copied from historical build_raw/clean_raw; no collector side effects."""
import re
import regions
WORLD = [('CA', '\\b(Canada|CAN|Toronto|Vancouver|Montreal|Montréal|Ottawa|Calgary|Waterloo|Ontario|Quebec|British Columbia|Alberta)\\b'), ('IN', '\\b(India|IND|Bengaluru|Bangalore|Hyderabad|Pune|Chennai|Mumbai|Gurgaon|Gurugram|Noida|Delhi)\\b'), ('LATAM', '\\b(Brazil|BRA|São Paulo|Sao Paulo|Mexico|MEX|Argentina|ARG|Colombia|COL|Chile|CHL|Peru|PER|Uruguay|URY|Costa Rica|Bogot[aá]|Buenos Aires|Latin America|LATAM)\\b'), ('APAC', '\\b(Singapore|SGP|Australia|AUS|Sydney|Melbourne|Japan|JPN|Tokyo|China|CHN|Hong Kong|HKG|Korea|KOR|Seoul|Taiwan|TWN|Philippines|PHL|Vietnam|VNM|Indonesia|IDN|Malaysia|MYS|Thailand|THA|New Zealand|NZL|APAC)\\b'), ('MEA', '\\b(Israel|ISR|Tel Aviv|UAE|ARE|Dubai|Abu Dhabi|Saudi|SAU|Egypt|EGY|Turkey|TUR|Türkiye|Istanbul|Nigeria|NGA|Kenya|KEN|South Africa|ZAF|Cape Town|Morocco|MAR|Pakistan|PAK)\\b')]

WORLD = [(k, re.compile(p, re.I)) for k, p in WORLD]

def region(locations, remote):
    """First location decides: UK | DE | EU | US | CA | IN | LATAM | APAC | MEA | REMOTE | UNKNOWN."""
    for loc in locations or []:
        r = regions.region_of(loc)
        if r:
            return r
        for k, rx in WORLD:
            if rx.search(loc):
                return k
    text = ' '.join(locations or [])
    if remote or re.search('\\bremote\\b|anywhere|worldwide', text, re.I):
        return 'REMOTE'
    return 'UNKNOWN'

ISO3 = {}

for reg, codes in {'US': 'USA', 'CA': 'CAN', 'IN': 'IND', 'UK': 'GBR', 'DE': 'DEU', 'EU': 'POL PRT ESP FRA ROU IRL BGR CZE ITA HUN NLD UKR SWE AUT LTU DNK SRB CHE CYP EST NOR BEL SVN LUX FIN BLR MDA HRV SVK MNE GRC EUR VAT', 'MEA': 'ISR ARE UAE TUR PAK EGY ZAF NGA MAR GHA NAM MWI MOZ KEN BEN GMB IRQ QAT CMR TLV', 'LATAM': 'MEX BRA ARG CHL COL CRI VEN PER URY PRY ECU NIC BLZ JAM', 'APAC': 'SGP NZL PHL MYS AUS JPN VNM HKG TWN IDN THA CHN KOR BGD LKA NPL'}.items():
    for c in codes.split():
        ISO3[c] = reg

def loc_region(loc, bld):
    m = re.fullmatch('(?:[^,]+, )?([A-Z]{3})', loc.strip())
    if m and m.group(1) in ISO3:
        return ISO3[m.group(1)]
    r = bld.region([loc], False)
    return None if r in ('UNKNOWN', 'REMOTE') else r


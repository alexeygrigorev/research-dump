"""Location text -> market region and city.

Regions: UK, DE, US, and EU (all of Europe incl. UK and DE, used when UK or DE alone
is too small for a stable monthly sample; Alexey t3382u "add sources/cities").
Works on free text ("London, England, United Kingdom", "Berlin", "New York, NY") and on
Workday-style slugs ("London-United-Kingdom", "New-York-NY").
"""
import re

US_STATES = ("AL|AK|AZ|AR|CA|CO|CT|DE|FL|GA|HI|ID|IL|IN|IA|KS|KY|LA|ME|MD|MA|MI|MN|MS|MO|MT|NE|NV|NH|NJ|NM|NY|NC|ND|"
             "OH|OK|OR|PA|RI|SC|SD|TN|TX|UT|VT|VA|WA|WV|WI|WY|DC")
UK = re.compile(r"\b(London|United[\s-]Kingdom|UK|GBR|England|Scotland|Wales|Manchester|Edinburgh|Glasgow|Bristol|Leeds|"
                r"Belfast|Birmingham|Cambridge,?[\s-](UK|England|GB)|Oxford|Reading,?[\s-](UK|England))\b", re.I)
DE = re.compile(r"\b(Berlin|Germany|Deutschland|DEU|M(ue|ü)nchen|Munich|Hamburg|Frankfurt|K(oe|ö)ln|Cologne|Stuttgart|"
                r"D(ue|ü)sseldorf|Leipzig|Dresden|Karlsruhe|Nuremberg|N(ue|ü)rnberg|Hannover|Bonn)\b", re.I)
EU_OTHER = re.compile(r"\b(Amsterdam|Netherlands|Rotterdam|Eindhoven|Utrecht|The[\s-]Hague|Dublin|Ireland|Cork|Galway|Paris|"
                      r"France|Lyon|Toulouse|Madrid|Barcelona|Spain|Valencia|Lisbon|Portugal|Porto|Warsaw|Poland|Krak(o|ó)w|"
                      r"Wroc(l|ł)aw|Gda(n|ń)sk|Prague|Czech|Brno|Vienna|Austria|Zurich|Z(ue|ü)rich|Switzerland|Geneva|"
                      r"Lausanne|Stockholm|Sweden|Gothenburg|Copenhagen|Denmark|Oslo|Norway|Helsinki|Finland|Brussels|"
                      r"Belgium|Antwerp|Milan|Italy|Rome|Turin|Bucharest|Romania|Cluj|Budapest|Hungary|Athens|Greece|"
                      r"Sofia|Bulgaria|Tallinn|Estonia|Riga|Latvia|Vilnius|Lithuania|Luxembourg|Belgrade|Serbia|"
                      r"Zagreb|Croatia|Ljubljana|Slovenia|Bratislava|Slovakia|Kyiv|Ukraine|EMEA|Europe)\b", re.I)
US = re.compile(rf"\b(United[\s-]States|USA|US|U\.S\.|New[\s-]York|San[\s-]Francisco|Seattle|Boston|Austin|Chicago|"
                rf"Los[\s-]Angeles|Denver|Atlanta|Remote[\s-]+-?[\s-]*US)\b|[,\s-]({US_STATES})(\b|$)")


def region_of(text):
    """'UK' | 'DE' | 'EU' (other Europe) | 'US' | ''  -- UK and DE also count toward Europe."""
    t = text or ""
    if UK.search(t):
        return "UK"
    if DE.search(t):
        return "DE"
    if EU_OTHER.search(t):
        return "EU"
    if US.search(t):
        return "US"
    return ""


def city_of(text):
    t = (text or "").lower()
    if "london" in t:
        return "london"
    if "berlin" in t:
        return "berlin"
    if re.search(r"new[\s-]york|brooklyn|manhattan|\bnyc\b", t):
        return "newyork"
    return ""


def in_region(region_code, target):
    """Europe = UK + DE + other Europe."""
    return region_code == target or (target == "EUROPE" and region_code in ("UK", "DE", "EU"))

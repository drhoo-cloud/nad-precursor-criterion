#!/usr/bin/env python3
"""
Reproduces the enzyme-naming counts of Table 1C and Appendix S7.7.

Retrieves the 236 records of the primary search, maps them to PubMed Central,
downloads the deposited full text, and counts mentions of NAMPT and NAPRT.

Two scopes are reported. "body" counts the article body only, excluding the
abstract, the reference list and back matter; it is the scope quoted in the
manuscript. "whole" counts every text node of the deposited record. The
asymmetry holds under both.

Requires network access to eutils.ncbi.nlm.nih.gov. Runs in a few minutes.
"""
import urllib.request, urllib.parse, json, time, re, sys
import xml.etree.ElementTree as ET

BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
QUERY = ('((NAD[Title]) AND (nicotinamide OR niacin OR "nicotinic acid" OR NMN OR '
         '"nicotinamide riboside")) AND review[pt] AND 2020:2026[dp]')
NAMPT = re.compile(r'\bNAMPT\b|nicotinamide phosphoribosyltransferase', re.I)
NAPRT = re.compile(r'\bNAPRT1?\b|nicotinic acid phosphoribosyltransferase', re.I)

def get(url, tries=4):
    for k in range(tries):
        try:
            return urllib.request.urlopen(url, timeout=90).read()
        except Exception:
            time.sleep(2 + 2 * k)
    return None

def search():
    u = BASE + "esearch.fcgi?" + urllib.parse.urlencode(
        {"db": "pubmed", "term": QUERY, "retmax": "1000", "retmode": "json"})
    d = json.loads(get(u))["esearchresult"]
    return d["count"], d["idlist"]

def map_to_pmc(pmids):
    """elink returns pubmed_pmc (the record) and pubmed_pmc_refs (records that
    cite it). Only the first is wanted; taking the last match is a silent error."""
    out = {}
    for i in range(0, len(pmids), 30):
        params = ([("dbfrom", "pubmed"), ("db", "pmc"), ("retmode", "json")]
                  + [("id", p) for p in pmids[i:i + 30]])
        raw = get(BASE + "elink.fcgi?" + urllib.parse.urlencode(params))
        if not raw:
            continue
        for ls in json.loads(raw).get("linksets", []):
            pm = str(ls["ids"][0])
            for db in ls.get("linksetdbs", []):
                if db.get("linkname") == "pubmed_pmc" and db.get("links"):
                    out[pm] = db["links"][0]
        time.sleep(0.6)
    return out

def count(pmcs):
    ids = list(pmcs.values())
    body, whole = {}, {}
    for i in range(0, len(ids), 15):
        raw = get(BASE + "efetch.fcgi?" + urllib.parse.urlencode(
            {"db": "pmc", "id": ",".join(ids[i:i + 15]), "retmode": "xml"}))
        if not raw:
            continue
        try:
            root = ET.fromstring(raw)
        except ET.ParseError:
            continue
        for art in root.findall(".//article"):
            pmid = next((a.text.strip() for a in art.findall(".//article-meta/article-id")
                         if a.get("pub-id-type") == "pmid" and a.text), None)
            if not pmid:
                continue
            b = art.find(".//body")
            bt = re.sub(r"\s+", " ", " ".join(b.itertext())) if b is not None else ""
            wt = re.sub(r"\s+", " ", " ".join(art.itertext()))
            if len(bt) > 2000:
                body[pmid] = (len(NAMPT.findall(bt)), len(NAPRT.findall(bt)))
            if len(wt) > 3000:
                whole[pmid] = (len(NAMPT.findall(wt)), len(NAPRT.findall(wt)))
        time.sleep(0.45)
    return body, whole

def report(label, d, quoted):
    a = sum(v[0] for v in d.values())
    b = sum(v[1] for v in d.values())
    z = sum(1 for v in d.values() if v[1] == 0)
    print(f"{label:>6s}  n = {len(d):3d}   NAMPT {a:5d}   NAPRT {b:4d}   "
          f"ratio {a / b:.1f} : 1   never NAPRT {z} ({100 * z / len(d):.0f}%)   {quoted}")

if __name__ == "__main__":
    n, pmids = search()
    print(f"search returned {n} records   (manuscript: 236)")
    pmcs = map_to_pmc(pmids)
    print(f"linked to PubMed Central: {len(pmcs)}")
    body, whole = count(pmcs)
    print()
    report("body", body, "manuscript: 2,973 : 517, 5.8 : 1, 76 (51%)")
    report("whole", whole, "manuscript: 4,893 : 741, 6.6 : 1")

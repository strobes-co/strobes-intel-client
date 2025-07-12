# Strobes Intel Python Client

A comprehensive Python client for accessing vulnerability intelligence data from the [Strobes Intel API](https://intel.strobes.co). This client provides easy access to detailed CVE information, including exploit availability, zero-day status, patch information, and comprehensive vulnerability classifications.

## 🚀 Features

- **Rich CVE Data**: Access detailed vulnerability information from multiple sources (CISA, GitHub Advisory, NVD)
- **Exploit Intelligence**: Real-time exploit availability and references
- **Zero-Day Tracking**: Identify zero-day vulnerabilities with source references
- **Patch Information**: Track patch availability and remediation guidance
- **CVSS Scoring**: Both predicted and official CVSS v2/v3 scores
- **Taxonomy Classification**: CWE, OWASP, NIST, CAPEC, and WASC classifications
- **Social Intelligence**: Twitter trend tracking and social media mentions
- **Priority Scoring**: Intelligent priority scoring for vulnerability triage
- **EPSS Integration**: Exploit Prediction Scoring System data
- **CLI Interface**: Command-line tool for quick vulnerability lookups

## 📦 Installation

```bash
pip install strobes-intel-client
```

### Development Installation

```bash
git clone https://github.com/your-org/strobes-intel-client.git
cd strobes-intel-client
pip install -e .
```

## 🛠️ Usage

### Command Line Interface

Query a specific CVE:

```bash
python -m strobes_intel_client.main -cve CVE-2025-4428
```

### Programmatic Usage

```python
from strobes_intel_client import client, CVE

# Fetch CVE data
cve_data = client("CVE-2025-4428")

# Access key information
print(f"CVE ID: {cve_data.id}")
print(f"CVSS v3 Score: {cve_data.cvss_v3}")
print(f"Priority Score: {cve_data.priority_score}")
print(f"Exploit Available: {cve_data.exploits.exploit_available}")
print(f"Zero-day: {cve_data.zeroday.is_zeroday}")
print(f"Patches Available: {cve_data.patches.patch_available}")

# Iterate through advisories
for advisory in cve_data.advisories:
    print(f"Source: {advisory.name}")
    print(f"Title: {advisory.title}")
    print(f"Summary: {advisory.description.summary}")
```

### Working with Exploit Data

```python
# Check exploit availability
if cve_data.exploits.exploit_available:
    print("⚠️  Exploits are available!")
    for exploit_ref in cve_data.exploits.references:
        print(f"  - {exploit_ref.source}: {exploit_ref.url}")
```

### Zero-Day Detection

```python
# Check for zero-day status
if cve_data.zeroday.is_zeroday:
    print("🚨 This is a zero-day vulnerability!")
    for ref in cve_data.zeroday.references:
        print(f"  Reference: {ref.url}")
```

### Patch Management

```python
# Check patch availability
if cve_data.patches.patch_available:
    print("✅ Patches are available")
    for patch_ref in cve_data.patches.references:
        print(f"  - {patch_ref.type}: {patch_ref.url}")
else:
    print("❌ No patches available")
```

## 📊 Data Structure

### CVE Object

The main CVE object contains comprehensive vulnerability information:

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | CVE identifier (e.g., "CVE-2025-4428") |
| `sources` | array[string] | Data sources (cisa, github_advisory, nvd) |
| `cvss_v2` | float | CVSS v2 base score |
| `cvss_v3` | float | CVSS v3 base score |
| `cvss_v2_vector` | string | CVSS v2 vector string |
| `cvss_v3_vector` | string | CVSS v3 vector string |
| `predicted_cvss_v2` | float | AI-predicted CVSS v2 score |
| `predicted_cvss_v3` | float | AI-predicted CVSS v3 score |
| `priority_score` | integer | Strobes priority score (0-999) |
| `epss_score` | float | EPSS (Exploit Prediction Scoring System) score |
| `seen_wild` | boolean | Whether exploits have been seen in the wild |
| `published` | string | Publication date |
| `last_modified` | string | Last modification date |
| `trend` | integer | Trending score |
| `likes` | integer | Community likes |
| `dislikes` | integer | Community dislikes |
| `cisa_due_date` | string | CISA Known Exploited Vulnerabilities due date |
| `advisories` | array[Advisory] | Security advisories from multiple sources |
| `exploits` | Exploits | Exploit availability information |
| `zeroday` | Zeroday | Zero-day status information |
| `patches` | Patches | Patch availability information |
| `taxonomy` | Taxonomy | Vulnerability classifications |
| `twitter` | Twitter | Social media tracking |
| `tags` | array[string] | Custom tags |
| `vulnerable_products` | array[VulnerableProducts] | Affected products |

### Advisory Object

Contains security advisory information from various sources:

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Advisory identifier |
| `name` | string | Source name (cisa, github_advisory, nvd) |
| `title` | string | Advisory title |
| `description` | Description | Advisory description with metadata |
| `cvss_v2` | float | CVSS v2 score from this source |
| `cvss_v3` | float | CVSS v3 score from this source |
| `cvss_v2_vector` | string | CVSS v2 vector from this source |
| `cvss_v3_vector` | string | CVSS v3 vector from this source |
| `cpe` | array[string] | Common Platform Enumeration identifiers |
| `remediation` | string | Remediation guidance |
| `impact` | string | Impact assessment |
| `exploitability_score_v2` | float | CVSS v2 exploitability subscore |
| `exploitability_score_v3` | float | CVSS v3 exploitability subscore |
| `impact_score_v2` | float | CVSS v2 impact subscore |
| `impact_score_v3` | float | CVSS v3 impact subscore |
| `references` | array[Reference] | Reference links |
| `assigner` | string | CVE assigner organization |

### Exploits Object

Information about exploit availability:

| Field | Type | Description |
|-------|------|-------------|
| `exploit_available` | boolean | Whether exploits are publicly available |
| `references` | array[Reference] | Links to exploit code and tools |

### Zeroday Object

Zero-day vulnerability tracking:

| Field | Type | Description |
|-------|------|-------------|
| `is_zeroday` | boolean | Whether this is classified as a zero-day |
| `references` | array[Reference] | Zero-day classification references |

### Patches Object

Patch availability information:

| Field | Type | Description |
|-------|------|-------------|
| `patch_available` | boolean | Whether patches are available |
| `references` | array[Reference] | Links to patches and advisories |

### Reference Object

Reference links with metadata:

| Field | Type | Description |
|-------|------|-------------|
| `url` | string | Reference URL |
| `type` | string | Reference type (WEB, ADVISORY, EXPLOIT_REF, etc.) |
| `source` | string | Reference source |

### Taxonomy Object

Vulnerability classification across multiple frameworks:

| Field | Type | Description |
|-------|------|-------------|
| `cwe` | array[CWE] | Common Weakness Enumeration |
| `predicted_cwe` | array[CWE] | AI-predicted CWE classifications |
| `owasp_2021` | array[OWASP] | OWASP Top 10 2021 classifications |
| `owasp_2007` | array[OWASP] | OWASP Top 10 2007 classifications |
| `owasp_2004` | array[OWASP] | OWASP Top 10 2004 classifications |
| `nist` | array[NIST] | NIST framework classifications |
| `capec` | array[CAPEC] | Common Attack Pattern Enumeration |
| `wasc` | array[WASC] | Web Application Security Consortium |

### Twitter Object

Social media tracking:

| Field | Type | Description |
|-------|------|-------------|
| `trending_now` | boolean | Currently trending on Twitter |
| `last_trending_at` | string | Last time this CVE was trending |
| `tweet_count` | integer | Number of tweets mentioning this CVE |

## 🔍 Advanced Examples

### Filtering High-Priority CVEs

```python
from strobes_intel_client import client

def analyze_cve(cve_id):
    cve = client(cve_id)
    
    # High priority indicators
    is_high_priority = (
        cve.priority_score > 800 or
        cve.exploits.exploit_available or
        cve.zeroday.is_zeroday or
        cve.cvss_v3 > 8.0
    )
    
    if is_high_priority:
        print(f"🚨 HIGH PRIORITY: {cve.id}")
        print(f"   Priority Score: {cve.priority_score}")
        print(f"   CVSS v3: {cve.cvss_v3}")
        print(f"   Exploits: {'Yes' if cve.exploits.exploit_available else 'No'}")
        print(f"   Zero-day: {'Yes' if cve.zeroday.is_zeroday else 'No'}")
        
        if cve.cisa_due_date:
            print(f"   CISA Due Date: {cve.cisa_due_date}")
    
    return is_high_priority

# Example usage
analyze_cve("CVE-2025-4428")
```

### Vulnerability Intelligence Summary

```python
def vulnerability_summary(cve_id):
    cve = client(cve_id)
    
    print(f"=== {cve.id} Vulnerability Intelligence ===")
    print(f"Published: {cve.published}")
    print(f"Last Modified: {cve.last_modified}")
    print(f"Priority Score: {cve.priority_score}/999")
    print(f"EPSS Score: {cve.epss_score}")
    print(f"CVSS v3: {cve.cvss_v3} ({cve.cvss_v3_vector})")
    
    print(f"\n📊 Threat Intelligence:")
    print(f"  Exploits Available: {'Yes' if cve.exploits.exploit_available else 'No'}")
    print(f"  Zero-day Status: {'Yes' if cve.zeroday.is_zeroday else 'No'}")
    print(f"  Patches Available: {'Yes' if cve.patches.patch_available else 'No'}")
    print(f"  Seen in Wild: {'Yes' if cve.seen_wild else 'No'}")
    
    if cve.taxonomy.cwe:
        print(f"\n🏷️  Classifications:")
        for cwe in cve.taxonomy.cwe:
            print(f"  CWE-{cwe.id}: {cwe.description}")
    
    print(f"\n📈 Social Intelligence:")
    print(f"  Trending: {'Yes' if cve.twitter.trending_now else 'No'}")
    print(f"  Tweet Count: {cve.twitter.tweet_count}")
    
    print(f"\n📝 Sources: {', '.join(cve.sources)}")
    
    return cve

# Example usage
vulnerability_summary("CVE-2025-4428")
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Run tests (`python -m pytest`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Development Setup

```bash
git clone https://github.com/your-org/strobes-intel-client.git
cd strobes-intel-client
pip install -e ".[dev]"
```

### Running Tests

```bash
python -m pytest tests/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

- **Documentation**: [https://intel.strobes.co/docs](https://intel.strobes.co/docs)
- **Issues**: [GitHub Issues](https://github.com/your-org/strobes-intel-client/issues)
- **Email**: support@strobes.co

## 🏆 Acknowledgments

- [Strobes Security](https://strobes.co) for providing the intelligence API
- The cybersecurity community for vulnerability research and disclosure
- All contributors who help improve this client

---

**⚠️ Security Notice**: This tool provides access to vulnerability intelligence data. Always verify information from multiple sources and follow responsible disclosure practices when handling vulnerability data.

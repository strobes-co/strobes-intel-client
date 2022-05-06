# Strobes Intel Python Client

## CVE

### Properties

- **`cve`** *(string)*
- **`predicted_cvss_v2`** *(float)*
- **`predicted_cvss_v3`** *(float)*
- **`advisories`** *(array of objects)*
  - **Items**: Refer to [`Advisory`](#advisory) object
- **`exploits`**: Refer to [`Exploits`](#exploits) object
- **`zeroday`**: Refer to [`Zeroday`](#zeroday) object
- **`patches`**: Refer to [`Patches`](#patches) object
- **`tags`** *(array of strings)*
- **`vulnerable_products`** *(array of objects)*
  - **Items**: Refer to [`VulnerableProducts`](#vulnerableproducts) object
- **`taxonomy`**: Refer to [`Taxonomy`](#taxonomy) object
- **`twitter`**: Refer to [`Twitter`](#twitter) object
- **`seen_wild`** *(boolean)*
- **`priority_score`** *(integer)*

## Definitions

### Advisory

- **`id`** *(string)*
- **`name`** *(string)*
- **`title`** *(string)*
- **`description`**: Refer to [`Description`](#description) object
- **`cvss_v2`** *(float)*
- **`cvss_v3`** *(float)*
- **`cvss_v2_vector`** *(string)*
- **`cvss_v3_vector`** *(string)*
- **`cpe`** *(array of strings)*
- **`exploitability_score_v2`** *(float)*
- **`exploitability_score_v3`** *(float)*
- **`impact_score_v2`** *(float)*
- **`impact_score_v3`** *(float)*
- **`references`** *(array of objects)*
  - **Items**: Refer to [`Reference`](#reference) object

### Description

- **`summary`** *(string)*
- **`published`** *(string)*
- **`last_modified`** *(string)*

### Exploits

- **`exploit_available`** *(boolean)*
- **`references`** *(array of objects)*
  - **Items**: Refer to [`Reference`](#reference) object

### Zeroday

- **`is_zeroday`** *(boolean)*
- **`references`** *(array of objects)*
  - **Items**: Refer to [`Reference`](#reference) object

### Patches

- **`patch_available`** *(boolean)*
- **`references`** *(array of objects)*
  - **Items**: Refer to [`Reference`](#reference) object

### Reference

- **`url`** *(string)*
- **`type`** *(string)*
- **`source`** *(string)*

### VulnerableProducts

- **`id`** *(string)*
- **`name`** *(string)*
- **`ecosystem`** *(string)*
- **`type`** *(string)*
- **`product_family`** *(string)*
- **`affected_versions`** *(array of objects)*
  - **Items**: Refer to [`Version`](#version) object

### Version

- **`fixed`** *(string)*
- **`introduced`** *(string)*

### Twitter

- **`trending_now`** *(boolean)*
- **`last_trending_at`** *(string)*
- **`tweet_count`** *(integer)*

### Taxonomy

- **`cwe`** *(array of objects)*
  - **Items**: Refer to [`CWE`](#cwe) object
- **`predicted_cwe`** *(array of objects)*
  - **Items**: Refer to [`CWE`](#cwe) object
- **`owasp_2007`** *(array of objects)*
  - **Items**: Refer to [`OWASP`](#owasp) object
- **`owasp_2004`** *(array of objects)*
  - **Items**: Refer to [`OWASP`](#owasp) object
- **`nist`** *(array of objects)*
  - **Items**: Refer to [`NIST`](#nist) object
- **`capec`** *(array of objects)*
  - **Items**: Refer to [`CAPEC`](#capec) object
- **`wasc`** *(array of objects)*
  - **Items**: Refer to [`WASC`](#wasc) object

### CWE

- **`id`** *(string)*
- **`description`** *(string)*

### OWASP

- **`id`** *(string)*
- **`description`** *(string)*

### NIST

- **`id`** *(string)*
- **`description`** *(string)*

### CAPEC

- **`id`** *(string)*
- **`description`** *(string)*

### WASC

- **`id`** *(string)*
- **`description`** *(string)*

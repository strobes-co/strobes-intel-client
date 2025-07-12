# Changelog

## v0.1.0 (2025-01-XX)

### 🚀 Major Updates

- **BREAKING CHANGE**: Updated to use new Strobes Intel API endpoint (`/api/cve/` instead of `/api/nvd/`)
- **BREAKING CHANGE**: Updated data models to match new API response structure
- **NEW**: Added support for multiple vulnerability data sources (CISA, GitHub Advisory, NVD)
- **NEW**: Enhanced CVE model with comprehensive vulnerability intelligence

### ✨ New Features

- **Exploit Intelligence**: Real-time exploit availability tracking with references
- **Zero-Day Detection**: Automatic zero-day vulnerability identification
- **Patch Management**: Track patch availability and remediation guidance
- **EPSS Integration**: Exploit Prediction Scoring System data
- **Enhanced CVSS**: Support for both CVSS v2 and v3 with vector strings
- **Social Intelligence**: Twitter trend tracking and social media mentions
- **Priority Scoring**: Intelligent priority scoring (0-999) for vulnerability triage
- **CISA KEV**: Integration with CISA Known Exploited Vulnerabilities catalog
- **Multi-Source Advisories**: Comprehensive advisory information from multiple sources

### 🔧 Technical Improvements

- **Pydantic v2 Compatibility**: Updated to use `model_dump_json()` for JSON serialization
- **Enhanced Error Handling**: Added `response.raise_for_status()` for better error reporting
- **Improved Package Structure**: Added proper exports in `__init__.py`
- **Field Additions**: Added `sources`, `remediation`, `impact`, `assigner`, `owasp_2021`, `trend`, `likes`, `dislikes`, `cisa_due_date`, `epss_score`
- **Type Safety**: Improved type annotations and optional field handling

### 📊 Data Model Updates

- **CVE Object**: Updated primary field from `cve` to `id` with `_id` alias
- **Advisory Object**: Added `remediation`, `impact`, and `assigner` fields
- **Taxonomy Object**: Added OWASP 2021 classifications
- **New Metadata**: Added publishing timestamps, trending data, and community engagement metrics

### 🛠️ API Changes

- **Endpoint Migration**: Changed from `https://intel.strobes.co/api/nvd/` to `https://intel.strobes.co/api/cve/`
- **Response Format**: Updated to handle new JSON structure with expanded metadata
- **Error Handling**: Improved HTTP error handling and status code checking

### 📝 Documentation

- **Complete README Rewrite**: Comprehensive documentation with examples, tables, and usage guides
- **API Reference**: Detailed field descriptions and data structure documentation
- **Code Examples**: Advanced usage examples for vulnerability analysis and intelligence gathering
- **Migration Guide**: Implicit breaking changes documented in README

### 🔒 Security Enhancements

- **Responsible Disclosure**: Added security notice about proper vulnerability data handling
- **Source Verification**: Support for multiple authoritative sources (CISA, NVD, GitHub)
- **Data Validation**: Enhanced Pydantic models with proper field validation

## v0.0.1

- Strobe Intel Client is introduced, with basic feature of getting data from Strobe Intel.

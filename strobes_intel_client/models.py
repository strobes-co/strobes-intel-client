from typing import List, Optional
from pydantic import Field, BaseModel


class Reference(BaseModel):
    """
    Embedded model for reference
    """

    source: Optional[str]
    type: str = Field(default="MISC")
    url: str = Field(required=True)


class Exploits(BaseModel):
    """
    Embedded model for exploits
    """

    exploit_available: bool = Field(default=False)
    references: List[Reference] = Field(default=[])


class Zeroday(BaseModel):
    """
    Embedded model for zeroday
    """

    is_zeroday: bool = Field(default=False)
    references: List[Reference] = Field(default=[])


class Patches(BaseModel):
    """
    Embedded model for patches
    """

    patch_available: bool = Field(default=False)
    references: List[Reference] = Field(default=[])


class Description(BaseModel):
    summary: Optional[str] = Field(default=None)
    published: Optional[str] = Field(default=None)
    last_modified: Optional[str] = Field(default=None)


class Version(BaseModel):
    fixed: Optional[str]
    introduced: Optional[str]


class VulnerableProducts(BaseModel):
    id: Optional[str] = Field(default=None)
    name: str
    ecosystem: str
    type: str
    product_family: Optional[str] = Field(default=None)
    affected_versions: List[Version] = Field(default=[])


class CWE(BaseModel):
    id: str
    description: Optional[str]


class OWASP(BaseModel):
    id: str
    description: Optional[str]


class NIST(BaseModel):
    id: str
    description: Optional[str]


class CAPEC(BaseModel):
    id: str
    description: Optional[str]


class WASC(BaseModel):
    id: str
    description: Optional[str]


class Taxonomy(BaseModel):
    cwe: List[CWE] = Field(default=[])
    predicted_cwe: List[CWE] = Field(default=[])
    owasp_2007: List[OWASP] = Field(default=[])
    owasp_2004: List[OWASP] = Field(default=[])
    nist: List[NIST] = Field(default=[])
    capec: List[CAPEC] = Field(default=[])
    wasc: List[WASC] = Field(default=[])


class Advisory(BaseModel):
    id: Optional[str] = Field(default=None)
    name: Optional[str] = Field(default=None)
    title: Optional[str] = Field(default=None)
    description: Description = Field(default=Description())
    cvss_v2: Optional[float] = Field(default=None)
    cvss_v3: Optional[float] = Field(default=None)
    cvss_v2_vector: Optional[str] = Field(default=None)
    cvss_v3_vector: Optional[str] = Field(default=None)
    cpe: List[str] = Field(default=[])
    exploitability_score_v2: Optional[float] = Field(default=None)
    impact_score_v2: Optional[float] = Field(default=None)
    exploitability_score_v3: Optional[float] = Field(default=None)
    impact_score_v3: Optional[float] = Field(default=None)
    references: List[Reference] = Field(default=[])


class Twitter(BaseModel):
    trending_now: bool = Field(default=False)
    last_trending_at: Optional[str] = Field(default=None)
    tweet_count: int = Field(default=0)


class CVE(BaseModel):
    cve: str = Field(primary_field=True)
    advisories: List[Advisory] = Field(default=[])
    predicted_cvss_v2: Optional[float] = Field(default=None)
    predicted_cvss_v3: Optional[float] = Field(default=None)
    exploits: Exploits = Field(default=Exploits())
    zeroday: Zeroday = Field(default=Zeroday())
    patches: Patches = Field(default=Patches())
    tags: List[str] = Field(default=[])
    vulnerable_products: List[VulnerableProducts] = Field(default=[])
    taxonomy: Taxonomy = Field(default=Taxonomy())
    twitter: Twitter = Field(default=Twitter())
    seen_wild: bool = Field(default=False)
    priority_score: int = Field(default=None)

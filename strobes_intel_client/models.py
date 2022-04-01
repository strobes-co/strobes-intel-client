from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field


class Exploits(BaseModel):
    exploit_available: Optional[bool] = Field(default=False)
    references: List[str]


class Zeroday(BaseModel):
    is_zeroday: Optional[bool] = Field(default=False)
    references: List[str]


class Patches(BaseModel):
    patch_available: Optional[bool] = Field(default=False)
    references: List[str]


class VulnerableProducts(BaseModel):
    id: str
    name: str
    vendor: str
    product_family: str


class CVE(BaseModel):
    cve: str = Field(primary_field=True)
    nvd: Dict[str, Any]
    exploits: Exploits
    zeroday: Zeroday
    patches: Patches
    vulnerable_products: List[VulnerableProducts]

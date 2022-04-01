# CVE

## Properties

- **`cve`** *(string)*
- **`nvd`** *(object)*
- **`exploits`**: Refer to *#/definitions/Exploits*.
- **`zeroday`**: Refer to *#/definitions/Zeroday*.
- **`patches`**: Refer to *#/definitions/Patches*.
- **`vulnerable_products`** *(array)*
  - **Items**: Refer to *#/definitions/VulnerableProducts*.
## Definitions

- **`Exploits`** *(object)*
  - **`exploit_available`** *(boolean)*: Default: `False`.
  - **`references`** *(array)*
    - **Items** *(string)*
- **`Zeroday`** *(object)*
  - **`is_zeroday`** *(boolean)*: Default: `False`.
  - **`references`** *(array)*
    - **Items** *(string)*
- **`Patches`** *(object)*
  - **`patch_available`** *(boolean)*: Default: `False`.
  - **`references`** *(array)*
    - **Items** *(string)*
- **`VulnerableProducts`** *(object)*
  - **`id`** *(string)*
  - **`name`** *(string)*
  - **`vendor`** *(string)*
  - **`product_family`** *(string)*

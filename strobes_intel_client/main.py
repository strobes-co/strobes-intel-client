import requests
from strobes_intel_client.models import CVE
from strobes_intel_client.input import parse_args


def client(cve: str) -> CVE:
    """
    Function that fetches cve data from strobes intel

    Args:
        cve (str): CVE to query

    Returns:
        CVE: CVE object using pydantic model
    """
    url = "https://intel.strobes.co/api/cve/"
    response = requests.get(url + cve)
    response.raise_for_status()  # Raise an exception for bad status codes
    return CVE(**response.json())


def main():
    arguments, unknown = parse_args()
    cve = arguments.cve
    if cve:
        print(client(cve).model_dump_json(indent=4))


if __name__ == "__main__":
    main()

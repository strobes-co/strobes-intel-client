import requests
from .input import parse_args
from .models import CVE


def client(cve: str):
    url = "https://intel.strobes.co/api/nvd/"
    response = requests.get(url + cve)
    return CVE(**response.json())


def main():
    arguments, unknown = parse_args()


if __name__ == "__main__":
    main()

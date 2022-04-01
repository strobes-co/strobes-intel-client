from argparse import ArgumentParser, Namespace
from typing import List, Tuple


def parse_args() -> Tuple[Namespace, List[str]]:
    """Function that parses arguments from command line
    Returns:
        Tuple[Namespace, List[str]]: Known arguments will be passed
        passed in Namespace object while unknown will be passed in list
    """
    parser = ArgumentParser()

    parser.add_argument("-cve", dest="cve", type=str, help="Give CVE to query")

    args, unknown = parser.parse_known_args()

    return args, unknown

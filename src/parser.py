import argparse

def get_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-u",
        "--username",
        type=str,
        default="cr7",
        help="Define insta profile",
        required=False,
    )
    
        
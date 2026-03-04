import sys

import pytest
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    sys.exit(pytest.main(["-s"]))

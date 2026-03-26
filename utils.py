import re

def filter_logs(content):
    """Extracts only high-priority lines related to CSME, FSP, and Servod."""
    patterns = [
        r'error', r'fail', r'fatal', r'timeout', 
        r'csme', r'fsp', r'servod', r'exception'
    ]
    lines = content.splitlines()
    filtered = [line for line in lines if any(re.search(p, line, re.I) for p in patterns)]
    # Return last 20 critical lines to maintain context window
    return "\n".join(filtered[-20:])
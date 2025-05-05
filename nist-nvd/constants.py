"""
Copyright start
MIT License
Copyright (c) 2025 Fortinet Inc
Copyright end
"""

# List of parameters required for CVE advance search
SEARCH_FLAG_LIST = [
    'isVulnerable',
    'keywordExactMatch'
]

SEARCH_FLAG_DICT = {
    'Has KEV': 'hasKev',
    'Has Technical Alerts': 'hasCertAlerts',
    'Has Cert Notes': 'hasCertNotes',
    'Has Oval': 'hasOval'
}

# List of parameters required to be removed before making REST API call
EXCLUDE_LIST = [
    'useCpeName',
    'useCweId',
    'useCVSSv2',
    'useCVSSv3',
    'usePublishDate',
    'useLastModDate',
    'useChangeDate',
    'filterBy',
    'useSearchFlags',
    'useCveId'
]
WAIT_TIME=10
MAX_RETRIES=5
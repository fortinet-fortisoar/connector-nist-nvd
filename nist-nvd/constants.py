"""
Copyright start
Copyright (C) 2008 - 2023 Fortinet Inc.
All rights reserved.
FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
Copyright end
"""

# List of parameters required for CVE advance search
SEARCH_FLAG_LIST = [
    'isVulnerable',
    'hasKev',
    'hasCertAlerts',
    'hasCertNotes',
    'hasOval',
    'keywordExactMatch'
]

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
    'useSearchFlags'
]

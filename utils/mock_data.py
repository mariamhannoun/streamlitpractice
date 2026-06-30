MOCK_RESULT = {

    "overall_status": "FAIL",       # "PASS" | "FAIL" | "PARTIAL"
    "confidence_score": 68,
    "criteria": [
        {
            "name": "Applicant Email Valid",
            "passed": False,
            "severity": "critical",
            "detail": "Email 'john.smith@council..nsw.gov.au' is malformed."
        },
        {
            "name": "Address Within NSW",
            "passed": True,
            "severity": "critical",
            "detail": "Postcode 2650 confirmed within NSW."
        },
        {
            "name": "ABN Present and Valid",
            "passed": True,
            "severity": "critical",
            "detail": "ABN passes checksum validation."
        },
        {
            "name": "Applicant Name Populated",
            "passed": False,
            "severity": "critical",
            "detail": "Council name field is empty."
        },
        {
            "name": "Pre-Disaster Function Documented",
            "passed": True,
            "severity": "critical",
            "detail": "Asset function described on page 3."
        },
        {
            "name": "Estimated Reconstruction Cost Present",
            "passed": True,
            "severity": "critical",
            "detail": "Cost estimate found: $240,000."
        },
        {
            "name": "Project Management Cost ≤30%",
            "passed": False,
            "severity": "warning",
            "detail": "PM costs appear to exceed 30% of total — review recommended."
        }
    ]
}
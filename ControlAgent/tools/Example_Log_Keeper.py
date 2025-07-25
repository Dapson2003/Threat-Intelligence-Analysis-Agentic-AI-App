#Example_Log_Keeper.py
example_log_body = {
          "node": {
            "id": "ea9632d7-8202-4b1d-92f1-d2ea18b542cf",
            "alert_id": "YOMA-2503-000769",
            "alert_name": "WINDOWS METHODOLOGY [UAC Bypass via Sdclt.exe] on host yb-lt2338.yomabank.org",
            "tags": "Alert",
            "incident_type": None,
            "severity": "High",
            "alert_status": "Closed",
            "log_source": "Trellix Helix",
            "case_result": "FalsePositives",
            "detected_time": "2025-03-20T01:11:38.959Z",
            "mitre": [
              {
                "id": "T1112",
                "link": "https://attack.mitre.org/techniques/T1112",
                "name_tactics": "Defense Evasion",
                "name_technique": "Modify Registry",
                "name_subtechnique": None
              },
              {
                "id": "T1548.002",
                "link": "https://attack.mitre.org/techniques/T1548/002",
                "name_tactics": "Defense Evasion",
                "name_technique": "Abuse Elevation Control Mechanism",
                "name_subtechnique": "Bypass User Account Control"
              },
              {
                "id": "T1548.002",
                "link": "https://attack.mitre.org/techniques/T1548/002",
                "name_tactics": "Privilege Escalation",
                "name_technique": "Abuse Elevation Control Mechanism",
                "name_subtechnique": "Bypass User Account Control"
              },
              {
                "id": "T1548",
                "link": "https://attack.mitre.org/techniques/T1548",
                "name_tactics": "Defense Evasion",
                "name_technique": "Abuse Elevation Control Mechanism",
                "name_subtechnique": None
              },
              {
                "id": "T1548",
                "link": "https://attack.mitre.org/techniques/T1548",
                "name_tactics": "Privilege Escalation",
                "name_technique": "Abuse Elevation Control Mechanism",
                "name_subtechnique": None
              }
            ],
            "objectMarking": [
              {
                "id": "3732dad0-3d47-4a09-9378-674e7385767a",
                "definition": "YOMA BANK"
              }
            ],
            "contexts": {
              "domain": None,
              "endpoint_type": None,
              "os": "windows 11 22631",
              "user": "yb-lt2338$",
              "user_priv": None,
              "src_ip": [
                "192.168.100.28"
              ]
            },
            "events": [
              {
                "domain": None,
                "dst_ip": None,
                "dst_port": None,
                "src_ip": None,
                "src_port": None,
                "user": None,
                "ip_malicious": None,
                "hash_malicious": None,
                "hash": {
                  "sha1": None,
                  "sha256": None,
                  "md5": None
                },
                "file_name": "c:\\users\\moetheingioo\\appdata\\local\\microsoft\\onedrive\\25.031.0217.0003\\filecoauth.exe",
                "file_size": None,
                "file_path": None,
                "cmd_line": "\"C:\\Users\\moetheingioo\\AppData\\Local\\Microsoft\\OneDrive\\25.031.0217.0003\\FileCoAuth.exe\" -Embedding",
                "parent_process": "c:\\windows\\system32\\svchost.exe",
                "event_type": "audit_success"
              },
              {
                "domain": None,
                "dst_ip": None,
                "dst_port": None,
                "src_ip": None,
                "src_port": None,
                "user": None,
                "ip_malicious": None,
                "hash_malicious": None,
                "hash": {
                  "sha1": None,
                  "sha256": None,
                  "md5": None
                },
                "file_name": "c:\\users\\moetheingioo\\appdata\\local\\microsoft\\onedrive\\25.031.0217.0003\\filecoauth.exe",
                "file_size": None,
                "file_path": None,
                "cmd_line": "\"C:\\Users\\moetheingioo\\AppData\\Local\\Microsoft\\OneDrive\\25.031.0217.0003\\FileCoAuth.exe\" -Embedding",
                "parent_process": "c:\\windows\\system32\\svchost.exe",
                "event_type": "audit_success"
              },
              {
                "domain": None,
                "dst_ip": None,
                "dst_port": None,
                "src_ip": None,
                "src_port": None,
                "user": None,
                "ip_malicious": None,
                "hash_malicious": None,
                "hash": {
                  "sha1": None,
                  "sha256": None,
                  "md5": None
                },
                "file_name": "c:\\users\\moetheingioo\\appdata\\local\\microsoft\\onedrive\\25.031.0217.0003\\filecoauth.exe",
                "file_size": None,
                "file_path": None,
                "cmd_line": "\"C:\\Users\\moetheingioo\\AppData\\Local\\Microsoft\\OneDrive\\25.031.0217.0003\\FileCoAuth.exe\" -Embedding",
                "parent_process": "c:\\windows\\system32\\svchost.exe",
                "event_type": "audit_success"
              },
              {
                "domain": None,
                "dst_ip": None,
                "dst_port": None,
                "src_ip": None,
                "src_port": None,
                "user": None,
                "ip_malicious": None,
                "hash_malicious": None,
                "hash": {
                  "sha1": None,
                  "sha256": None,
                  "md5": None
                },
                "file_name": "c:\\users\\moetheingioo\\appdata\\local\\microsoft\\onedrive\\25.031.0217.0003\\filecoauth.exe",
                "file_size": None,
                "file_path": None,
                "cmd_line": "\"C:\\Users\\moetheingioo\\AppData\\Local\\Microsoft\\OneDrive\\25.031.0217.0003\\FileCoAuth.exe\" -Embedding",
                "parent_process": "c:\\windows\\system32\\svchost.exe",
                "event_type": "audit_success"
              },
              {
                "domain": None,
                "dst_ip": None,
                "dst_port": None,
                "src_ip": None,
                "src_port": None,
                "user": None,
                "ip_malicious": None,
                "hash_malicious": None,
                "hash": {
                  "sha1": None,
                  "sha256": None,
                  "md5": None
                },
                "file_name": "c:\\users\\moetheingioo\\appdata\\local\\microsoft\\onedrive\\25.031.0217.0003\\filecoauth.exe",
                "file_size": None,
                "file_path": None,
                "cmd_line": "\"C:\\Users\\moetheingioo\\AppData\\Local\\Microsoft\\OneDrive\\25.031.0217.0003\\FileCoAuth.exe\" -Embedding",
                "parent_process": "c:\\windows\\system32\\svchost.exe",
                "event_type": "audit_success"
              },
              {
                "domain": None,
                "dst_ip": None,
                "dst_port": None,
                "src_ip": None,
                "src_port": None,
                "user": None,
                "ip_malicious": None,
                "hash_malicious": None,
                "hash": {
                  "sha1": None,
                  "sha256": None,
                  "md5": None
                },
                "file_name": "c:\\users\\moetheingioo\\appdata\\local\\microsoft\\onedrive\\25.031.0217.0003\\filecoauth.exe",
                "file_size": None,
                "file_path": None,
                "cmd_line": "\"C:\\Users\\moetheingioo\\AppData\\Local\\Microsoft\\OneDrive\\25.031.0217.0003\\FileCoAuth.exe\" -Embedding",
                "parent_process": "c:\\windows\\system32\\svchost.exe",
                "event_type": "audit_success"
              },
              {
                "domain": None,
                "dst_ip": None,
                "dst_port": None,
                "src_ip": None,
                "src_port": None,
                "user": None,
                "ip_malicious": None,
                "hash_malicious": None,
                "hash": {
                  "sha1": None,
                  "sha256": None,
                  "md5": None
                },
                "file_name": "c:\\users\\moetheingioo\\appdata\\local\\microsoft\\onedrive\\25.031.0217.0003\\filecoauth.exe",
                "file_size": None,
                "file_path": None,
                "cmd_line": "\"C:\\Users\\moetheingioo\\AppData\\Local\\Microsoft\\OneDrive\\25.031.0217.0003\\FileCoAuth.exe\" -Embedding",
                "parent_process": "c:\\windows\\system32\\svchost.exe",
                "event_type": "audit_success"
              },
              {
                "domain": None,
                "dst_ip": None,
                "dst_port": None,
                "src_ip": None,
                "src_port": None,
                "user": None,
                "ip_malicious": None,
                "hash_malicious": None,
                "hash": {
                  "sha1": None,
                  "sha256": None,
                  "md5": None
                },
                "file_name": "c:\\users\\moetheingioo\\appdata\\local\\microsoft\\onedrive\\25.031.0217.0003\\filecoauth.exe",
                "file_size": None,
                "file_path": None,
                "cmd_line": "\"C:\\Users\\moetheingioo\\AppData\\Local\\Microsoft\\OneDrive\\25.031.0217.0003\\FileCoAuth.exe\" -Embedding",
                "parent_process": "c:\\windows\\system32\\svchost.exe",
                "event_type": "audit_success"
              },
              {
                "domain": None,
                "dst_ip": None,
                "dst_port": None,
                "src_ip": None,
                "src_port": None,
                "user": None,
                "ip_malicious": None,
                "hash_malicious": None,
                "hash": {
                  "sha1": None,
                  "sha256": None,
                  "md5": None
                },
                "file_name": "c:\\users\\moetheingioo\\appdata\\local\\microsoft\\onedrive\\25.031.0217.0003\\filecoauth.exe",
                "file_size": None,
                "file_path": None,
                "cmd_line": "\"C:\\Users\\moetheingioo\\AppData\\Local\\Microsoft\\OneDrive\\25.031.0217.0003\\FileCoAuth.exe\" -Embedding",
                "parent_process": "c:\\windows\\system32\\svchost.exe",
                "event_type": "audit_success"
              },
              {
                "domain": None,
                "dst_ip": None,
                "dst_port": None,
                "src_ip": None,
                "src_port": None,
                "user": None,
                "ip_malicious": None,
                "hash_malicious": None,
                "hash": {
                  "sha1": None,
                  "sha256": None,
                  "md5": None
                },
                "file_name": "c:\\users\\moetheingioo\\appdata\\local\\microsoft\\onedrive\\25.031.0217.0003\\filecoauth.exe",
                "file_size": None,
                "file_path": None,
                "cmd_line": "\"C:\\Users\\moetheingioo\\AppData\\Local\\Microsoft\\OneDrive\\25.031.0217.0003\\FileCoAuth.exe\" -Embedding",
                "parent_process": "c:\\windows\\system32\\svchost.exe",
                "event_type": "audit_success"
              },
              {
                "domain": None,
                "dst_ip": None,
                "dst_port": None,
                "src_ip": None,
                "src_port": None,
                "user": None,
                "ip_malicious": None,
                "hash_malicious": None,
                "hash": {
                  "sha1": None,
                  "sha256": None,
                  "md5": None
                },
                "file_name": "c:\\users\\moetheingioo\\appdata\\local\\microsoft\\onedrive\\25.031.0217.0003\\filecoauth.exe",
                "file_size": None,
                "file_path": None,
                "cmd_line": "\"C:\\Users\\moetheingioo\\AppData\\Local\\Microsoft\\OneDrive\\25.031.0217.0003\\FileCoAuth.exe\" -Embedding",
                "parent_process": "c:\\windows\\system32\\svchost.exe",
                "event_type": "audit_success"
              },
              {
                "domain": None,
                "dst_ip": None,
                "dst_port": None,
                "src_ip": None,
                "src_port": None,
                "user": None,
                "ip_malicious": None,
                "hash_malicious": None,
                "hash": {
                  "sha1": None,
                  "sha256": None,
                  "md5": None
                },
                "file_name": "c:\\users\\moetheingioo\\appdata\\local\\microsoft\\onedrive\\25.031.0217.0003\\filecoauth.exe",
                "file_size": None,
                "file_path": None,
                "cmd_line": "\"C:\\Users\\moetheingioo\\AppData\\Local\\Microsoft\\OneDrive\\25.031.0217.0003\\FileCoAuth.exe\" -Embedding",
                "parent_process": "c:\\windows\\system32\\svchost.exe",
                "event_type": "audit_success"
              },
              {
                "domain": None,
                "dst_ip": None,
                "dst_port": None,
                "src_ip": None,
                "src_port": None,
                "user": None,
                "ip_malicious": None,
                "hash_malicious": None,
                "hash": {
                  "sha1": None,
                  "sha256": None,
                  "md5": None
                },
                "file_name": "c:\\users\\moetheingioo\\appdata\\local\\microsoft\\onedrive\\25.031.0217.0003\\filecoauth.exe",
                "file_size": None,
                "file_path": None,
                "cmd_line": "\"C:\\Users\\moetheingioo\\AppData\\Local\\Microsoft\\OneDrive\\25.031.0217.0003\\FileCoAuth.exe\" -Embedding",
                "parent_process": "c:\\windows\\system32\\svchost.exe",
                "event_type": "audit_success"
              },
              {
                "domain": None,
                "dst_ip": None,
                "dst_port": None,
                "src_ip": None,
                "src_port": None,
                "user": None,
                "ip_malicious": None,
                "hash_malicious": None,
                "hash": {
                  "sha1": None,
                  "sha256": None,
                  "md5": None
                },
                "file_name": "c:\\users\\moetheingioo\\appdata\\local\\microsoft\\onedrive\\25.031.0217.0003\\filecoauth.exe",
                "file_size": None,
                "file_path": None,
                "cmd_line": "\"C:\\Users\\moetheingioo\\AppData\\Local\\Microsoft\\OneDrive\\25.031.0217.0003\\FileCoAuth.exe\" -Embedding",
                "parent_process": "c:\\windows\\system32\\svchost.exe",
                "event_type": "audit_success"
              },
              {
                "domain": None,
                "dst_ip": None,
                "dst_port": None,
                "src_ip": None,
                "src_port": None,
                "user": None,
                "ip_malicious": None,
                "hash_malicious": None,
                "hash": {
                  "sha1": None,
                  "sha256": None,
                  "md5": None
                },
                "file_name": "c:\\users\\moetheingioo\\appdata\\local\\microsoft\\onedrive\\25.031.0217.0003\\filecoauth.exe",
                "file_size": None,
                "file_path": None,
                "cmd_line": "\"C:\\Users\\moetheingioo\\AppData\\Local\\Microsoft\\OneDrive\\25.031.0217.0003\\FileCoAuth.exe\" -Embedding",
                "parent_process": "c:\\windows\\system32\\svchost.exe",
                "event_type": "audit_success"
              },
              {
                "domain": None,
                "dst_ip": None,
                "dst_port": None,
                "src_ip": None,
                "src_port": None,
                "user": None,
                "ip_malicious": None,
                "hash_malicious": None,
                "hash": {
                  "sha1": None,
                  "sha256": None,
                  "md5": None
                },
                "file_name": "c:\\users\\moetheingioo\\appdata\\local\\microsoft\\onedrive\\25.031.0217.0003\\filecoauth.exe",
                "file_size": None,
                "file_path": None,
                "cmd_line": "\"C:\\Users\\moetheingioo\\AppData\\Local\\Microsoft\\OneDrive\\25.031.0217.0003\\FileCoAuth.exe\" -Embedding",
                "parent_process": "c:\\windows\\system32\\svchost.exe",
                "event_type": "audit_success"
              },
              {
                "domain": None,
                "dst_ip": None,
                "dst_port": None,
                "src_ip": None,
                "src_port": None,
                "user": None,
                "ip_malicious": None,
                "hash_malicious": None,
                "hash": {
                  "sha1": None,
                  "sha256": None,
                  "md5": None
                },
                "file_name": "c:\\users\\moetheingioo\\appdata\\local\\microsoft\\onedrive\\25.031.0217.0003\\filecoauth.exe",
                "file_size": None,
                "file_path": None,
                "cmd_line": "\"C:\\Users\\moetheingioo\\AppData\\Local\\Microsoft\\OneDrive\\25.031.0217.0003\\FileCoAuth.exe\" -Embedding",
                "parent_process": "c:\\windows\\system32\\svchost.exe",
                "event_type": "audit_success"
              },
              {
                "domain": None,
                "dst_ip": None,
                "dst_port": None,
                "src_ip": None,
                "src_port": None,
                "user": None,
                "ip_malicious": None,
                "hash_malicious": None,
                "hash": {
                  "sha1": None,
                  "sha256": None,
                  "md5": None
                },
                "file_name": "c:\\users\\moetheingioo\\appdata\\local\\microsoft\\onedrive\\25.031.0217.0003\\filecoauth.exe",
                "file_size": None,
                "file_path": None,
                "cmd_line": "\"C:\\Users\\moetheingioo\\AppData\\Local\\Microsoft\\OneDrive\\25.031.0217.0003\\FileCoAuth.exe\" -Embedding",
                "parent_process": "c:\\windows\\system32\\svchost.exe",
                "event_type": "audit_success"
              }
            ],
            "sla": {
              "mttd": 73,
              "mtta": 11,
              "mttt": 5,
              "mtti": None,
              "mttn": None,
              "mttv": 39155.283,
              "mttr": None
            }
          }
        }

example_prediction_body = {
  "prediction": {
    "tactic": [
      [
        "Privilege Escalation",
        0.8073485842635361
      ],
      [
        "Defense Evasion",
        0.1913660317755721
      ]
    ],
    "technique": [
      [
        "Abuse Elevation Control Mechanism",
        0.9999484878515933
      ]
    ],
    "subtechnique": [
      [
        "Bypass User Account Control",
        0.999921352605669
      ]
    ]
  }
}
example_type_body = {
  "prediction": {
    "tactic": [
      [
        "Privilege Escalation",
        0.8073485842635361
      ],
      [
        "Defense Evasion",
        0.1913660317755721
      ]
    ],
    "technique": [
      [
        "Abuse Elevation Control Mechanism",
        0.9999484878515933
      ]
    ],
    "subtechnique": [
      [
        "Bypass User Account Control",
        0.999921352605669
      ]
    ]
  },
  "Mitre_Match": [
    {
      "tactic": "Defense Evasion",
      "technique": "Abuse Elevation Control Mechanism",
      "subtechnique": "",
      "Detection": "DS0024,DS0002,DS0009,DS0022,DS0017"
    },
    {
      "tactic": "Defense Evasion",
      "technique": "Abuse Elevation Control Mechanism",
      "subtechnique": "Bypass User Account Control",
      "Detection": "DS0024,DS0009,DS0017"
    }
  ]
}

# example_client_tools_body = {
#     "currentTechnologies": [
#         {
#             "technology": "EDR",
#             "product": "TrendMicro"
#         },
#         {
#             "technology": "SIEM/ELK",
#             "product": ""null""
#         },
#         {
#             "technology": "SOAR",
#             "product": ""null""
#         }
#     ],
#     "monitorAssets": [
#         {
#             "hostname": "yb-lt2338.yomabank.org",
#             "ipAddress": "192.168.100.28",
#             "assetLocation": ""null"",
#             "InProduction": ""null"",
#             "IncludedAPi": ""null"",
#             "os": ""null"",
#             "purpose": ""null""
#         }
#     ]
#   }


# example_client_tools_body_null = {
#     "currentTechnologies": [
#         {
#             "technology": "EDR",
#             "product": ""null""
#         },
#         {
#             "technology": "SIEM/ELK",
#             "product": ""null""
#         },
#         {
#             "technology": "SOAR",
#             "product": ""null""
#         }
#     ],
#     "monitorAssets": [
#         {
#             "hostname": "yb-lt2338.yomabank.org",
#             "ipAddress": "192.168.100.28",
#             "assetLocation": ""null"",
#             "InProduction": ""null"",
#             "IncludedAPi": ""null"",
#             "os": ""null"",
#             "purpose": ""null""
#         }
#     ]
#   }

example_prediction_body = {
  "prediction": {
    "tactic": [
      [
        "Privilege Escalation",
        0.8073485842635361
      ],
      [
        "Defense Evasion",
        0.1913660317755721
      ]
    ],
    "technique": [
      [
        "Abuse Elevation Control Mechanism",
        0.9999484878515933
      ]
    ],
    "subtechnique": [
      [
        "Bypass User Account Control",
        0.999921352605669
      ]
    ]
  }
}
example_type_body_null = {
  "prediction": {
    "tactic": [
      [
        "Privilege Escalation",
        0.8073485842635361
      ],
      [
        "Defense Evasion",
        0.1913660317755721
      ]
    ],
    "technique": [
      [
        "Abuse Elevation Control Mechanism",
        0.9999484878515933
      ]
    ],
    "subtechnique": [
      [
        "Bypass User Account Control",
        0.999921352605669
      ]
    ]
  },
  "Mitre-Match": [
  ]
}

example_log_body2 =  {
          "node": {
            "id": "4fc171b7-fe0f-473f-81ca-afaed1438d5b",
            "alert_id": "N-Health-2502-000001",
            "alert_name": "svchost.exe on host NH-PUWANAT-SU",
            "tags": "Alert",
            "incident_type": "null",
            "severity": "Low",
            "alert_status": "Closed",
            "log_source": "Palo Alto Cortex XDR",
            "case_result": "FalsePositives",
            "detected_time": "2025-02-28T09:23:16.000Z",
            "mitre": [],
            "objectMarking": [
              {
                "id": "03ec5d32-5cca-4c24-8bbc-8cef8c4dcd3f",
                "definition": "N-Health"
              }
            ],
            "contexts": {
              "domain": "null",
              "endpoint_type": "null",
              "os": "Windows",
              "user": "NT AUTHORITY\\SYSTEM",
              "user_priv": "null",
              "src_ip": [
                "10.148.61.24"
              ]
            },
            "events": [
              {
                "domain": "null",
                "dst_ip": "null",
                "dst_port": "null",
                "src_ip": "null",
                "src_port": "null",
                "user": "null",
                "ip_malicious": "null",
                "hash_malicious": "null",
                "hash": {
                  "sha1": "null",
                  "sha256": "add683a6910abbbf0e28b557fad0ba998166394932ae2aca069d9aa19ea8fe88",
                  "md5": "b7f884c1b74a263f746ee12a5f7c9f6a"
                },
                "file_name": "svchost.exe",
                "file_size": "null",
                "file_path": "C:\\Windows\\System32\\svchost.exe",
                "cmd_line": "C:\\Windows\\system32\\svchost.exe -k LocalService -p -s WebClient",
                "parent_process": "null",
                "event_type": "Network Connections"
              }
            ],
            "sla": {
              "mttd": 24,
              "mtta": 6,
              "mttt": 4,
              "mtti": 986,
              "mttn": "null",
              "mttv": 2156.666,
              "mttr": "null"
            }
          }
        }

example_type_body2 = {
  "prediction": {
    "tactic": [
      [
        "Credential Access",
        0.9712095890597232
      ]
    ],
    "technique": [
      [
        "Unsecured Credentials",
        0.9311461182117761
      ]
    ],
    "subtechnique": [
      [
        "Credentials In Files",
        0.752552347537426
      ],
      [
        "LSASS Memory",
        0.14838355769405737
      ],
      [
        "LSA Secrets",
        0.06560069020417288
      ]
    ]
  },
  "Mitre_Match": [
    {
      "tactic": "Credential Access",
      "technique": "Unsecured Credentials",
      "subtechnique": "",
      "Detection": "DS0024,DS0002,DS0009,DS0022,DS0017,DS0015"
    },
    {
      "tactic": "Credential Access",
      "technique": "Unsecured Credentials",
      "subtechnique": "Credentials In Files",
      "Detection": "DS0009,DS0022,DS0017"
    }
  ]
}
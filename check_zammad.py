#!/usr/bin/python3
import requests
import json
import sys
import argparse
####
#
#  Complete Documentation: https://github.com/marekbeckmann/Icinga2-Zammad-Check
#
####

# STATES
OK = 0
WARNING = 1
CRITICAL = 2
UNKNOWN = 3

# Icinga Message
message = {
    'status': OK,
    'summary': 'Zammad Health Message: ',
}


def check(server, token):

    try:
        zammad_data = requests.get(
            server + "/api/v1/monitoring/health_check?token=" + token).text

        zammad_data = json.loads(zammad_data)
        status = UNKNOWN
    except:
        status = WARNING
        message['summary'] = 'Zammad Health information retrieval failed!'
        return status

    health = zammad_data['healthy']
    issues = zammad_data['issues']

    if health:
        status = OK
    else:
        status = CRITICAL

    message['summary'] += '\nIssues: '.join(issues)
    return status


def args():
    parser = argparse.ArgumentParser(
        prog=sys.argv[0],
        description='Icinga/Nagios Check Script for Zammad',
        epilog="Thanks for using my Plugin. \nDocumentation: https://github.com/marekbeckmann/Icinga2-Zammad-Check"
    )

    parser.add_argument(
        "--token",
        help="Specify the Zammad Monitoring Token.",
        required=True,
        action='store',
        type=str
    )

    parser.add_argument(
        "--server",
        required=True,
        action='store',
        type=str
    )

    return parser


args = args().parse_args()
token = args.token
server = args.server

message['status'] += check(server, token)
print("{summary}".format(
    summary=message.get('summary'),
))
raise SystemExit(message['status'])

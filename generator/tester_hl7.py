#!/usr/bin/env python3
"""
"""

import os
import re
import sys
import argparse
import subprocess
from src import jurisdictions as J

_HL7_DIR = '/data/csels/preprocessed_data/hl7_update'


###############################################################################
if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Test synthetic data generation for all codes in a ' \
        'given jurisdiction')

    parser.add_argument('--jurisdiction',
                        dest='jurisdiction',
                        required=True,
                        help='jurisdiction of the source data (full or abbreviation)')

    args = parser.parse_args()

    
    jurisdiction = args.jurisdiction
    # get the required args
    
    # expand jurisdiction abbreviation, if any
    if jurisdiction in J.ABBREV_MAP:
        jurisdiction = J.ABBREV_MAP[jurisdiction]
        
    if jurisdiction == 'all':
        for j in os.listdir(_HL7_DIR):
            jurisdiction = j
            data_dir = os.path.join(_HL7_DIR, jurisdiction)
            if not os.path.isdir(data_dir):
                print('Directory not found: "{0}"'.format(data_dir))
                sys.exit(-1)

            # get all CSV files in the jurisdiction (filename == code.csv)
            for item in os.listdir(data_dir):
                fullpath = os.path.join(data_dir, item)
                if os.path.isfile(fullpath):
                    code = item[:-4]

                    command = []
                    command.append('python3')
                    command.append('gen_synthetic_data_hl7.py')
                    command.append('--hl7_dir')
                    command.append('{0}'.format(_HL7_DIR))
                    command.append('--jurisdiction')
                    command.append('{0}'.format(jurisdiction))
                    command.append('--code')
                    command.append('{0}'.format(code))
                    command.append('--outfile')
                    command.append('{0}'.format('all_synthetic_hl7_july_json/' + str(j) + '_' + str(code) + '.json'))
                    command.append('--syphilis_total')

                    print(command)

                    cp = subprocess.run(command,
                                        stdout=subprocess.PIPE,
                                        universal_newlines=True)

                    print(cp.stdout)
                    
    else:
        data_dir = os.path.join(_HL7_DIR, jurisdiction)
        if not os.path.isdir(data_dir):
            print('Directory not found: "{0}"'.format(data_dir))
            sys.exit(-1)

        # get all CSV files in the jurisdiction (filename == code.csv)
        for item in os.listdir(data_dir):
            fullpath = os.path.join(data_dir, item)
            if os.path.isfile(fullpath):
                code = item[:-4]

                command = []
                command.append('python3')
                command.append('gen_synthetic_data_hl7.py')
                command.append('--hl7_dir')
                command.append('{0}'.format(_HL7_DIR))
                command.append('--jurisdiction')
                command.append('{0}'.format(jurisdiction))
                command.append('--code')
                command.append('{0}'.format(code))
                command.append('--outfile')
                command.append('{0}'.format('all_synthetic_hl7_july_json/' + str(jurisdiction) + '_' + str(code) + '.json'))
                command.append('--syphilis_total')

                print(command)

                cp = subprocess.run(command,
                                    stdout=subprocess.PIPE,
                                    universal_newlines=True)

                print(cp.stdout)

            

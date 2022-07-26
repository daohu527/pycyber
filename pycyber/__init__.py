#!/usr/bin/env python3

# ****************************************************************************
# Copyright 2019 The Apollo Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ****************************************************************************

import os
import sys

# Set environment variables
if os.getenv('CYBER_PATH') is None:
    os.environ['CYBER_PATH'] = os.path.dirname(os.path.abspath(__file__))

if os.getenv('CYBER_DOMAIN_ID') is None:
    os.environ['CYBER_DOMAIN_ID'] = "80"

if os.getenv('CYBER_IP', default = None) is None:
    os.environ['CYBER_IP'] = "127.0.0.1"

if sys.version_info[0] < 3:
    sys.stderr.write('''
        You are running Python2 while importing Python3 Cyber wrapper!
        Please change to "import cyber_py.xyz" accordingly.\n''')
    sys.exit(1)

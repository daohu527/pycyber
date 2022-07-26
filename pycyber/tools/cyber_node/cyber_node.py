#!/usr/bin/env python3
# ****************************************************************************
# Copyright 2019 The Apollo Authors. All Rights Reserved.

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

from pycyber import cyber

def print_node_info(node_name, sleep_s=2):
    roleattr_rawdata = cyber.NodeUtils.get_node_attr(node_name, sleep_s)
    from cyber.proto.role_attributes_pb2 import RoleAttributes
    try:
        msg = RoleAttributes()
        msg.ParseFromString(roleattr_rawdata)
        assert(node_name == msg.node_name)
    except:
        print("RoleAttributes ParseFromString failed. size is ", len(roleattr_rawdata))
        return
    print("nodename\t%s" %  msg.node_name)
    print("processid\t%d" % msg.process_id)
    print("hostname\t%s" % msg.host_name)

    print("[Reading Channels]:")
    reader_channels = sorted(cyber.NodeUtils.get_readersofnode(node_name, 0))
    for channel in reader_channels:
        print(channel)
    print("")

    print("[Writing Channels]:")
    writer_channels = sorted(cyber.NodeUtils.get_writersofnode(node_name, 0))
    for channel in writer_channels:
        print(channel)
    print("")


def _node_cmd_info(argv):
    """
    Command-line parsing for 'cyber_node info' command.
    """
    args = argv[2:]
    from optparse import OptionParser
    parser = OptionParser(
        usage="usage: cyber_node info channelname ")
    parser.add_option("-a", "--all",
                      dest="all_channels", default=False,
                      action="store_true",
                      help="display all channels info")

    (options, args) = parser.parse_args(args)
    if len(args) == 0 and not options.all_channels:
        parser.error("channelname must be specified")
    elif len(args) > 1:
        parser.error("you may only specify one channel name")
    elif len(args) == 1:
        print_node_info(args[0])
    elif len(args) == 0 and options.all_channels:
        nodes = cyber.NodeUtils.get_nodes()
        for nodename in nodes:
            print_node_info(nodename, 0)


def print_node_list():
    nodes = cyber.NodeUtils.get_nodes()
    print("The number of nodes is: ", len(nodes))
    nodes.sort()
    for node_name in nodes:
        print(node_name)


def _node_cmd_list(argv):
    """
    Command-line parsing for 'cyber_node list' command.
    """
    args = argv[2:]
    from optparse import OptionParser
    parser = OptionParser(
        usage="usage: cyber_node list")
    (options, args) = parser.parse_args(args)
    if len(args) > 0:
        parser.error("param is too much")
    print_node_list()


def _printallusage():
    print("""cyber_node is a command-line tool for printing information about CyberRT Nodes.

Commands:
\tcyber_node list\tlist active nodes
\tcyber_node info\tprint information about active node

Type cyber_node <command> -h for more detailed usage, e.g. 'cyber_node info -h'
""")
    sys.exit(getattr(os, 'EX_USAGE', 1))


def main(args=sys.argv):
    if len(sys.argv) == 1:
        _printallusage()

    cyber.init()

    argv = sys.argv[0:]
    command = argv[1]
    if command == 'list':
        _node_cmd_list(argv)
    elif command == 'info':
        _node_cmd_info(argv)
    else:
        _printallusage()

    cyber.shutdown()

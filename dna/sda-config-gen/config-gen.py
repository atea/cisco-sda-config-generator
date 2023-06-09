#!/usr/bin/env python3

import ipaddress
import os
import yaml
from jinja2 import Environment, FileSystemLoader

def yaml_from_file(file):
  with open(file, 'r') as f:
    return yaml.safe_load(f)

work_dir = os.path.dirname(os.path.realpath(__file__))
project = 'projectx'
config_file = work_dir + '/config_' + project + '.yml'
generated_config_dir = work_dir + '/generated-configs/' + project
if not os.path.exists(generated_config_dir):
  os.mkdir(generated_config_dir)
config = yaml_from_file(config_file)

def generate_config(env, template, local, peer=None, fs=None):
  t = env.get_template(template + '.j2')
  d = t.render(config=config, local=local, peer=peer, fs=fs)
  save_config(work_dir, template + '_' + local, d)

def save_config(work_dir, hostname, data):
  full_path = generated_config_dir + '/' + hostname + '.txt'
  save_to_file(full_path, data)

def save_to_file(filename, data):
  with open(filename, 'w') as f:
    print(data, file=f)

def get_netmask(network):
  return ipaddress.ip_network(network).netmask

def get_network(network):
  return ipaddress.ip_network(network).network_address

def get_first_ip(network):
  return list(ipaddress.ip_network(network).hosts())[0]

def get_last_ip(network):
  return list(ipaddress.ip_network(network).hosts())[1]

def get_first_ip_with_prefix(network):
  prefix = ipaddress.ip_network(network).prefixlen
  ip = get_first_ip(network)
  return(str(ip) + '/' + str(prefix))

def get_last_ip_with_prefix(network):
  prefix = ipaddress.ip_network(network).prefixlen
  ip = get_last_ip(network)
  return(str(ip) + '/' + str(prefix))

def get_ip_version(network):
  return ipaddress.ip_network(network).version

# prepare templates & filters
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
env.filters['netmask'] = get_netmask
env.filters['network'] = get_network
env.filters['first_ip'] = get_first_ip
env.filters['last_ip'] = get_last_ip
env.filters['first_ip_prefix'] = get_first_ip_with_prefix
env.filters['last_ip_prefix'] = get_last_ip_with_prefix
env.filters['ip_version'] = get_ip_version

# generate fusion1 + fusion2
generate_config(env, 'fusion', 'fusion1')
generate_config(env, 'fusion', 'fusion2')

# generate tcn1 + tcn2
generate_config(env, 'tcn', 'tcn1')
generate_config(env, 'tcn', 'tcn2')

# generate fexit1 + fexit2
generate_config(env, 'fexit', 'fexit1', 'fexit2')
generate_config(env, 'fexit', 'fexit2', 'fexit1')

# generate fs1a + fs1b
generate_config(env, 'fs', 'fs1a', 'fs1b', 'fs1')
generate_config(env, 'fs', 'fs1b', 'fs1a', 'fs1')

# generate fs2a + fs2b
generate_config(env, 'fs', 'fs2a', 'fs2b', 'fs2')
generate_config(env, 'fs', 'fs2b', 'fs2a', 'fs2')

# generate fexit bgp peer-session inherit
generate_config(env, 'fexit_iptransit', 'fexit1')
generate_config(env, 'fexit_iptransit', 'fexit2')

# generate fusion ip-transit
generate_config(env, 'fusion_iptransit', 'fusion1')
generate_config(env, 'fusion_iptransit', 'fusion2')
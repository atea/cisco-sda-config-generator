#!/usr/bin/env python3

import ipaddress
import os
import yaml
from jinja2 import Environment, FileSystemLoader

def yaml_from_file(file):
  with open(file, 'r') as f:
    return yaml.safe_load(f)

def get_netmask(network):
  return ipaddress.ip_network(network).netmask

def get_network(network):
  return ipaddress.ip_network(network).network_address

def get_first_ip(network):
  return list(ipaddress.ip_network(network).hosts())[0]

def get_last_ip(network):
  return list(ipaddress.ip_network(network).hosts())[-1]

work_dir = os.path.dirname(os.path.realpath(__file__))
config_file = work_dir + '/config.yml'
config = yaml_from_file(config_file)

# prepare templates & filters
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
env.filters['netmask'] = get_netmask
env.filters['network'] = get_network
env.filters['first_ip'] = get_first_ip
env.filters['last_ip'] = get_last_ip

# generate fusion1 + fusion2
template = env.get_template('fusion.jinja2')
fusion1 = template.render(config=config, local='fusion1')
fusion2 = template.render(config=config, local='fusion2')

# generate tcn1 + tcn2
template = env.get_template('tcn.jinja2')
tcn1 = template.render(config=config, local='tcn1')
tcn2 = template.render(config=config, local='tcn2')

print(tcn1)

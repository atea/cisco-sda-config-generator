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

def get_first_ip(network):
  return list(ipaddress.ip_network(network).hosts())[0]

def get_last_ip(network):
  return list(ipaddress.ip_network(network).hosts())[-1]

work_dir = os.path.dirname(os.path.realpath(__file__))
config_file = work_dir + '/config.yml'
config = yaml_from_file(config_file)


#persons = [
#    {'name': 'Andrej', 'age': 34}, 
#    {'name': 'Mark', 'age': 17}, 
#    {'name': 'Thomas', 'age': 44}, 
#    {'name': 'Lucy', 'age': 14}, 
#    {'name': 'Robert', 'age': 23}, 
#    {'name': 'Dragomir', 'age': 54}
#]
#
#
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
env.filters['netmask'] = get_netmask
env.filters['first_ip'] = get_first_ip
env.filters['last_ip'] = get_last_ip

# generate pe1
template = env.get_template('pe.jinja2')
output = template.render(
  config=config,
  local='pe1'
)
#  
#  pe=config['pe'])
print(output)
#
## generate pe2
#
#
#template = env.get_template('showpersons.txt')
#
#output = template.render(persons=persons)
#print(output)
#
#name = input("Enter your name: ")
#
#tm = Template("Hello {{ name }}")
#msg = tm.render(name=name)
#
#print(msg)
# Cisco SDA config generator
This script aims to assist creating baseline configuration for a new SDA setup.

It will generate configuration files for the following nodes;

 * FUSION1 and FUSION2 (core, PE nodes, etc)
 * TCN1 and TCN2 (two Transit Control Plane nodes)
 * FEXIT1 and FEXIT2 (two-node fabric site to provide default way out of all other fabrics)
 * FS1a and FS1b (first fabric site connected to FEXIT1 and FEXIT2 via SD-transit)
 * FS2a and FS2b (second fabric site connected to FEXIT1 and FEXIT2 via SD-transit)
 * Firewall config (linknets on FUSION + FW config if Palo Alto)

The following is assumed;

 * All nodes except FUSION is assumed to be "blank", hence minimal "global" config on FUSION (we assume they are in production)
 * Assumes LISP PubSub (we run BGP as only routing protocol on TCN with our own ASN, which would not work with LISP/BGP)
 * eBGP is used between each layer (i.e. between FS1/FS2 and FEXIT, between FEXIT and FUSION, between FUSION and each TCN, and between FUSION and firewalls)
 * TCN nodes are connected directly to FUSION or FEXIT (can be changed via config)
 * ISIS between border nodes (FEXIT1+2, FS1a+FS1b, FS2a+FS2b, etc), to distribute Lo0 for the automatically configured iBGP between Lo0 interfaces
 * Assumes /30 or /31 IPv4 linknets, and /126 or /127 IPv6 linknets (larger linknets is untested, but should work; the logic will then pick the two first available IPs for each side of the linknets).
 * FUSION/FW-interconnection is assumed to be SVI on FUSION side, with two links to active+passive FW (where same IPs are used on FW side during a failover).
 * Device-specific config is properly configured (proper descriptions and similar), while common config only has bare minimum to get the device discoverable and configurable from DNAC. Full and best-practice config pushed via dayN templates from DNAC when provisioning the device (SNMP ACLs, VTY config, etc).

```
     _______________                                _______________                         
    |               |___                           |               |                        
    |  FS1a (B+CP)  |__ \                          |      FW       |                        
    |_______________|  \ \                         |_______________|                        
            |          |  \                                |                                
     _______|_______   \   \ _______________        _______|_______        _______________
    |               |___\___|               |______|               |______|               |
    |  FS1b (B+CP)  |_   \__| FEXIT1 (B+CP) |_    _|    FUSION1    |_    _|      TCN1     |
    |_______________| \  /\ |_______________| \  / |_______________| \  / |_______________|
                       \/  X        |          \/          |          \/         
     _______________   /\ / \_______|_______   /\   _______|_______   /\   _______________
    |               |_/  X__|               |_/  \_|               |_/  \_|               |
    |  FS2a (B+CP)  |___/___| FEXIT2 (B+CP) |______|    FUSION2    |______|      TCN2     |
    |_______________|  /    |_______________|      |_______________|      |_______________|
            |          |   /                               |                                
     _______|_______   /  /                         _______|_______                         
    |               |_/  /                         |               |                        
    |  FS2b (B+CP)  |___/                          |      FW       |                        
    |_______________|                              |_______________|                        
 
```

## Setup
 * Clone this repo
 * Optional: initialize virtual environment
 * Install requirements
 * Copy `config_projectx.yml.dist` to `config_projectx.yml` and update with desired values
 * Run script
 * Profit???

```
git clone https://github.com/atea/cisco-sda-config-generator.git
cd cisco-sda-config-generator
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp config_projectx.yml.dist config_projectx.yml
python config-gen.py
```

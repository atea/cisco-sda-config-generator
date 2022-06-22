# Cisco SDA config generator
This script aims to assist creating baseline configuration for a new SDA setup.

It will generate configuration files for the following nodes;

 * FUSION1 and FUSION2 (core, PE nodes, etc)
 * TCN1 and TCN2 (two Transit Control Plane nodes)
 * FEXIT1 and FEXIT2 (two-node fabric site to provide default way out of all other fabrics)
 * FS1 and FS2 (first fabric site connected to FEXIT1 and FEXIT2 via SD-transit)

The following is assumed;

 * All nodes except FUSION is assumed to be "blank", hence minimal "global" config on FUSION (we assume they are in production)
 * Assumes LISP PubSub (we run BGP as only routing protocol on TCN with our own ASN, which would not work with LISP/BGP)
 * eBGP is used between each layer (i.e. between FS1 and FEXIT, between FEXIT and FUSION, and between FUSION and each TCN)
 * TCN nodes are connected directly to FUSION
 * ISIS between FEXIT1+2 (to distribute Lo0 for the automatically configured iBGP to avoid multihop via FS or FUSION)

```
                                                               _______________ 
                                                              |               |
                                                              |      MPLS     |
                                                              |_______________|
                                                                      |
     _______________              _______________              _______|_______              _______________
    |               |____________|               |____________|               |____________|               |
    | FS1 #1 (B+CP) |____    ____| FEXIT1 (B+CP) |____    ____|    FUSION1    |____    ____|      TCN1     |
    |_______________|    \  /    |_______________|    \  /    |_______________|    \  /    |_______________|
            |             \/             |             \/             |             \/            
     _______|_______      /\      _______|_______      /\      _______|_______      /\      _______________
    |               |____/  \____|               |____/  \____|               |____/  \____|               |
    | FS1 #2 (B+CP) |____________| FEXIT2 (B+CP) |____________|    FUSION2    |____________|      TCN2     |
    |_______________|            |_______________|            |_______________|            |_______________|
                                                                      |
                                                               _______|_______ 
                                                              |               |
                                                              |      MPLS     |
                                                              |_______________|

```

## Setup
 * Clone this repo
 * Optional: initialize virtual environment
 * Install requirements
 * Copy `config.yml.dist` to `config.yml` and update with desired values
 * Run script
 * Profit???

```
git clone https://github.com/ateanorge/cisco.git
cd cisco/dna/sda-config-gen
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp config.yml.dist config.yml
python config-gen.py
```

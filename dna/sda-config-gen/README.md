# Cisco SDA config generator
This script aims to assist creating baseline configuration for a new SDA setup.

It will generate configuration files for the following nodes;

 * PE1 and PE2 ("fusion")
 * TCN1 and TCN2 (two Transport Control Node)
 * FEXIT1 and FEXIT2 (two-node fabric site to provide default way out of fabrics)
 * FS1 and FS2 (first fabric site connected to FEXIT1 and FEXIT2 via SD-transit)

The following is assumed;

 * Assumes LISP PubSub
 * eBGP is used between each layer (i.e. between FS1 and FEXIT, between FEXIT and PE, and between PE and each TCN)
 * TCN nodes are connected directly to PE

```
     _______________              _______________              _______________              _______________
    |               |____________|               |____________|               |____________|               |
    | FS1 #1 (B+CP) |____    ____| FEXIT1 (B+CP) |____    ____|  PE1 (MPLS)   |____    ____|      TCN1     |
    |_______________|    \  /    |_______________|    \  /    |_______________|    \  /    |_______________|
            |             \/             |             \/             |             \/            
     _______|_______      /\      _______|_______      /\      _______|_______      /\      _______________
    |               |____/  \____|               |____/  \____|               |____/  \____|               |
    | FS1 #2 (B+CP) |____________| FEXIT2 (B+CP) |____________|  PE2 (MPLS)   |____________|      TCN2     |
    |_______________|            |_______________|            |_______________|            |_______________|

```

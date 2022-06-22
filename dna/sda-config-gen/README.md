# Cisco SDA config generator
This script aims to assist creating baseline configuration for a new SDA setup.

It will generate configuration files for the following nodes;

 * PE1 and PE2 ("fusion")
 * TCN1 and TCN2 (two Transit Control Plane nodes)
 * FEXIT1 and FEXIT2 (two-node fabric site to provide default way out of all other fabrics)
 * FS1 and FS2 (first fabric site connected to FEXIT1 and FEXIT2 via SD-transit)

The following is assumed;

 * All nodes except PE is assumed to be "blank", hence minimal "global" config on PE (we assume they are in production)
 * Assumes LISP PubSub (we run BGP as only routing protocol on TCN with our own ASN)
 * eBGP is used between each layer (i.e. between FS1 and FEXIT, between FEXIT and PE, and between PE and each TCN)
 * TCN nodes are connected directly to PE
 * ISIS between FEXIT1+2 (to distribute Lo0 for the automatically configured iBGP to avoid multihop via FS or PE)

```
                                                               _______________ 
                                                              |               |
                                                              |      MPLS     |
                                                              |_______________|
                                                                      |
     _______________              _______________              _______|_______              _______________
    |               |____________|               |____________|               |____________|               |
    | FS1 #1 (B+CP) |____    ____| FEXIT1 (B+CP) |____    ____|      PE1      |____    ____|      TCN1     |
    |_______________|    \  /    |_______________|    \  /    |_______________|    \  /    |_______________|
            |             \/             |             \/             |             \/            
     _______|_______      /\      _______|_______      /\      _______|_______      /\      _______________
    |               |____/  \____|               |____/  \____|               |____/  \____|               |
    | FS1 #2 (B+CP) |____________| FEXIT2 (B+CP) |____________|      PE2      |____________|      TCN2     |
    |_______________|            |_______________|            |_______________|            |_______________|
                                                                      |
                                                               _______|_______ 
                                                              |               |
                                                              |      MPLS     |
                                                              |_______________|

```

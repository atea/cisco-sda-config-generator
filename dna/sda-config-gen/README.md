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

    _________________           _________________           _________________           _________________
    |               |___________|               |___________|               |___________|               |
    | FS1 #1 (B+CP) |___        | FEXIT1 (B+CP) |___        |  PE1 (MPLS)   |___        |      TCN1     |
    |_______________|   \     __|_______________|   \     __|_______________|   \     __|_______________|
            |            \   /          |            \   /          |            \   /          
    ________|________     \_/_  ________|________     \_/_  ________|________     \_/_  _________________
    |               |______/  \_|               |______/  \_|               |______/  \_|               |
    | FS1 #2 (B+CP) |___________| FEXIT2 (B+CP) |___________|  PE2 (MPLS)   |___________|      TCN2     |
    |_______________|           |_______________|           |_______________|           |_______________|


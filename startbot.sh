#!/bin/bash
patch_to_bot=/opt/godvile_bot

docker run  -it --rm  -p 94.141.168.73:5901:5901  --name godvile -v $patch_to_bot:/opt/ bot /opt/godville.py
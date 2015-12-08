#!/bin/bash

output=$(curl --data "maxMoveTime=&name=&player0-name=&player0-type=COMPUTER&player1-name=&player1-type=COMPUTER&takeover=" -H "Accept: application/json" http://sysprak.priv.lab.nm.ifi.lmu.de/sysprak/Reversi)

gameid=${output:19:11}

echo $gameid

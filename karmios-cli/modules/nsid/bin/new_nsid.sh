#!/bin/bash

USER=$1
PWD=$2
#NODE=$3
DockerPalth=$(which docker)

#Descargando imagen
echo "10" |dialog --title "Please Wait" --gauge "Getting Container" 10 80 0
$DockerPalth pull nsoporte/cloudnode:1 > /dev/null

#INstalando 
echo "85" |dialog --title "Please Wait" --gauge "Getting Container" 10 80 0
$DockerPalth run --name=cloudnode --restart=always --net=host --privileged -v /etc/localtime:/etc/localtime:ro -e USER=$USER -e SECRET=$PWD -d nsoporte/cloudnode:1 > /dev/null

echo "100" |dialog --title "Please Wait" --gauge "Getting Container" 10 80 0


#!/bin/bash 


DockerPath=$(which docker)
order=$1
ContainerName=$2


#Get process from docker container
function GetDockerPs () {

	CMD=$($DockerPath container top $ContainerName |tail -n +2)
	
	IFS=$'\n'
	for item in $CMD; do

		DUID=$(echo "$CMD" |awk '{print $1}')		
		DPID=$(echo "$CMD" |awk '{print $2}')
		DPPID=$(echo "$CMD" |awk '{print $3}')
		DC=$(echo "$CMD" |awk '{print $4}')
		DSTIME=$(echo "$CMD" |awk '{print $5}')
		DTTY=$(echo "$CMD" |awk '{print $6}')
		DTIME=$(echo "$CMD" |awk '{print $7}')
		DCMD=$(echo "$CMD" |awk '{print $8 $9 $10 $11 $12 $13 $14 $15 $16}')

		echo "$DUID  $DPPID  $DPPID  $DC  $DSTIME  $DTTY  $DTIME  $DCMD"

	done




}


#List containers 
function ListDockers() {

	dockers=$($DockerPath ps -a | awk '{if(NR>1) print $NF}'|grep -v "karmios-cli")
	#echo -n "{ "
	
	json=""

	for docker in $dockers; do

		STATE=$($DockerPath inspect -f '{{.State.Running}}' $docker)
		ID=$($DockerPath inspect --format="{{.Id}}" $docker)
		

		json="$json "\""$docker""\" : { "\""status""\" : "\""$STATE""\" , "\""id""\" : "\""$ID""\" },"

	done	

    	JsonOutPut=$(echo -n "{ ${json::-1} }")
    	echo -n "$JsonOutPut"
}







#Check docker name
function CheckDocker() {
	

	ANS=2
	CheckRun=$($DockerPath ps |grep  -w $ContainerName |head -n 1 )
	CheckStop=$($DockerPath ps -a|grep  -w $ContainerName |head -n 1 )
	
	if [ "$CheckStop" != "" ];then
		ANS=1 	
	fi

	if [ "$CheckRun" != "" ];then
		ANS=0 	
	fi


	#Exit codes
	#0 = Installed and running
	#1 = Installed and stoped 
	#3 = No instlalled

	#echo $ANS #Debug
	echo -n "{ "
	echo -n "\""return""\"
	echo -n " : "
	echo -n "\""$ANS""\"
	echo -n " }"

}


function help() {

	echo "Usage: ./script command container_name

				Where command:
				check: Check container status ( 0=Running, 1=Stoped, 2=Not Installed)

	"

	exit 3

}



##################  Use functions UP ###########


case $order in
				check)	CheckDocker
				;;

				dockers) ListDockers
				;;

				getps) GetDockerPs
				;;


				*) 		help
				;;

esac	
				


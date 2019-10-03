#!/bin/bash 

ContainerName="samba4"
DockerPath=$(which docker)
STOOL=$($DockerPath exec -i $ContainerName which samba-tool)
CMD=$1
var1=$2
var2=$3
var3=$4
var4=$5


function DelUser () {

	$DockerPath exec -i $ContainerName $STOOL user delete $var1 > /dev/null 2>&1
	ExitCode=$?





} 




function AddUser () {


	$DockerPath exec -i $ContainerName $STOOL user create $var1 $var2 --given-name "\"$var3"\" --surname "\"$var4"\" > /dev/null 2>&1
	ExitCode=$?

}




function ListUsers () {


	for user in $($DockerPath exec -i $ContainerName $STOOL user list);do

		UserDetail=$($DockerPath exec -i $ContainerName $STOOL user show $user |grep "name:" |cut -d ":" -f2)
		echo $UserDetail




	done


}




case $CMD in
	adduser) AddUser 
	;;

	listusers) ListUsers
	;;

	deluser) DelUser
	;;

	*)		 exit 0
	;;

esac
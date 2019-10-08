#!/usr/bin/python3

import sys, ldap
import subprocess 

Container="samba4"
SmbFile="/data/apps/samba4/etc/smb.conf"
LdapServer="ldap://127.0.0.1"
DN="cn=administrator,cn=Users,dc=eurocenter,dc=local"
PWD="055Admintmp123."


def GetGroupMembers(groupname):

    Path = GetContainerFunc()
    command = Path['LocalDocker'] + " exec -i " + Container + " " + Path['SmbTool'] + ' group listmembers "' + groupname + '"'
    a = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    c = str(a.communicate()[0], 'utf-8')
    info = c.split('\n')
    del info[-1]
    
    return info




def GetGroups(): #Get groups on AD, retunrs a list

    Path = GetContainerFunc()
    command = Path['LocalDocker'] + " exec -i " + Container + " " + Path['SmbTool'] + ' group list' 
    a = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    c = str(a.communicate()[0], 'utf-8')
    info = c.split('\n')
    del info[-1]
    
    return info




def GetUsersInfo(): #Obtengo toda la informacion de los usuarios del AD, una lista con diccionarios 

    UserInfo = []
    users = GetUsers()

    for user in users:

        UserInfo.append(GetUserInfo(user))

    return UserInfo



def GetUsers(): #Get users on AD, retunrs a list

    Path = GetContainerFunc()
    command = Path['LocalDocker'] + " exec -i " + Container + " " + Path['SmbTool'] + ' user list' 
    a = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    c = str(a.communicate()[0], 'utf-8')
    info = c.split('\n')
    del info[-1]
    
    return info





def GetContainerFunc(): #Get Important Path from container, returns a dictionary
    Path = {}
    a = subprocess.Popen('which docker |tr -d "\n"',stdout=subprocess.PIPE,shell=True)
    Path['LocalDocker'] = str((a.communicate()[0]), 'utf-8')

    bcmd = Path['LocalDocker'] + " exec -i " + Container + ' which samba-tool |tr -d "\n"'
    b = subprocess.Popen(bcmd,stdout=subprocess.PIPE,shell=True)
    Path['SmbTool'] = str((b.communicate()[0]), 'utf-8')
    
    return Path



def GetDnFromFile(file): #Obtengo el nombre de dominio para generar el DN de Ldap

    command='cat ' + file + ' |grep realm |cut -d "=" -f2 |tr -d "\n"'

    realname = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
    domain=str(realname.communicate()[0], 'utf-8').strip()

    dn = "DC=%s" % ",DC=".join(domain.split("."))



    return dn



def GetUserInfo(username):  #Get user info from Ldap

    con = ldap.initialize(LdapServer)
    con.simple_bind_s(DN, PWD)

    ldap_base = GetDnFromFile(SmbFile)
    query = '(sAMAccountName=' + username + ')'
    attribute = ['name', 'mail', 'telephoneNumber'] 
    result = con.search_s(ldap_base, ldap.SCOPE_SUBTREE, query, attribute)


    FulInfo=result[0][1]


    if 'mail' in FulInfo:
        Mail=str(FulInfo['mail'][0], 'utf-8') 
    else:
        Mail="None"
 
    if 'telephoneNumber' in FulInfo:   
        Ext=str(FulInfo['telephoneNumber'][0], 'utf-8')
    else:
        Ext="None"


    Name=str(FulInfo['name'][0], 'utf-8')

    data = {
    	'mail' : Mail,
    	'ext' : Ext,
    	'name' : Name

    	}

    con.unbind_s()

    return data
  





    

print(GetGroupMembers('Domain Users'))



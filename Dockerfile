FROM			debian:buster
MAINTAINER		<cnaranjo@nsoporte.com>


RUN				apt-get update; apt-get -y upgrade; \
				apt-get -y  install apt-transport-https curl wget; \
				apt-get -y install ca-certificates curl gnupg2 software-properties-common; \
				curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - ; \
				add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"; \
				apt-get update; apt-get -y install docker-ce dialog python3-dialog openssh-server 

	




EXPOSE 2223
CMD ["/usr/sbin/sshd", "-D"]
# se_hunter_deploy

**Note**: if you are using a 3.X linux kernel (`uname -r`), be sure to follow these extra steps:
https://docs.docker.com/install/linux/docker-ce/ubuntu/#supported-storage-drivers

1. Install docker (bash setup_docker.sh)
2. docker login
3. docker pull pvadrevu/se_hunter
4. Adjust the parameters in se_hunter.yml
      * Set the # of replicas to a suitable value.
      * As the 1st command, choose a suitable name for the host to identify the logs
      * If its a residential IP, append the word "residential" to the commands
5. docker swarm init
6. To start: docker stack deploy -c se_hunter.yml se_hunter_service --with-registry-auth
7. To stop: docker service rm se_hunter_service_web
8. To check status:
    * docker service ls
    * docker container ls

**Note**: Use sar if you want to monitor the system usage to decide the number of replicas:
http://www.leonardoborda.com/blog/how-to-configure-sysstatsar-on-ubuntudebian/

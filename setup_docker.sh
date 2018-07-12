# From: https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1
# Set up Docker APT Repository
sudo apt-get update
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

# Install Docker CE
sudo apt-get update
sudo apt-get install -y docker-ce

# Create a docker group and add this user there 
sudo groupadd docker
sudo usermod -aG docker $USER

echo "Log out and login and try this command to make sure the installation went smoothly:"
echo "docker run hello-world"

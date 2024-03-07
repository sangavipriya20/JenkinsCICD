# JenkinsCICD


Setting up Jenkins master node in EC2 
1. Launch EC2 instance, i created Ubuntu Image
2. Prerequisite to install jenkins---> Java(JDK)
   ssh to the ec2 instance.
   sudo apt update
   sudo apt install openjdk-11-jre
   java -version
4. Install jenkins
   curl -fsSL https://pkg.jenkins.io/debian/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
5. By default, Jenkins will not be accessible to the external world due to the inbound traffic restriction by AWS. Open port 8080 in the inbound traffic rules.
6. Login to jenkins using http://ec2-instance-public-ip:8080
7. To get the jenkins admin password:
   sudo cat /var/lib/jenkins/secrets/initialAdminPassword
8. Install suggested plugins
---------------------------------------------------------------------------------------------------------------------------
** To integrate Docker with Jenkins, which expands Jenkins' capabilities by allowing it to use Docker containers as dynamic build environments:**

    Docker slave configuration:
9.  In the same ec2 instance, Install Docker
    sudo apt update
    sudo apt install docker.io
10. Grant Jenkins user and Ubuntu user permission to docker deamon. It allows Jenkins to control Docker containers.Granting them the necessary permissions without needing sudo.
    sudo su - 
    usermod -aG docker jenkins
    usermod -aG docker ubuntu
    systemctl restart docker
11.  Install docker pipeline plugin ---> enables Jenkins to define pipelines with Docker, allowing Jenkins jobs to build, test, and deploy within Docker containers.
12. restart Jenkins.
    http://<ec2-instance-public-ip>:8080/restart
    The docker agent configuration is now successful.
--------------------------------------------------------------------------------------------------------------------------
16. Create pipeline type project in jenkins.
    In script path : python-jenkins-argocd-k8s/Jenkinsfile

Run a jenkins file which contains the CI process consisting of multiple stages. Jenkins takes care of CI.
   
   

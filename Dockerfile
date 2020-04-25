# specify the image you want to use build docker image

FROM python:3.7

#apt is the ubuntu command line tool for advanced packaging tool(APT) for sw upgrade '''

RUN apt update && \
    apt install -y netcat-openbsd git-core curl build-essential openssl libssl-dev python

# set the env variable to tell where the app will be installed inside the docker

ENV INSTALL_PATH /Photos-Docker-Flask
RUN mkdir -p $INSTALL_PATH

#this sets the context of where commands will be ran in and is documented

WORKDIR $INSTALL_PATH

# Copy in the application code from your work station at the current directory
# over to the working directory.

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

#Install Node.js
RUN curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash - \
    sudo apt-get install -y nodejs

#Install NPM
RUN curl -L https://npmjs.org/install.sh | sudo sh

#Install Less.js
RUN npm install -g less

COPY . .

EXPOSE 5000

RUN chmod +x /Photos-Docker-Flask/start.sh

CMD ["/bin/bash", "/Photos-Docker-Flask/start.sh"]

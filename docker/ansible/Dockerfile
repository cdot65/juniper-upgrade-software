FROM python:3.10-alpine

# ---------------------------------------------------------------------------
# METADATA
# ---------------------------------------------------------------------------
LABEL name="juniper-upgrade-software"
LABEL maintainer="cremsburg.dev@gmail.com"
LABEL description="Docker container to upgrade Juniper Networks devices."
LABEL license="Apache 2.0"
LABEL url="https://github.com/cdot65/juniper-upgrade-software"
LABEL build-date="20220709"


# ---------------------------------------------------------------------------
# Change directory to /home/ansible
# ---------------------------------------------------------------------------
WORKDIR /home/ansible

# ---------------------------------------------------------------------------
# Add and install python packages
# ---------------------------------------------------------------------------
ADD docker/ansible/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# ---------------------------------------------------------------------------
# Install Ansible Galaxy roles and collections
# ---------------------------------------------------------------------------
RUN ansible-galaxy collection install juniper.device

# ---------------------------------------------------------------------------
# COPY OVER ansible.cfg
# ---------------------------------------------------------------------------
COPY docker/ansible/ansible.cfg /etc/ansible/ansible.cfg

# ---------------------------------------------------------------------------
# ENVIRONMENT SETUP
# ---------------------------------------------------------------------------
ENV ANSIBLE_CONFIG /etc/ansible/ansible.cfg

# ---------------------------------------------------------------------------
# we create a placeholder object for the docker build argument to fill in
# ---------------------------------------------------------------------------
ARG ANSIBLE_NET_USERNAME="placeholder, will be replaced by build-arg" 
ARG ANSIBLE_NET_PASSWORD="placeholder, will be replaced by build-arg" 

ENV ANSIBLE_NET_USERNAME=${ANSIBLE_NET_USERNAME}
ENV ANSIBLE_NET_PASSWORD=${ANSIBLE_NET_PASSWORD}

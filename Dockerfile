####################################################
# Use python 2.x and the latest version of alpine  #
####################################################
FROM python:2-alpine

LABEL maintainer=peter@grainger.xyz

###################################################
# Add a compiler                                  #
###################################################
RUN apk update && \
    apk add --no-cache gcc \
                       libffi-dev \
                       openssl-dev \
                       libxslt-dev \
                       libxml2-dev \
                       musl-dev \
                       linux-headers

###################################################
# Create somewhere to put the files               #
###################################################
RUN mkdir -p /opt/jarvis
WORKDIR /opt/jarvis

###################################################
# Requirements file first to help cache           #
###################################################
COPY requirements.txt .
RUN pip install -r requirements.txt

###################################################
# Copy over the rest.                             #
###################################################
COPY ./ ./

###################################################
# Expose the port externally from the container   #
###################################################
EXPOSE 5000

###################################################
# Run jarvis                                         #
###################################################
CMD python jarvis.py
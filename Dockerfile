# -------------------------------------------------------------------------- #
# Copyright 2025-present, Federation Manager, by Software Networks, i2CAT    #
#                                                                            #
# Licensed under the Apache License, Version 2.0 (the "License"); you may    #
# not use this file except in compliance with the License. You may obtain    #
# a copy of the License at                                                   #
#                                                                            #
# http://www.apache.org/licenses/LICENSE-2.0                                 #
#                                                                            #
# Unless required by applicable law or agreed to in writing, software        #
# distributed under the License is distributed on an "AS IS" BASIS,          #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.   #
# See the License for the specific language governing permissions and        #
# limitations under the License.                                             #
# -------------------------------------------------------------------------- #

#########################################################
#                                                       #
#   Dockerfile for creating a container image for the   #
#   federation-manager                                  #
#                                                       #
#########################################################

FROM python:3.9

# Set working directory
WORKDIR /usr/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    bash \
    build-essential \
    git \
    wget \
    iptables \
    libcurl4-openssl-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy application code
COPY . .

# Install Python dependencies
RUN python -m pip install --no-cache-dir -r requirements.txt

# Set working directory for application execution
WORKDIR /usr/app/src/

# Expose application port
EXPOSE 8989

# Set Gunicorn as the entrypoint
ENTRYPOINT ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:8989", "--workers", "4", "--log-level", "debug", "--timeout", "1000"]

FROM python:3.11
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY

# update apt-get
RUN apt-get update -y && apt-get upgrade -y

RUN wget https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip \
  && unzip awscli-exe-linux-x86_64.zip \
  && ./aws/install \
  # Clean up
  && rm -f awscli-exe-linux-x86_64.zip

ENV NVM_DIR /root/.nvm
ENV NODE_VERSION 18.17.1
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash \
  && . $HOME/.nvm/nvm.sh \
  && nvm install $NODE_VERSION \
  && nvm alias default $NODE_VERSION \
  && nvm use default \
  && node -v && npm -v && which npm \
  && npm install -g serverless

# use nvm でインストールした nodeとnpmを使うので、ここで入れるとPATHが合わず失敗するのでPATHの設定をする
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH
RUN node -v
RUN npm -v

# install boto3
RUN pip install boto3

# set aws key 
RUN sls config credentials --provider aws --key $AWS_ACCESS_KEY_ID --secret $AWS_SECRET_ACCESS_KEY

# change work directory
RUN mkdir -p /app
WORKDIR /app/app

###
### インストールパス関係の情報
###
# which node
# /root/.nvm/versions/node/v18.17.1/bin/node
# which npm
# /root/.nvm/versions/node/v18.17.1/bin/npm
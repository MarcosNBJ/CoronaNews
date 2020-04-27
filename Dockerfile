FROM python:3.6

# chrome
RUN BUILD_DEPS='gnupg unzip' && \
    RUN_DEPS='wget' && \
    apt-get update && \
    apt-get install -yqq $RUN_DEPS $BUILD_DEPS --no-install-recommends && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list && \
    wget https://dl-ssl.google.com/linux/linux_signing_key.pub && \
    apt-key add linux_signing_key.pub && \
    apt-get update && \
    apt-get install -yqq google-chrome-stable --no-install-recommends && \
    rm -rf linux_signing_key.pub && \
    apt-get purge -y --auto-remove $BUILD_DEPS && \
    rm -rf /var/lib/apt/lists/*

# chromedriver
RUN BUILD_DEPS='unzip' && \
    RUN_DEPS='wget' && \
    apt-get update && \
    apt-get install -yqq $RUN_DEPS $BUILD_DEPS --no-install-recommends && \
    wget https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    chmod 755 chromedriver && \
    mv chromedriver /usr/local/bin/chromedriver && \
    rm -rf chromedriver_linux64.zip && \
    apt-get purge -y --auto-remove $BUILD_DEPS && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -r requirements.txt
COPY . /code
CMD [sh, -c, "pip install -r requirements.txt && python web/app.py & cd news_crawler && scrapyrt -i 0.0.0.0 -p $PORT"]
FROM python:3.7

WORKDIR /opt/app

ADD requirements.txt .
RUN pip install -r requirements.txt

ADD Makefile ./Makefile
ADD keymaster ./keymaster
ADD setup.py ./setup.py

# Install
RUN pip install .

# Remove files
RUN rm -Rf *

# Test run
RUN keymaster -h

CMD keymaster serve

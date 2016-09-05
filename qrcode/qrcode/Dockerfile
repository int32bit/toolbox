FROM python:2
MAINTAINER int32bit krystism@gmail.com

Add source.list /etc/apt/sources.list

RUN apt-get -y update
RUN apt-get install -y --no-install-recommends python-qrtools
RUN sed -i '181s/tostring/tobytes/' /usr/lib/python2.7/dist-packages/qrtools.py

ADD . /opt/qrcode
RUN pip install -r /opt/qrcode/requirements.txt
WORKDIR /root
ENTRYPOINT ["/opt/qrcode/endpoint.sh"]
CMD ["--help"]

#RUN set -ex \
#        && apt-get update -y \
#        && apt-get install -y --no-install-recommends \
#        && python-qrtools \
#        && rm -rf /var/lib/apt/lists/*

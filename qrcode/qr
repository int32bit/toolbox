#!/bin/bash
IMAGE=krystism/qrcode
if [ x$1 == "xrebuild" ]; then
    docker rmi -f $IMAGE
    docker build -t $IMAGE qrcode
    exit 0
fi

if ! docker images | grep -q $IMAGE
then
    docker build -t $IMAGE qrcode
fi
docker run -t -i --rm -v `pwd`:/root krystism/qrcode "$@" | sed "s#usage: qrcode#usage: $0#"

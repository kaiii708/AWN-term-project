FROM ubuntu:bionic


WORKDIR /app/boost

RUN apt-get -qq update && apt-get install -q -y software-properties-common
RUN add-apt-repository ppa:ubuntu-toolchain-r/test -y
RUN apt-get -qq update && apt-get install -qy g++ gcc git wget

RUN wget https://boostorg.jfrog.io/artifactory/main/release/1.77.0/source/boost_1_77_0.tar.gz
RUN tar xvf boost_1_77_0.tar.gz

WORKDIR /app/boost/boost_1_77_0

RUN ./bootstrap.sh --prefix=/usr/local/
RUN ./b2
RUN ./b2 install

WORKDIR /app

COPY . .

RUN g++ proxy.cpp -o proxy -g -Wall -lpthread

EXPOSE 8080

CMD ["./proxy", "8080"]

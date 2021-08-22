FROM tensorflow/tfx:0.27.0

LABEL maintainer="hannes.hapke@gmail.com"

RUN apt-get update
RUN apt-get install -y \
        curl \
        gnupg \
        vim \
        git \
        build-essential \
        tmux \
        htop \
        tcl
RUN apt-get remove sqlite3
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
ENV SLUGIFY_USES_UNIDECODE=yes

# Update sqlite to avoid https://github.com/apache/airflow/issues/14208
RUN wget https://www.sqlite.org/src/tarball/sqlite.tar.gz
RUN tar xzf sqlite.tar.gz
WORKDIR sqlite/
RUN ./configure
RUN make
RUN make sqlite3.c
RUN make install

RUN cd /root; mkdir tfx; cd tfx
RUN mkdir -p /root/airflow/dags

# RUN git clone https://github.com/tensorflow/tfx.git
COPY setup_airflow.sh /root/setup_airflow.sh
COPY setup_env.sh /root/setup_env.sh
COPY launch_airflow.sh /root/launch_airflow.sh

WORKDIR /root/
RUN sh setup_env.sh
RUN sh setup_airflow.sh
RUN chmod +x launch_airflow.sh
ENTRYPOINT [ "sh", "-c", "./launch_airflow.sh" ]

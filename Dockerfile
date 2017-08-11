FROM ubuntu:16.04

RUN apt-get update && apt-get dist-upgrade -y
RUN apt-get install -y curl wget git ruby python3 sra-toolkit snakemake libssl-dev libcurl4-openssl-dev libxml2-dev

WORKDIR /tmp
RUN curl -O -L http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.8.2-1/sratoolkit.2.8.2-1-ubuntu64.tar.gz && \
    tar xzf sratoolkit.2.8.2-1-ubuntu64.tar.gz && \
    cp -r sratoolkit.2.8.2-1-ubuntu64/bin/* /usr/bin && \
    rm -fr sratoolkit.2.8.2-1-ubuntu64

WORKDIR /root
RUN wget https://github.com/pachterlab/kallisto/releases/download/v0.43.0/kallisto_linux-v0.43.0.tar.gz && \
    tar xzf kallisto_linux-v0.43.0.tar.gz && \
    mv kallisto_linux-v0.43.0/kallisto /usr/bin/ && \
    rm -rf kallisto_linux-v0.43.0 kallisto_linux-v0.43.0.tar.gz

RUN echo 'source("http://bioconductor.org/biocLite.R"); biocLite("devtools"); biocLite("pachterlab/sleuth", ref = "devel"); biocLite("biomaRt")' \
    | R --no-save

WORKDIR /root
RUN mkdir bears_analyses
#RUN git clone https://github.com/pachterlab/bears_analyses.git

WORKDIR /root/bears_analyses/

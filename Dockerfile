FROM python:2-onbuild

ENV ZK_HOSTS localhost:2181

ADD setup.py /
ADD daemon.py /

CMD python setup.py --zk_hosts=${ZK_HOSTS}
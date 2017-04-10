FROM python:2-onbuild

ENV ASSIGNMENT '{"kafka-address":"localhost:0000","time":0,"factories":[]}'

ADD Producer.py /
ADD Factory/ /Factory/
ADD run.py /

CMD python run.py --assigment=${ASSIGNMENT}
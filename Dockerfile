FROM python
MAINTAINER harshitgarg2006@gmail.com , 7300243823
RUN apt-get install python 
COPY pass.py /pass_encrypt/pass.py
CMD python /pass_encrypt/pass.py 

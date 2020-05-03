FROM centos:7
USER root

WORKDIR /app
COPY . /app

#RUN yum -y install python3
RUN yum -y install epel-release && yum clean all
RUN yum -y install python-pip && yum clean all

RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
RUN yum -y install libaio-devel && yum install -y wget
#RUN yum install -y wget
RUN wget http://yum.oracle.com/repo/OracleLinux/OL7/oracle/instantclient/x86_64/getPackage/oracle-instantclient19.3-basic-19.3.0.0.0-1.x86_64.rpm \
    && rpm -ivh oracle-instantclient19.3-basic-19.3.0.0.0-1.x86_64.rpm \
    && wget http://yum.oracle.com/repo/OracleLinux/OL7/oracle/instantclient/x86_64/getPackage/oracle-instantclient19.3-sqlplus-19.3.0.0.0-1.x86_64.rpm \
    && rpm -ivh oracle-instantclient19.3-sqlplus-19.3.0.0.0-1.x86_64.rpm
#RUN rpm -ivh oracle-instantclient19.3-basic-19.3.0.0.0-1.x86_64.rpm
#RUN wget http://yum.oracle.com/repo/OracleLinux/OL7/oracle/instantclient/x86_64/getPackage/oracle-instantclient19.3-sqlplus-19.3.0.0.0-1.x86_64.rpm
#RUN rpm -ivh oracle-instantclient19.3-sqlplus-19.3.0.0.0-1.x86_64.rpm

#ENV TNS_ADMIN=/app/wallet

EXPOSE 5000

CMD python server.py

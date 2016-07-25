FROM registry.opensource.zalan.do/stups/openjdk:8-29

COPY target/helloworld-1.0.0-SNAPSHOT.jar /helloworld.jar
COPY target/scm-source.json /

CMD java $JAVA_OPTS $(java-dynamic-memory-opts) -jar /helloworld.jar

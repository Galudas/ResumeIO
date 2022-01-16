FROM openjdk:11
COPY target/resumeio-api-0.0.1-SNAPSHOT.jar app.jar
ADD docker-run.sh run.sh
RUN bash -c 'chmod +x /run.sh'
ENTRYPOINT ["/run.sh"]
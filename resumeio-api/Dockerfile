FROM openjdk:11
COPY target/resumeio-api-0.0.1-SNAPSHOT.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-XX:MaxRAMPercentage=80", "-jar", "/app.jar"]
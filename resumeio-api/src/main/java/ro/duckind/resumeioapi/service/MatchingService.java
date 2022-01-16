package ro.duckind.resumeioapi.service;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.*;
import org.springframework.scheduling.annotation.Async;
import org.springframework.scheduling.annotation.EnableAsync;
import org.springframework.web.client.RestTemplate;
import ro.duckind.resumeioapi.entity.MatchingObject;

import java.util.concurrent.CompletableFuture;
import java.util.concurrent.Future;

@Configuration
@EnableAsync
public class MatchingService {
    @Value(value = "${matching.service.url}")
    private String matchingServiceUrl;

    @Async("threadPoolTaskExecutor")
    public Future<String> match(MatchingObject matchingObject) {
        RestTemplate restTemplate = new RestTemplate();
        HttpEntity<?> requestEntity = new HttpEntity<>(matchingObject, getHeaders());
        ResponseEntity<String> response;
        ParameterizedTypeReference<String> t = new ParameterizedTypeReference<>() {
        };
        response = restTemplate.exchange(matchingServiceUrl, HttpMethod.POST, requestEntity, t);
        return CompletableFuture.completedFuture(response.getBody());
    }

    private HttpHeaders getHeaders() {
        final HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        return headers;
    }
}

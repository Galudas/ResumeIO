package ro.duckind.resumeioapi.service;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import ro.duckind.resumeioapi.dto.MatchingDto;
import ro.duckind.resumeioapi.dto.ScoreDto;
import ro.duckind.resumeioapi.entity.MatchHistory;
import ro.duckind.resumeioapi.repo.MatchHistoryRepository;

import java.util.List;

@Configuration
@Service
@RequiredArgsConstructor
@Slf4j
public class MatchingService {
    @Value(value = "${matching.service.url}")
    private String matchingServiceUrl;

    private final MatchHistoryRepository matchHistoryRepository;

    public List<MatchHistory> getMatchHistory() {
        return matchHistoryRepository.findAll();
    }

    public ScoreDto match(MatchingDto matchingDto) {
        RestTemplate restTemplate = new RestTemplate();
        HttpEntity<?> requestEntity = new HttpEntity<>(matchingDto, getHeaders());
        log.debug(matchingDto.getJobDescription());
        log.debug(matchingDto.getCandidateDescription());
        ResponseEntity<String> response;
        ParameterizedTypeReference<String> t = new ParameterizedTypeReference<>() {
        };
        log.debug("Sent data to " + matchingServiceUrl);
        response = restTemplate.exchange(matchingServiceUrl, HttpMethod.POST, requestEntity, t);

        log.debug("Got response " + response.getBody());
        saveMatchHistory(matchingDto, response.getBody());
        return new ScoreDto(response.getBody());
    }

    private void saveMatchHistory(MatchingDto matchingDto, String score) {
        MatchHistory matchHistory = new MatchHistory();
        matchHistory.setScore(score);
        matchHistory.setName(matchingDto.getCandidateName());
        matchHistory.setCandidateDescription(matchingDto.getCandidateDescription());
        matchHistory.setJobDescription(matchingDto.getJobDescription());
        matchHistoryRepository.save(matchHistory);
    }

    private HttpHeaders getHeaders() {
        final HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        return headers;
    }
}

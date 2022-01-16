package ro.duckind.resumeioapi.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import ro.duckind.resumeioapi.dto.MatchingDto;
import ro.duckind.resumeioapi.dto.ScoreDto;
import ro.duckind.resumeioapi.service.MatchingService;

@RestController
@RequiredArgsConstructor
@RequestMapping("/matching")
public class MatchingController {

    private final MatchingService matchingService;

    @PostMapping()
    public ScoreDto matchCandidate(@RequestBody MatchingDto matchingDto) {
        return matchingService.match(matchingDto);
    }
}

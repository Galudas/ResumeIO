package ro.duckind.resumeioapi.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;
import ro.duckind.resumeioapi.dto.MatchingDto;
import ro.duckind.resumeioapi.dto.ScoreDto;
import ro.duckind.resumeioapi.entity.MatchHistory;
import ro.duckind.resumeioapi.service.MatchingService;

import java.util.List;

@RestController
@RequiredArgsConstructor
@RequestMapping("/matching")
public class MatchingController {

    private final MatchingService matchingService;

    @GetMapping()
    public List<MatchHistory> getMatchHistory() {
        return matchingService.getMatchHistory();
    }

    @PostMapping()
    public ScoreDto matchCandidate(@RequestBody MatchingDto matchingDto) {
        return matchingService.match(matchingDto);
    }
}

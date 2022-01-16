package ro.duckind.resumeioapi.controller;

import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import ro.duckind.resumeioapi.entity.MatchingObject;
import ro.duckind.resumeioapi.service.MatchingService;

import java.util.concurrent.Future;

@RestController
@RequiredArgsConstructor
@RequestMapping("/matching")
public class MatchingController {

    private final MatchingService matchingService;

    @PostMapping()
    public Future<String> matchCandidate(@RequestBody MatchingObject matchingObject) {
        return matchingService.match(matchingObject);
    }
}

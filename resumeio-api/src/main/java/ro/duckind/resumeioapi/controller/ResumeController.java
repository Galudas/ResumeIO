package ro.duckind.resumeioapi.controller;


import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;
import ro.duckind.resumeioapi.entity.Resume;
import ro.duckind.resumeioapi.repo.ResumeRepository;

import java.util.List;

@RestController
@RequiredArgsConstructor
@RequestMapping("/resumes")
public class ResumeController {

    private final ResumeRepository resumeRepository;

    @GetMapping("/")
    public List<Resume> resumes() {
        return resumeRepository.findAll();
    }

    @PostMapping("/")
    public void resumes(@RequestBody Resume resume) {
        resumeRepository.save(resume);
    }
}

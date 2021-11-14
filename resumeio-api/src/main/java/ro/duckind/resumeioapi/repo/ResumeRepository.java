package ro.duckind.resumeioapi.repo;

import org.springframework.data.jpa.repository.JpaRepository;
import ro.duckind.resumeioapi.entity.Resume;

public interface ResumeRepository extends JpaRepository<Resume, Long> {
}

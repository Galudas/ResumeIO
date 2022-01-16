package ro.duckind.resumeioapi.repo;

import org.springframework.data.jpa.repository.JpaRepository;
import ro.duckind.resumeioapi.entity.MatchHistory;

public interface MatchHistoryRepository extends JpaRepository<MatchHistory, Long> {
}

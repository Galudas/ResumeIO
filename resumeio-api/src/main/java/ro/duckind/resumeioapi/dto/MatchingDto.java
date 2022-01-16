package ro.duckind.resumeioapi.dto;

import lombok.Data;

@Data
public class MatchingDto {
    private String candidateName;
    private String jobDescription;
    private String candidateDescription;
}

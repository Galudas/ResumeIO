package ro.duckind.resumeioapi.entity;

import lombok.Getter;
import lombok.Setter;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Getter
@Setter
@Table(name = "resume")
public class Resume {
    @Id
    Long id;
    String name;
}

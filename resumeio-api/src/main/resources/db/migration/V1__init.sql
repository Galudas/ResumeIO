create table match_history
(
    id                    bigserial
        primary key,
    candidate_description varchar(10000),
    job_description       varchar(10000),
    score                 varchar(10000),
    name                 varchar(10000)
);

alter table match_history
    owner to resumeio;

INSERT INTO public.match_history (id, candidate_description, job_description, score, name) VALUES (10, 'Working on Replicator(Generic Web App engine),
developing generic React components(Tables,
Pages, Forms etc), which consumes auto
generated APIs.', 'Java 11, Spring Boot, Spring REST, React.js
React Hooks, PostgreSQL, HTML/CSS, docker
docker-compose, C', '0.14285714285714285', 'andrei10');
INSERT INTO public.match_history (id, candidate_description, job_description, score, name) VALUES (1, 'sad', 'sad', '1.0', 'andrei1');
INSERT INTO public.match_history (id, candidate_description, job_description, score, name) VALUES (9, 'Working on Replicator(Generic Web App engine),
developing generic React components(Tables,
Pages, Forms etc), which consumes auto
generated APIs.', 'Java 11, Spring Boot, Spring REST, React.js
React Hooks, PostgreSQL, HTML/CSS, docker
docker-compose, C', '0.14285714285714285', 'andrei9');
INSERT INTO public.match_history (id, candidate_description, job_description, score, name) VALUES (8, 'Working on Replicator(Generic Web App engine),
developing generic React components(Tables,
Pages, Forms etc), which consumes auto
generated APIs.', 'Java 11, Spring Boot, Spring REST, React.js
React Hooks, PostgreSQL, HTML/CSS, docker
docker-compose, C', '0.14285714285714285', 'andrei8');
INSERT INTO public.match_history (id, candidate_description, job_description, score, name) VALUES (3, 'sad', 'sad', '1.0', 'andrei3');
INSERT INTO public.match_history (id, candidate_description, job_description, score, name) VALUES (6, 'Working on Replicator(Generic Web App engine),
developing generic React components(Tables,
Pages, Forms etc), which consumes auto
generated APIs.', 'Java, Python React', '0.14285714285714285', 'andrei6');
INSERT INTO public.match_history (id, candidate_description, job_description, score, name) VALUES (7, 'Working on Replicator(Generic Web App engine),
developing generic React components(Tables,
Pages, Forms etc), which consumes auto
generated APIs.', 'Java 11, Spring Boot, Spring REST, React.js
React Hooks, PostgreSQL, HTML/CSS, docker
docker-compose, C', '0.14285714285714285', 'andrei7');
INSERT INTO public.match_history (id, candidate_description, job_description, score, name) VALUES (2, 'sad', 'sad', '1.0', 'andrei2');
INSERT INTO public.match_history (id, candidate_description, job_description, score, name) VALUES (5, 'Working on Replicator(Generic Web App engine),
developing generic React components(Tables,
Pages, Forms etc), which consumes auto
generated APIs.', 'Java, Python ', '0.0', 'andrei5');
INSERT INTO public.match_history (id, candidate_description, job_description, score, name) VALUES (4, '• Working on Replicator(Generic Web App engine),
developing generic React components(Tables,
Pages, Forms etc), which consumes auto
generated APIs.', 'Java, Python ', '0.0', 'andrei4');
INSERT INTO public.match_history (id, candidate_description, job_description, score, name) VALUES (11, 'Working on Replicator(Generic Web App engine),
developing generic React components(Tables,
Pages, Forms etc), which consumes auto
generated APIs.', 'React.js, Spring REST, Spring Boot,
PostgreSQL, Hibernate, Docker, Docker-compos', '0.14285714285714285', 'andrei199');
INSERT INTO public.match_history (id, candidate_description, job_description, score, name) VALUES (16, 'sd', 'dsa', '0.0', 'dsa');
INSERT INTO public.match_history (id, candidate_description, job_description, score, name) VALUES (15, 'asd', 'asd', '1.0', 'sd');
INSERT INTO public.match_history (id, candidate_description, job_description, score, name) VALUES (14, 'asd', 'asd', '1.0', 'dsd');
INSERT INTO public.match_history (id, candidate_description, job_description, score, name) VALUES (12, 'Working on Replicator(Generic Web App engine),
developing generic React components(Tables,
Pages, Forms etc), which consumes auto
generated APIs', 'React.js, Spring REST, Spring Boot,
PostgreSQL, Hibernate, Docker, Docker-compos', '0.14285714285714285', 'sad');
INSERT INTO public.match_history (id, candidate_description, job_description, score, name) VALUES (13, 'asd', 'asd', '1.0', 'sads');
INSERT INTO public.match_history (id, candidate_description, job_description, score, name) VALUES (17, 'Working on Replicator(Generic Web App engine),
developing generic React components(Tables,
Pages, Forms etc), which consumes auto
generated APIs', 'React.js, Spring REST, Spring Boot,
PostgreSQL, Hibernate, Docker, Docker-compose.', '0.14285714285714285', 'Andrei Rata');
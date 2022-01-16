import gensim.downloader as api
import numpy as np

import cv_parser
import job_parser

model = api.load("glove-wiki-gigaword-300")


def find_similarities(candidate_description, job_description):
    similar_words = []
    similar_words_aux = []
    for candidate_description_word in candidate_description:
        for job_description_word in job_description:
            similarity = np.dot(candidate_description_word[0], job_description_word[0]) / (
                    np.linalg.norm(candidate_description_word[0]) * np.linalg.norm(job_description_word[0]))
            if similarity > 0.7:
                if candidate_description_word[1] not in similar_words_aux:
                    similar_words_aux.append(candidate_description_word[1])
                    similar_words.append((candidate_description_word[1], job_description_word[1]))
    return similar_words


def encode_words(word_list):
    codifications = []
    for word in word_list:
        if word in model:
            codifications.append((model[word], word))
    return codifications


def match():
    print("START")
    candidates = cv_parser.extract_cv_data()
    job_description = job_parser.extract_job_data()
    job_encoded = list(np.append(job_description.description, job_description.requirements))
    job_encoded = encode_words(job_encoded)
    rank = {}
    for candidate in candidates:
        candidate_encoded = list(np.append(candidate.skills, candidate.experience))
        candidate_encoded = encode_words(candidate_encoded)
        similarities = find_similarities(candidate_encoded, job_encoded)
        if len(candidate_encoded) != 0:
            rank[candidate.name] = len(similarities) / len(candidate_encoded)
        print(similarities)
    rank = [(k, v) for k, v in sorted(rank.items(), key=lambda item: item[1],  reverse=True)]
    print(rank)


match()

import gensim.downloader as api
import numpy as np
import util

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


def match(job_description, candidate_description):
    print("Start matching")
    print(job_description)
    print(candidate_description)
    parsed_job = util.get_most_important_words(job_description)
    parsed_candidate = util.get_most_important_words(candidate_description)
    encoded_job = encode_words(parsed_job)
    encoded_candidate = encode_words(parsed_candidate)
    similarities = find_similarities(encoded_candidate, encoded_job)
    if len(encoded_candidate) != 0:
        similarity_score = len(similarities) / len(encoded_candidate)
        print("Similarity score: " + str(similarity_score))
        return similarity_score
    return 0

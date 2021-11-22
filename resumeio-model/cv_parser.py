import os
import random
import docx
import regex
import applicant

cv_file_path = "../resumeio-cv-generator/cv_data/"
position_file_path = "../resumeio-cv-generator/positions.txt"


def random_position(file_name):
    file = open(file_name, "r")
    line = next(file)
    for num, aline in enumerate(file, 2):
        if random.randrange(num):
            continue
        line = aline
    return line


def read_docx():
    position_name = random_position(position_file_path)
    file_regex = "cv_" + position_name.replace("\n", "") + "_.*"
    cv_list = [file for file in os.listdir(cv_file_path) if regex.match(file_regex, file)]
    for cv in cv_list:
        print(cv_data(cv_file_path + cv))


def cv_data(filename):
    doc = docx.Document(filename)
    last_name = ""
    firs_name = ""
    email = ""
    position = ""
    experience = ""
    skills = ""
    i = 0
    # print(doc.paragraphs)
    # while i < len(doc.paragraphs):
    #     if str(doc.paragraphs[i]).find("Last name:"):
    #         print(str(doc.paragraphs[i]))
    #         last_name = str(doc.paragraphs[i]).split("Last name: ")[1]
    #     if str(doc.paragraphs[i]).find("First name:"):
    #         firs_name = str(doc.paragraphs[i]).split("First name: ")[1]
    #     if str(doc.paragraphs[i]).find("Email:"):
    #         email = str(doc.paragraphs[i]).split("Email: ")[1]
    #     if str(doc.paragraphs[i]).find("Experience:"):
    #         position = str(doc.paragraphs[i]).split("Experience: ")[1]
    #         i += 1
    #         experience = str(doc.paragraphs[i])
    #     if str(doc.paragraphs[i]).find("Skills:"):
    #         i += 1
    #         skills = str(doc.paragraphs[i])
    #     i += 1
    return applicant.Applicant(experience, skills, firs_name + " " + last_name, email, position)


read_docx()

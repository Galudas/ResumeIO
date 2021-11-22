import docx2txt


def get_text(file_name):
    my_text = docx2txt.process(file_name)
    print(my_text)


get_text("cv_data/1.docx")
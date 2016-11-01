import argparse
import string

import docx2txt

parser = argparse.ArgumentParser()
parser.add_argument('target', type=int,
                    help='target word count')
parser.add_argument('file_path', help='path to the file')
args = parser.parse_args()


def display(word_count, progress):
    print("*" * 50 + "*")
    print("Target: {}".format(args.target))
    print("Word Count: {}".format(word_count))
    print("Progress: {}".format(progress))
    print("*" * 50 + "*")


def main():
    full_text = docx2txt.process(args.file_path)
    punctuations = string.punctuation + "…“”"
    empty_string = ' ' * len(punctuations)
    translation_table = full_text.maketrans(punctuations, empty_string)
    clean_text = full_text.translate(translation_table)
    word_count = len(clean_text.split())
    progress = (word_count / args.target) * 100
    return display(word_count=word_count, progress=progress)


if __name__ == '__main__':
    main()

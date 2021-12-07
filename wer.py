#!/usr/bin/env python3
import jiwer
import sys


class ReplaceYo(jiwer.AbstractTransform):

    def process_string(self, s: str):
        s = s.replace("ё", "е")
        return s


def load_file(path):
    with open(path) as f:
        result = f.read()
    return result


def main(ref_path, hyp_path):
    ref = load_file(ref_path)
    hyp = load_file(hyp_path)

    tr = [
        jiwer.ToLowerCase(),
        jiwer.RemovePunctuation(),
        ReplaceYo(),
        jiwer.RemoveWhiteSpace(replace_by_space=True),
        jiwer.RemoveMultipleSpaces(),
        jiwer.ReduceToSingleSentence(),
        jiwer.ReduceToListOfListOfWords(word_delimiter=" "),
    ]

    transformation = jiwer.Compose(tr)

    measures = jiwer.compute_measures(
        ref,
        hyp,
        truth_transform=transformation,
        hypothesis_transform=transformation
    )
    print(f"WER (Words Error Rate): {measures['wer']}")
    print(f"MER (Match Error Rate): {measures['mer']}")
    print(f"WIL (Word Information Lost): {measures['wil']}")
    print(f"WIP (Word Information Preserved): {measures['wip']}")
    print(f"Hits: {measures['hits']}")
    print(f"Substitutions: {measures['substitutions']}")
    print(f"Deletions: {measures['deletions']}")
    print(f"Insertions: {measures['insertions']}")


if __name__ == '__main__':
    try:
        r, h = sys.argv[1:3]
    except TypeError:
        print("This program must be run with 2 arguments: 'python wer.py <hypothesys_file_path> <reference_file_path>'")
        sys.exit(1)
    main(r, h)

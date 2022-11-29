def _process_word(word: str) -> str:
    # Possible weakness - unusual punctuation can be missing in the list
    mark = word[-1] if word[-1] in [".", ",", "!", "?", "(", ")"] else ""
    if mark:
        word = word[:-1]
    rev_word = word[::-1]
    if word[0].isupper():
        rev_word = f"{rev_word[0].upper()}{rev_word[1:-1]}{rev_word[-1].lower() if word[-1].islower() else rev_word[-1]}"
    return f"{rev_word}{mark}"


def revert(sentence: str) -> str:
    return " ".join([_process_word(word) for word in sentence.split()])


if __name__ == '__main__':
    assert revert("The brown dog jumps in the meadows.") == "Eht nworb god spmuj ni eht swodaem."
    assert revert("Is it correct? I'm not sure.") == "Si ti tcerroc? M'i ton erus."
    assert revert("hOw AbOuT dIfFeReNt CaSeS?") == "wOh TuObA tNeReFfId SeSaC?"
    assert revert("Ops, (I forgot to close bracket") == "Spo, I( togrof ot esolc tekcarb"
    assert revert("My favorite group is SUM41") == "Ym etirovaf puorg si 14MUS"

def spell_checker(wordlist: list[str], queries: list[str]) -> list[str]:
    result = []
    case_insensitive = dict()
    no_vowels_words = dict()
    vowels = set("aeiou")

    def form_new_word(wrd: str):
        new_word = ''.join('_' if c in vowels else c for c in wrd.lower())
        return new_word

    for w in wordlist:
        lower_w = w.lower()
        nv_word = form_new_word(w)

        if lower_w not in case_insensitive:
            case_insensitive[lower_w] = w

        if nv_word not in no_vowels_words:
            no_vowels_words[nv_word] = w

    for q in queries:
        if q in wordlist:
            result.append(q)
        elif q.lower() in case_insensitive:
            result.append(case_insensitive[q.lower()])
        else:
            nv_q = form_new_word(q)
            if nv_q in no_vowels_words:
                result.append(no_vowels_words[nv_q])
            else:
                result.append("")

    return result


print(spell_checker(["KiTe", "kite", "hare", "Hare"],
                    ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]))
print(spell_checker(["yellow"], ["YellOw"]))
print(spell_checker(["ae", "aa"], ["UU"]))

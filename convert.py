from pathlib import Path
import jaconv
import bz2

def is_hiragana(text):
    hira_list = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔ"
    for i in range( len(text)):
        if text[i] not in hira_list:
            return False
        return True


with bz2.open("./mozcdic-ut-jawiki.txt.bz2", "rt", encoding="utf-8") as f:
    data = f.read()

data = data.split("\n")

out = []
for line in data:
    split_line = line.split("\t")
    if len(split_line) >= 2:
        surface = split_line[4]
        yomi = split_line[0]
        yomi = jaconv.kata2hira(yomi)
        if is_hiragana(yomi):

            new_line = f"{surface},1345,1345,8000,名詞,一般,*,*,*,*,{surface},{yomi},{yomi}"
            out.append((new_line))

num = len(out) // 4
out_0 = out[:num]
out_1 = out[num:num*2]
out_2 = out[num*2:num*3]
out_3 = out[num*3:]

Path("./build/jtalkdic-ud-jawiki-ipadic-00.csv").write_text("\n".join(out_0), encoding="utf-8")
Path("./build/jtalkdic-ud-jawiki-ipadic-01.csv").write_text("\n".join(out_1), encoding="utf-8")
Path("./build/jtalkdic-ud-jawiki-ipadic-02.csv").write_text("\n".join(out_2), encoding="utf-8")
Path("./build/jtalkdic-ud-jawiki-ipadic-03.csv").write_text("\n".join(out_3), encoding="utf-8")

out = []
for line in data:
    split_line = line.split("\t")
    if len(split_line) >= 2:
        surface = split_line[4]
        yomi = split_line[0]
        if is_hiragana(yomi):
            yomi = jaconv.hira2kata(yomi)
            new_line = f"{surface},1345,1345,8000,名詞,一般,*,*,*,*,{surface},{yomi},{yomi},*/*,*"
            out.append((new_line))

num = len(out) // 4
out_0 = out[:num]
out_1 = out[num:num*2]
out_2 = out[num*2:num*3]
out_3 = out[num*3:]

Path("./build/jtalkdic-ud-jawiki-noacc-00.csv").write_text("\n".join(out_0), encoding="utf-8")
Path("./build/jtalkdic-ud-jawiki-noacc-01.csv").write_text("\n".join(out_1), encoding="utf-8")
Path("./build/jtalkdic-ud-jawiki-noacc-02.csv").write_text("\n".join(out_2), encoding="utf-8")
Path("./build/jtalkdic-ud-jawiki-noacc-03.csv").write_text("\n".join(out_3), encoding="utf-8")
import html.entities, re, sys

def ucode(c):
    retval = "\\u" + ("0000" + hex(c)[2:])[-4:] 
    return retval

def uchr(c):
    retval = chr(c)
    return retval

def DeMarkup(text):
    # remove HTML markup and replace selected HTML entities with alternatives
    retval = re.sub('\>\[\<', '><', text)
    retval = re.sub('<[^<]+?>', '', retval)
    retval = re.sub('&nbsp;', ' ', retval)
    retval = re.sub('&rsquo;', "'", retval)
    retval = re.sub('&rdquo;', "'", retval)
    retval = re.sub('&ldquo;', "'", retval)
    retval = re.sub('&ndash;', "-", retval)
    retval = re.sub('&mdash;', "-", retval)
    retval = re.sub(u"\u2010", "-", retval)
    retval = re.sub(u"\uFB02", "fl", retval)
    return retval

def DeEntify(text):
    # replace HTML entities with unicode
    retval = re.sub('&([^;]+);', lambda m: chr(html.entities.name2codepoint[m.group(1)]), text)
    return retval

def CleanText(text):
    retval = DeMarkup(text)
    retval = DeEntify(retval)
    return retval

fname = "chars.txt"
f = open(fname, "w", encoding="utf-8-sig")
print("\t".join(["Hex", "UTF-8", "Dec", "Entity", "Char"]))
f.write("\t".join(["Hex", "UTF-8", "Dec", "Entity", "Char"]) + "\n")      
for i in range(0x0000, 0x27BF):
    try:
        print("\t".join([hex(i), ucode(i), str(i), "&"+html.entities.codepoint2name[i]+";", uchr(i)]))
        f.write("\t".join([hex(i), ucode(i), str(i), "&"+html.entities.codepoint2name[i]+";", uchr(i)]) + "\n")
    except:
        pass
f.close()

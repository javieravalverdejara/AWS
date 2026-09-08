import re

with open("preproinsulin-seq.txt", "r") as f:
    content = f.read()

clean = re.sub(r'[^a-zA-Z]', '', content.replace("ORIGIN", "").replace("//", ""))
clean = clean.lower()

print(f"Total caracteres: {len(clean)}")
print(clean)

with open("preproinsulin-seq-clean.txt", "w") as f:
    f.write(clean)

with open("lsinsulin-seq-clean.txt", "w") as f:
    f.write(clean[0:24])

with open("binsulin-seq-clean.txt", "w") as f:
    f.write(clean[24:54])

with open("cinsulin-seq-clean.txt", "w") as f:
    f.write(clean[54:89])

with open("ainsulin-seq-clean.txt", "w") as f:
    f.write(clean[89:110])

print("Archivos creados exitosamente!")

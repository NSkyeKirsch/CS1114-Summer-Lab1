dna = "ACTGATCGATTAGCAGTAAGCGCTTAGCT"

new_str = ""

for i in range(len(dna)):
    if dna[i] == "A":
        new_str += "T"
    elif dna[i] == "T":
        new_str += "A"
    elif dna[i] == "C":
        new_str += "G"
    elif dna[i] == "G":
        new_str += "C"

print(new_str)
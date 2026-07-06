mutated_dna=input('enter the dna segment')
mutated_sequence=input('enter the sequence')
c=mutated_dna.find(mutated_sequence)
d=c+len(mutated_sequence)
segment_1=mutated_dna[:c]
segment_2=mutated_dna[d:]
print(segment_1+segment_2)


#cách 2
chuoi = "ATTAGCGC"
mappingTable = chuoi.maketrans('ATGC', 'UAGC')
print(chuoi.translate(mappingTable))

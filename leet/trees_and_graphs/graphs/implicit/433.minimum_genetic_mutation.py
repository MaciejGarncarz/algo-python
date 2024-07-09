# https://leetcode.com/problems/minimum-genetic-mutation/description/

from collections import deque
from typing import List


def minMutation(startGene: str, endGene: str, bank: List[str]) -> int:
    moleculeTypes = ['A', 'C', 'G', 'T']

    queue = deque([(startGene, 0)])
    seen = set(startGene)

    while queue:
        gene, steps = queue.popleft()

        if gene == endGene:
            return steps
        
        for x in range(0, 8):
            for type in moleculeTypes:
                gene_list = list(gene)
                gene_list[x] = type
                geneModified = ''.join(gene_list)
                if geneModified not in seen:
                    if geneModified in bank and geneModified not in seen:
                        queue.append((geneModified, steps + 1))
                    seen.add(geneModified)
    
    return -1

# startGene = "AACCGGTT"
# endGene = "AACCGGTA"
# bank = ["AACCGGTA"]

startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]

print(minMutation(startGene, endGene, bank))


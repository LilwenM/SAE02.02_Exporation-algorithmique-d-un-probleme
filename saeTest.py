import LePostierChinois1 as pc1
import LePostierChinois2 as pc2


graphe_algo1 = {
                  "A" : {"B"}, 
                  "B" : {"A"},
                  "C" : {"D", "E"}, 
                  "D" : {"C", "E"}, 
                  "E" : {"C", "D"}, 
                  "F" : set()
               }

graphe_algo2 = {
                  "A" : ["B"], 
                  "B" : ["A"],
                  "C" : ["D", "E"], 
                  "D" : ["C", "E"], 
                  "E" : ["C", "D"],
                  "F" : []
               }


G1 = pc1.LePostierChinois(graphe_algo1)
G2 = pc2.LePostierChinois(graphe_algo2)

print(G1.algorithme_pc1())
print(G2.algorithme_pc2())
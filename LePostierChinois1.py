class LePostierChinois : 
    
    #--------------Initialisation----------------
    def __init__(self, graphe) :
        """ initialise un objet graphe. Si aucun dictionnaire n'est créé ou donné, on en utilisera un vide """
        self._graphe = graphe
        self._sommet_depart = list(graphe.keys())[0]
        return

    
    #----------------
    
    def __str__(self):
        affichage = "{\n"
        
        for sommet in self.liste_sommets() :
            affichage += "  " + sommet + "  :  "
            affichage += f"{self.aretes(sommet)}\n"
        affichage += "}\n"
        return affichage

    
    #-----------------Methode----------------
    
    def liste_sommets(self) : 
        return list(self._graphe)
    
    def aretes(self, sommet):
        """ retourne une liste de toutes les aretes d'un sommet """
        liste = []
        for i in self._graphe[sommet] : 
            liste.append([sommet, i])
        return liste
    
    def liste_aretes(self) : 
        """ liste les du graphe """
        liste_aretes = []

        for i in self.liste_sommets() :
            for j in self.aretes(i) : 
                liste_aretes.append(j)
        return liste_aretes
    
    def liste_voisin(self, sommet) : 
        """ liste des voisins du sommet """
        return self._graphe[sommet]
    

        #------Aretes------
        
    def arete_existante(self, s1, s2) : 
        """ true si l'arete existe, false sinon """
        
        arete_existante = False
        
        if s2 in self._graphe[s1] and s1 in self._graphe[s2] : 
            arete_existante = True
        
        return arete_existante
    
    
    def ajouter_arete(self, s1, s2) : 
        """ permet d'ajouter l'arete souhaitee au graphe """
        
        liste_AllSommets = self.liste_sommets()
        
        if (s1 not in liste_AllSommets or s2 not in liste_AllSommets) : 
            return None
        
        self._graphe[s1].add(s2)
        self._graphe[s2].add(s1)
        return
    
    
    def supprimer_arete(self, s1, s2) : 
        """ permet de supprimer l'arete souhaitee au graphe """
        liste_AllSommets = self.liste_sommets()
        
        if (s1 not in liste_AllSommets or s2 not in liste_AllSommets) : 
            return None
        
        voisin = set()
        for i in self._graphe[s1] : 
            if i != s2 : 
                voisin.add(i)
        self._graphe[s1] = voisin
        
        voisin = set()
        for i in self._graphe[s2] : 
            if i != s1 : 
                voisin.add(i)
        self._graphe[s2] = voisin
        return
    
    
        #------Degre------
    def degre_sommet(self, sommet):
        """ renvoie le degre du sommet """
        return len(self._graphe[sommet])
    
    
    def allSommets_degrePair(self) : 
        """ retourne la liste de tous les sommets de degre pair """
        
        allSommets_isole = self.allSommet_isole()
        allSommets_degrePair = []
        
        liste_AllSommets = self.liste_sommets()
        for sommet in liste_AllSommets : 
            if self.degre_sommet(sommet)%2 == 0 and not(sommet in allSommets_isole) : # si le nombre de voisin est impaire
                allSommets_degrePair.append(sommet)
        
        return allSommets_degrePair
   
   
    def allSommets_degreImpair(self) : 
        """ retourne la liste de tous les sommets de degre impair """
        
        allSommets_degreImpair = []
        
        liste_AllSommets = self.liste_sommets()
        for sommet in liste_AllSommets : 
            if self.degre_sommet(sommet)%2 != 0 : # si le nombre de voisin est impaire
                allSommets_degreImpair.append(sommet)
        
        return allSommets_degreImpair


    def allSommet_isole(self) : 
        """ retourne la liste de tous les sommets isoles """
        
        allSommet_isole = []
        
        liste_AllSommets = self.liste_sommets()
        for sommet in liste_AllSommets : 
            if self.degre_sommet(sommet) == 0 :
                allSommet_isole.append(sommet)
        
        return allSommet_isole
    
    
        #------Verif Boolean------
    def est_connexe(self) : 
        """ verifie si le graphe est bien connexe. Retourne true dans ce cas, 
        false dans l'autre """
        est_connexe = True
        
        liste_AllSommets = self.liste_sommets()
        for i in liste_AllSommets : 
            if self._graphe[i] == set() : 
                est_connexe = False
        
        return est_connexe
       
   
    def est_eulerien(self) : 
        """ verifie si le graphe est eulerien. Retourne true si dans ce cas,
        false dans l'autre """
        est_eulerien = True
                
        if not(self.est_connexe()) or len(self.allSommets_degrePair()) != len(self.liste_sommets()) : 
            est_eulerien = False
        return est_eulerien
    
    
        #------Completement connexe------
    
    def chemin_existe(self, sommet_dep, sommet_arr) :
        """ trouve le chemin permettant de parcourir le graphe pour aller du sommet_dep au sommet_arr """

        if not(sommet_dep in self.liste_sommets()) or not(sommet_arr in self.liste_sommets()):
            return None
        
        pile = [(sommet_dep,[sommet_dep])]
        chemin = []

        while len(pile) != 0 :
            sommet,chemin = pile.pop()
            
            liste_nouveaux_sommets_voisins = []
            liste_voisin = self.aretes(sommet)
            for i in range(len(liste_voisin)) :
                voisin = liste_voisin[i]
                voisin = voisin[1]
                if voisin not in chemin : 
                    liste_nouveaux_sommets_voisins.append(voisin)
            
            for voisin in liste_nouveaux_sommets_voisins :
                if voisin == sommet_arr :
                    return chemin + [sommet_arr]
                pile.append((voisin,chemin + [voisin]))

        return None
    

    def graphe_toParcourable(self) : 
        """ fait en sorte que de n'importe quel sommet, il soit possible d'aller à n'importe quel autre sommet """
        
        liste_AllSommet = self.liste_sommets()
        
        for i in liste_AllSommet : 
            for j in liste_AllSommet :
                if i != j and self.chemin_existe(i, j) == None : 
                    self.ajouter_arete(i, j)
        
        return
    
        #------Cycle eulerien------
    
    def sommet_suivant_cycle_eulerien(self, dict_voisins, sommet_en_cours) : 
        """ determine le sommet devant être le prochain dans la création du cycle et le retourne """
        sommet_suivant = list(dict_voisins.items())[0][0]
        mini_degre = dict_voisins[sommet_suivant]
        
        if self.degre_sommet(sommet_en_cours) > 1 : 
            
            for i in dict_voisins.keys() : 
                if mini_degre == 1 or (dict_voisins[i] < mini_degre and dict_voisins[i] != 1) :
                    sommet_suivant = i
                    mini_degre = dict_voisins[i]
                        
        return sommet_suivant      
    
    
    def cycle_eulerien(self) : 
        """ creer et renvoie un cycle eulerien du graphe """
        
        cycle = []
        
        sommet = self._sommet_depart
        cycle.append(sommet)

        while len(self.liste_aretes()) > 0 :
            voisins = self.liste_voisin(sommet)
            dict_voisins = {}
            
            for i in voisins : 
                dict_voisins[i] = self.degre_sommet(i)
            
            sommet_suivant = self.sommet_suivant_cycle_eulerien(dict_voisins, sommet)

            cycle.append(sommet_suivant)
            self.supprimer_arete(sommet, sommet_suivant)
            
            sommet = sommet_suivant
                
        return cycle
    
    
        #------Transformation en eulerien------
    
    def trans_sommetIsole(self) : 
        """ permet de lier les sommets isolé entre eux puis de lier le dernier au reste du graphe """
        
        allSommet_isole = self.allSommet_isole()
        allSommet_degreImpair = self.allSommets_degreImpair()
        allSommet_degrePair = self.allSommets_degrePair()
        
        if len(allSommet_isole) > 0 :
            for i in range(len(allSommet_isole)-1) : 
                self.ajouter_arete(allSommet_isole[i], allSommet_isole[i+1])
            
            if len(allSommet_degreImpair) > 0 : 
                self.ajouter_arete(allSommet_isole[-1], allSommet_degreImpair[0])
            elif len(allSommet_degrePair) > 0 :
                self.ajouter_arete(allSommet_isole[-1], allSommet_degrePair[0])
            else :
                self.ajouter_arete(allSommet_isole[-1], allSommet_isole[0])
        return
    
    
    def trans_sommetImpair(self) : 
        """ permet d'ajouter des aretes aux sommets de degres impair pour les rendrent pair """
                
        i = 0
        allSommet_degreImpair = self.allSommets_degreImpair()
     
                
        while len(allSommet_degreImpair) > 0 : 
            
            nbr_sommetImpair = len(allSommet_degreImpair)
            est_cree = False
                        
            for j in range(1, nbr_sommetImpair) : 
                if not(self.arete_existante(allSommet_degreImpair[i], allSommet_degreImpair[j])) and allSommet_degreImpair[i] != allSommet_degreImpair[j] : 
                    self.ajouter_arete(allSommet_degreImpair[i], allSommet_degreImpair[j])
                    i = 0
                    est_cree = True
                    break
            
            if est_cree == False : 
                listeVoisin = self.liste_voisin(allSommet_degreImpair[i])
                listeVoisinPair = []
                
                for k in listeVoisin : 
                    if self.degre_sommet(k)%2 == 0 :
                        listeVoisinPair.append(k)
                
                if len(listeVoisinPair) > 0 :
                    
                    self.supprimer_arete(allSommet_degreImpair[i], listeVoisinPair[0])
                    i = 0
                else : 
                    i += 1
                    
            allSommet_degreImpair = self.allSommets_degreImpair()
            
        return
    
    
    def transforme_toEulerien(self) : 
        """ permet de transformer un graphe non eulerien en eulerien """
        
        self.trans_sommetIsole()
        
        if self.est_eulerien() : 
            return
                
        self.trans_sommetImpair()
        
        return
    

        #------ ------
        
    def algorithme_pc1(self) : 
        """ La méthode permet de résoudre le problème du postier chinois et 
        de retourner un chemin que le postier pourra emprunter. """
        
        if len(self.liste_sommets()) >= 3 :
            
            if not(self.est_eulerien()) :
                self.transforme_toEulerien()
            
            self.graphe_toParcourable()
            
            if not(self.est_eulerien()) :
                self.transforme_toEulerien()

            chemin = self.cycle_eulerien()
            return chemin
        
        elif len(self.liste_sommets()) == 2 : 
            return self.liste_sommets() + [self.liste_sommets()[0]]
        
        else : 
            return self.liste_sommets()
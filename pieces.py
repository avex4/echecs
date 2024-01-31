class piece():
    def __init__(self,type,couleur):
        self.type = type
        self.couleur = couleur
        
class vide():
    def __init__(self):
        pass

class pion():
    def __init__(self,board,x,y):
        self.x = x
        self.y = y
        self.range = []
        if y == 0 :
            pass
        if board[y-1][x] == vide :
            range.append([y-1,x])
        if x != 0 and board[y-1,x-1].piece.couleur == "noir":
            range.append([y-1,x-1])
        if x != 7 and board[y-1,x+1].piece.couleur == "blanc":
            range.append([y-1,x+1])
        
               

        
                        
                        
class tour():
    def __init__(self,board,x,y) :
        self.x = x
        self.y = y
        self.range = []            
        
        # if x != 7:
        #     aim_x = x+1
        #     while aiming :
                
        
    def aiming_(self,board) : 
        
        aim_x = self.x
        aim_y = self.y
        
        if self.x != 0:
            aim_x = self.x-1
            aiming = True
            while aiming :
                if aim_x == 0 :
                    self.range.append([aim_y,aim_x])
                    aiming = False
                else :
                    if board[aim_y][aim_x].piece.couleur != board[self.y][self.x].piece.couleur:
                        self.range.append([aim_y,aim_x])
                        aiming = False
                    if board[aim_y][aim_x].type == vide : 
                        self.range.append([aim_y,aim_x])
                        aim_x -= 1
                    else  :
                        aiming = False
                        
        if self.x != 7:
            aim_x = self.x+1
            aiming = True
            while aiming :
                if aim_x == 7 :
                    if board[aim_y][aim_x].piece.couleur != board[self.y][self.x].piece.couleur:
                        self.range.append([aim_y,aim_x])
                    aiming = False
                else :
                    if board[aim_y][aim_x].piece.couleur != board[self.y][self.x].piece.couleur:
                        self.range.append([aim_y,aim_x])
                        aiming = False
                    if board[aim_y][aim_x].type == vide : 
                        self.range.append([aim_y,aim_x])
                        aim_x += 1
                    else  :
                        aiming = False
                        
        if self.y != 0:
            aim_y = self.y-1
            aiming = True
            while aiming :
                if aim_y == 0 :
                    self.range.append([aim_y,aim_x])
                    aiming = False
                else :
                    if board[aim_y][aim_x].piece.couleur != board[self.y][self.x].piece.couleur:
                        self.range.append([aim_y,aim_x])
                        aiming = False
                    if board[aim_y][aim_x].type == vide : 
                        self.range.append([aim_y,aim_x])
                        aim_y -= 1
                    else  :
                        aiming = False
                        
        if self.y != 7:
            aim_y = self.y + 1
            aiming = True
            while aiming :
                if aim_y == 7 :
                    if board[aim_y][aim_x].piece.couleur != board[self.y][self.x].piece.couleur:
                        self.range.append([aim_y,aim_x])
                    aiming = False
                else :
                    if board[aim_y][aim_x].piece.couleur != board[self.y][self.x].piece.couleur:
                        self.range.append([aim_y,aim_x])
                        aiming = False
                    if board[aim_y][aim_x].type == vide : 
                        self.range.append([aim_y,aim_x])
                        aim_y += 1
                    else  :
                        aiming = False
            
                
            
        
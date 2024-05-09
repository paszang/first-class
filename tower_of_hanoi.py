class solution:
    def toh(self, N, fromm, to, aux):  #base case: if there is only one disk to move, move it directly from 'fromm' to 'to'
        if N == 1:
            print("move disk" + str(N) + "from rod"+ str(fromm)+"to rod" + str(to))
            print("\n")
            return 1
        # return 1 move made

        #Recursive case: move N-1 disks from 'fromm' to 'aux', using 'to' as an auxiliary rod

        moves = 0
        moves += self.toh(N-1, fromm, aux, to)  #Recursive call 
        moves += 1  #Increment the total moves count for the current step

        #Move the remaining largest disk from 'fromm' to 'to'
        print("move disk"+ str(N)+ "from rod"+ str(fromm) + "to rod"+ str(to))

        #Recursive call: Move the N-1 disks from 'aux' to 'to', using 'fromm' as an auxiliary rod
        moves += self.toh(N-1, aux, to, fromm)   #recursive call
        return moves  #return the total moves made for this step and all recursuve steps
    
s = solution()
print(s.toh(3,1,3,2))
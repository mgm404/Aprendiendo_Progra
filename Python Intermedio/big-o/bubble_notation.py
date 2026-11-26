def bubble_sorting_norm(list_needs_sorting):
    for outer_loops in range(0, len(list_needs_sorting)-1): #O(n)
        changed_positions=False#O(1)

        for i in range(0, len( list_needs_sorting)-1-outer_loops): #O(n^2)
            current_item= list_needs_sorting[i]#O(1)
            next_item=list_needs_sorting[i+1]#O(1)
            print(f"Revisando: {current_item}, siguiente a revisar: {next_item}")#O(1)

            if current_item>next_item:#O(n^3)
                list_needs_sorting[i]=next_item#O(1)
                list_needs_sorting[i+1]=current_item#O(1)
                print("estaban en el lugar equivocado, ya se cambiaron :3")#O(1)
                changed_positions=True#O(1)

        if not changed_positions:#O(n^2)
            print("No se cambio nada, ya esta perfecta la lista ~(°u°)~")#O(1)
            return#O(1)



disorganized_list=[1, 15, 2, 3, 8, 4, 6, 10]#O(1)
print(disorganized_list)#O(1)
bubble_sorting_norm(disorganized_list)#O(n)
print(disorganized_list)#O(1)
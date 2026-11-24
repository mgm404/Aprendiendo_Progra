def bubble_sorting_backwards(list_needs_sorting):
    for outer_loops in range(0, len(list_needs_sorting)-1): #passes through each item based on the total amount of items
        changed_positions=False#to catch and stop unnecessary loops

        for i in range(len(list_needs_sorting)-1, 0+outer_loops, -1): #so it doesn't bug out + doesn't touch correccted positions
            #range goes from the last item to the first
            current_item= list_needs_sorting[i]
            next_item=list_needs_sorting[i-1]
            print(f"Revisando: {current_item}, siguiente a revisar: {next_item}")

            if current_item<next_item: #checks if its in the wrong spot, moving the smaller item
                list_needs_sorting[i]=next_item
                list_needs_sorting[i-1]=current_item
                print("estaban en el lugar equivocado, ya se cambiaron :3")
                changed_positions=True

        if not changed_positions:
            print("No se cambio nada, ya esta perfecta la lista ~(°u°)~")
            return

def bubble_sorting_norm(list_needs_sorting):
    for outer_loops in range(0, len(list_needs_sorting)-1): #passes through each item based on the total amount of items
        changed_positions=False#to catch and stop unnecessary loops

        for i in range(0, len( list_needs_sorting)-1-outer_loops): #so it doesn't bug out + doesn't touch correccted positions
            current_item= list_needs_sorting[i]
            next_item=list_needs_sorting[i+1]
            print(f"Revisando: {current_item}, siguiente a revisar: {next_item}")

            if current_item>next_item: #checks if its in the wrong spot, moving the smaller item
                list_needs_sorting[i]=next_item
                list_needs_sorting[i+1]=current_item
                print("estaban en el lugar equivocado, ya se cambiaron :3")
                changed_positions=True

        if not changed_positions:
            print("No se cambio nada, ya esta perfecta la lista ~(°u°)~")
            return



disorganized_list=[1, 15, 2, 3, 8, 4, 6, 10]
print(disorganized_list)
bubble_sorting_norm(disorganized_list)
print(disorganized_list)

disorganized_list2=[1, 15, 2, 3, 8, 4, 6, 10]
print(disorganized_list2)
bubble_sorting_backwards(disorganized_list2)
print(disorganized_list2)
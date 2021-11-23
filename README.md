# DTW-algorithm
Data-Time Warping algorithm

functions description
normalize - normilizes array fron 0 to 100 
  (takes 1 array to normilize, returns normilized array)
dist - function to compute distance
  (takes 2 elements, returns computed distance (float))
Data_Time_Warping - main algorithm
  (takes 2 arrays, returns path (array) and distance (float))
Restore_path - from path and two arrays computes aligment
  (takes path fron DTW and 2 arrays, returns aligment (array))
Format_data_for_Excel - prints data in format for Excel to create Graphs
  (takes aligment from Restore_path, prints 1st and 2nd aligned lines for graps)
Format_path_to_table - prints table of path that algorithm chose
  (takes path (array) and sizes of original data arrays (floats), prints table)

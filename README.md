<a name="br1"></a>**Project Definition**

Project Title: Graph Coloring of the South America Map using Backtrack Search Algorithm


**Introduction**

The purpose of this project is to implement and demonstrate the application of the backtrack
search algorithm in solving the graph coloring problem for the South America map, while
adhering to the constraint of using only four colors (Blue, Green, Red, and Yellow). The project
aims to explore how the backtrack search algorithm can be utilized to assign these colors to
different regions of the South America map, ensuring that neighboring regions have different
colors. By successfully applying the algorithm within this constraint, the project aims to provide a
solution to the graph coloring problem for the South America map, showcasing the effectiveness
and efficiency of the backtrack search approach in a real-world scenario with limited color
choices.

**Inputs**

1\. neighbors: A CSV file containing the neighboring relationships between cities in a tabular
 format.

**Methods**

**1. set\_color\_map(): void**

**a.** Parameters: None

**b.** Implementation:

• An empty dictionary, color\_map, is initialized to store the color

assignments.

• The countries list contains the names of the countries to be included in the

color map.

• The for loop iterates over each country in the countries list. Inside the loop,
 the current country is used as a key in the color\_map dictionary, and its
 initial color assignment is set as None.

• After iterating over all the countries, the resulting color\_map dictionary is

returned.

• You can call this method simply by invoking set\_color\_map().




<a name="br2"></a>**2. read\_neighbors(filename): void**

**a.** Parameters:

• filename: CSV file path.

**b.** Implementation

• The graph dictionary is initialized to store the graph data.
• The CSV file is read using pandas' read\_csv() function, specifying the
 delimiter as ';' and header=None to treat all rows as data.
• The for loop iterates over each row in the data DataFrame using the
 iterrows() method.

• Inside the loop, the country name is extracted from the first column of the

current row (row[0]).

• The neighboring countries are extracted from the second column of the
 current row (row[1]) using the split() method to split them by comma.
• The country and its neighboring countries are added to the graph
 dictionary.

• After iterating over all the rows, the resulting graph dictionary is returned.
• You can call this method by passing the CSV file path as an argument, like
 this: graph = read\_neighbors('neighbors.csv').

**3. set\_colors(nextColor,nextNode): void**

**a.** Parameters:

• nextColor: Index of the current color in color list.
• nextNode: Index of the current country in graph.

**b.** Implementation

• The first if condition checks if the color assignment for the last country in
 the color\_map dictionary is not None. If so, it means all countries have
 been assigned colors, and the method returns.

• The second if condition checks if either the nextNode is the last country or
 if it is the first country and nextColor has reached the maximum number of
 colors. If so, it means the algorithm has explored all possible color
 assignments, and the method returns.

• The for loop iterates from nextNode to the end of the countries list.
• Inside the loop, the first if condition checks if nextColor has reached the
 maximum number of colors. If so, it means all colors have been tried for
 the current country. In that case, it updates nextNode and nextColor to
 backtrack to the previous country and try the next color for that country,
 and then calls the set\_colors() method recursively with the updated values.
• The elif condition checks if it is safe to assign the nextColor to the current
 country based on the neighboring countries' color assignments. If it is safe,



<a name="br3"></a>it assigns the color to the current country in the color\_map dictionary and
calls the set\_colors() method recursively with nextColor reset to 0 and
nextNode set to the next country index.

• The else block is reached when the current color is not safe for the current
 country. In that case, it increments nextColor and calls the set\_colors()
 method recursively with the updated nextColor and the same nextNode.
• The method does not have an explicit return value.

**4. is\_safe(neighbors,nextColor): Boolean**

**a.** Parameters:

• neighbors**:** A list consists of neighbors of current country.

• nextColor: Index of the color to be assigned to the current country.

**b.** Implementation

• The first if condition checks if the node has a value of 'NONE' or if the
 color\_map dictionary is empty. If either of these conditions is true, it
 means the current node can be safely assigned the next color, and the
 method returns True.

• The for loop iterates over each element in the node list.

• Inside the loop, the condition checks if the color assigned to the current
 neighboring node (node[i]) in the color\_map dictionary is the same as the
 nextColor. If it is the same, it means the current color is not safe to assign
 to the current node, and the method returns False.

• If none of the conditions in the loop are met, it means the current color is

safe for the current node, and the method returns True.

**5. findColorIndex(nextNode):**

**a.** Parameters:

• nextNode: Index of current node in graph.

**b.** Implementation

• Retrieves the color assigned to the country at nextNode from the
 color\_map dictionary using color\_map[countries[nextNode]] and assigns it
 to the color variable.

• The for loop iterates over each index in the range of the length of the

colors list.,

• Inside the loop, the condition checks if the color at the current ind ex of the
 colors list is equal to the color retrieved from the color\_map dictionary. If
 there's a match, it means the color has been found, and the method returns
 the current index.

• If the loop finishes without finding a match, it means the color was not

found in the colors list. In that case, the method returns 0.




<a name="br4"></a>**6. plot\_choropleth(colormap):**

**a.** Parameters:

• colormap: A graph consists of countries and colors assigned to them as a

dictionary.

**b.** Implementation

• Plots a choropleth graph based on the provided dictionary. **7. main():**

**a.** Parameters: None

**b.** Implementation:

• It calls the read\_neighbors() function, passing sys.argv[1] as an argument.
 This reads the neighbors from the CSV file specified as the command-line
 argument.

• It calls the set\_color\_map() function to initialize the color map.
• It calls the set\_colors() function, starting with nextColor = 0 and nextNode
 = 0, to assign colors to the countries using the backtrack search algorithm.
• It prints the resulting color map using the print(color\_map) statement.
• It calls the plot\_choropleth() function, passing the color\_map as an
 argument, to plot the choropleth graph based on the color assignments.

**Conclusion**

This project implements a backtrack search algorithm to color the map of South America. The
implemented algorithm successfully assigns colors to the countries while ensuring that
neighboring countries have distinct colors. By visualizing the colored map using a choropleth
graph, the effectiveness of the coloring algorithm is demonstrated. This project showcases the
application of backtrack search in solving graph coloring problems and provides a foundation for
further exploration in related domains.

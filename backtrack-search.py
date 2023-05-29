import plotly.express as px
import pandas as pd
import sys

countries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Falkland Islands", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"]

colors = ["blue", "green", "red", "yellow"]

graph = {}

color_map = {}


def set_color_map(): 

    for country in countries:
        color_map[country] = None

def read_neighbors(filename):
    data = pd.read_csv(filename, delimiter=';', header=None)

    for index, row in data.iterrows():
        country = row[0]
        neighbors = row[1].split(',')
        graph[country] = neighbors



def set_colors(nextColor,nextNode):


    if(color_map[countries[len(color_map)-1]] != None):
        return 

    if(nextNode == len(countries) -1 or nextNode == 0 and nextColor == len(colors)):
        return

    for i in range(nextNode,len(countries)):
        
        if(nextColor == len(colors)):
            nextNode = nextNode -1
            nextColor = findColorIndex(nextNode) + 1
            set_colors(nextColor,nextNode)
        
        elif(is_safe(graph[countries[i]],nextColor)) :

            color_map[countries[i]] = colors[nextColor]
            set_colors(0,i+1)

        else:
            
            set_colors(nextColor+1,i)

    return 


def is_safe(neighbors,nextColor):


    if (neighbors[0] == 'NONE'or len(color_map) == 0):
        return True

    for i in range(len(neighbors)) : 
        if(color_map[neighbors[i]] == colors[nextColor]) : 
            return False

    return True

def findColorIndex(nextNode):
    color = color_map[countries[nextNode]]

    for i in range(len(colors)):
        if(color == colors[i]):
            return i
    return 0 

def plot_choropleth(colormap):
    fig = px.choropleth(locationmode="country names",
                        locations=countries,
                        color=countries,
                        color_discrete_sequence=[colormap[c] for c in countries],
                        scope="south america")
    fig.show()


if __name__ == "__main__":
    
    read_neighbors(sys.argv[1])

    set_color_map()

    set_colors(0,0)

    print(color_map)

    plot_choropleth(color_map)

  


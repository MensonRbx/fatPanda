
import matplotlib.pyplot as plt
import checkIfPandasObject    

#todo
def getLinePlots(pandasObject, kwargs):
    checkIfPandasObject.check(pandasObject)
        
    #seems exactly the same as the bar plot, must investigate
        
    for index, column in pandasObject.iteritems():
            
        if column.name != kwargs["x"]:
            _plotLine(pandasObject, column.name, kwargs)
            
def _plotLine(pandasObject, yAxisName, kwargs):
        
    fig, axs = plt.subplots(1, 1, figsize = (5, 5))
    
    kwargs["y"] = yAxisName
    kwargs["ax"] = axs
        
    pandasObject.plot.line(**kwargs)
        
    if not "title" in kwargs:
        axs.set_title(f'Line Plot Showing Relationship Between {kwargs["x"]} and {yAxisName}')
     
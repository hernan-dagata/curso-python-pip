import matplotlib.pyplot as pyplot

def generate_pie_chart():
    labels = ['A', 'B', 'C', 'D', 'E', 'F']
    values = [200, 300, 320, 145, 112, 150]
    
    fig, ax = pyplot.subplots()
    ax.pie(values, labels = labels)
    pyplot.savefig('pie.png')
    pyplot.close()
import uuid, base64
from .models import *
from io import BytesIO
from matplotlib import pyplot

def get_key(res_by):
    if res_by == '#4':
        key = 'marks'
    return key
def get_graph():
    buffer = BytesIO()
    pyplot.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph
def get_chart(chart_type, data, results_by, **kwargs):
    pyplot.switch_backend('AGG')
    fig = pyplot.figure(figsize=(10, 4))
    key = get_key(results_by)
    d = data.groupby(key, as_index=False)['marks'].agg('sum')
    if chart_type == '#1':
        print("Bar graph")
        pyplot.bar(d[key], d['marks'])
    
    elif chart_type == '#3':
        print("Line graph")
        pyplot.plot(d[key], d['marks'], color='gray', marker='o', linestyle='dashed')
    else:
        print("Apparently...chart_type not identified")
    pyplot.tight_layout()
    chart = get_graph()
    return chart
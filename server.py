# coding=utf-8
import web
from web import form
from simpleeval import simple_eval
from star import Star
import json

render = web.template.render('templates/')

urls = (
    '/star/(.*)', 'star',
    '/', 'index'
)




class star:
    def GET(self, q):
        d = {'status': 'Not found', 'data': None}
        s = Star(q)
        if not s.not_found:
            d['status'] = 'OK'
            d['data'] = s.__dict__

        return json.dumps(d)



calculator_form = form.Form(
    form.Textbox('expr', description='Expr: '),
    form.Button('Calculate', type='submit', description='Calculate!')
)


class index:
    def GET(self):
        data = web.input(name=None)
        f = calculator_form()
        return render.index(data.name, f, 0)  # render 的方法 index 与模板文件夹下的模板文件需要同名

    def POST(self):
        f = calculator_form()
        data = web.input(name=None, expr='')
        expr = data.expr
        try:
            result = expr + ' = ' + str(simple_eval(expr))
        except:
            result = 'Error!'
        return render.index(data.name, f, result)

app = web.application(urls, globals())
wsgiapp = app.wsgifunc()

if __name__ == '__main__':
    app.run() 
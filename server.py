import web

render = web.template.render('templates/')

urls = (
    '/', 'index'
)


class index:
    def GET(self):
        data = web.input(name=None)
        return render.index(data.name)  # render 的方法 index 与模板文件夹下的模板文件需要同名


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run() 
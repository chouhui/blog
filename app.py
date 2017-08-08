from flask import Flask, render_template
from routes.routes_todo import main as todo_view
from routes.api_todo import main as todo_api
from routes.routes_blog import main as blog_view
from routes.api_blog import main as blog_api
from routes.routes_user import main as user_view
from routes.api_user import main as user_api
from routes.routes_static import main as index_view

app = Flask(__name__)
# 注册路由
app.register_blueprint(todo_view, url_prefix='/todo')
app.register_blueprint(todo_api, url_prefix='/api/todo')
app.register_blueprint(blog_view, url_prefix='/blog')
app.register_blueprint(blog_api, url_prefix='/api/blog')
app.register_blueprint(user_view, url_prefix='/user')
app.register_blueprint(user_api, url_prefix='/api/user')
app.register_blueprint(index_view)

app.secret_key = 'bdjsdlkgjsklgelgjelgjsegker234252542342525g'


@app.errorhandler(404)
def error(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    # 生成配置并且运行程序
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=3000,

    )
    # 如果不了解 **kwargs 的用法, 上过基础课的请复习函数, 新同学自行搜索
    app.run(**config)

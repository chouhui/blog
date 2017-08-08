from flask import (
    jsonify,
    Blueprint,
    request,
    redirect,
    url_for,
    session,
)

from utils import log
from models.blog import Blog
from routes import current_user
main = Blueprint('blog_api', __name__)


# 本文件只返回 json 格式的数据
# 而不是 html 格式的数据


@main.route('/all', methods=['GET'])
def all():
    blogs = Blog.all_json()
    return jsonify(blogs)


@main.route('/detail', methods=['GET'])
def detail():
    blog_id = int(request.args.get('id'))
    b = Blog.find(blog_id)
    return jsonify(b.json())


@main.route('/add', methods=['POST'])
def add():
    # 得到浏览器发送的表单, 浏览器用 ajax 发送 json 格式的数据过来
    # 所以这里我们用新增加的 json 函数来获取格式化后的 json 数据
    form = request.form
    u = current_user()
    # 创建一个 blog
    Blog.new(form, u.username)
    # 把创建好的 blog 返回给浏览器
    return redirect(url_for('blog.index'))


@main.route('/delete', methods=['GET'])
def delete():
    blog_id = int(request.args.get('id'))
    t = Blog.delete(blog_id)
    return jsonify(t.json())


@main.route('/update', methods=['POST'])
def update():
    form = request.get_json()
    blog_id = int(form.get('id'))
    t = Blog.update(blog_id, form)
    return jsonify(t.json())

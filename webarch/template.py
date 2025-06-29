# 模板谁加载
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader

env = Environment(
    loader=PackageLoader('webarch', 'templates'),
    # loader=FileSyetemLoader('webarch/templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

d = {
    'userlist': [
        (1, 'tom', 20),
        (5, 'jerry', 23),
        (7, 'sam', 23)
    ]
}

template = env.get_template('index.html')
html = template.render(**d)
print(html)


def render(name, data: dict):
    """
    模板的渲染
    :param name: 模板html的文件名
    :param data: 数据字典
    :return: html的字符串
    """
    template = env.get_template(name)
    html = template.render(**data)
    return html



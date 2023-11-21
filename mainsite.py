from jinja2 import Environment, FileSystemLoader


file_loader = FileSystemLoader('site')
env = Environment(loader=file_loader)

tm = env.get_template('main1.html')
msg = tm.render(title="домашнее задание", text1="Страница с домашним заданием",
                text2="Домашнее задание выполнено!!!")

print(msg)

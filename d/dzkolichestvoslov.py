import re


def finder(mstr):
    res = re.findall(r'\b\w', mstr)
    mlist1 = [i for i in res if i == 'е']
    print(*mlist1)
    print(len(mlist1))

    return res


print("ежевику для ежат\nпринесли два ежа\nежевику еле еле\nежата возли ели съели\n\nколичество слов:", )
if __name__ == '__main__':
    assert finder(mstr='ежевику для ежат\nпринесли два ежа\nежевику еле еле\nежата возли ели съели')

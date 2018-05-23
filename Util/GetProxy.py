from Web.Util import getHtmlTree


class GetFreeProxy():
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_first(pagecount=2):
        url = 'http://www.xicidaili.com/nn'
        for i in range(1, pagecount):
            u = str(url+'/{0}').format(i)
            html_tree = getHtmlTree(u)
            ips = html_tree.xpath('.//table[@id="ip_list"]//tr')
            for i in ips:
                try:
                    yield ':'.join(i.xpath('./td/text()')[0:2])
                except Exception:
                    pass


if __name__ == '__main__':
    g = GetFreeProxy()
    a =g.get_proxy_first()
    for i in a:
        print(i)
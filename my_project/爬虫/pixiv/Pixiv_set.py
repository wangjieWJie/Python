class Pixiv:
    def __init__(self) -> None:
        # P站网址
        self.url_pixiv = "https://www.pixiv.net"
        # 阅读排行榜地址
        self.url_monthly = "https://www.pixiv.net/ranking.php?"
        self.params = {"mode": "monthly"}
        # 排行榜图片总数
        self.total_img = 100
        # 获取图片个数：排行榜前几
        self.fact_img = 3

        # 图片详情页地址
        self.img_more = []
        # 图片原图地址 and 标题
        self.img_link = []

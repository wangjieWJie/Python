class Haitang:
    def __init__(self) -> None:
        # 海棠链接
        self.haitang_url = "https://www.haitangsoshu.org/"
        # 海棠排行榜链接
        self.rank_link = "https://www.haitangsoshu.org/rank/"
        # 海棠排行榜所有的小说的详情页链接
        self.more_link = []
        # 小说第一章链接
        self.novel_frist = []
        # 所有的一章小说的列表
        self.all_novel = []

        # setting
        # 要保存的小说数（排行榜前几个），最大是10
        self.max_save = 2
        # 当前保存的小说为：
        self.now_save = 0
        # 当前保存的页数：
        self.now_page = 0
        # 当前保存的章节数：
        self.chapter = 0

        # 当前进程中的网页是否能打开
        self.url_ok = True
        # 页码总数
        self.total_page = 0

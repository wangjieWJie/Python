from HaiTang import Haitang
from Get_it import (
    return_web,
    find_more,
    find_novel,
    get_novel,
    tmp_save,
    save_txt,
    download,
)


# 预设
ht = Haitang()
# 解析海棠排行榜页面
rank_web = return_web(ht, ht.rank_link)
# 寻找小说详情页链接
find_more(rank_web, ht)
# 解析所有详情页链接并储存小说第一章链接
find_novel(ht)
print(ht.novel_frist)
# 下载一部小说
download(ht)

import subprocess


def 运行(命令):
    # TODO: 需提取 stdout, 以查看更新内容
    return subprocess.run(命令.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE).stderr.decode('utf-8')

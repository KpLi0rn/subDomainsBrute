import optparse
import sys

# 这个模块里面定义了方法的参数
def parse_args():
    parser = optparse.OptionParser('usage: %prog [options] target.com',
                                   version="%prog 1.2")
    parser.add_option('-f', dest='file', default='subnames.txt',
                      help='File contains new line delimited subs, default is subnames.txt.')
    parser.add_option('--full', dest='full_scan', default=False, action='store_true',
                      help='Full scan, NAMES FILE subnames_full.txt will be used to brute')
    parser.add_option('-i', '--ignore-intranet', dest='i', default=False, action='store_true',
                      help='Ignore domains pointed to private IPs')
    parser.add_option('-t', '--threads', dest='threads', default=200, type=int,
                      help='Num of scan threads, 200 by default')
    parser.add_option('-p', '--process', dest='process', default=6, type=int,
                      help='Num of scan Process, 6 by default')
    parser.add_option('-o', '--output', dest='output', default=None,
                      type='string', help='Output file name. default is {target}.txt')

    (options, args) = parser.parse_args()
    # 解析选项后剩余位置的参数列表 懂了 就是 lijiejie这里是 直接python subdomainsbrutes baidu.com
    # 就是通过这个命令来进行判定 有没有输入域名 如果没有输入域名的话就提示help
    if len(args) < 1:
        parser.print_help()
        sys.exit(0)
    return options, args

import tkinter as tk

import os
import random

pool = [
    "财务活动",
    "财务管理目标",
    "财务环境",
    "资金时间价值与利率",
    "风险与报酬",
    "投资组合理论",
    "债券估值",
    "股票估值",
    "期权、期权组合与期权估值",
    "有效市场假设与市场异象",
    "项目现金流量的内容、构成与估算方法",
    "项目投资评价方法",
    "项目投资决策",
    "项目投资风险",
    "股权融资",
    "债务融资",
    "混合融资",
    "综合资本成本与边际资本成本计算",
    "经营风险与财务风险",
    "资本结构决策",
    "营运资本投资管理和融资策略",
    "现金管理",
    "应收账款管理",
    "存货管理",
    "股利理论",
    "股利政策",
    "现金股利与股票股利",
    "股票回购",
    "企业财务能力分析",
    "市值管理能力分析",
    "企业财务综合分析"
]

active_pool = []

theme = None

back = None

n = len(pool)

def reset_list():
    global active_pool, n, theme
    theme.configure(text="")
    print('reset')
    active_pool = pool.copy()
    n = len(active_pool)

def fetch():
    global n, theme, active_pool
    if not n:
        theme.configure(text="empty")
        return
    ind = random.randrange(n)
    tt = active_pool[ind]
    theme.configure(text=tt)
    if not back.get():
        del active_pool[ind]
        n -= 1
    print('fetch' + tt + " left: " + str(n))

def main():
    
    global pool, active_pool, theme, back

    if os.path.exists('list.txt') and os.path.isfile('list.txt'):
        with open('list.txt') as f:
            pool = [line.rstrip('\n').rstrip('\r') for line in f]
            print('read in file')

    active_pool = pool.copy()
    print(len(active_pool), active_pool)

    # init window
    window = tk.Tk()
    window.title('Random Selector')
    
    label = tk.Label(text="题目随机抽取器", fg='orange', bg='white', font=('黑体', 32, 'bold'))
    label.grid(column=0, row=0, pady=(50, 50), padx=(50, 50), columnspan=3)
    theme = tk.Label(text="", fg='green', bg='white', font=('黑体', 32, 'bold'))
    theme.grid(column=0, row=1, columnspan=3)
   
    back = tk.BooleanVar()
    tick = tk.Checkbutton(
        window, text='有放回', font=('黑体', 32, 'bold'), 
        variable=back, onvalue=True, offvalue=False
        )
    tick.grid(column=2, row=2, pady=(50, 50))

    reset = tk.Button(
        window, text='重置', height=2, width=10, font=('黑体', 24, 'bold'), command=reset_list
        )
    reset.grid(column=0, row=2)

    select = tk.Button(window, text='抽取', height=2, width=10, font=('黑体', 24, 'bold'), command=fetch)
    select.grid(column=1, row=2)

    window.mainloop()



if __name__ == '__main__':
    main()
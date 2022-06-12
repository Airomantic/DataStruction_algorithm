"""
贪心结论:最先结束的活动一定是最优解的一部分。
证明:假设a是所有活动中最先结束的活动,b是最优解中最先结束的活动。
如果a=b,结论成立。
如果a≠b,则b的结束时间一定晚于a的结束时间,则此时用a替换掉最优解中的b,aー定不与最优解中的其他活动时间重叠,因此替换后的解也是最优解。

"""
meeting=[(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(8,12),(2,14),(12,16)]
meeting.sort(key=lambda x:x[1])

def plan(cur_meeting):
    res=[cur_meeting[0]] #排序后，第一个会议一定选结束时间最早的，要整体放入一个list中，注意有[]
    for i in range(1,len(cur_meeting)): #从1开始
        if cur_meeting[i][0]>=res[-1][1]: #当前会议的开始时间大于等于列表中最后一个会议结束时间
            res.append(cur_meeting[i])
    return res
print(plan(meeting))


from barcoTest import BarcoTest

testList = [1863552437, 18635524374556, 1235456, '', 'EUIHFOeeHklas', '#*$&(^*(&#@', 0]

index = 0
for element in testList:
    if BarcoTest.WarrantyTest(element) == True:
        print(element)
        index += 1

print(f"-------------- Total {index} tests passed, {len(testList) - index} failed. -----------------")

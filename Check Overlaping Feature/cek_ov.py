import itertools, arcpy

fc = r'E:\Hara\Tes.gdb\tes\polyWWFSwap1'

def findOverlaps(x):
    with arcpy.da.SearchCursor(x, ['OID@', 'SHAPE@']) as cur:
        for feature1,feature2 in itertools.combinations(cur, 2):
            if feature1[1].equals(feature2[1]):
                print "{},equals,{}".format(feature1[0],feature2[0])
            if feature1[1].overlaps(feature2[1]):
                print "{},overlaps,{}".format(feature1[0],feature2[0])
            if feature1[1].contains(feature2[1]):
                print "{},contains,{}".format(feature1[0],feature2[0])

findOverlaps(fc)

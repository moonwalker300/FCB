echo "Dimension 50"
python mkdata.py 1000000 50 b
for q in $(seq 0 49)
do
   echo "testCase---->".$q
   python mklog.py 5000 2 0.1 3 0
   python main.py 2 1 1 >& "Exp".$q
done
python gdtruth.py 1 0 > "GroundTruth".gdt

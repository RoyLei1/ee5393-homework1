#!/bin/bash

echo "Running lambda simulations (100 trials each for faster results)..."
echo "----------------------------------------------------------"
printf "| %-5s | %-22s | %-21s |\n" "MOI" "Stealth (cI2 >= 145)" "Hijack (Cro2 >= 55)"
echo "----------------------------------------------------------"

for i in {1..10}
do
    # 替换 MOI 的值
    sed -i '' "s/^MOI .*/MOI $i N/" lambda.in
    
    # 把 1000 改成了 100 次，加快速度
    output=$(./aleae lambda.in lambda.r 100 -1 0)
    
    # 提取百分比
    stealth=$(echo "$output" | grep "cI2" | awk '{print $5}')
    hijack=$(echo "$output" | grep "Cro2" | awk '{print $5}')
    
    # 跑完一个就立刻打印一行，让你看到进度！
    printf "| %-5s | %-22s | %-21s |\n" "$i" "$stealth" "$hijack"
done

echo "----------------------------------------------------------"

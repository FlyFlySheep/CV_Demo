```python
# bitwise_and(src1, src2, dst=None, mask=None) 与
# bitwise_or(src1, src2, dst=None, mask=None)  或
# bitwise_xor(src1, src2, dst=None, mask=None) 异或
# bitwise_not(src1, src2, dst=None, mask=None) 非
```

###### Src1，Src2 ：输入的两个图像，可以为一张图片输入两边

######  dst ：图像输出大小，默认和输入图片大小一致

######  mask ：指给图像添加蒙版信息

```python
bottom_left = [col * 0.05, row]
top_left = [col * 0.45, row * 0.6]
top_right = [col * 0.55, row * 0.6]
bottom_right = [col * 0.95, row]
```

我们知道，车载行车摄像头对于车道进行拍摄的时候，我们当前车辆所处的车道的信息只会出现在车头前方的指定的梯形区域，因此我们只对梯形区域出现的图线信息进行识别，体现ROI思想。
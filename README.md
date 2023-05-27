# PlantBiCNet and PlantBiCNet-Lite
<div align=center>
<img src="https://github.com/Ye-Sk/PlantBiCNet/blob/master/linear.png"/>  
</div>   

**The resources in this repository are implemented in this paper :**  
[___PlantBiCNet: A New Paradigm in Plant Science with Bi-directional Concatenation Neural Network for Detection and Counting___](https://v.qq.com/x/cover/mpqzavrt4qvdstw/d00148c52qt.html?ptag=360kan.cartoon.free)

# Main results
### Quantitative results of MrMT dataset
|Model|P|R|AP<sub>50</sub>|MAE|RMSE|rMAE|rRMSE|R<sup>2</sup>|
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
|PlantBiCNet-Lite|0.945|0.928|0.963|3.11|5.09|6.8%|11.2%|0.9830|
|PlantBiCNet|0.948|0.910|0.956|2.47|3.68|5.4%|8.1%|0.9863|  
### Quantitative results of WED dataset
|Model|P|R|AP<sub>50</sub>|MAE|RMSE|rMAE|rRMSE|R<sup>2</sup>|
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
|PlantBiCNet-Lite|0.929|0.910|0.958|6.04|7.68|4.5%|5.7%|0.9452|
|PlantBiCNet|0.931|0.913|0.951|5.35|6.61|4.0%|4.9%|0.9589|  
### Quantitative results of DRPD dataset
|Model|P|R|AP<sub>50</sub>|MAE|RMSE|rMAE|rRMSE|R<sup>2</sup>|
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
|PlantBiCNet-Lite|0.888|0.868|0.927|1.86|2.52|8.0%|10.8%|0.9089|
|PlantBiCNet|0.907|0.871|0.923|1.65|2.22|7.1%|9.5%|0.9269|  
### Quantitative results of CBD dataset
|Model|P|R|AP<sub>50</sub>|MAE|RMSE|rMAE|rRMSE|R<sup>2</sup>|
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
|PlantBiCNet-Lite|0.724|0.769|0.801|2.73|3.36|22.0%|27.0%|0.8007|
|PlantBiCNet|0.815|0.758|0.826|2.23|3.15|18.0%|25.3%|0.8102|  
### Quantitative results of MTDC dataset
|Model|P|R|AP<sub>50</sub>|MAE|RMSE|rMAE|rRMSE|R<sup>2</sup>|
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
|PlantBiCNet-Lite|0.899|0.817|0.871|4.14|6.57|12.0%|19.0%|0.9383|
|PlantBiCNet|0.898|0.803|0.851|3.14|4.93|9.1%|14.3%|0.9681|  
### Quantitative results of RFRB dataset
|Model|P|R|AP<sub>50</sub>|MAE|RMSE|rMAE|rRMSE|R<sup>2</sup>|
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
|PlantBiCNet-Lite|0.866|0.823|0.871|28.79|43.22|9.7%|14.5%|0.9319|
|PlantBiCNet|0.893|0.876|0.924|25.33|32.16|8.5%|10.8%|0.9593|  
# Dataset download
<div align=center>
<img src="https://github.com/Ye-Sk/PlantBiCNet/blob/master/dataset.png"/>   
</div>  

# 
**I have reorganized six challenging small-scale plant detection and counting datasets.   
All of the datasets contain annotated bounding boxes.**
### Multi-regional Maize Tassels（MrMT）
[___Baidu Drive___](https://github.com/Ye-Sk/MrMT)  
——The credit of this dataset belongs to [this repository](https://pan.baidu.com/s/1crD8phKmfBQMI7FZwVXwSg).

### Wheat Ears Detection（WED）
[___Baidu Drive___](https://github.com/Ye-Sk/MrMT)  
——The credit of this dataset belongs to [this repository](https://pan.baidu.com/s/16cjcCZ-TL5gXvXXcBKdWOw).

### Diverse Rice Panicle Detection（DRPD）
[___Baidu Drive___](https://github.com/Ye-Sk/MrMT)  
——The credit of this dataset belongs to [this repository](https://pan.baidu.com/s/174M_9LOmHdWi7cuu0dsySg).

### Cotton Boll Detection（CBD）
[___Baidu Drive___](https://github.com/Ye-Sk/MrMT)  
——The credit of this dataset belongs to [this repository](https://pan.baidu.com/s/1EEyRuy_ESVtE7_2yrg14Mw?).

### Maize Tassels Detection and Counting（MTDC）
[___Baidu Drive___](https://github.com/Ye-Sk/MrMT)  
——The credit of this dataset belongs to [this repository](https://pan.baidu.com/s/1uBCdXdTM1l2ttQhvseMavA).

# Citation
~~~
@article{ye2023PlantBiCNet,  
  title={PlantBiCNet: A New Paradigm in Plant Science with Bi-directional Concatenation Neural Network for Detection and Counting},  
  author={Ye, Jianxiong and Yu, Zhenghong and Wang, Yangxu and Lu, Dunlu and Zhou, Huabing}, 
  year={2023}
}
~~~

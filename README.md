# PlantBiCNet and PlantBiCNet-Lite
<div align=center>
<img src="https://github.com/Ye-Sk/PlantBiCNet/blob/master/linear.png"/>  
</div>   

**The resources in this repository are implemented in this paper :**  
[___PlantBiCNet: A New Paradigm in Plant Science with Bi-directional Concatenation Neural Network for Detection and Counting___](https://www.sciencedirect.com/science/article/pii/S0952197623018882)

## Main results
#### Quantitative results of MrMT dataset
|Model|P|R|AP<sub>50</sub>|MAE|RMSE|R<sup>2</sup>|
| :----: | :----: | :----: | :----: | :----: | :----: | :----: |
|PlantBiCNet-Lite|0.945|0.928|0.963|3.11|5.09|0.9830|
|PlantBiCNet|0.948|0.910|0.956|2.47|3.68|0.9863|  
#### Quantitative results of WED dataset
|Model|P|R|AP<sub>50</sub>|MAE|RMSE|R<sup>2</sup>|
| :----: | :----: | :----: | :----: | :----: | :----: | :----: |
|PlantBiCNet-Lite|0.929|0.910|0.958|6.04|7.68|0.9452|
|PlantBiCNet|0.931|0.913|0.951|5.35|6.61|0.9589|  
#### Quantitative results of DRPD dataset
|Model|P|R|AP<sub>50</sub>|MAE|RMSE|R<sup>2</sup>|
| :----: | :----: | :----: | :----: | :----: | :----: | :----: |
|PlantBiCNet-Lite|0.888|0.868|0.927|1.86|2.52|0.9089|
|PlantBiCNet|0.907|0.871|0.923|1.65|2.22|0.9269|  
#### Quantitative results of CBD dataset
|Model|P|R|AP<sub>50</sub>|MAE|RMSE|R<sup>2</sup>|
| :----: | :----: | :----: | :----: | :----: | :----:| :----: |
|PlantBiCNet-Lite|0.724|0.769|0.801|2.73|3.36|0.8007|
|PlantBiCNet|0.815|0.758|0.826|2.23|3.15|0.8102|  
#### Quantitative results of MTDC dataset
|Model|P|R|AP<sub>50</sub>|MAE|RMSE|R<sup>2</sup>|
| :----: | :----: | :----: | :----: | :----: | :----: | :----: |
|PlantBiCNet-Lite|0.899|0.817|0.871|4.14|6.57|0.9383|
|PlantBiCNet|0.898|0.803|0.851|3.14|4.93|0.9681|  
#### Quantitative results of RFRB dataset
|Model|P|R|AP<sub>50</sub>|MAE|RMSE|R<sup>2</sup>|
| :----: | :----: | :----: | :----: | :----: | :----: | :----: |
|PlantBiCNet-Lite|0.866|0.823|0.871|28.79|43.22|0.9319|
|PlantBiCNet|0.893|0.876|0.924|25.33|32.16|0.9593|  

## Dataset download
<div align=center>
<img src="https://github.com/Ye-Sk/PlantBiCNet/blob/master/dataset.png"/>   
</div>  

* *I have reorganized six challenging small-scale plant detection and counting datasets.   
All of the datasets contain annotated bounding boxes.*

|Dataset|Train|Test|Baidu|Google|Source|
| :----: | :----: | :----: | :----: | :----: | :----: |
|MrMT|300|368|[Baidu](https://pan.baidu.com/s/1uoh9EhC3COEt7TqC5pmA0w?pwd=plat)|[Google](https://drive.google.com/file/d/19cRDCZ4sOSv_DAyecLyOTDAegPXiIMIT/view?usp=sharing)|[Source](https://github.com/Ye-Sk/MrMT)|
|WED|165|71|[Baidu](https://pan.baidu.com/s/1pMQB-YNViPwRfdWtryyrFw?pwd=plat)|[Google](https://drive.google.com/file/d/1HRWXaR_Gid7-yEQbG_6wAigQ_m93bqHh/view?usp=sharing)|[Source](https://github.com/Ye-Sk/Plant-dataset)|
|DRPD|200|220|[Baidu](https://pan.baidu.com/s/1nRPwA1mg2bP60RecUkuW4A?pwd=etuo)|[Google](https://drive.google.com/file/d/1duBg8yLWAs-LRtTAEFkSi3La3kBQe85_/view?usp=sharing)|[Source](https://github.com/changcaiyang/Panicle-AI)|
|CBD|52|30|[Baidu](https://pan.baidu.com/s/1kfDf0YYT0q9lQNHKBKJvHw?pwd=plat)|[Google](https://drive.google.com/file/d/165A4E45L9DJEVVs2LN0xfgJ3k4qQxKUz/view?usp=sharing)|[Source](https://github.com/Ye-Sk/PlantBiCNet)|
|MTDC|186|175|[Baidu](https://pan.baidu.com/s/1UVQ6VBQRz-e0ETEKJS5dPQ?pwd=plat)|[Google](https://drive.google.com/file/d/14iZrdaQ5FZz8nbTiqlx3-BPh0aYiAbxP/view?usp=sharing)|[Source](https://github.com/poppinace/mtdc)|
|RFRB|90|24|[Baidu](https://pan.baidu.com/s/1E1WloGVl_F2Nwyko3BM9QQ?pwd=plat)|[Google](https://drive.google.com/file/d/1-2AD__2rf5vkALBuwhF3nL1JxD3T9AYp/view?usp=sharing)|[Source](https://github.com/CV-Wang/RapeNet)|

## Citation
#### If you find this work or code useful for your research, please cite those, Thank you!🤗
~~~
@ARTICLE{YE2024107704,
  title={PlantBiCNet: A new paradigm in plant science with bi-directional cascade neural network for detection and counting},
  author={Ye, Jianxiong and Yu, Zhenghong and Wang, Yangxu and Lu, Dunlu and Zhou, Huabing},
  journal={Engineering Applications of Artificial Intelligence},
  volume={130},
  pages={107704-107722},
  year={2024},
  doi={10.1016/j.engappai.2023.107704}
}
~~~
~~~
@ARTICLE{YE20231004,  
  title={WheatLFANet: In-field detection and counting of wheat heads with high-real-time global regression network},  
  author={Ye, Jianxiong and Yu, Zhenghong and Wang, Yangxu and Lu, Dunlu and Zhou, Huabing},  
  journal={Plant Methods},  
  volume={19},  
  number={103},  
  year={2023},  
  doi={10.1186/s13007-023-01079-x}  
}
~~~
~~~
@ARTICLE{10287390,
  title={Plant Detection and Counting: Enhancing Precision Agriculture in UAV and General Scenes}, 
  author={Lu, Dunlu and Ye, Jianxiong and Wang, Yangxu and Yu, Zhenghong},
  journal={IEEE Access}, 
  year={2023},
  volume={11},
  pages={116196-116205},
  doi={10.1109/ACCESS.2023.3325747}
}
~~~



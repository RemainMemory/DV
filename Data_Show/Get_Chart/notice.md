将这部分代码添加进3D图生成的html文件中series上方
```javascript
"visualMap": {  // <-- 这部分是新增的
                "type": "piecewise",
                "pieces": [
                    // 重新写每2000一个区间
                    { "min": 0, "max": 2000, "color": "blue" },
                    { "min": 2000, "max": 4000, "color": "green" },
                    { "min": 4000, "max": 6000, "color": "yellow" },
                    { "min": 6000, "max": 8000, "color": "red" },
                    { "min": 8000, "max": 10000, "color": "black" },
                    { "min": 10000, "max": 12000, "color": "pink" },
                    { "min": 12000, "max": 14000, "color": "purple" },
                    { "min": 14000, "max": 16000, "color": "orange" },
                    { "min": 16000, "max": 18000, "color": "gray" },
                    { "min": 18000, "max": 20000, "color": "brown" },
                    { "min": 20000, "max": 22000, "color": "white" },
                    { "min": 22000, "max": 24000, "color": "cyan" },
                    { "min": 24000, "max": 26000, "color": "magenta" },
                    { "min": 26000, "max": 28000, "color": "silver" },
                    { "min": 28000, "max": 30000, "color": "gold" },
                    { "min": 30000, "max": 32000, "color": "lime" },
                    { "min": 32000, "max": 34000, "color": "ivory" },
                    { "min": 34000, "max": 36000, "color": "olive" },
                    { "min": 36000, "max": 38000, "color": "navy" },
                    { "min": 38000, "max": 40000, "color": "teal" },
                    { "min": 40000, "max": 42000, "color": "maroon" },
                    { "min": 42000, "max": 44000, "color": "azure" },
                ]
            },
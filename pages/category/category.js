

Page({

    /**
     * 页面的初始数据
     */
    data: {
        activeKey:1,
        categoryData:[],
        sliderData:[
            {
                "id":0,
                "text":"杭州市 中医馆",
                
                "icon":"like",
                "color":"#3fb666"

            },
            {
                "id":1,
                "text":"钱塘区"
            },
            {
                "id":2,
                "text":"西湖区"
            },
            {
                "id":3,
                "text":"上城区"
            },
            {
                "id":4,
                "text":"余杭区"
            },
            {
                "id":5,
                "text":"萧山区"
            },
            {
                "id":6,
                "text":"滨江区"
            },
            {
                "id":7,
                "text":"拱墅区"
            },
            {
                "id":8,
                "text":"富阳区"
            },


        ],
        sliderData1:[
          {
              "id":0,
              "text":"河庄街道",
              "icon":"like",
              "color":"#3fb666"
          },
          {
              "id":1,
              "text":"下沙街道"
          },
          {
              "id":2,
              "text":"义蓬街道"
          },
          {
              "id":3,
              "text":"新湾街道"
          },
          {
              "id":4,
              "text":"临江街道"
          },
          {
              "id":5,
              "text":"前进街道"
          },
          
         
      ],
        currentTag:"热门推荐"
    },
    


    /**
     * 生命周期函数--监听页面加载
     */

   
    clickItem(e){

    }
})
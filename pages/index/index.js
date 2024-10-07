
Page({
    data: {
        value: "",
        swiperOptions:{
            indicatorDots:true,
            autoplay:true,
            interval:3000,
            duration:1000,
            swiperData:[]
        },
        navData:[
            {
                text:"药店",
                icon:"shop-collect-o",
                color:"rgb(216, 207, 125)"
            },
            {
                text:"诊所",
                icon:"star-o",
                color:"rgb(216, 207, 125)"
            },
            {
                text:"中医馆",
                icon:"fire-o",
                color:"rgb(216, 207, 125)"
            },
            {
                text:"医保卡",
                icon:"points",
                color:"rgb(216, 207, 125)"
            },
            {
              text:"中药介绍",
              icon:"service-o",
              color:"rgb(216, 207, 125)"
          },
          {
            text:"中药医膳",
            icon:"smile-o",
            color:"rgb(216, 207, 125)"
        },
        {
          text:"食疗食谱",
          icon:"like-o",
          color:"rgb(216, 207, 125)"
      },
      {

        text:"日常理疗",
        icon:"smile-comment-o",
        color:"rgb(216, 207, 125)"
    },

        ],
        page:1,
        goodsData:[]
    },
    onLoad() {

    },
    http(page){
        getGoods({page}).then(res =>{
            if(!res.data.msg){
                this.setData({
                    // 老数据合并新数据，做累加操作
                    goodsData:this.data.goodsData.concat(res.data.data.result)
                })
            }else{
                // 给出用户提示
                wx.showToast({
                  title: res.data.msg,
                  icon:"success",
                  duration:2000
                })
            }
        })
    },
    onReachBottom(){
        // 更改页码


    },
    /**
     * 点击搜索框获取焦点
     */
    clickSearch(){
        wx.navigateTo({
          url: '/pages/search/search',
        })
    }
})



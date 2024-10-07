

Page({
    data: {
        goodsData:{}
    },
    onLoad(options) {

    },
    onSubmit(){
        wx.showToast({
          title: '预定成功',
          icon:"success"
        })
    }
})
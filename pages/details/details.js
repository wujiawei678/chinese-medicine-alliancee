

Page({

    /**
     * 页面的初始数据
     */
    data: {
        goodsDetails:{}
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad(options) {

    },

    onClickKF(){},
    
    onClickCart(){
        wx.switchTab({
          url: '/pages/cart/cart',
        })
    },
  
    onClickAddCart(){
        addGoodsCart({
            title:this.data.goodsDetails.title,
            price:this.data.goodsDetails.price,
            image:this.data.goodsDetails.topimage,
            currentID:this.data.goodsDetails.id
        }).then(res =>{
            if(res.data.status === 200){
                wx.showToast({
                  title: res.data.msg,
                })
            }else{
                wx.showToast({
                  title: res.data.msg,
                })
            }
        })
    },
    
    onClickBuy(e){
        wx.navigateTo({
          url: '/pages/buy/buy?id='+e.currentTarget.dataset.id,
        })
    }
})
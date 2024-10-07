

Page({

    /**
     * 页面的初始数据
     */
    data: {
        cartData:[]
    },
    /**
     * 每次打开页面，都会执行
     */
    onShow(){

    },
    // 根源
    delCartHandle(e){
        console.log(e.currentTarget.dataset.id);
        /**
         * 这里有两个ID
         *  1. currentID:商品ID（同一个商品，加入购物车多次的时候，会一次性全删除）
         *  2. id:每条数据的唯一索引(推荐)课程中选择的方式
         */
        delGoodsCart({currentID:e.currentTarget.dataset.id}).then(res =>{
            if(res.data.status === 200){
                wx.showToast({
                  title: '删除成功',
                })

            }else{
                wx.showToast({
                    title: '删除失败',
                  })
            }
        })
    },

})
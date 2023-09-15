// pages/home/home.js
Page({

  /**
   * 页面的初始数据
   */
  data: {

  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    this.getswpdata()
    this.getcom1data()
    this.getcom2data()
    this.getliteimg()
  },

  getswpdata(){
    wx.cloud.database().collection('swpimg').get()
    .then(res=>{
      this.setData({
        swpimgsrc: res.data
      })
    })  
  },

  getcom1data(){
    wx.cloud.database().collection('comimg1').get()
    .then(res=>{
      this.setData({
        homcomsrc1: res.data
      })
    })
  },

  getcom2data(){
    wx.cloud.database().collection('comimg2').get()
    .then(res=>{
      this.setData({
        homcomsrc2: res.data
      })
    })
  },

  getliteimg(){
    wx.cloud.database().collection('liteimg').get()
    .then(res=>{
      this.setData({
        zlklmsrc: res.data[4].img,
      })
    })
  },

  tocom(e){
    getApp().globaldata.jumpname = e.target.dataset.homtyp
    wx.switchTab({
      url: '/pages/commodity/commodity'
    })
  },
 

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {
    wx.stopPullDownRefresh()
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {

  }
})
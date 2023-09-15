// pages/mine/mine.js

Page({

  /**
   * 页面的初始数据
   */
  data: {
    userimg: "",
    username: "",
    actblc: 0
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    if (wx.getStorageSync('user')==0) {
      this.setData({
        userimg: "/icons/klm.png",
        username: "库洛米大王"
      })
    }
    if (wx.getStorageSync('user')==1) {
      this.setData({
        userimg: "/icons/bk.png",
        username: "巴库保安"
      })
    }
    this.setData({
      actblc: getApp().globaldata.actblc
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

  },
})
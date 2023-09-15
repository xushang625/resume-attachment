// pages/commodity/commodity.js

Page({
  /**
   * 页面的初始数据
   */
  data: {
    scrolltop: 0,
    tmpname: "日常必点",
    ttlprc: 0,
    crtmsk: 0,
    ttlnum: 0,
  },

  add(a, b) {
    let m, n, x; // m: a的小数位数，n: b的小数位数，x: 放大倍数
    try {
      m = a.toString().split(".")[1].length;// 获取加数a的小数位数
    } catch (e) {
      m = 0;// a也可能是个整数，于是小数位数设置为0
    }
    try {
      n = b.toString().split(".")[1].length;// 获取加数b的小数位数
    } catch (e) {
      n = 0;// b也可能是个整数，于是小数位数设置为0
    }
    x = Math.max(m, n);// 找出m, n中更大的那一个，用来放大a和b
    // 下面这个函数接收一个数字
    // 把该数字保留x位小数
    // 然后把小数点给删除，得到一个字符串
    // 字符串转化为整数，然后返回
    // 这样做的目的是把a和b都给放大10的x次方倍
    const transform = (num) => Number(num.toFixed(x).toString().replace(".", ""));
    // 放大后的a和b都是整数，进行加法计算不会丢失精度
    // 最后记得缩小10的x次方倍，把结果还原回来
    return (transform(+a) + transform(+b)) / 10 ** x;// 10 ** x 等效于Math.pow(10, x)或者 10的x次方
  },

  sub(a, b) {
    return this.add(a, -b);// 减法就相当于加上一个-b
  },

  
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    this.getuppimg()
    this.getpayimg()
    this.getgoods()
    this.getgdstyp()
    this.setData({
      actblc: getApp().globaldata.actblc
    })
  },

  getuppimg(){
    wx.cloud.database().collection('comimg').get()
    .then(res=>{
      this.setData({
        uppimgsrc: res.data
      })
    })
  },

  getpayimg(){
    wx.cloud.database().collection('liteimg').get()
    .then(res=>{
      this.setData({
        payimgsrc: res.data[2].img
      })
    })
  },

  getgoods(tmpname){
    wx.cloud.database().collection('com').get()
    .then(res=>{
      this.setData({
        com: res.data
      })
    })
  },

  getgdstyp(){
    wx.cloud.database().collection('gdstyp').get()
    .then(res=>{
      this.setData({
        typlst: res.data
      })
    })
  },

  typtap(e){
    this.setData({
      scrolltop: this.scrolltop ? 0 : 0,
      tmpname: e.target.dataset.t
    })
  },

  addtap(e){
    var comlist = this.data.com
    var index = e.target.dataset.idx
    var ttlprice = this.data.ttlprc
    comlist[index].num = comlist[index].num + 1
    ttlprice = this.add(ttlprice,comlist[index].price)
    this.setData({
      com: comlist,
      ttlprc: ttlprice,
      ttlnum: this.data.ttlnum + 1
    })
  },

  subtap(e){
    var comlist = this.data.com
    var index = e.target.dataset.idx
    var ttlprice = this.data.ttlprc
    if (comlist[index].num>0) {
      comlist[index].num = comlist[index].num - 1
      ttlprice = this.sub(ttlprice,comlist[index].price)
    }
    this.setData({
      com: comlist,
      ttlprc: ttlprice,
      ttlnum: this.data.ttlnum - 1
    })
  },

  crttap(){
    if (this.data.ttlnum==0) {
      wx.showToast({
        title: '请先添加商品哦饱饱',
        icon: 'none'
      })
    }
    else{
      this.setData({
      crtmsk: this.data.crtmsk ? 0 : 1
      })
    }
  },

  paytap(){
    if (this.data.ttlnum==0) {
      wx.showToast({
        title: '请先添加商品哦饱饱',
        icon: 'none'
      })
    }
    else{
      wx.showModal({
        title: '库库提醒',
        content: '你确定要买这么多么 饱饱',
        complete: (res) => {
          if (res.cancel) {
          }
          if (res.confirm) {
            var blc = getApp().globaldata.actblc
            var comlist = this.data.com
            blc = this.sub(blc,this.data.ttlprc)
            getApp().globaldata.actblc = blc
            for (let i = 0; i < this.data.com.length; i++) {
              comlist[i].num = 0
            }
            this.setData({
              com: comlist,
              ttlnum: 0,
              ttlprc: 0
            })
            wx.showToast({
              title: '购买成功啦饱饱,小巴库正在送货的路上哟',
              icon: 'none',
              duration: 2000
            })
          }
        }
      })
    }
    
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
    this.setData({
      tmpname: getApp().globaldata.jumpname
    })
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
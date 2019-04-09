import Vue from 'vue'
import Vuex from 'vuex'
import qs from 'querystring'
import axios from 'axios'

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        count: 1,
        price: 20,
        uName: '',
        uPwd: '',
        isLogin: localStorage.getItem('isLogin')
    },
    // 修改数据还是要靠它
    mutations: {
        modifySuccess(state, payload) {
            state.uName = payload.userName;
            state.uPwd = payload.userPwd;
            state.isLogin = true;
            localStorage.setItem('uName', state.uName);
            localStorage.setItem('isLogin', state.isLogin);
        }
    },
    // 只执行异步操作
    actions: {
        getData(state, payload) {
            axios.post('/sys/login', qs.stringify({
                username: payload.userName,
                userpwd: payload.userPwd
            })).then(resp => {
                let result = resp.data;
                if (result == "success") {
                    this.commit({
                        type: 'modifySuccess',
                        userName: payload.userName,
                        userPwd: payload.userPwd,
                    })
                }

            }).catch(error => {
                console.error(error);
            })
        }
    }
})

export default store;
import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        uName: '',
        bName: ''
    },
    mutations: {
        modifySuccess(state, paylood){
            state.uName = paylood.userName;
            state.bName = paylood.backName
            sessionStorage.setItem('uName', state.uName);
            sessionStorage.setItem('bName', state.bName);
        }
    },
    actions: {
        authenticateUser(state, paylood){
            this.commit({
                type: 'modifySuccess',
                userName: paylood.userName,
                backName: paylood.backName
            });
        }
    }
});

export default store;
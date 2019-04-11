import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        uName: ''
    },
    mutations: {
        modifySuccess(state, paylood){
            state.uName = paylood.userName;
            sessionStorage.setItem('uName', state.uName);
        }
    },
    actions: {
        authenticateUser(state, paylood){
            this.commit({
                type: 'modifySuccess',
                userName: paylood.userName
            });
        }
    }
});

export default store;
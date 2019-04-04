import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/login'
import Register from '../components/register'
import HomePage from '../components/homepage'
import Detail from '../components/detail'
import VuexOne from '../components/VuexOne'
import VuexTwo from '../components/VuexTwo'
import User from '../components/user'
import UserInfo from '../components/userInfo'
import store from '../store/index'

Vue.use(VueRouter);

const router = new VueRouter({
    routes: [
        { path: '/', component: HomePage },
        {
            path: '/det/:id', component: Detail,
            meta: {
                requireAuth: true
            },
            children: [
                { path: '/det/log', component: Login },
                { path: '/det/reg', component: Register },
            ]
        },
        { path: '/log', component: Login },
        { path: '/reg', component: Register },
        { path: '/one', component: VuexOne },
        { path: '/two', component: VuexTwo },
        { path: '/user', component: User },
        { path: '/userInfo/:id', component: UserInfo }
    ]
}); 

router.beforeEach((to, from, next)=>{
    if ( to.meta.requireAuth ){
        let userValue = store.state.isLogin;
        console.log(userValue);
        if ( userValue ){
            next();
        }else{
            next({path: '/log'});
        }
    }else{
        next();
    }
});

export default router;
import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '../components/login'
import Register from '../components/register'
import HomePage from '../components/homepage'
import Detail from '../components/detail'

Vue.use(VueRouter);

const router = new VueRouter({
    routes: [
        { path: '/', component: HomePage },
        {
            path: '/det/:id', component: Detail,
            children: [
                { path: '/det/log', component: Login },
                { path: '/det/reg', component: Register },
            ]
        },
        { path: '/log', component: Login },
        { path: '/reg', component: Register }
    ]
}); 

export default router;
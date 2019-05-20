import Vue from 'vue'
import Router from 'vue-router'
import Workspace from './views/workspace'
import Cal_Monthly from './components/Cal_Monthly'
import HelloWorld from './components/HelloWorld'
import login from './components/login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      //name: 'workspace',
      component: Workspace,
      children: [
        {
          path: '',
          name: 'Cal_Monthly',
          component: Cal_Monthly
        },
        {
          path: 'test',
          name: 'HelloWorld',
          component: HelloWorld
        },
        {
          path: 'login',
          name: 'login',
          component: login
        }
        //캘린더 두개 더 추가
      ]

      //다른 path추가 login, project
      //create project는 어떤식으로 할것인가?
    },
  ]
})
import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '@/views/Home'
import Login from '@/components/Login'
import Signup from '@/views/Signup'
import Community from '@/views/Community'
import CommunityDetail from '@/views/CommunityDetail'
import CommunityControl from '@/views/CommunityControl'
import Profile from '@/views/Profile'
import Search from '@/views/Search.vue'
import MovieDetailFromTMDB from '@/views/MovieDetailFromTMDB.vue'
import CreateCommunity from '@/views/CreateCommunity.vue'
import Worldcup from '@/views/Worldcup.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/search',
    name: 'search',
    component: Search
  },
  {
    path: '/worldcup',
    name: 'Worldcup',
    component: Worldcup
  },
  {
    path: '/:id',
    name: 'MovieDetailFromTMDB',
    component: MovieDetailFromTMDB
  },
  {
    path: '/community',
    name: 'Community',
    component: Community,
  },
  {
    path: '/community',
    name: 'CreateCommunity',
    component: CreateCommunity,
  },
  {
    path: '/communitydetail/:community_pk',
    name: 'CommunityDetail',
    component: CommunityDetail,
  },
  {
    path: '/CommunityControl/:community_pk',
    name: 'CommunityControl',
    component: CommunityControl,
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/accounts/profile',
    name: 'Profile',
    component: Profile,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
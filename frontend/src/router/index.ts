import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      component: () => import("@/pages/CoursesPage.vue")
    },
    {
      path: "/add-course",
      component: () => import('@/pages/AddCoursePage.vue')
    }
  ],
})

export default router

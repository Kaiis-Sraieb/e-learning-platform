<template>
    <div v-for="course in courses">
        <div>
            <h1>{{ course.title }}</h1>
            <p>{{ course.description }}</p>
        </div>
    </div>
</template>

<script setup lang="ts">
import { getCourses } from '@/services/courseService';
import { onMounted, ref } from 'vue';


const courses = ref<[{ title: string; description: string }]>()

onMounted(async () => {
    courses.value = await getCourses()
})

</script>
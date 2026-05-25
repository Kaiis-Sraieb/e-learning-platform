<template>
    <input type="text" v-model="title" placeholder="title">
    <textarea name="description" v-model="description" id="" placeholder="description"></textarea>
    <button @click="add">add course</button>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { addCourse } from "@/services/courseService"


const title = ref<string>("");
const description = ref<string>("");

const add = async () => {
    const response = await addCourse({ title: title.value, description: description.value })

    if (response) {
        console.log("added")
        console.log(response)
    }
} 

</script>
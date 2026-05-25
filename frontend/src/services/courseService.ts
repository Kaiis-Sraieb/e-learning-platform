import axios from "axios";

const API_URL = "https://yourusername.pythonanywhere.com/api"

export const getCourses = async () => {
    const response = await axios.get(`${API_URL}/courses`)
    return response.data
}

export const addCourse = async (payload: { title: string, description: string }) => {
    const response = await axios.post(`${API_URL}/courses`, payload);
    return response.data
}